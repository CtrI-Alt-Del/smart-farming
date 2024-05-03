document.addEventListener("DOMContentLoaded", function () {
  var options = {
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
        //THIAGO VIADO obrigado viado :).
      },
    },
    fill: {
      type: "gradient",
      gradient: {
        opacityFrom: 0.55,
        opacityTo: 0,
        shade: "#1C64F2",
        gradientToColors: ["#1C64F2"],
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
        name: "Indice",
        data: [30, 40, 35, 50, 49, 60, 70, 91, 125],
        color: "#000000",
      },
    ],
    xaxis: {
      categories: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
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
      min: 0,
      max: 100,
      stepSize: 25,
      labels: {
        show: true,
        offsetX: -12,
      },
    },
  }

  var chart = new ApexCharts(document.querySelector("#chart"), options)
  chart.render()
})
