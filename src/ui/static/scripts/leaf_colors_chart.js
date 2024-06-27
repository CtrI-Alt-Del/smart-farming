class LeafColorsChart {
  constructor() {
    const container = document.querySelector(
      '[data-leaf-colors-chart="container"]',
    )
    const chartData = document.querySelector('[data-leaf-colors-chart="data"]')
    const select = document.querySelector('[data-leaf-colors-chart="select"]')
    const legendColors = document.querySelector(
      '[data-leaf-colors-chart="legend-colors"]',
    )

    if (
      chartData &&
      select &&
      legendColors &&
      typeof ApexCharts !== "undefined"
    ) {
      this.legendColors = legendColors.value.split(";")
      this.data = JSON.parse(chartData.value)
      const initialData = this.getSelectedData("default")

      const chart = new ApexCharts(container, this.getChartOptions(initialData))

      chart.render()

      this.chart = chart

      select.addEventListener("change", (event) =>
        this.handleSelectChange(event),
      )
    }
  }

  calculatePercentages(values) {
    const total = values.reduce((total, currentValue) => {
      return total + currentValue
    }, 0)

    const percentages = values.map((value) =>
      ((value / total) * 100).toFixed(2),
    )

    return percentages.map(Number)
  }

  getChartOptions(data) {
    const labels = Object.keys(data).map((label) => label.toLocaleLowerCase())
    const values = Object.values(data)

    return {
      series: values,
      colors: this.legendColors,
      chart: {
        name: "leaf-colors-chart",
        height: 320,
        width: "100%",
        type: "pie",
      },
      stroke: {
        colors: ["white"],
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
        show: false,
        position: "top",
        fontFamily: "Inter, sans-serif",
        horizontalAlign: "left",
      },
      yaxis: {
        min: 0,
        max: 100,
        stepSize: 25,
        labels: {
          formatter: (value) => {
            return `${value} dias`
          },
        },
      },
      xaxis: {
        labels: {
          show: false,
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

window.addEventListener("load", () => new LeafColorsChart())
