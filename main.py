import subprocess

if __name__ == "__main__":
    subprocess.run(["celery", "-A", "app", "worker", "--loglevel=INFO"])