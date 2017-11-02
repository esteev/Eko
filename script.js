const endpoint = './Data/LogData.json';

function populateLine(cycle = "water_cycle", variable = "Atmosphere") {
    var logData = [];
    fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            z = data[cycle][variable].map(z => parseInt(z));
            logData.push(...z);
        })
        .then(() => {

            var z = [];
            z = logData.map((val, i) => {
                return {
                    x: i,
                    y: val
                }
            });
            var chart = new CanvasJS.Chart("chartContainer", {
                title: {
                    text: "Log details of Atmosphere in " + cycle
                },
                data: [{
                    type: "line",

                    dataPoints: z
                }]
            });
            chart.render();
        });
}

function generateComponents(cycle){
    fetch(endpoint)
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

function handleCycleSelector(e){
    generateComponents(this.value);
}

function handleComponentSelector(e){
    populateLine(cycle.value, this.value);
}

generateComponents('water_cycle');
populateLine();

const cycle = document.querySelector('.select-cycle');
const variable = document.querySelector('.select-var');

cycle.addEventListener('change', handleCycleSelector);
variable.addEventListener('change', handleComponentSelector);