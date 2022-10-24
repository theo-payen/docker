
const SSH = require('simple-ssh');

function fssh(host,port, user ,password){

	console.log('inside the system')
	console.log(host,user,password)
	var ssh = new SSH({
	    host: host,
		port: port,
	    user: user,
	    pass: password
	});
	// execute the df -h command to find out disk utilization

		ssh.exec('pwd && ls -l', {
			out: function(stdout) {
				console.log(stdout);
			}
		}).start();

}
fssh("172.20.20.2","22","gfive","gfive")