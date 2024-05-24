class Hyperscript {
  constructor() {
    document.body.addEventListener("htmx:afterOnLoad", (event) => {
      this.precessElements(event.detail.elt)
    })
  }

  precessElements(element) {
    const hyperscriptElements = element.querySelectorAll("[_]")
    const htmxElements = element.querySelectorAll("[data-^=hx-]")

    for (const element of hyperscriptElements) {
      _hyperscript.processNode(element)
    }
    for (const element of htmxElements) {
      htmx.process(element)
    }
  }
}

window.addEventListener("load", () => new Hyperscript())
