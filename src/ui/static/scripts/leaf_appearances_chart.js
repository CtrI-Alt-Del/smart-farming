class LeafAppearancesChart {
  constructor() {
    // const container = document.querySelector(
    //   '[leaf-appearances-chart="container"]',
    // )
    const dataField = document.querySelector(
      '[data-leaf-appearances-chart="data"]',
    )

    // const select = document.querySelector('[leaf-appearances-chart="select"]')

    if (dataField && typeof ApexCharts !== "undefined") {
      this.data = JSON.parse(dataField.value)
      const initialData = this.getSelectedData("all")

      // const chart = new ApexCharts(
      //   container,
      //   this.getChartOptions(initialData, initialDates),
      // )

      // chart.render()

      // this.chart = chart

      // select.addEventListener("change", (event) =>
      //   this.handleSelectChange(event),
      // )
    }
  }

  getSelectedData(plant_id) {
    if (plant_id === "all") {
      return Object.values(this.data)
    }

    return this.data[plant_id]
  }

  handleSelectChange(event) {
    const selectedValue = event.currentTarget.value

    const data = this.getSelectedData(selectedValue)

    // this.chart.updateOptions(this.getChartOptions(data))
  }
}

window.addEventListener("load", () => new LeafAppearancesChart())
