var ctx = document.getElementById('myChart').getContext('2d');

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

var personalRecords = {
    label: "Personal Records",
    data: [270, 205, 330],
    lineTension: 0,
    fill: false,
    borderColor: 'orange'
};

var goals = {
    label: "Goal",
    data: [315, 225, 405],
    lineTension: 0,
    fill: false,
    borderColor: 'green'
};

var lifts = {
    labels: ["squat", "bench", "deadlift"],
    datasets: [personalRecords, goals]
};

var chartOptions = {
    legend: {
        display: true,
        position: 'top',
        lables: {
            boxwidth: 80,
            fontColor: 'black'
        }
    }   ,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true,
                fontColor: 'white'
            }
        }],
        xAxes: [{
                ticks: {
                    fontColor:'yellow'
                }
        }]
    }

};

var lineChart = new Chart(ctx, {
    type: 'line',
    data: lifts,
    options: chartOptions
});

Chart.plugins.register({
    beforeDraw: function(chartInstance, easing) {
      var ctx = chartInstance.chart.ctx;
      ctx.fillStyle = 'white'; // your color here
  
      var chartArea = chartInstance.chartArea;
      ctx.fillRect(chartArea.left, chartArea.top, chartArea.right - chartArea.left, chartArea.bottom - chartArea.top);
    }
  });