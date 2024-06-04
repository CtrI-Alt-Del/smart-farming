class CsvOutput {
  constructor() {
    const output = document.querySelector("[data-csv-output='output']")

    if (!output) return

    this.output = output
    this.queryParam = new QueryParam()

    document.addEventListener("addFilter", () => this.addQueryParam())

    setTimeout(() => {
      this.addQueryParam()
    }, 1000)
  }

  addQueryParam() {
    const currentHref = this.output.getAttribute("href").split("?")[0]

    const params = this.queryParam.getAll().filter(([key]) => key !== "page")

    const paramsString = params
      .map((param) => `${param[0]}=${param[1]}`)
      .join("&")

    this.output.setAttribute("href", `${currentHref}?${paramsString}`)
  }
}

window.addEventListener("load", () => new CsvOutput())
