import time
from pssh.clients import SSHClient

from src.lib import shell
from src.lib import exceptions


class RemoteDevice:
    """Remote device instance"""

    _WAIT_TIME = 10

    def __init__(self, host, username, password, port=22):
        """ Create the SSH instance and returns the object

        :param host: Device IP or Hostname
        :param username: username
        :param password: password
        :param port: ssh port
        :return: instance of ssh connection
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.device = SSHClient(self.host, user=self.username, password=self.password, port=self.port)

    def wait_for_remote(self, timeout=60):
        """Wait for the remote device up"""
        start_time = time.time()
        while time.time() - start_time <= timeout:
            print("Waiting for device to be online")
            if shell.is_device_pingable(self.host):
                print("device is up")
                return
            time.sleep(self._WAIT_TIME)
        raise exceptions.TestError("%s is not up" % self.host)


