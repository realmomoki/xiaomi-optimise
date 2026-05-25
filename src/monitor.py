"""Real-time system monitor for Xiaomi devices."""

import time
import os
from rich.table import Table
from rich.live import Live
from rich.console import Console


class SystemMonitor:
    """Real-time system monitoring dashboard."""

    def __init__(self, adb):
        self.adb = adb
        self.console = Console()

    def _get_stats(self) -> dict:
        return {
            "cpu": self.adb.run_command(
                "top -bn1 | grep CPU | awk '{print $2}'"
            ) or "0%",
            "ram": self.adb.run_command(
                "free -m | grep Mem | awk '{printf \"%d%%\", $3/$2*100}'"
            ) or "0%",
            "battery": self.adb.run_command(
                "dumpsys battery | grep level | awk '{print $3}'"
            ) or "0",
            "temp": self.adb.run_command(
                "cat /sys/class/thermal/thermal_zone0/temp"
            ) or "0",
        }

    def start(self, duration: int = 30):
        """Start real-time monitoring."""
        self.console.print("[cyan]📊 System Monitor — Press Ctrl+C to stop[/cyan]\n")

        try:
            for _ in range(duration * 2):
                stats = self._get_stats()
                table = Table(title="System Status", show_header=True)
                table.add_column("Metric", style="cyan")
                table.add_column("Value", style="green")
                table.add_row("CPU Usage", stats["cpu"])
                table.add_row("RAM Usage", stats["ram"])
                table.add_row("Battery", f"{stats['battery']}%")
                table.add_row("Temperature", f"{int(stats['temp'])/1000:.1f}°C")
                self.console.print(table)
                time.sleep(0.5)
        except KeyboardInterrupt:
            self.console.print("\n[yellow]Monitor stopped.[/yellow]")
