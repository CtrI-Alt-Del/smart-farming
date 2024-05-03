class PlantGrowthChart {
  constructor() {
    const chartData = document.querySelector('[data-plant-growth-chart="data"]')

    const container = document.querySelector(
      '[data-plant-growth-chart="container"]',
    )

    const plantSelect = document.querySelector(
      '[data-plant-growth-chart="plant-select"]',
    )

    const daysRangeSelect = document.querySelector(
      '[data-plant-growth-chart="days-range-select"]',
    )

    const averageElement = document.querySelector(
      '[data-plant-growth-chart="average"]',
    )

    if (
      chartData &&
      container &&
      plantSelect &&
      averageElement &&
      daysRangeSelect &&
      typeof ApexCharts !== "undefined"
    ) {
      this.data = JSON.parse(chartData.value)
      this.plantId = Object.keys(this.data)[0]
      this.daysRange = Object.keys(this.data[this.plantId])[0]
      this.average = averageElement
      this.color = "#548C2F"

      const chart = new ApexCharts(container, this.getChartOptions())

      chart.render()

      this.chart = chart

      console.log({ plantSelect })

      plantSelect.addEventListener("change", (event) => {
        this.handlePlantSelectChange(event)
      })

      daysRangeSelect.addEventListener("change", (event) => {
        this.handleDaysRangeSelectChange(event)
      })

      this.renderAverageValue()
    }
  }

  renderAverageValue() {
    const averageValue = this.data[this.plantId][this.daysRange].average
    this.average.textContent = `${averageValue}%`
  }

  handlePlantSelectChange(event) {
    const plantId = event.currentTarget.value
    this.plantId = plantId

    this.updateChart()
  }

  handleDaysRangeSelectChange(event) {
    const daysRange = event.currentTarget.value
    console.log({ daysRange })
    this.daysRange = daysRange

    this.updateChart()
  }

  updateChart() {
    this.chart.updateOptions(this.getChartOptions())
    this.renderAverageValue()
  }

  getChartOptions() {
    const data = this.data[this.plantId][this.daysRange]

    const dates = data.dates
    const records = data.records
    const laiValues = records.map((record) => record.lai)

    return {
      chart: {
        height: 200,
        type: "area",
        fontFamily: "Inter, sans-serif",
        dropShadow: {
          enabled: false,
        },
        toolbar: {
          show: false,
        },
      },
      tooltip: {
        enabled: true,
        x: {
          show: false,
        },
        y: {
          show: true,
        },
      },
      fill: {
        type: "gradient",
        gradient: {
          opacityFrom: 0.55,
          opacityTo: 0,
          shade: this.color,
          gradientToColors: [this.color],
        },
      },
      dataLabels: {
        enabled: false,
      },
      stroke: {
        width: 6,
      },
      grid: {
        show: false,
        strokeDashArray: 4,
        padding: {
          left: 2,
          right: 2,
          top: 0,
        },
      },
      series: [
        {
          name: "Crescimento",
          data: laiValues,
          color: this.color,
        },
      ],
      xaxis: {
        categories: dates,
        labels: {
          show: false,
        },
        axisBorder: {
          show: false,
        },
        axisTicks: {
          show: false,
        },
      },
      yaxis: {
        show: true,
        min: 0,
        max: 100,
        stepSize: 25,
        labels: {
          show: true,
          offsetX: -12,
          formatter: (value) => {
            return `${value}%`
          },
        },
      },
    }
  }
}

window.addEventListener("load", () => new PlantGrowthChart())
