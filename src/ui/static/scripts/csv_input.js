class CsvInput {
  constructor() {
    const input = document.querySelector('[data-csv-input="input"]')
    const submitIcon = document.querySelector('[data-csv-input="submit-icon"]')
    const submitButton = document.querySelector(
      '[data-csv-input="submit-button"]',
    )
    const loading = document.querySelector('[data-csv-input="loading"]')

    if (input && submitIcon && submitButton && loading) {
      input.addEventListener("change", (event) =>
        this.handleInputChange(event, submitIcon),
      )

      submitButton.addEventListener("click", () =>
        this.handleSubmitButtonClick(submitButton, submitIcon, loading),
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

  handleSubmitButtonClick(submitButton, submitIcon, loading) {
    submitButton.setAttribute("disabled", "true")
    submitIcon.remove()

    loading.classList.remove("hidden")
    loading.classList.add("grid")
  }
}

window.addEventListener("load", () => new CsvInput())
