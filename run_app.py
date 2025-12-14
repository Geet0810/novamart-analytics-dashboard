#!/usr/bin/env python
"""
NovaMart Analytics Dashboard Launcher
Run this script to start the Streamlit dashboard
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    print("=" * 50)
    print("  NovaMart Analytics Dashboard")
    print("=" * 50)
    print()
    print("Starting Streamlit dashboard...")
    print()
    
    # Change to script directory
    os.chdir(script_dir)
    
    # Run streamlit
    try:
        subprocess.run([
            sys.executable, 
            "-m", 
            "streamlit", 
            "run", 
            "app.py"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running dashboard: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()
