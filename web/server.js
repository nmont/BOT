var fs = require("fs");
var express = require('express');
var app = express();

app.use(express.static('www'));

app.get('/data', function(req, res) {
  var content = fs.readFileSync("./sample.json");
  console.log(content);
  var jsoncontent = JSON.parse(content);
  console.log(jsoncontent);
  res.json(jsoncontent);
});

var server = app.listen(8000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
