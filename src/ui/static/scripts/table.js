class Table {
  constructor() {
    const container = document.querySelector("[data-table='container']")
    const deleteButton = document.querySelector("[data-table='delete-button']")

    if (!container || !deleteButton) return

    this.rowsIds = []
    this.deleteButton = deleteButton
    this.queryParam = new QueryParam()

    this.addEventListenerToCheckboxes(container)

    const observer = new MutationObserver((mutations) => {
      if (mutations[0].type === "childList") {
        this.addEventListenerToCheckboxes(mutations[0].target)
      }
    })

    observer.observe(container, { childList: true })

    const updateRowEvent = new Event("updateRow")
    document.dispatchEvent(updateRowEvent)

    container.addEventListener("updateRow", () =>
      this.addEventListenerToCheckboxes(container),
    )
  }

  addEventListenerToCheckboxes(container) {
    const checkboxes = container.querySelectorAll("[data-table='checkbox-row']")

    if (!checkboxes.length) return

    this.hideDeleteButton()
    this.rowsIds = []

    for (const checkbox of checkboxes) {
      checkbox.addEventListener("change", (event) =>
        this.handleCheckboxChange(event),
      )
    }
  }

  hideDeleteButton() {
    this.deleteButton.classList.remove("block")
    this.deleteButton.classList.add("hidden")
  }

  showDeleteButton() {
    this.deleteButton.classList.remove("hidden")
    this.deleteButton.classList.add("block")
  }

  handleCheckboxChange(event) {
    const checkbox = event.currentTarget
    const rowId = checkbox.value
    const isChecked = checkbox.checked


    if (isChecked) {
      this.rowsIds.push(rowId)
    } else {
      this.rowsIds = this.rowsIds.filter((id) => id !== rowId)
    }

    if (this.rowsIds.length) {
      this.showDeleteButton()
    } else {
      this.hideDeleteButton()
    }
  }
}

window.addEventListener("load", () => new Table())
