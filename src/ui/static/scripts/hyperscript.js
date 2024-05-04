class Hyperscript {
  constructor() {
    document.body.addEventListener("htmx:afterOnLoad", (event) => {
      this.precessElement(event.detail.elt)
    })
  }

  precessElement(element) {
    const elementsToBeProcessed = element.querySelectorAll("[_]")

    for (const element of elementsToBeProcessed) {
      _hyperscript.processNode(element)
    }
  }
}

window.addEventListener("load", () => new Hyperscript())
