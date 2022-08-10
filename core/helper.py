import sys
import os
import subprocess


def pip_install(module_name):
    """Pip install module

    Args:
        module_name (__str__): Name of the module to install
    """

    print(f"Module '{module_name}' is not installed ! \n Installing ...")
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', module_name])
    print("Finish installation !!!")


def run_shell(cmd):
    """Execute a Shell command on Python
    Args:
        cmd (str): A specific Shell command that need to be execute in the Python enviroment
    """
    # Create a sub process
    proc = subprocess.Popen(cmd, shell=True, stdin=None,
                            stdout=None, stderr=None, executable="/bin/bash")


def apt_install(module_name):
    """Apt install module

    Args:
        module_name (__str__): Name of the module to install
    """

    print(f"Module '{module_name}' is not installed ! \nInstalling ...")
    subprocess.Popen(f'apt-get install -y {module_name}')
    print("Finish installation !!!")
