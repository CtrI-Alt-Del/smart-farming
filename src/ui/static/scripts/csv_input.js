class CsvInput {
  constructor() {
    const input = document.querySelector('[data-csv-input="input"]')
    const submitIcon = document.querySelector('[data-csv-input="submit-icon"]')
    const submitButton = document.querySelector(
      '[data-csv-input="submit-button"]',
    )

    if (input && submitIcon && submitButton) {
      input.addEventListener("change", (event) =>
        this.handleInputChange(event, submitIcon),
      )

      submitButton.addEventListener("click", () =>
        this.handleSubmitButtonClick(submitButton, submitIcon),
      )
    }
  }

  handleInputChange(event, submitIcon) {
    const hasFile = event.currentTarget.value

    if (hasFile) {
      submitIcon.classList.remove("hidden")
      submitIcon.classList.add("flex")
    } else {
      submitIcon.classList.add("hidden")
      submitIcon.classList.remove("flex")
    }
  }
}

window.addEventListener("load", () => new CsvInput())
