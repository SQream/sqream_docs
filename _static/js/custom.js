document.addEventListener('DOMContentLoaded', function() {
    // Select the flyout menu container and hide it
    var flyoutMenu = document.querySelector('.floating.container.bottom-right');
    if (flyoutMenu) {
        flyoutMenu.style.display = 'none';
    }
});
