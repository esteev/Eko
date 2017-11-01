const endpoint = './Data/LogData.json';

function populateLine(cycle = "water_cycle", variable = "Atmosphere") {
    var logData = [];
    fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            console.log(cycle);
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
            console.log(z);
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

function handleCycleSelector(e){
    // console.log(e);
    // console.log(this.value);
    populateLine(this.value, "Hydrosphere");
}

populateLine();

const cycle = document.querySelector('.select-cycle');
const variable = document.querySelector('.select-var');

console.log(cycle.value);

cycle.addEventListener('change', handleCycleSelector);