(function () {
  "use strict";

  var base = window.FM_BASE || "";

  function store(key, value) {
    try {
      if (value === undefined) { return localStorage.getItem(key); }
      if (value === null) { localStorage.removeItem(key); } else { localStorage.setItem(key, value); }
    } catch (e) { return null; }
    return null;
  }

  // Theme
  var toggle = document.querySelector(".theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      store("fm-theme", next);
    });
  }

  // Mobile navigation
  var navBtn = document.querySelector(".nav-toggle");
  var scrim = document.querySelector(".scrim");
  function setNav(open) {
    document.body.classList.toggle("nav-open", open);
    if (navBtn) { navBtn.setAttribute("aria-expanded", open ? "true" : "false"); }
    if (scrim) { scrim.hidden = !open; }
  }
  if (navBtn) { navBtn.addEventListener("click", function () { setNav(!document.body.classList.contains("nav-open")); }); }
  if (scrim) { scrim.addEventListener("click", function () { setNav(false); }); }
  var current = document.querySelector('.sidebar a[aria-current="page"]');
  if (current) { current.scrollIntoView({ block: "center" }); window.scrollTo(0, 0); }

  // Heading anchors and table of contents
  var body = document.querySelector(".doc-body");
  var toc = document.getElementById("toc");
  if (body) {
    var heads = body.querySelectorAll("h2[id], h3[id]");
    heads.forEach(function (h) {
      var a = document.createElement("a");
      a.className = "anchor";
      a.href = "#" + h.id;
      a.setAttribute("aria-label", "Link to this section");
      a.textContent = "#";
      h.insertBefore(a, h.firstChild);
    });
    if (toc) {
      if (heads.length < 2) {
        toc.closest(".toc").style.visibility = "hidden";
      }
      var links = [];
      heads.forEach(function (h) {
        var a = document.createElement("a");
        a.href = "#" + h.id;
        a.className = "lvl" + h.tagName.charAt(1);
        a.textContent = h.textContent.replace(/^#/, "").trim();
        toc.appendChild(a);
        links.push({ a: a, h: h });
      });
      var onScroll = function () {
        var y = window.scrollY + 120;
        var active = null;
        links.forEach(function (l) { if (l.h.offsetTop <= y) { active = l; } });
        links.forEach(function (l) { l.a.classList.toggle("active", l === active); });
      };
      window.addEventListener("scroll", onScroll, { passive: true });
      onScroll();
    }
    // Wide tables scroll inside their own box
    body.querySelectorAll(":scope > table").forEach(function (t) {
      var w = document.createElement("div");
      w.className = "table-wrap";
      t.parentNode.insertBefore(w, t);
      w.appendChild(t);
    });
  }

  // Figures: hovering a legend entry or a callout highlights its pair
  document.querySelectorAll(".fig").forEach(function (fig) {
    var svg = fig.querySelector(".fig-svg");
    if (!svg) { return; }
    function hl(n) {
      svg.classList.toggle("dim", n !== null);
      svg.querySelectorAll(".co").forEach(function (g) { g.classList.toggle("hl", g.getAttribute("data-n") === n); });
      fig.querySelectorAll(".fig-legend li").forEach(function (li) { li.classList.toggle("hl", li.getAttribute("data-n") === n); });
    }
    fig.querySelectorAll(".fig-legend li").forEach(function (li) {
      li.addEventListener("mouseenter", function () { hl(li.getAttribute("data-n")); });
      li.addEventListener("mouseleave", function () { hl(null); });
    });
    svg.querySelectorAll(".co").forEach(function (g) {
      g.addEventListener("mouseenter", function () { hl(g.getAttribute("data-n")); });
      g.addEventListener("mouseleave", function () { hl(null); });
    });
  });

  // Procedures: click a step to tick it off, remembered per page
  document.querySelectorAll("ol.steps").forEach(function (ol, idx) {
    var key = "fm-steps:" + location.pathname + ":" + idx;
    var done = (store(key) || "").split(",").filter(Boolean);
    var items = Array.prototype.slice.call(ol.children);
    items.forEach(function (li, i) {
      if (done.indexOf(String(i)) !== -1) { li.classList.add("done"); }
      li.addEventListener("click", function (e) {
        if (e.target.closest("a")) { return; }
        li.classList.toggle("done");
        var now = items.map(function (x, j) { return x.classList.contains("done") ? j : null; }).filter(function (x) { return x !== null; });
        store(key, now.length ? now.join(",") : null);
      });
    });
    var reset = document.createElement("button");
    reset.type = "button";
    reset.className = "steps-reset";
    reset.textContent = "Clear ticks";
    reset.addEventListener("click", function () {
      items.forEach(function (li) { li.classList.remove("done"); });
      store(key, null);
    });
    ol.parentNode.insertBefore(reset, ol.nextSibling);
  });

  // Search
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");
  var index = null;
  var active = -1;

  function load(cb) {
    if (index) { cb(); return; }
    fetch(base + "/search.json").then(function (r) { return r.json(); }).then(function (data) {
      index = data.map(function (d) {
        d.lt = d.title.toLowerCase();
        d.lx = (d.text || "").toLowerCase();
        d.lk = (d.keywords || "").toLowerCase();
        return d;
      });
      cb();
    }).catch(function () {});
  }

  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function snippet(d, terms) {
    var i = -1;
    for (var t = 0; t < terms.length && i < 0; t++) { i = d.lx.indexOf(terms[t]); }
    if (i < 0) { return esc((d.text || "").slice(0, 140)) + "…"; }
    var start = Math.max(0, i - 50);
    var s = esc((start ? "…" : "") + d.text.slice(start, start + 170) + "…");
    terms.forEach(function (t) {
      if (t.length < 2) { return; }
      s = s.replace(new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig"), "<mark>$1</mark>");
    });
    return s;
  }

  function search(q) {
    var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) { results.hidden = true; return; }
    var hits = [];
    index.forEach(function (d) {
      var score = 0;
      for (var i = 0; i < terms.length; i++) {
        var t = terms[i];
        var s = 0;
        if (d.lt.indexOf(t) !== -1) { s += d.lt.indexOf(t) === 0 ? 30 : 18; }
        if (d.lk.indexOf(t) !== -1) { s += 12; }
        var c = d.lx.split(t).length - 1;
        if (c) { s += Math.min(c, 8) + 2; }
        if (!s) { return; }
        score += s;
      }
      hits.push({ d: d, s: score });
    });
    hits.sort(function (a, b) { return b.s - a.s; });
    hits = hits.slice(0, 12);
    active = -1;
    if (!hits.length) {
      results.innerHTML = '<div class="sr-empty">No matches for “' + esc(q) + '”</div>';
    } else {
      results.innerHTML = hits.map(function (h) {
        return '<a href="' + base + h.d.url + '"><span class="sr-sec">' + esc(h.d.section || "") + '</span><span class="sr-title">' +
          esc(h.d.title) + '</span><span class="sr-snip">' + snippet(h.d, terms) + "</span></a>";
      }).join("");
    }
    results.hidden = false;
  }

  if (input && results) {
    input.addEventListener("focus", function () { load(function () { if (input.value) { search(input.value); } }); });
    input.addEventListener("input", function () { load(function () { search(input.value); }); });
    input.addEventListener("keydown", function (e) {
      var items = results.querySelectorAll("a");
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        if (!items.length) { return; }
        active = (active + (e.key === "ArrowDown" ? 1 : -1) + items.length) % items.length;
        items.forEach(function (a, i) { a.classList.toggle("active", i === active); });
        items[active].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter") {
        var target = items[active >= 0 ? active : 0];
        if (target) { location.href = target.href; }
      } else if (e.key === "Escape") {
        results.hidden = true;
        input.blur();
      }
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".search")) { results.hidden = true; }
    });
    document.addEventListener("keydown", function (e) {
      var tag = (document.activeElement && document.activeElement.tagName) || "";
      if ((e.key === "/" || (e.key === "k" && (e.ctrlKey || e.metaKey))) && tag !== "INPUT" && tag !== "TEXTAREA") {
        e.preventDefault();
        input.focus();
        input.select();
      }
    });
  }
})();
