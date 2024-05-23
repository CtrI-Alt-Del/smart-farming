class Colorpicker {
  constructor() {
    const forms = document.querySelectorAll("[data-colorpicker='form']")

    if (!forms.length) return

    const colorpickerEvent = new Event("colorpicker")
    document.dispatchEvent(colorpickerEvent)

    for (const form of forms) {
      this.addEventListeners(form)
      form.addEventListener("colorpicker", () => this.addEventListeners(form))
    }
  }

  addEventListeners(form) {
    const control = form.querySelector("[data-colorpicker='control']")
    const label = form.querySelector("[data-colorpicker='label']")
    const textInput = form.querySelector("[data-colorpicker='text-input']")
    const textPreview = form.querySelector("[data-colorpicker='text-preview']")

    if (!control || !label || !textInput || !textPreview) return

    if (control.defaultValue) {
      label.style.backgroundColor = control.defaultValue
    }

    if (textInput.value) {
      textPreview.textContent = textInput.value
    }

    control.addEventListener("input", () =>
      this.handleControlChange(label, control),
    )

    textInput.addEventListener("input", () =>
      this.handleTextInputChange(textPreview, textInput),
    )
  }

  handleControlChange(label, control) {
    label.style.backgroundColor = control.value
  }

  handleTextInputChange(textPreview, textInput) {
    textPreview.textContent = textInput.value
  }
}

window.addEventListener('load', () => new Colorpicker())