// Map value
function map(x, inMin, inMax, outMin, outMax) {

    return (x - inMin) * (outMax - outMin) / (inMax - inMin) + outMin;
}

// Start here
// Get canvas 2d context to draw on
var dailyActivityCanvas = document.getElementById("daily-activity-canvas");
var dC = dailyActivityCanvas.getContext("2d");

window.onload = function() {

    dailyActivityCanvas.style.width = $("#daily-activity-canvas").parent().width() + "px";
    dailyActivityCanvas.style.height = "128px";
    dailyActivityCanvas.width = $("#daily-activity-canvas").parent().width();
    dailyActivityCanvas.height = 128;

    dC.beginPath();
    dC.moveTo(0, map(dailyActivity[0], minDailyActivity, maxDailyActivity, dailyActivityCanvas.height - 1, 1));

    for (var i = 1; i < dailyActivity.length; i++) {

        dC.lineTo(map(i, 0, dailyActivity.length - 1, 0, dailyActivityCanvas.width),
                  map(dailyActivity[i], minDailyActivity, maxDailyActivity, dailyActivityCanvas.height - 1, 1));
    }

    dC.strokeStyle = "#3491ff";
    dC.stroke();

    dC.fillStyle = "#3491ff";
    dC.font = "12px Open Sans";
    dC.fillText(maxDailyActivity + " Lines", 2, 13);
    dC.fillText(minDailyActivity + " Lines", 2, dailyActivityCanvas.height - 4);

    dC.strokeStyle = "#6eaefa";

    dC.beginPath();
    dC.moveTo(0, dailyActivityCanvas.height - 1);
    dC.lineTo(dailyActivityCanvas.width, dailyActivityCanvas.height - 1);
    dC.stroke();

    dC.beginPath();
    dC.moveTo(0, 1);
    dC.lineTo(dailyActivityCanvas.width, 1);
    dC.stroke();
}
