document.addEventListener('DOMContentLoaded', function() {
    const flyoutElement = document.querySelector('readthedocs-flyout');

    if (flyoutElement) {
        // Modify the position property
        flyoutElement.position = 'bottom-left'; // or any other position if available
        flyoutElement.requestUpdate(); // Request an update to apply the change

        // Apply custom styles directly if needed
        const style = document.createElement('style');
        style.textContent = `
            readthedocs-flyout {
                /* Custom styles if needed */
            }
        `;
        document.head.appendChild(style);
    }
});
