import os
import sys
import json
import time
import subprocess
import re
import yaml
from datetime import datetime, timezone

# Configuration
API_KEY = os.environ.get("ANTHROPIC_API_KEY")
MODELS = [
    "claude-3-5-sonnet-latest",
    "claude-3-5-haiku-latest",
]
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_FILE = os.path.join(SCRIPT_DIR, "task.yaml")
ARTIFACTS_DIR = os.getcwd()

def log_event(event_type, content, **kwargs):
    """Log event to agent.log in JSONL format."""
    log_file = os.path.join(ARTIFACTS_DIR, "agent.log")
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "type": event_type,
        "content": content
    }
    entry.update(kwargs)
    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")

def run_command(command, cwd=None, log_file=None):
    """Execute a bash command and return its output."""
    print(f"Executing: {command}")
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = f"/testbed:/testbed/vendor/infogami:{env.get('PYTHONPATH', '')}"
        
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=cwd,
            env=env
        )
        output = result.stdout
