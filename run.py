"""SafeOption AI v3.1.3 Freeze Candidate — Launcher"""
import subprocess, sys, os

def main():
    app = os.path.join(os.path.dirname(__file__), "app", "streamlit_app.py")
    subprocess.run([sys.executable, "-m", "streamlit", "run", app,
                    "--server.headless", "true"])

if __name__ == "__main__":
    main()
