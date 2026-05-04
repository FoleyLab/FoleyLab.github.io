(function() {
  function formatNumber(value) {
    return new Intl.NumberFormat("en-US", {
      maximumFractionDigits: 6
    }).format(value);
  }

  function convertValue(value, mode) {
    if (!isFinite(value)) {
      return "Please enter a valid numeric value.";
    }

    if (mode === "nm-to-ev") {
      return formatNumber(1239.841984 / value) + " eV";
    }

    if (mode === "ev-to-nm") {
      return formatNumber(1239.841984 / value) + " nm";
    }

    if (mode === "cm-to-ev") {
      return formatNumber(value / 8065.54429) + " eV";
    }

    if (mode === "ev-to-cm") {
      return formatNumber(value * 8065.54429) + " cm^-1";
    }

    return "Conversion mode not recognized.";
  }

  function onReady(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
      return;
    }

    fn();
  }

  onReady(function() {
    var forms = document.querySelectorAll(".tool-form");

    forms.forEach(function(form) {
      form.addEventListener("submit", function(event) {
        event.preventDefault();

        var tool = form.getAttribute("data-tool");
        var output = form.parentElement.querySelector(".tool-output");

        if (!output) {
          return;
        }

        if (tool === "converter") {
          var value = parseFloat(form.elements.value.value);
          var mode = form.elements.mode.value;
          output.textContent = convertValue(value, mode);
          return;
        }

        if (tool === "placeholder") {
          output.textContent = form.getAttribute("data-placeholder") || "Tool logic can be added later.";
        }
      });
    });
  });
})();
