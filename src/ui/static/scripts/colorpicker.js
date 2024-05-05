class Colorpicker {
  constructor(formId) {
    const form = document.getElementById(formId)

    if (!form) return

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
