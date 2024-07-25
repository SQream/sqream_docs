import { LitElement, html, css, nothing } from 'https://cdn.jsdelivr.net/npm/lit-element@2.5.1/lit-element.js';
import { classMap } from 'https://cdn.jsdelivr.net/npm/lit-html@1.4.1/directives/class-map.js';
import { library, icon } from 'https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-svg-core@1.2.30/index.js';
import { faCodeBranch } from 'https://cdn.jsdelivr.net/npm/@fortawesome/free-solid-svg-icons@5.15.3/index.js';

const READTHEDOCS_LOGO = 'https://assets.readthedocs.org/static/images/logo-wordmark-light.svg';

class CustomFlyoutElement extends LitElement {
  static get properties() {
    return {
      config: { type: Object },
      opened: { type: Boolean },
      floating: { type: Boolean },
      position: { type: String },
    };
  }

  constructor() {
    super();
    this.config = null;
    this.opened = false;
    this.floating = true;
    this.position = "bottom-left";  // Set default position to bottom-left
  }

  loadConfig(config) {
    if (!this.isEnabled(config)) {
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
    library.add(faCodeBranch);
    const iconCodeBranch = icon(faCodeBranch, {
      classes: ["icon"],
    });
    let version = nothing;
    if (
      this.config.projects.current.versioning_scheme !==
      "single_version_without_translations"
    ) {
      version = html`<span>${iconCodeBranch.node[0]} ${this.config.versions.current.slug}</span>`;
    }

    return html`
      <header @click="${this._toggleOpen}">
        <img class="logo" src="${READTHEDOCS_LOGO}" alt="Read the Docs" />
        ${version}
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

  isEnabled(config) {
    return config.addons && config.addons.flyout && config.addons.flyout.enabled;
  }
}

customElements.define("readthedocs-flyout", CustomFlyoutElement);

document.addEventListener('DOMContentLoaded', function() {
  const flyoutElement = document.querySelector('readthedocs-flyout');

  if (flyoutElement) {
    flyoutElement.position = 'bottom-left'; // Set position to bottom-left
  }
});
