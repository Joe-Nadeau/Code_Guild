const ctx = document.getElementById('myChart').getContext('2d');

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

const personalRecord = {
    label: "Squat Personal Record",
    data: [135, 185, 205, 215, 225, 235, 250, 265, 270],
    lineTension: 0,
    fill: false,
    borderColor: 'orange'
};

const goal = {
    label: "Squat Goal",
    data: [315, 315, 315, 315, 315, 315, 315, 315, 315, 315, 315, 315],
    lineTension: 0,
    fill: false,
    borderColor: 'green'
};

const lifts = {
    labels: ["1/2020", "2/2020", "3/2020", "4/2020", "5/2020", "6/2020", "7/2020", "8/2020", "9/2020", "10,2020", "11/2020", "12/2020"],
    datasets: [personalRecord, goal]
};

const chartOptions = {
    legend: {
        display: true,
        position: 'top',
        labels: {
            boxwidth: 100,
            fontColor: 'white'
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

const lineChart = new Chart(ctx, {
    type: 'line',
    data: lifts,
    options: chartOptions
});

Chart.plugins.register({
    beforeDraw: function(chartInstance, easing) {
      const ctx = chartInstance.chart.ctx;
      ctx.fillStyle = 'white'; // your color here
  
      const chartArea = chartInstance.chartArea;
      ctx.fillRect(chartArea.left, chartArea.top, chartArea.right - chartArea.left, chartArea.bottom - chartArea.top);
    }
  });

//   turn this into three separate graphs. One for squat, one for deadlift, and one for bench. Have dates on the x-axis so that you can track progress over time.