import unittest
from src.lib.device import RemoteDevice


class DeviceTest(unittest.TestCase):
    HOST = "192.168.1.106"
    USER = "kbogineni"
    PASSWORD = "password"

    def test_values(self):
        d = RemoteDevice(self.HOST, self.USER, self.PASSWORD)
        self.assertRaises(ValueError, d.wait_for_remote, -20)
