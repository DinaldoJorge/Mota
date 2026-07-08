import sys
from streamlit.web import cli as stcli

if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        "app.py",
        "--server.headless=true",
        "--browser.gatherUsageStats=false",
    ]
    sys.exit(stcli.main())