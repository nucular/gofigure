// Map value
function map(x, inMin, inMax, outMin, outMax) {

    return (x - inMin) * (outMax - outMin) / (inMax - inMin) + outMin;
}

// Start here
// Get canvas 2d context to draw on
var dailyActivityCanvas = document.getElementById("daily-activity-canvas");
var dC = dailyActivityCanvas.getContext("2d");

var averageActivityCanvas = document.getElementById("average-activity-canvas");
var aC = averageActivityCanvas.getContext("2d");

window.onload = function() {

    dailyActivityCanvas.style.width = $("#daily-activity-canvas").parent().width() + "px";
    dailyActivityCanvas.style.height = "128px";
    dailyActivityCanvas.width = $("#daily-activity-canvas").parent().width();
    dailyActivityCanvas.height = 128;

    averageActivityCanvas.style.width = $("#average-activity-canvas").parent().width() + "px";
    averageActivityCanvas.style.height = "128px";
    averageActivityCanvas.width = $("#average-activity-canvas").parent().width();
    averageActivityCanvas.height = 128;

    dC.beginPath();
    dC.moveTo(0, map(dailyActivity[0], minDailyActivity, maxDailyActivity, dailyActivityCanvas.height - 14, 14));

    for (var i = 1; i < dailyActivity.length; i++) {

        dC.lineTo(map(i, 0, dailyActivity.length - 1, 0, dailyActivityCanvas.width),
                  map(dailyActivity[i], minDailyActivity, maxDailyActivity, dailyActivityCanvas.height - 14, 14));
    }

    dC.strokeStyle = "#3491ff";
    dC.stroke();

    dC.fillStyle = "#3491ff";
    dC.font = "12px Open Sans";
    dC.fillText(maxDailyActivity + " Lines", 2, 11);
    dC.fillText(minDailyActivity + " Lines", 2, dailyActivityCanvas.height - 2);

    dC.strokeStyle = "#6eaefa";

    dC.beginPath();
    dC.moveTo(0, dailyActivityCanvas.height - 14);
    dC.lineTo(dailyActivityCanvas.width, dailyActivityCanvas.height - 14);
    dC.stroke();

    dC.beginPath();
    dC.moveTo(0, 14);
    dC.lineTo(dailyActivityCanvas.width, 14);
    dC.stroke();

    aC.beginPath();
    aC.moveTo(0, map(averageActivity[0], minAverageActivity, maxAverageActivity, averageActivityCanvas.height - 14, 14));

    for (var i = 1; i < averageActivity.length; i++) {

        aC.lineTo(map(i, 0, averageActivity.length - 1, 0, averageActivityCanvas.width),
                  map(averageActivity[i], minAverageActivity, maxAverageActivity, averageActivityCanvas.height - 14, 14));
    }

    aC.strokeStyle = "#3491ff";
    aC.stroke();

    aC.fillStyle = "#3491ff";
    aC.font = "12px Open Sans";
    aC.fillText(maxAverageActivity + " Lines", 2, 11);
    aC.fillText(minAverageActivity + " Lines", 2, averageActivityCanvas.height - 2);

    aC.strokeStyle = "#6eaefa";

    aC.beginPath();
    aC.moveTo(0, averageActivityCanvas.height - 14);
    aC.lineTo(averageActivityCanvas.width, averageActivityCanvas.height - 14);
    aC.stroke();

    aC.beginPath();
    aC.moveTo(0, 14);
    aC.lineTo(averageActivityCanvas.width, 14);
    aC.stroke();
}
