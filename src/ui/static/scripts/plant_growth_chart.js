class PlantGrowthChart {
  constructor() {
    const container = document.querySelector(
      '[data-plant-growth-chart="container"]',
    )

    const select = document.querySelector(
      '[data-plant-growth-chart="select"]',
    )

    if (container && select && typeof ApexCharts !== "undefined") {
      const initialData = this.getSelectedData("7 days")
      const initialDates = this.getSelectedDates("7 days")
      const initialAverage = this.getAverage("7 days")

      const chart = new ApexCharts(
        container,
        this.getChartOptions(initialData, initialDates),
      )

      chart.render()

      this.chart = chart

      select.addEventListener("change", (event) =>
        this.handleSelectChange(event),
      )

      this.renderAverageValue(initialAverage)
    }
  }

  handleSelectChange(event) {
    const selectedValue = event.currentTarget.value

    const data = this.getSelectedData(selectedValue)
    const dates = this.getSelectedDates(selectedValue)
    const average = this.getAverage(selectedValue)

    this.chart.updateOptions(this.getChartOptions(data, dates))
    this.renderAverageValue(average)
  }

  getChartOptions(data, dates) {
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
          shade: "#34D399",
          gradientToColors: ["#34D399"],
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
          data: data,
          color: "#34D399",
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

  getSelectedData(selectedDaysRange) {
    const chartDataField = document.querySelector(
      `[data-filtered-data-chart="${selectedDaysRange}"][name="plant_growth"]`,
    )

    if (chartDataField) {
      const data = chartDataField.value.split(";").map(Number)
      return data
    }

    return []
  }

  getSelectedDates(selectedDaysRange) {
    const chartDatesField = document.querySelector(
      `[data-filtered-data-chart="${selectedDaysRange}"]`,
    )

    if (chartDatesField) {
      const dates = chartDatesField.value.split(";")
      return dates
    }

    return []
  }

  getAverage(selectedDaysRange) {
    const averageValue = document.querySelector(
      `[data-filtered-data-chart="${selectedDaysRange}"][name="plant_growth_average"]`,
    )

    return averageValue.value
  }

  renderAverageValue(value) {
    const average = document.querySelector(
      '[data-plant-growth-chart="average"]',
    )

    if (average) {
      average.textContent = `${value}%`
    }
  }
}

window.addEventListener("load", () => new PlantGrowthChart())
