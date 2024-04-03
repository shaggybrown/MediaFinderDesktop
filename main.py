"""
The main entry point for the MediaFinder Desktop application. This script initializes
the application, setting up the necessary configurations and launching the graphical
user interface. It ties together functionalities from the backend and frontend modules
to provide a seamless user experience for managing and exploring media libraries.
"""
from frontend.app_gui import main as start_gui

# main.py

if __name__ == "__main__":
    print("MediaFinder Desktop is starting up...")
    start_gui()
