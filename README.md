# Display Password (Advanced Fork)  
**Ultimate Cracked Password Aggregator for Pwnagotchi**

A powerful, fully reworked plugin to display recently cracked passwords directly on your Pwnagotchi's e-ink screen.  
Supports multiple sources, smart time-based sorting, better_quickdic integration, and modern displays without breaking your UI.

[🇷🇺 Перевести на русский язык](https://github.com/Newfpv/display-password/blob/main/READMERU.md)

![image](https://github.com/Newfpv/display-password/blob/main/image.webp)

## ✨ Features
- **Multi-Source Aggregation:** automatically scans multiple databases including `wpa-sec`, `onlinehashcrack` (OHC), and local bruteforce files (`*.pcap.cracked`) from **better_quickdic**.
- **Smart Selection (mtime):** compares file modification times to *always* display the absolute newest cracked password, regardless of the tool used.
- **better_quickdic Support:** intelligently extracts the ESSID directly from the filename (e.g., `MyWiFi_AA:BB:CC:DD.pcap.cracked`) since the file only contains the password.
- **Modern Display Support:** fully compatible with Waveshare v3, Waveshare v4, and standard e-ink displays.
- **Pure Python Parsing:** completely removed unstable `awk` and `tail` bash pipelines in favor of native Python processing for lower CPU usage and higher stability.
- **Clean UI:** no more ugly tracebacks (`Error: file not found...`) ruining your e-ink layout. Shows a clean "No cracked passwords" if databases are empty.
- **Modern Firmware Paths:** natively searches both `/root/handshakes/` and `/home/pi/handshakes/` (perfect for Jayofelony / Aluminum-Ice images).

## 🚀 Installation
```bash
ssh pi@10.0.0.2
cd /usr/local/share/pwnagotchi/custom-plugins/
sudo wget [https://raw.githubusercontent.com/Newfpv/display-password/main/display-password.py](https://raw.githubusercontent.com/Newfpv/display-password/main/display-password.py)
sudo nano /etc/pwnagotchi/config.toml
```
Add plugin config:
```toml
main.plugins.display-password.enabled = true
# Optional: text output orientation (horizontal by default)
main.plugins.display-password.orientation = "horizontal"
```
Restart:
```bash
sudo systemctl restart pwnagotchi
```

## 🛠 Troubleshooting
### "No cracked passwords" is stuck on screen
Ensure your handshakes or `.potfile`s are located in `/root/handshakes/` or `/home/pi/handshakes/`. The plugin checks these directories automatically. 

### UI Layout is Broken / Text Overflow
If a cracked password or ESSID is exceptionally long, the plugin safely truncates it to prevent breaking the e-ink screen layout.

## 🤝 Acknowledgments
- **@nagy_craig**, **@vanshksingh**, and **@avipars** — for the original idea and base code of the plugin.
- **NewFPV** (and contributors) — for the complete architecture rework, better_quickdic support, and mtime sorting algorithm.

## 📝 License
This project is licensed under the GPL3 License.

## ☕ Support
<div align="left"><a href="https://www.donationalerts.com/r/newfpv"><img src="https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-yellow.svg" alt="Donate"></a></div>