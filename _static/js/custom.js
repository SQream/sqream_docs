document.addEventListener('DOMContentLoaded', function() {
    // Select the flyout menu container and hide it
    var flyoutMenu = document.querySelector("body > readthedocs-flyout").shadowRoot.querySelector("div");
    if (flyoutMenu) {
        flyoutMenu.style.display = 'none';
    }
});



