import ssl
import paramiko


host = "172.20.20.2"
username = "gfive"
password = "gfive"



class SSH():
    def __init__(self):
        self.host = "172.20.20.2"
        #default port
        self.port = 22
        self.username = "gfive"
        self.password = "gfive"
        
        
    
    def connect(self):
        # for try
        # port
        # paramiko.ssh_exception.NoValidConnectionsError
        # NoValidConnectionsError(errors)
        # ip invalide  time out
        # timed out

        self.ssh = paramiko.client.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(
            self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            timeout=5
            )

    def change_port(self,port):
        self.port = port
    
    def exec_command(self,command):
        _stdin, _stdout,_stderr = self.ssh.exec_command(command)
        print(_stdout.read().decode())
    
        #print(_stdin.read())
        #print(_stderr.read())

    def close(self):
        self.ssh.close()


client = SSH()
client.connect()
client.exec_command("su -")
client.exec_command("root")
client.exec_command("who")
client.close()