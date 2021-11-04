const express = require("express");
const router = express.Router();
const fs = require("fs");

function whichFilesINeed(canal, initialDateTime, endDateTime) {
    var path = [];
    initialDateTime = new Date(parseFloat(initialDateTime) * 1000);
    endDateTime = new Date(parseFloat(endDateTime) * 1000);
    initialYear = initialDateTime.getFullYear();
    initialDayOfYear = Math.floor((initialDateTime - new Date(initialDateTime.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
    initialHour = initialDateTime.getHours();
    
    endYear = endDateTime.getFullYear();
    endDayOfYear = Math.floor((endDateTime - new Date(endDateTime.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
    endHour = endDateTime.getHours();

    while(initialYear <= endYear){
        while(initialDayOfYear <= endDayOfYear){
            while(initialHour <= 23 && (initialHour <= endHour || initialDayOfYear < endDayOfYear)){
                path.push(`${initialYear}/${initialDayOfYear}/${canal}/${initialHour}.txt`);
                initialHour++;
            }
            initialHour = 0;
            initialDayOfYear++;
        }
        initialYear++;
    }
    
    return path
}

function readFilesINeed(path, initialDateTime, endDateTime){
    defaultPath = "/home/reftek/bin/archive/SeismicData/"
    seismicData = [];

    from = new Date(parseFloat(initialDateTime) * 1000);
    to = new Date(parseFloat(endDateTime) * 1000);
    timeData = [
        from.getTime()/1000,
        to.getTime()/1000
    ];

    for(var i = 0; i < path.length; i++){
        prop = path[i];
        data = fs.readFileSync((defaultPath + prop), "utf8");
        data = data.split("\n");
        for(var j = 0; j < data.length; j++){
            acq = data[j].split(": ");
            if(parseFloat(acq[0]) >= parseFloat(initialDateTime) && parseFloat(acq[0]) <= parseFloat(endDateTime)){
                seismicData.push(Math.round(parseFloat(acq[1]) * (10**10))/(10**10));
            } else
                break;
        }
    }
    
    return [seismicData, timeData];    
}

// Retorna todos os produtos
router.get("/:channel/:initialDate/:endDate", (request, response) => {
    var channel = request.params.channel;
    var initialDate = request.params.initialDate;
    var endDate = request.params.endDate;
    var path = whichFilesINeed(channel, initialDate, endDate);
    var [seismicData, timeData] = readFilesINeed(path, initialDate, endDate);
    response.status(200).send({
        time: timeData,
        magnitude: seismicData
    });
});

module.exports = router;