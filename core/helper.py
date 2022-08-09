def pip_install(module_name):
    """Pip install module

    Args:
        module_name (__str__): Name of the module to install
    """
    import sys
    import subprocess

    print(f"Module '{module_name}' is not installed ! \n Installing ...")
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', module_name])
    print("Finish installation !!!")
