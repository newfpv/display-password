# Display Password (Advanced Fork)  
**Ultimate Cracked Password Aggregator for Pwnagotchi**

A powerful, fully reworked plugin to display recently cracked passwords directly on your Pwnagotchi's e-ink screen.  
Supports multiple sources, smart time-based sorting, better_quickdic integration, and modern displays without breaking your UI.

[🇷🇺 Перевести на русский язык](https://github.com/Newfpv/display-password/blob/main/READMERU.md)

![image](https://github.com/Newfpv/display-password/blob/main/image.webp)

## ⚡ Key Differences from Original
This is a deep refactor of the original `@nagy_craig` and `@vanshksingh` code:
- **Modular Sources:** unlike the original, you can enable/disable specific databases (`wpa_sec`, `ohc`, `better_quickdic`) in your config.
- **Smart Selection (mtime):** the original shows the last line of a single file. This fork compares modification times across ALL sources to show the **absolute newest** password.
- **Better_quickdic Support:** native support for `.pcap.cracked` files. It intelligently extracts the ESSID directly from the filename.
- **Smart Truncation:** if the text is too long, it truncates only the ESSID and adds a dot (`.`), keeping the password fully visible (e.g., `MySuperLongWifi.:password123`).
- **Pure Python:** no more unstable `awk` and `tail` shell pipelines. Native processing means lower CPU usage and zero screen-breaking tracebacks.

## ✨ Features
- **Multi-Source Aggregation:** scans `wpa-sec`, `onlinehashcrack` (OHC), and `better_quickdic`.
- **Modern Display Support:** compatible with Waveshare v2/v3/v4 and Inky.
- **Modern Firmware Paths:** natively searches both `/root/handshakes/` and `/home/pi/handshakes/`.

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
main.plugins.display-password.orientation = "horizontal"

# Optional: Source Toggles (True by default)
main.plugins.display-password.wpa_sec = true
main.plugins.display-password.ohc = true
main.plugins.display-password.better_quickdic = true

# Max characters on screen before truncation
main.plugins.display-password.max_length = 22
```

## 🛠 Troubleshooting
### "No cracked passwords" is stuck on screen
Ensure your handshakes or `.potfile`s are located in `/root/handshakes/` or `/home/pi/handshakes/`. 

## 🤝 Acknowledgments
- **@nagy_craig**, **@vanshksingh**, and **@avipars** — for the original idea and base code.
- **NewFPV** — for the architecture rework, smart-sorting, and modularity.

## 📝 License
GPL3 License.

## ☕ Support
<div align="left"><a href="https://www.donationalerts.com/r/newfpv"><img src="https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-yellow.svg" alt="Donate"></a></div>
