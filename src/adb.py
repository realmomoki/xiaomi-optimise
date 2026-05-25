"""ADB connection manager for Xiaomi devices."""

import subprocess
import re
from typing import Optional, Dict


class ADBManager:
    """Manages ADB connection to Xiaomi devices."""

    def __init__(self):
        self.connected = False
        self.device_id = None
        self._check_connection()

    def _check_connection(self):
        """Check if an Android device is connected via ADB."""
        try:
            result = subprocess.run(
                ["adb", "devices"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            lines = result.stdout.strip().split("\n")
            devices = [l for l in lines[1:] if l.strip() and "device" in l]
            if devices:
                self.device_id = devices[0].split("\t")[0]
                self.connected = True
        except (subprocess.TimeoutExpired, FileNotFoundError):
            self.connected = False

    def run_command(self, command: str, timeout: int = 10) -> Optional[str]:
        """Run an ADB shell command and return output."""
        if not self.connected:
            return None
        try:
            result = subprocess.run(
                ["adb", "-s", self.device_id, "shell", command],
                capture_output=True,
                text=True,
                timeout=timeout,
            )
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            return None

    def get_device_info(self) -> Dict:
        """Get device information."""
        return {
            "model": self.run_command("getprop ro.product.model") or "Unknown",
            "codename": self.run_command("getprop ro.product.device") or "unknown",
            "os_version": f"MIUI {self.run_command('getprop ro.miui.ui.version.name') or '?'} (Android {self.run_command('getprop ro.build.version.release') or '?'})",
"battery": int(self.run_command("dumpsys battery | grep level | awk '{print $3}'") or "0"),
            "ram_used": self.run_command("free -m | grep Mem | awk '{print $3}'") or "?",
            "ram_total": self.run_command("free -m | grep Mem | awk '{print $2}'") or "?",
        }

    def push_file(self, local_path: str, remote_path: str) -> bool:
        """Push a file to the device."""
        try:
            subprocess.run(
                ["adb", "-s", self.device_id, "push", local_path, remote_path],
                capture_output=True,
                timeout=30,
            )
            return True
        except subprocess.TimeoutExpired:
            return False
