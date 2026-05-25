"""Storage cleanup module for Xiaomi devices."""

from typing import Dict


class StorageCleaner:
    """Cleans junk files and frees storage space."""

    def __init__(self, adb):
        self.adb = adb

    def clean(self, dry_run: bool = False) -> Dict:
        """Clean junk files."""
        try:
            freed_bytes = 0

            if not dry_run:
                # Clear app caches
                self.adb.run_command("pm cache-clear --all")
                # Clear log files
                self.adb.run_command("rm -rf /data/log/*")
                # Clear temp files
                self.adb.run_command("rm -rf /data/local/tmp/*")

            freed = self.adb.run_command(
                "du -sh /data/cache 2>/dev/null | awk '{print $1}'"
            ) or "0MB"

            return {
                "success": True,
                "details": f"{freed} freed from cache and temp files",
            }
        except Exception as e:
            return {"success": False, "details": str(e)}
