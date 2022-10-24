const SSH = require('simple-ssh');

var ssh = new SSH({
    host: "172.20.20.2",
    user: "gfive",
    pass: "gfive"
});
var CMD = "cd /var && pwd" 
ssh.exec(CMD, {
    out: function (stdout) { console.log(stdout); },
    err: function (stderr) { console.log(stderr); },
    exit: function (code) { console.log(code); }
}).start();
