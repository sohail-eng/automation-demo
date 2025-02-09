# Automation Script

## Overview
This project provides an automated solution for logging into Gmail and performing a Google search, followed by signing out, using Playwright for browser automation. The script connects to a running Chrome instance using remote debugging and handles the login, search, and sign-out processes.

## Features
- Logs into Gmail using provided email and password
- Performs a Google search with a specified query
- Signs out of the Gmail account after the search
- Supports interacting with Chrome through Playwright and remote debugging

## Prerequisites

### System Requirements
- Python 3.8+
- pip (Python package manager)

### Dependencies
The following Python libraries are required for this project:
- **playwright**: For browser automation
- **logging**: For logging errors and information
- **csv**: If working with CSV input for bulk lesson data (can be adapted based on project)

### Prepare data
Create `data.,csv` file in the project directory and write email and password in this file

Install the dependencies by running:

```bash
pip install -r requirements.txt
```

### Start Project
Run this command on terminal to start google chrome in debug mode, this will works for ubantu, you can search for your related systemd

```bash
google-chrome --remote-debugging-port=9223 --user-data-dir=$HOME/chrome-debug
```
After running this command first time, you should setting up chrome to proceed any intial process that required to start chrome for the first time.

Run Script
```bash
python run_main.py
```
