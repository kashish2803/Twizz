
// The percentages of sentiments
var ppercent = $('#ppercent').data();
var npercent = $('#npercent').data();
var neutral = $('#neutral').data();

// Pie chart
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Negative', 'Positive', 'Neutral'],
        datasets: [{
            label: '# of Votes',
            data: [npercent.name, ppercent.name, neutral.name],
            backgroundColor: ["#F7464A", "#46BFBD", "#FDB45C"],
            hoverBackgroundColor: ["#FF5A5E", "#5AD3D1", "#FFC870"],
            borderWidth: 1
        }]
    },
    options: {
        responsive: false
      }
});
