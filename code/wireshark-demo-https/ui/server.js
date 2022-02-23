const fs = require('fs');
const https = require('https');
const express = require('express');

const app = express();
app.use(express.static('static'));
app.get('/', function(req, res) {
    return res.end('<p>This server serves up static files.</p>');
});

const options = {
    key: fs.readFileSync('key.pem', 'utf8'),
    cert: fs.readFileSync('cert.pem', 'utf8'),
};
const server = https.createServer(options, app);

server.listen(8443);