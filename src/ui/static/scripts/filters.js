class Filters {
  constructor() {
    const filters = document.querySelectorAll("[data-filters='filter']")
    const removeAllButton = document.querySelector(
      "[data-filters='remove-all-button']",
    )

    if (!filters.length) return

    this.filters = filters
    this.queryParam = new QueryParam()

    for (const filter of this.filters) {
      filter.addEventListener("input", (event) =>
        this.handleFilterChange(event),
      )
    }

    if (removeAllButton) {
      this.removeAllButton = removeAllButton
      this.removeAllButton.addEventListener("click", () =>
        this.handleRemoveAllButtonClick(),
      )

      const currentParams = this.queryParam.getAll()
      const filtersNames = Array.from(this.filters).map((filter) => filter.name)
      const hasFilters = currentParams.some((param) =>
        filtersNames.includes(param),
      )

      if (hasFilters) this.showRemoveAllButton()
    }
  }

  resetFilter(filter) {
    switch (filter.nodeName) {
      case "SELECT":
        filter.selectedIndex = 0
        break
      default:
        filter.value = ""
    }

    this.queryParam.remove(filter.name)
  }

  showRemoveAllButton() {
    this.removeAllButton.classList.remove("hidden")
  }

  hideRemoveAllButton() {
    this.removeAllButton.classList.add("hidden")
  }

  handleRemoveAllButtonClick() {
    for (const filter of this.filters) {
      this.resetFilter(filter)
    }

    const changeEvent = new Event("change", { bubbles: true })
    this.filters[0].dispatchEvent(changeEvent)
    this.hideRemoveAllButton()
  }

  handleFilterChange(event) {
    const field = event.currentTarget
    this.queryParam.append(field.name, field.value)

    if (this.removeAllButton) this.showRemoveAllButton()
  }
}

window.addEventListener("load", () => new Filters())
