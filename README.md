# ⚡ Xiaomi Optimise

> Advanced system optimizer for Xiaomi / MIUI / HyperOS devices. Boost performance, save battery, and clean junk — all from your terminal.

![Xiaomi Optimise](https://img.shields.io/badge/Platform-Android-3DDC84?style=flat-square&logo=android)
![Version](https://img.shields.io/badge/Version-2.0.0-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🔍 What is Xiaomi Optimise?

**Xiaomi Optimise** is a Python-based CLI tool that optimizes Xiaomi, Redmi, and POCO devices running MIUI or HyperOS. It automates system tuning, battery optimization, memory management, and junk cleanup — things that usually require root access or complex ADB commands.

### Key Features

| Feature | Description |
|---------|-------------|
| 🚀 **Performance Boost** | Optimize CPU governor, I/O scheduler, and kernel parameters |
| 🔋 **Battery Saver** | Disable wakelocks, optimize Doze mode, reduce background drain |
| 🧹 **Junk Cleaner** | Clear cache, logs, and temporary files safely |
| 📱 **App Manager** | Debloat pre-installed apps, freeze bloatware |
| 🌡️ **Thermal Control** | Monitor and manage thermal throttling |
| 💾 **Memory Optimizer** | Kill background processes, optimize RAM usage |
| 📊 **System Monitor** | Real-time CPU, RAM, battery, and storage stats |
| 🔄 **Auto Optimise** | Schedule automatic optimization tasks |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/realmomoki/xiaomi-optimise.git
cd xiaomi-optimise

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x xiaomi_optimise.py
```

### Requirements

- Python 3.8+
- ADB (Android Debug Bridge) installed
- USB Debugging enabled on your Xiaomi device
- Device connected via USB or wireless ADB

---

## 🚀 Usage

### Basic Commands

```bash
# Run full optimization
python xiaomi_optimise.py --optimize

# Battery optimization only
python xiaomi_optimise.py --battery

# Clean junk files
python xiaomi_optimise.py --clean

# Debloat apps
python xiaomi_optimise.py --debloat

# System monitor
python xiaomi_optimise.py --monitor

# Thermal control
python xiaomi_optimise.py --thermal
```

### Advanced Options

```bash
# Custom CPU governor
python xiaomi_optimise.py --cpu-governor performance

# Aggressive battery saving
python xiaomi_optimise.py --battery --aggressive

# Dry run (preview changes)
python xiaomi_optimise.py --optimize --dry-run

# Export optimization log
python xiaomi_optimise.py --optimize --log output.log

# Schedule auto-optimization (every 6 hours)
python xiaomi_optimise.py --schedule 6h
```

---

## 📊 Example Output

```
⚡ Xiaomi Optimise v2.0.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📱 Device: Xiaomi 14 (houji)
🤖 OS: HyperOS 1.0.3.0 (Android 14)
🔋 Battery: 87% (Charging)
💾 RAM: 4.2GB / 12GB (35%)
📦 Storage: 68.4GB / 256GB (27%)

━━━ Optimization Results ━━━

✅ CPU governor: schedutil → performance (+15% speed)
✅ I/O scheduler: cfq → bfq (better throughput)
✅ Doze mode: optimized (background drain -40%)
✅ Wakelocks: disabled 12 aggressive wakelocks
✅ Cache cleared: 1.2GB freed
✅ Background apps: 23 processes killed
✅ Thermal: monitoring active
✅ Debloat: 15 apps frozen

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 Optimization complete! +28% performance boost
📁 Log saved: logs/optimize_2026-05-25.log
```

---

## 🏗️ Project Structure

```
xiaomi-optimise/
├── xiaomi_optimise.py      # Main entry point
├── requirements.txt        # Python dependencies
├── src/
│   ├── __init__.py
│   ├── adb.py             # ADB connection manager
│   ├── cpu.py             # CPU optimization
│   ├── battery.py         # Battery optimization
│   ├── memory.py          # Memory/RAM optimizer
│   ├── storage.py         # Storage/junk cleaner
│   ├── thermal.py         # Thermal management
│   ├── apps.py            # App manager/debloat
│   ├── monitor.py         # System monitor
│   └── utils.py           # Utility functions
├── assets/
│   └── bloatware_list.json  # Known bloatware apps
├── logs/                  # Optimization logs
├── tests/                 # Unit tests
└── README.md
```

---

## 🛡️ Safety

- **No root required** for most features (ADB-based)
- **Backup before debloat** — tool creates restore point
- **Dry run mode** — preview changes before applying
- **Rollback support** — undo any optimization
- **Safe defaults** — won't brick your device

---

## 📱 Supported Devices

| Brand | Models | OS |
|-------|--------|-----|
| Xiaomi | 14, 13, 12, 11, Mi 10 series | MIUI 14+, HyperOS |
| Redmi | Note 13, 12, 11 series | MIUI 14+, HyperOS |
| POCO | F6, X6, M6 series | MIUI 14+, HyperOS |

---

## 🤝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## ⭐ Support

If this project helped you, give it a ⭐ on GitHub!
