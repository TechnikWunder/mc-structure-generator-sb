import subprocess

print("Installing requirements...")
subprocess.run("pip install -r requirements.txt")
subprocess.run("pip3 install -r requirements.txt")
print("Done")