var express = require('express');
var app = express();

app.use(express.static('www'));

app.get('/data', function(req, res) {
  res.json({
    file: 'test.json',
    list: [
      'data',
      'more_data'
    ]
  });
});

var server = app.listen(8000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
