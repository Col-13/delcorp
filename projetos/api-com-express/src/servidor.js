const porta = 3003

const express = require('express')
const app = express()

app.get('/produtos', (req, res, next) => {
    res.send({nome: 'ventilador', preco: 203.54})
})

app.listen(porta, () => {
    console.log(`Servidor executando na porta ${porta}.`)
})