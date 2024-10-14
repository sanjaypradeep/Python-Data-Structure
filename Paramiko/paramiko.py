# below code needs to be refactored to a bigger level

import paramiko
from paramiko import AUTH_SUCCESSFUL, AUTH_FAILED
from paramiko import (
    SSHException,
    AuthenticationException,
    BadAuthenticationType,
    PartialAuthentication,
)

class CustomParamiko:
    def __init__(self, hostname, username, paassword):
        self.hostname = hostname
        self.username = username
        self.password = paassword
    
    def connectToHost(self):
        try:
            ssh_client=paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=self.hostname,username=self.username,password=self.password)

            return {AUTH_SUCCESSFUL: "Connected Successfully"}
        except (SSHException, AuthenticationException, BadAuthenticationType) as e:
            print(e.with_traceback)
            return {AUTH_FAILED: "Failed to Connect"}        

    def runCommand(self, commandToExecute):
        if commandToExecute == '' or len(commandToExecute) == 0 :
        raise Exception
        try:
            result = ssh_client.exec_command(commandToExecute)
            return result
        except Exception as e:
            print(e)
    
    def downloadFileFromRemote(self, remoteFilePath, localFilePath):
        ftp_client=ssh_client.open_sftp()
        ftp_client.get(remoteFilePath,localFilePath)
        # not sure do I need to close the connection or not. 
        ftp_client.close()

    def uploadFileFromLocal(self, localFilePath, remoteFilePath):
        ftp_client=ssh.open_sftp()
        ftp_client.put(localFilePath,remoteFilePath)
        # not sure do I need to close the connection or not. 
        ftp_client.close()


    def closeConnection(self):
        ssh_client.close()
