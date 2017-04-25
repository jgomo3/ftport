import ftplib

class FTP(ftplib.FTP):

    def __init__(self, ftp_port=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ftp_port = ftp_port
        self.set_pasv(not self.ftp_port)

    def sendport(self, host, port):
        return super().sendport(self.ftp_port or host, port)
