import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Todo esta correcto, ya puedes iniciar tu proyecto{RESET_ALL}")

subprocess.call(["git","init"])
subprocess.call(["git", "add", "."])
subprocess.call(["git","commit", "-m", "initial commit"])

#subprocess.call(["conda", "update", "-n", "base", "-c", "defaults", "conda"])

#subprocess.call(["conda", "env", "create", "-f", "environment.yml"])

print(f"{MESSAGE_COLOR}Tu repositorio GIT fue iniciado{RESET_ALL}")