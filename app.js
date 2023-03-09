const express = require('express');
const ejs = require("ejs");
const bodyParser = require('body-parser');
const {spawn} = require('child_process');

const app = express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

// let x = [7.5, 17.3, 30.6, 40.2, 49.5, 62.6, 68.3, 78.6, 87.5, 98.6];
let x = [98.6, 87.5, 78.6, 68.3, 62.6, 49.5, 40.2, 30.6, 17.3, 7.5];
// let y =  [695, 719, 750, 773, 798, 830, 843, 870, 892, 920];
let y = [920, 892, 870, 843, 830, 798, 773, 750, 719, 695];

app.get('/', (req, res) => {
    const python1 = spawn("python3", ["script1.py", x, y], {detached: true,});
    const python2 = spawn("python3", ["script2.py", x, y], {detached: true,});
    python1.stdout.on('data', function (absolute_zero) {
        python2.stdout.on('data', function (equation) {
            res.render("chart", {equation: equation, absolute_zero: absolute_zero, step: 0});
        });
    });
    
})

app.get("/set_values", (req, res) => {
    const data = [[], []];
    x.forEach((value) => data[0].push(value));
    y.forEach((value) => data[1].push(value));
    res.render("set-values", {data: data, step: 1})
})

app.get("/about", (req, res) => {
    res.render("about", {step: 1})
})

app.post("/set_values", (req, res) => {
    rec_x = req.body.temp;
    rec_y = req.body.pressure;

    x = [];
    y = [];

    rec_x.forEach((value) => {
        x.push(+value);
    })
    rec_y.forEach((value) => {
        y.push(+value);
    })
    res.redirect("/");
})

// Express App listens on localhost:3000
app.listen(3000, function() {
    console.log("Server successfully started on port 3000");
});