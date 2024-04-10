class WaterVolumeChart {
  constructor() {
    const container = document.querySelector(
      '[data-water-volume-chart="container"]',
    )

    const select = document.querySelector(
      '[data-water-volume-chart="select"]',
    )

    const averageValue = document.querySelector(
      '[name="{{ attribute }}-average"]'
    )

    if (container && select && typeof ApexCharts !== 'undefined') {
      const initialData = this.getSelectedData("7 days")
      const initialDates = this.getSelectedDates("7 days")

      const chart = new ApexCharts(
        container,
        this.getChartOptions(initialData, initialDates),
      )

      chart.render()

      this.chart = chart

      select.addEventListener('change', (event) =>
        this.handleSelectChange(event),
      )
    }
  }

  getChartOptions(data, dates) {
    return {
      chart: {
        height: 200,
        type: 'area',
        fontFamily: 'Inter, sans-serif',
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
          show: true
        }
      },
      fill: {
        type: 'gradient',
        gradient: {
          opacityFrom: 0.55,
          opacityTo: 0,
          shade: '#7E22CE',
          gradientToColors: ['#7E22CE'],
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
          name: 'Litros',
          data: data,
          color: '#7E22CE',
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
        max: 12,
        stepSize: 3,
        labels: {
          show: true,
          offsetX: -12,
          formatter: (value) => {
            return `${value}L`
          },
        }
      },
    };
  }

  handleSelectChange(event) {
    const selectedValue = event.currentTarget.value

    const data = this.getSelectedData(selectedValue)
    const dates = this.getSelectedDates(selectedValue)

    this.chart.updateOptions(this.getChartOptions(data, dates))
  }

  getSelectedData(selectedDaysRange) {
    const chartDataField = document.querySelector(
      `[data-filtered-data-chart="${selectedDaysRange}"][name="water_volume"]`,
    )

    if (chartDataField) {
      const data = chartDataField.value.split(';').map(Number)
      return data
    }

    return []
  }

  getSelectedDates(selectedDaysRange) {
    const chartDatesField = document.querySelector(
      `[data-filtered-data-chart="${selectedDaysRange}"]`,
    )

    if (chartDatesField) {
      const dates = chartDatesField.value.split(';')
      return dates
    }

    return []
  }

  getSelectedDate(selectedDaysRange) {
    const averageField = document.querySelector(
      `[data-filtered-data-chart="${selectedDaysRange}"][name="water_volume-average"]`,
    )

    if (averageField) {
      return Number(averageField.value)
    }

    return 0
  }
}

window.addEventListener('load', () => new WaterVolumeChart())





