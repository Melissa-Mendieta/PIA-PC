import subprocess
comando = "status.ps1"
lineaPS = "powershell -Executionpolicy ByPass -File "+ comando
runningProcesses = subprocess.check_output(lineaPS)
print(runningProcesses.decode('utf-8', 'ignore'))
