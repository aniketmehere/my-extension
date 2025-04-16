import subprocess

def dangerous_function():
    subprocess.call("rm -rf /", shell=True)  # ⚠️ shell=True is unsafe
