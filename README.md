# Simple Keylogger Detection Tool

This project monitors your system for suspicious processes and file activity that may indicate keylogger behavior.

## How It Works
- Scans running processes for keywords like `keylog`, `pynput`, `keylog`
- Watches a folder for rapid file changes (keylog simulation)
- Logs all findings to `detection_log.txt`


## Installation

```bash
pip install psutil watchdog pynput


## Run

```bash

# Start the keylogger detection tool
python main.py

# Simulate keylogger activity
python logger_sim.py
