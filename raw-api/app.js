const express = require("express");
const app = express();
const morgan = require("morgan");
const bodyParser = require("body-parser");

const rotaSismico = require("./routes/seismic");

app.use(morgan("dev")); //Monitora a execução gerando um log
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json()); // Json de entrada no body

app.use((request, response, next) => {
    response.header("Acces-Control-Allow-Origin", "*");
    response.header(
        "Acces-Control-Allow-Header", 
        "Origin, X-Requested-With, Content-Type, Accept, Authorization"
    );
    if(request.method == "OPTIONS") {
        response.header("Acces-Control-Allow-Methods", "PUT, POST, PATCH, DELETE, GET");
        return response.status(200).send({});
    }
    next();
})

app.use("/SeismicData", rotaSismico);

// Quando não encontra rota, entra aqui
app.use((request, response, next) => {
    const erro = new Error("Não encontrado");
    erro.status = 404;
    next(erro);
});

app.use((error, request, response, next) => {
    response.status(error.status || 500);
    return response.send({
        erro: {
            mensagem: error.message
        }
    });
});

module.exports = app;