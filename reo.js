// Reo.dev developer insights tracking
(function () {
  var clientID = "2f9f4a96601bb63";
  var script = document.createElement("script");
  script.src = "https://static.reo.dev/" + clientID + "/reo.js";
  script.defer = true;
  script.onload = function () {
    Reo.init({ clientID: clientID, enableThirdPartyTracking: true });
  };
  document.head.appendChild(script);
})();
