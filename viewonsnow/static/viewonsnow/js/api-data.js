const calc_id = JSON.parse(document.getElementById('calc_id').textContent);
//var endpoint = 'api/chart/data/'
var endpoint = 'api/data/' + calc_id
var output_after_snow = []
var input_before_snow = []
var labels = []


$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    labels = data.labels
    input_before_snow = data.input_before_snow
    output_after_snow = data.output_after_snow

    console.log(data)
    console.log(calc_id)
    console.log(endpoint)
    setChart_before('myChart_before')
    setChart_after('myChart_after')

  },
  error: function (error_data) {
    console.log("error")
    console.log(error_data)
  }

})

function setChart_before(chart) {
  var ctx = document.getElementById(chart).getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        data: input_before_snow,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
        borderWidth: 1
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  })
}

function setChart_after(chart) {
  var ctx = document.getElementById(chart).getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        data: output_after_snow,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
        borderWidth: 1
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  })
}