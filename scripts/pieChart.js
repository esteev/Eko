const abioticsUrl = './Data/AbioticsData.json';

const pieChart = document.querySelector('.pieCharts');

function generatePieHTML(x) {
    var html = '';
    for (var i = 0; i < x; i++) {
        html = html.concat('<div id="pieContainer' + i + '" class="col-xs-6" style="height: 300px; width: 300px;"></div>');
    }
    pieChart.innerHTML = html;
}

function generatePies(x, data) {
    generatePieHTML(x);
    var i = 0;
    for (keys in data) {
        var pieData = [];
        for(one in data[keys]['tags']){
	    	pieData.push({y: parseInt(data[keys]['tags'][one]['value']), indexLabel: one});
        }
        id = `pieContainer${i}`;
        var chart = new CanvasJS.Chart(id, {
            backgroundColor: '#002738',
            animationEnabled: true,
            title: {
                fontColor: '#ffffff',
                text: keys,
            },
            data: [{
                indexLabelFontColor: '#ffffff',
                type: "pie",
                dataPoints: pieData
            }]
        });
        chart.render();
        i++;
    }
}

function countCycles() {
    fetch(abioticsUrl)
        .then(response => response.json())
        .then(data => generatePies(Object.keys(data).length, data));
}

countCycles();
