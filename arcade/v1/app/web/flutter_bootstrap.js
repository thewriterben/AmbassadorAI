{{flutter_js}}
{{flutter_build_config}}

// Branded splash: advance the bar through the load stages, then fade it out
// on Flutter's first frame. The splash markup lives in index.html.
(function () {
  var fill = document.getElementById('fill');
  var msg = document.getElementById('msg');
  var splash = document.getElementById('splash');
  function stage(pct, text) {
    if (fill) fill.style.width = pct + '%';
    if (msg && text) msg.textContent = text;
  }
  stage(15, 'LOADING THE ARCADE');
  window.addEventListener('flutter-first-frame', function () {
    stage(100);
    if (splash) {
      splash.classList.add('gone');
      setTimeout(function () { splash.remove(); }, 400);
    }
  });
  _flutter.loader.load({
    config: { suppressMultithreadingWarning: true },
    onEntrypointLoaded: async function (engineInitializer) {
      stage(55, 'STARTING THE ENGINE');
      var appRunner = await engineInitializer.initializeEngine();
      stage(80, 'OPENING THE VAULT');
      await appRunner.runApp();
    }
  });
})();
