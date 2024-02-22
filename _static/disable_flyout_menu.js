// disable_flyout_menu.js

document.addEventListener("DOMContentLoaded", function() {
    var flyoutMenu = document.querySelector(".rst-other-versions");
    if (flyoutMenu) {
        flyoutMenu.parentNode.removeChild(flyoutMenu);
    }
});
