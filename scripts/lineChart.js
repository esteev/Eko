const logUrl = './Data/LogData.json';
var dataPoints = [];

function generateLine(data, variable, cycle) {
    var chart = new CanvasJS.Chart("lineChartContainer", {
        animationEnabled: true,
        title: {
            text: "Log details of " + variable + " in " + cycle
        },
        data: [{
            type: "line",
            dataPoints: data
        }]
    });
    chart.render();
    return chart;
}

function updateLineChart(chart, dataPoints) {
    chart.options.data[0].dataPoints = dataPoints;
    chart.render();
    return chart;
}

function fetchData(cycle = "water_cycle", variable = "Atmosphere") {
    var logData = [];
    fetch(logUrl)
        .then(response => response.json())
        .then(data => {
            z = data[cycle][variable].map(z => parseInt(z));
            logData.push(...z);
        })
        .then(() => {
            dataPoints = logData.map((val, i) => {
                return {
                    x: i,
                    y: val
                }
            });
            chart = flag ? updateLineChart(chart, dataPoints) : generateLine(dataPoints, variable, cycle);
            flag = 1;
        });
}


function generateComponents(cycle) {
    fetch(logUrl)
        .then(response => response.json())
        .then(data => {
            components = [];
            for (x in data[cycle]) {
                components.push(x);
            }
            var options = components.map((comp, i) => {
                return `
                <option value="${ comp }"> ${ comp } </option>
            `;
            }).join('');
            variable.innerHTML = options;
        });
}

function handleCycleSelector(e) {
    generateComponents(this.value);
}

function handleComponentSelector(e) {
    fetchData(cycle.value, this.value);
}

generateComponents('water_cycle');
var flag = 0;
window.setInterval(() => fetchData(), 1000);

const cycle = document.querySelector('.select-cycle');
const variable = document.querySelector('.select-var');

cycle.addEventListener('change', handleCycleSelector);
variable.addEventListener('change', handleComponentSelector);