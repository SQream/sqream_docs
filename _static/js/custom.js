// Import necessary modules from jsDelivr
import { LitElement, html, css, nothing } from 'https://cdn.jsdelivr.net/npm/lit-element@2.5.1/lit-element.js';
import { classMap } from 'https://cdn.jsdelivr.net/npm/lit-html@1.3.0/directives/class-map.js';

// Define the custom flyout element
class CustomFlyoutElement extends LitElement {
  static elementName = "readthedocs-flyout";

  static properties = {
    config: { state: true },
    opened: { type: Boolean },
    floating: { type: Boolean },
    position: { type: String },
  };

  constructor() {
    super();
    this.config = null;
    this.opened = false;
    this.floating = true;
    this.position = "bottom-left";  // Set default position to bottom-left
  }

  loadConfig(config) {
    if (!FlyoutAddon.isEnabled(config)) {
      return;
    }
    this.config = config;
  }

  _toggleOpen() {
    this.opened = !this.opened;
  }

  _onOutsideClick(e) {
    if (e.target !== this) {
      this.opened = false;
    }
  }

  renderHeader() {
    return html`
      <header @click="${this._toggleOpen}">
        <img class="logo" src="https://example.com/logo.svg" alt="Read the Docs" />
      </header>
    `;
  }

  render() {
    if (this.config === null) {
      return nothing;
    }

    const classes = { floating: this.floating, container: true };
    classes[this.position] = true;

    return html`
      <div class=${classMap(classes)}>
        ${this.renderHeader()}
        <main class=${classMap({ closed: !this.opened })}>
          <!-- Add other render methods if needed -->
        </main>
      </div>
    `;
  }

  connectedCallback() {
    super.connectedCallback();
    window.addEventListener("click", this._onOutsideClick.bind(this));
  }

  disconnectedCallback() {
    window.removeEventListener("click", this._onOutsideClick.bind(this));
    super.disconnectedCallback();
  }
}

customElements.define("readthedocs-flyout", CustomFlyoutElement);

document.addEventListener('DOMContentLoaded', function() {
    const flyoutElement = document.querySelector('readthedocs-flyout');

    if (flyoutElement) {
        flyoutElement.position = 'bottom-left'; // Set position to bottom-left
    }
});
