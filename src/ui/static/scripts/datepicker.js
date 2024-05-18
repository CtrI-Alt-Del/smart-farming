document.addEventListener("DOMContentLoaded", () => {
  const startDateInput = document.getElementById("startDate")
  const endDateInput = document.getElementById("endDate")
  let previousEndDateValue = endDateInput.value

  endDateInput.disabled = true
  endDateInput.style.opacity = "0.5"
  endDateInput.style.cursor = "not-allowed"

  function setEndDateToStartDate() {
    if (!endDateInput.value) {
      endDateInput.value = startDateInput.value
    }
  }

  startDateInput.addEventListener("blur", () => {
    setEndDateToStartDate()
  })

  endDateInput.addEventListener("input", () => {
    if (new Date(startDateInput.value) > new Date(this.value)) {
      this.value = previousEndDateValue
    } else {
      previousEndDateValue = this.value
    }
  })

  startDateInput.addEventListener("change", () => {
    const selectedDate = new Date(this.value)
    selectedDate.setDate(selectedDate.getDate() + 1)
    endDateInput.min = selectedDate.toISOString().split("T")[0]
    endDateInput.disabled = false
    endDateInput.style.opacity = "1"
    endDateInput.style.cursor = "auto"
  })
})