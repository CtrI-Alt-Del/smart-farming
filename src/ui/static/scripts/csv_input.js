class CsvInput {
  constructor() {
    const input = document.querySelector('[data-csv-input="input"]')
    const submitIcon = document.querySelector('[data-csv-input="submit-icon"]')
    const submitButton = document.querySelector(
      '[data-csv-input="submit-button"]',
    )

    if (input && submitIcon && submitButton) {
      this.submitButton = submitButton
      this.submitIcon = submitIcon
      this.input = input

      input.addEventListener("change", (event) =>
        this.handleInputChange(event, submitIcon),
      )

      submitButton.addEventListener("click", () =>
        this.handleSubmitButtonClick(),
      )
    }
  }

  showSubmitButton() {
    this.submitIcon.classList.remove("hidden")
    this.submitIcon.classList.add("flex")
  }

  hideSubmitButton() {
    this.submitIcon.classList.add("hidden")
    this.submitIcon.classList.remove("flex")
  }

  handleInputChange(event) {
    const hasFile = event.currentTarget.value

    if (hasFile) {
      this.showSubmitButton()
    } else {
      this.hideSubmitButton()
    }
  }

  handleSubmitButtonClick() {
    this.hideSubmitButton()
    setTimeout(() => {
      this.input.value = null
    }, 1000)
  }
}

window.addEventListener("load", () => new CsvInput())
