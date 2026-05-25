"""Thermal management module for Xiaomi devices."""

from typing import Dict


class ThermalManager:
    """Monitors and manages thermal throttling."""

    def __init__(self, adb):
        self.adb = adb

    def optimize(self, dry_run: bool = False) -> Dict:
        """Apply thermal optimizations."""
        try:
            if not dry_run:
                # Set thermal mitigation to balanced
                self.adb.run_command(
                    "settings put global thermal_mitigation_level 0"
                )

            return {
                "success": True,
                "details": "Thermal: monitoring active, balanced mode",
            }
        except Exception as e:
            return {"success": False, "details": str(e)}

    def get_status(self) -> Dict:
        """Get thermal sensor readings."""
        sensors = {}
        for i in range(10):
            temp = self.adb.run_command(
                f"cat /sys/class/thermal/thermal_zone{i}/temp"
            )
            if temp:
                try:
                    sensors[f"zone{i}"] = int(temp) / 1000
                except ValueError:
                    pass
        return {"sensors": sensors}
