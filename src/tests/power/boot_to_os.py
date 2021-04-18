from src.lib.device import RemoteDevice

d = RemoteDevice("192.168.1.106", "kbogineni", "password")
d.wait_for_remote()

