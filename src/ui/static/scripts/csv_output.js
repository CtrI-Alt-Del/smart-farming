class CsvOutput {
  constructor() {
    const output = document.querySelector("[data-csv-output='output']")

    if (!output) return

    document.addEventListener("queryParam", () => this.addQueryParam())
  }

  addQueryParam() {
    alert("EITA")
  }
}

window.addEventListener("load", () => new CsvOutput())