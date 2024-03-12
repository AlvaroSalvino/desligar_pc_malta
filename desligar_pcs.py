import os
import subprocess

# Endereço IP do computador que você deseja desligar
ip = "192.168.254.51"

# O comando 'shutdown' pode ser usado para desligar ou reiniciar um computador
command = f"shutdown /s /m /f \\\\{ip} /t 0"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
