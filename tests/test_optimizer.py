"""Tests for Xiaomi Optimise."""

import pytest
from unittest.mock import Mock, MagicMock, patch
from src.adb import ADBManager
from src.cpu import CPUOptimizer
from src.battery import BatteryOptimizer
from src.memory import MemoryOptimizer
from src.storage import StorageCleaner


class TestADBManager:
    def test_check_connection(self):
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = Mock(
                stdout="List of devices attached\nABC123\tdevice\n"
            )
            adb = ADBManager()
            assert adb.connected is True
            assert adb.device_id == "ABC123"

    def test_no_connection(self):
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = Mock(
                stdout="List of devices attached\n"
            )
            adb = ADBManager()
            assert adb.connected is False

    def test_run_command(self):
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = Mock(
                stdout="List of devices attached\nABC123\tdevice\n"
            )
            adb = ADBManager()
            mock_run.return_value = Mock(stdout="Xiaomi 14\n")
            result = adb.run_command("getprop ro.product.model")
            assert result == "Xiaomi 14"


class TestCPUOptimizer:
    def test_optimize(self):
        adb = Mock()
        adb.run_command.return_value = "schedutil"
        optimizer = CPUOptimizer(adb)
        result = optimizer.optimize(dry_run=False)
        assert result["success"] is True
        assert "performance" in result["details"]


class TestBatteryOptimizer:
    def test_optimize(self):
        adb = Mock()
        adb.run_command.return_value = "12"
        optimizer = BatteryOptimizer(adb)
        result = optimizer.optimize(dry_run=False)
        assert result["success"] is True


class TestMemoryOptimizer:
    def test_optimize(self):
        adb = Mock()
        adb.run_command.return_value = "150"
        optimizer = MemoryOptimizer(adb)
        result = optimizer.optimize(dry_run=False)
        assert result["success"] is True


class TestStorageCleaner:
    def test_clean(self):
        adb = Mock()
        adb.run_command.return_value = "500MB"
        cleaner = StorageCleaner(adb)
        result = cleaner.clean(dry_run=False)
        assert result["success"] is True
        assert "500MB" in result["details"]
