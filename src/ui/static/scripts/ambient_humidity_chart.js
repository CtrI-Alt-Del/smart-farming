class AmbientHumidityChart {
  constructor() {
    const container = document.querySelector(
      '[data-ambient-humidity-chart="container"]',
    )

    const select = document.querySelector(
      '[data-ambient-humidity-chart="select"]',
    )

    this.averageValue = document.querySelector(
      '[name="attribute_humidity-average"]'
    )

    console.log(this.averageValue)

    if (container && select && typeof ApexCharts !== 'undefined') {
      const initialData = this.getSelectedData("7 days")
      const initialDates = this.getSelectedDates("7 days")

      const chart = new ApexCharts(
        container,
        this.getChartOptions(initialData, initialDates),
        this.averageValue.innerHTML = this.getAverageData(initialData).toFixed(2)
      )

      chart.render()

      this.chart = chart

      select.addEventListener('change', (event) =>
        this.handleSelectChange(event),
      )
    }
  }

  getAverageData(data) {
    let mediaArr = 0
    for (let i = 0; i < data.length; i++) {
      mediaArr += data[i] 
    }
    return mediaArr / data.length
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
          shade: '#1C64F2',
          gradientToColors: ['#1C64F2'],
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
          name: 'Umidade',
          data: data,
          color: '#1A56DB',
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
        }
      },
    };
  }

  handleSelectChange(event) {
    const selectedValue = event.currentTarget.value
    const data = this.getSelectedData(selectedValue)
    const dates = this.getSelectedDates(selectedValue)
    this.chart.updateOptions(this.getChartOptions(data, dates))
    this.averageValue.innerHTML = this.getAverageData(data).toFixed(2);
  }

  getSelectedData(selectedDaysRange) {
    const chartDataField = document.querySelector(
      `[data-filtered-data-chart="${selectedDaysRange}"][name="ambient_humidity"]`,
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
      `[data-filtered-data-chart="${selectedDaysRange}"][name="ambient_humidity-average"]`,
    )

    if (averageField) {
      return Number(averageField.value)
    }

    return 0
  }
}

window.addEventListener('load', () => new AmbientHumidityChart())
