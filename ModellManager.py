import subprocess

def download_modell(modell):
    print("Downloading " + modell + "...")
    subprocess.run("ollama pull " + modell)
    print("Done!")


def create_modell(modell):
    print("Configuring modell...")
    subprocess.run("ollama create mc-builder-sb-" + modell + " -f mc-builder-sb.mf")
    print("Done!")