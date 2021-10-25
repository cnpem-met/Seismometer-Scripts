const express = require("express");
const router = express.Router();
const fs = require("fs");

function fourierTransform(channel, initialDateTime, endDateTime){
    var fourierTransform = [];
    var defaultPath = "/home/reftek/bin/archive/FourierRec/";
    var data = channel + ";" + initialDateTime + ";" + endDateTime;
    data = fs.writeFileSync((defaultPath + "request.txt"), data);
    outputFile = defaultPath + channel + ";" + initialDateTime + ";" + endDateTime + "-complete.txt";
    while(!fs.existsSync(outputFile)); // Wait the file be create;
    data = fs.readFileSync(outputFile, "utf8");
    fs.unlinkSync(outputFile)
    data = data.split("\n");
    for(var j = 0; j < data.length; j++)
        fourierTransform.push(parseFloat(data[j]));
    return fourierTransform;
}

// Retorna todos os produtos
router.get("/:channel/:initialDate/:endDate", (request, response) => {
    var channel = request.params.channel;
    var initialDate = request.params.initialDate;
    var endDate = request.params.endDate;
    var fft = fourierTransform(channel, initialDate, endDate)
    response.status(200).send({
        frequencies: fft
    });
});

module.exports = router;