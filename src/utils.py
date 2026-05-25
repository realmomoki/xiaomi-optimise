"""Utility functions for Xiaomi Optimise."""

import os
import json
from datetime import datetime
from typing import Dict


def get_log_path() -> str:
    """Get the log directory path."""
    base = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(base, exist_ok=True)
    return base


def save_log(results: Dict, prefix: str = "optimize") -> str:
    """Save optimization results to log file."""
    log_dir = get_log_path()
    filename = f"{prefix}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    filepath = os.path.join(log_dir, filename)
    
    with open(filepath, "w") as f:
        json.dump(results, f, indent=2)
    
    return filepath


def format_bytes(size: int) -> str:
    """Format bytes to human readable string."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"
