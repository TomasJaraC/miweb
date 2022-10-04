import re
import subprocess

def gmail_finder(mail):
    patron = r"\b[\w.-]+@gmail.com"
    resultado = re.search(patron,mail)
    
    if resultado is None:
        return "No es gmail"
    return resultado[0]


print(gmail_finder("tomas_tuprofeonline@gmail.com"))

subprocess.run(["date"])
