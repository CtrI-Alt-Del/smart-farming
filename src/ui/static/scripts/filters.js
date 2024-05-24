class Filters {
  constructor() {
    const filters = document.querySelectorAll("[data-filters='filter']")

    if (!filters.length) return

    this.queryParam = new QueryParam()

    for (const filter of filters) {
      filter.addEventListener("input", (event) =>
        this.handleFilterChange(event),
      )
    }
  }

  handleFilterChange(event) {
    const field = event.currentTarget
    this.queryParam.append(field.name, field.value)
  }
}

window.addEventListener("load", () => new Filters())
