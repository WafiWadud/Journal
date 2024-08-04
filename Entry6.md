# A new, Better marquee tag

---

The old `<marquee>` tag has practically been eradicated from most browsers. Instead the user should use CSS3 animation. So, i did just that in a small script anyone can embed. To create a marquee, use the `<new-marquee>` tag with this in your code:

```js
class MarqueeElement extends HTMLSpanElement {
  constructor() {
    super();

    // Create a shadow DOM
    this.attachShadow({ mode: "open" });

    // Create a <p> element to wrap the content
    const content = document.createElement("p");
    content.innerHTML = this.innerHTML;

    // Create styles
    const style = document.createElement("style");
    style.textContent = `
      :host {
        width: 100%;
        display: inline-block;
        line-height: 50px;
        white-space: nowrap;
        overflow: hidden;
        box-sizing: border-box;
      }
      p {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 15s linear infinite;
      }
      @keyframes marquee {
        0%   { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
      }
    `;

    // Append style and content to shadow DOM
    this.shadowRoot.appendChild(style);
    this.shadowRoot.appendChild(content);
  }
}

// Define the custom element
customElements.define("new-marquee", MarqueeElement, { extends: "span" });
```

[Previous Page](Entry5.md) [Next Page](Entry7.md)
