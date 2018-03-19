function plot_bar_chart(data, labels) {
	var ctx = document.getElementById('barChart').getContext('2d');
	var myBarChart = new Chart(ctx, {
		type: 'bar',
		easing: 'easeInQuad',
		data: {
			labels: labels,
			datasets: [
				{
					label: 'Probability Score',
					backgroundColor: 'rgb(52, 152, 219)',
					borderColor: 'rgb(52, 152, 219)',
					data: data
				}
			]
		},
		options: {
			scales: {
				xAxes: [
					{
						scaleLabel: {
							display: true,
							labelString: 'Character'
						},
						ticks: {
							// Include a dollar sign in the ticks
							callback: function(value, index, values) {
								return 'Char - ' + value;
							}
						}
					}
				],
				yAxes: [
					{
						scaleLabel: {
							display: true,
							labelString: 'Probability'
						}
					}
				]
			}
		}
	});
}
