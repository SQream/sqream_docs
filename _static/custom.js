document.addEventListener('readthedocsdataready', function(event) {
    var data = event.detail;
    console.log('RTD Data:', data);

    // Select the shadow host element
    var shadowHost = document.querySelector('body > readthedocs-flyout');

    if (shadowHost) {
        // Access the shadow root
        var shadowRoot = shadowHost.shadowRoot;
        if (shadowRoot) {
            // Select the flyout menu within the shadow root
            var flyoutMenu = shadowRoot.querySelector('div');

            if (flyoutMenu) {
                // Select the new parent element where you want to move the flyout menu
                var newParent = document.querySelector('.custom-location'); // Replace with your desired new parent selector

                if (newParent) {
                    // Move the flyout menu to the new location
                    newParent.appendChild(flyoutMenu);
                } else {
                    console.error('New parent element not found!');
                }
            } else {
                console.error('Flyout menu not found in shadow DOM!');
            }
        } else {
            console.error('Shadow root not found!');
        }
    } else {
        console.error('Shadow host element not found!');
    }
});
