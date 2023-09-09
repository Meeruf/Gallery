document.querySelector('.full').addEventListener('click', function() {
    var button = this;
    
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().then(() => {
        button.classList.add('active');
      });
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen().then(() => {
          button.classList.remove('active');
        });
      }
    }
  });
  