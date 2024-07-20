from src.lib.device import RemoteDevice

d = RemoteDevice("192.168.1.106", "kbogineni", "pass)
d.wait_for_remote()

