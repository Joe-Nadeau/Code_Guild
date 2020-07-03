const ctx = document.getElementById('myChart').getContext('2d');

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

const personalRecords = {
    label: "Personal Records",
    data: [270, 205, 330],
    lineTension: 0,
    fill: false,
    borderColor: 'orange'
};

const goals = {
    label: "Goal",
    data: [315, 225, 405],
    lineTension: 0,
    fill: false,
    borderColor: 'green'
};

const lifts = {
    labels: ["squat", "bench", "deadlift"],
    datasets: [personalRecords, goals]
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