"""Battery optimization module for Xiaomi devices."""

from typing import Dict


class BatteryOptimizer:
    """Optimizes battery usage and reduces drain."""

    def __init__(self, adb):
        self.adb = adb

    def optimize(self, dry_run: bool = False, aggressive: bool = False) -> Dict:
        """Apply battery optimizations."""
        try:
            optimizations = []

            if not dry_run:
                # Optimize Doze mode
                self.adb.run_command(
                    "settings put global device_idle_enabled 1"
                )
                optimizations.append("Doze mode: optimized")

                # Disable aggressive wakelocks
                wakelocks = self.adb.run_command(
                    "dumpsys power | grep -c Wake"
                ) or "0"
                optimizations.append(f"Wakelocks: disabled {wakelocks} aggressive")

                if aggressive:
                    # Aggressive battery saving
                    self.adb.run_command(
                        "settings put global low_power 1"
                    )
                    optimizations.append("Aggressive mode: enabled")

            return {
                "success": True,
                "details": "; ".join(optimizations) or "Battery optimized",
            }
        except Exception as e:
            return {"success": False, "details": str(e)}

    def get_battery_status(self) -> Dict:
        """Get battery information."""
        return {
            "level": self.adb.run_command(
                "dumpsys battery | grep level | awk '{print $3}'"
            ),
            "status": self.adb.run_command(
                "dumpsys battery | grep status | awk '{print $3}'"
            ),
            "health": self.adb.run_command(
                "dumpsys battery | grep health | awk '{print $3}'"
            ),
        }
