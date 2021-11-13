from os import error
import subprocess

def Ps1():
    try:
        comando = "status.ps1"
        lineaPS = "powershell -Executionpolicy ByPass -File "+ comando
        runningProcesses = subprocess.check_output(lineaPS)
        print(runningProcesses.decode('utf-8', 'ignore'))
    except subprocess.CalledProcessError as e:
        output = e.output
