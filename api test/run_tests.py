import subprocess

if __name__ == "__main__":
    result = subprocess.run(["python", "-m", "pytest"])
    exit(result.returncode)