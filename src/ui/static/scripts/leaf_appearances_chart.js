class LeafAppearancesChart {
  constructor() {
    const container = document.querySelector(
      '[data-leaf-appearances-chart="container"]',
    )
    const dataField = document.querySelector(
      '[data-leaf-appearances-chart="data"]',
    )

    const select = document.querySelector(
      '[data-leaf-appearances-chart="select"]',
    )

    if (dataField && select && typeof ApexCharts !== "undefined") {
      this.data = JSON.parse(dataField.value)
      const initialData = this.getSelectedData("default")

      const chart = new ApexCharts(container, this.getChartOptions(initialData))

      chart.render()

      this.chart = chart

      select.addEventListener("change", (event) =>
        this.handleSelectChange(event),
      )
    }
  }

  getChartOptions(data) {
    const labels = Object.keys(data).map((label) => label.toLocaleLowerCase())
    const series = Object.values(data)

    return {
      series,
      colors: ["#16BDCA", "#1C64F2", "#9061F9"],
      chart: {
        height: 360,
        width: "100%",
        type: "pie",
      },
      stroke: {
        colors: ["white"],
        lineCap: "",
      },
      plotOptions: {
        pie: {
          labels: {
            show: true,
          },
          size: "100%",
          dataLabels: {
            offset: -25,
          },
        },
      },
      labels,
      dataLabels: {
        enabled: true,
        style: {
          fontFamily: "Inter, sans-serif",
        },
        formatter: (value) => {
          return `${Number(value).toFixed(2)}%`
        },
      },
      legend: {
        position: "bottom",
        fontFamily: "Inter, sans-serif",
      },
      yaxis: {
        labels: {
          formatter: (value) => {
            return `${value} dias`
          },
        },
      },
      xaxis: {
        labels: {
          formatter: (value) => {
            return `${value} dias`
          },
        },
        axisTicks: {
          show: false,
        },
        axisBorder: {
          show: false,
        },
      },
    }
  }

  getSelectedData(plantId) {
    if (plantId === "default") {
      const defaultValues = Object.values(this.data)[0]
      return defaultValues
    }

    return this.data[plantId]
  }

  handleSelectChange(event) {
    const selectedValue = event.currentTarget.value

    const data = this.getSelectedData(selectedValue)

    this.chart.updateOptions(this.getChartOptions(data))
  }
}

window.addEventListener("load", () => new LeafAppearancesChart())
