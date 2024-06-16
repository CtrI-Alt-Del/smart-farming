class Datepicker {
  constructor() {
    const startDateInput = document.querySelector("[data-datepicker='start-date']")
    const endDateInput = document.querySelector("[data-datepicker='end-date']")
    const form = document.querySelector("[data-datepicker='form']")

    if (!startDateInput || !endDateInput || !form) return

    this.startDateInput = startDateInput
    this.endDateInput = endDateInput
    this.previousEndDateValue = endDateInput.value
    this.form = form
    this.queryParam = new QueryParam()

    endDateInput.addEventListener("input", () => this.handleEndInputChange())
    startDateInput.addEventListener("change", (event) => this.handleStartInputChange(event))
  }

  setEndDateToStartDate() {
    if (!this.endDateInput.value) {
      this.endDateInput.value = this.startDateInput.value
      this.queryParam.append("end-date", this.startDateInput.value)
    }
  }

  handleEndInputChange() {
    if (new Date(this.startDateInput.value) > new Date(this.endDateInput.value)) {
      this.endDateInput.value = this.previousEndDateValue
    } else {
      this.previousEndDateValue = this.endDateInput.value
    }

    if (this.startDateInput.value) this.submitForm()
  }

  handleStartInputChange(event) {
    const selectedDate = new Date(event.target.value)

    if (selectedDate > new Date()) {
      alert("Datas futuras não são permitidas.")
      return
    }
    selectedDate.setDate(selectedDate.getDate() + 1)
    this.endDateInput.min = selectedDate.toISOString().split("T")[0]
    this.endDateInput.disabled = false
    this.endDateInput.style.opacity = "1"
    this.endDateInput.style.cursor = "auto"

    this.setEndDateToStartDate()
  }
}

window.addEventListener("load", () => new Datepicker())
