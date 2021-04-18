import subprocess

from src.lib import exceptions


def execute_host_command_get_output(command, ignore_status=False):
    """ Execute the given command on host and gives the output

    :param command: command to execute
    :param ignore_status: To check the command execution status
    :return: output
    """
    status, output = subprocess.getstatusoutput(command)
    if not ignore_status:
        if status:
            raise exceptions.TestFail("'%s' command execution failed with status %d" % (command, status))
    return status, output


def is_device_pingable(host):
    """ Checks whether device is pingable

    :param host: device ip address
    :return: bool value either True or False
    """
    status, _ = execute_host_command_get_output("ping %s" % host, ignore_status=True)
    return not status

