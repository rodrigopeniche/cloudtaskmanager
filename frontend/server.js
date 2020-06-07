var static = require('node-static');
var http = require('http');

var fileServer = new(static.Server)

http.createServer(function (req, res) {
    fileServer.serveFile('/index.html', 500, {}, req, res);
}).listen(8081);