import subprocess

if __name__ == "__main__":
    result = subprocess.run(["python", "-m", "pytest", "--html=report.html"])
    exit(result.returncode)