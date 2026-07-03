/*!
 * MyOwnClone Embed Widget v1.0
 *
 * Inserta un iframe con el chat de un clon en cualquier web.
 *
 * Uso:
 *   <script src="https://myownclone.com/embed/widget.js"
 *           data-clone="slug-del-clon"
 *           data-mode="support"
 *           data-color="#6366f1"></script>
 *   <div id="myownclone-widget"></div>
 */
(function () {
  "use strict";

  function getAttr(script, name, fallback) {
    var v = script.getAttribute("data-" + name);
    return v == null ? fallback : v;
  }

  function buildIframe(clone, mode, color) {
    var url = new URL("/embed/" + encodeURIComponent(clone), scriptOrigin());
    if (mode) url.searchParams.set("mode", mode);
    if (color) url.searchParams.set("color", color);

    var iframe = document.createElement("iframe");
    iframe.src = url.toString();
    iframe.style.width = "100%";
    iframe.style.height = "560px";
    iframe.style.border = "none";
    iframe.style.borderRadius = "12px";
    iframe.style.boxShadow = "0 4px 12px rgba(0,0,0,0.08)";
    iframe.setAttribute("title", "MyOwnClone — " + clone);
    iframe.setAttribute("allow", "microphone");
    iframe.setAttribute("loading", "lazy");
    return iframe;
  }

  function scriptOrigin() {
    // Toma el origen del propio script (https://myownclone.com)
    var scripts = document.getElementsByTagName("script");
    for (var i = 0; i < scripts.length; i++) {
      var src = scripts[i].src || "";
      if (src.indexOf("/embed/widget.js") !== -1) {
        try {
          return new URL(src).origin;
        } catch (e) {}
      }
    }
    return window.location.origin;
  }

  function mount() {
    var scripts = document.querySelectorAll(
      'script[src*="/embed/widget.js"]'
    );
    scripts.forEach(function (script) {
      var clone = getAttr(script, "clone", "");
      if (!clone) return;

      var mode = getAttr(script, "mode", "support");
      var color = getAttr(script, "color", "#6366f1");

      var container = document.createElement("div");
      container.id = "myownclone-widget-" + clone;
      container.style.maxWidth = "480px";
      container.style.margin = "20px auto";

      var iframe = buildIframe(clone, mode, color);
      container.appendChild(iframe);
      script.parentNode.insertBefore(container, script.nextSibling);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();