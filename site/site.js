(function () {
  // Mobile menu
  document.querySelectorAll(".menu-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var list = btn.parentElement.querySelector(".nav-links");
      var open = list.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.textContent = open ? "Close" : "Menu";
    });
  });

  // Copy buttons
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      var done = function () { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = "Copy"; }, 1800); };
      var fallback = function () {
        var code = btn.parentElement.querySelector("code");
        if (!code) return;
        var r = document.createRange(); r.selectNodeContents(code);
        var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
        btn.textContent = "Selected";
      };
      try { navigator.clipboard.writeText(text).then(done, fallback); } catch (e) { fallback(); }
    });
  });

  // Donation amount picker
  document.querySelectorAll(".amount-picker").forEach(function (picker) {
    var out = picker.querySelector("[data-amount-out]");
    picker.querySelectorAll("[data-amount]").forEach(function (b) {
      b.addEventListener("click", function () {
        picker.querySelectorAll("[data-amount]").forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        if (out) out.textContent = "$" + b.getAttribute("data-amount");
      });
    });
  });

  // Forms: until a form service is connected, each form opens a pre-filled email.
  document.querySelectorAll("form[data-mailto]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var to = form.getAttribute("data-mailto");
      var subject = form.getAttribute("data-subject") || "Website enquiry";
      var lines = [];
      new FormData(form).forEach(function (v, k) {
        if (k === "subject") subject = subject + ": " + v;
        else lines.push(k.replace(/_/g, " ") + ": " + v);
      });
      var href = "mailto:" + to + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(lines.join("\n"));
      var status = form.parentElement.querySelector(".form-status");
      if (status) status.textContent = "Your email app should open with this message. If it doesn't, write to " + to + ".";
      window.location.href = href;
    });
  });
})();
