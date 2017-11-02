const abioticsUrl = './Data/AbioticsData.json';

const pieChart = document.querySelector('.pieCharts');

function generatePieHTML(x) {
    console.log(x);
    var html = '';
    for (var i = 0; i < x; i++) {
    	html = html.concat('<div id="pieContainer' + i + '" class="col-xs-6" style="height: 300px; width: 300px;"></div>');
	    console.log(html);
    }
    console.log(html);
    pieChart.innerHTML = html;
}

function generatePies(x) {
    generatePieHTML(x);
    for (var i = 0; i < x; i++) {
    	id = `pieContainer${i}`;
        var chart = new CanvasJS.Chart(id, {
        	backgroundColor: '#002738',
        	animationEnabled: true,
            title: {
    			fontColor: '#ffffff',
                text: "EkO ka pie chart"
            },
            data: [{
	        	indexLabelFontColor: '#ffffff',
                type: "pie",
                dataPoints: [
                    { y: 90, indexLabel: "kuchKuch" },
                    { y: 90, indexLabel: "Atmoshpere" },
                    { y: 90, indexLabel: "unUsed" },
                    { y: 90, indexLabel: "Hydrosphere" }
                ]
            }]
        });
        chart.render();
        console.log("Generating Pie " + i);
    }
}

generatePies(5);
