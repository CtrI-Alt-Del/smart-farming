class AmbientHumidityChartOptions {
  constructor() {
    const container = document.querySelector(
      '[data-ambient-humidity-chart="container"]',
    )

    const select = document.querySelector(
      '[data-ambient-humidity-chart="select"]',
    )

    if (container && select && typeof ApexCharts !== 'undefined') {
      const chart = new ApexCharts(
        container,
        this.getChartOptions([0, 2, 3, 4, 5, 6]),
      )
      chart.render()

      this.chart = chart

      select.addEventListener('change', (event) =>
        this.handleSelectChange(event),
      )
    }
  }

  getChartOptions(data) {
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
        categories: [
          '01 February',
          '02 February',
          '03 February',
          '04 February',
          '05 February',
          '06 February',
          '07 February',
        ],
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
        categories: [
          '0',
          '25',
          '50',
          '75',
          '100',
        ],
        labels: {
          show: true,
        }
      },
    };
  }


  handleSelectChange(event) {
    const selectedValue = event.currentTarget.value
    const chartDataField = document.querySelector(
      `[data-chart-data="${selectedValue}"]`,
    )
    const data = chartDataField.value.split(';').map(Number)
    console.log(data)

    this.chart.updateOptions(this.getChartOptions(data))
  }
}

window.addEventListener('load', () => new AmbientHumidityChartOptions())
