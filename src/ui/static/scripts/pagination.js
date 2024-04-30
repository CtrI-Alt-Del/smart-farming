class Pagination {
  constructor() {
    const pageButtons = document.querySelectorAll(
      '[data-pagination="page-button"]',
    )
    const form = document.querySelector('[data-pagination="form"]')
    const input = document.querySelector('[data-pagination="input"]')

    if (!pageButtons.length || !form || !input) return

    this.pageButtons = pageButtons
    this.form = form
    this.input = input
    this.queryParam = new QueryParam()

    const currentPage = this.queryParam.get("page")

    console.log({ currentPage })

    this.activePageButton(currentPage ?? "1")

    for (const pageButton of this.pageButtons) {
      pageButton.addEventListener("click", (event) =>
        this.handlePageButtonClick(event),
      )
    }
  }

  activePageButton(pageNumber) {
    for (const pageButton of this.pageButtons) {
      if (pageButton.value === pageNumber) {
        pageButton.classList.add("bg-gray-800", "text-white")
      } else {
        pageButton.classList.remove("bg-gray-800", "text-white")
      }
    }
  }

  handlePageButtonClick(event) {
    const pageNumber = event.currentTarget.value

    this.activePageButton(pageNumber)

    this.queryParam.remove("page")
    this.queryParam.append("page", pageNumber)

    this.input.value = pageNumber
    htmx.trigger(`#${this.form.id}`, "submit")
  }
}

window.addEventListener("load", () => new Pagination())
