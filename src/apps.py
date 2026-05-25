"""App manager module for Xiaomi devices."""

import json
import os
from typing import Dict, List


class AppManager:
    """Manages apps — debloat, freeze, and backup."""

    BLOATWARE_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "bloatware_list.json")

    def __init__(self, adb):
        self.adb = adb
        self.bloatware = self._load_bloatware()

    def _load_bloatware(self) -> List[str]:
        """Load list of known bloatware packages."""
        try:
            with open(self.BLOATWARE_PATH) as f:
                return json.load(f).get("packages", [])
        except FileNotFoundError:
            return []

    def debloat(self, dry_run: bool = False) -> Dict:
        """Freeze/disable bloatware apps."""
        frozen = 0
        for pkg in self.bloatware:
            if not dry_run:
                self.adb.run_command(f"pm disable-user --user 0 {pkg}")
            frozen += 1

        backup_path = os.path.join(
            os.path.dirname(__file__), "..", "logs", "debloat_backup.json"
        )
        with open(backup_path, "w") as f:
            json.dump({"frozen": self.bloatware}, f, indent=2)

        return {
            "frozen": frozen,
            "backup_path": backup_path,
        }
