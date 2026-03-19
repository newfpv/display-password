# Display Password (Advanced Fork)  
**Ультимативный агрегатор взломанных паролей для Pwnagotchi**

Мощный, полностью переработанный плагин для отображения недавно взломанных паролей прямо на e-ink экране вашего Pwnagotchi.  
Поддерживает несколько источников, умную сортировку по времени, интеграцию с better_quickdic и современные дисплеи без поломки интерфейса.

[🇬🇧 View in English](https://github.com/Newfpv/display-password/blob/main/README.md)

![image](https://github.com/Newfpv/display-password/blob/main/image.webp)

## ✨ Возможности
- **Мульти-источники:** автоматически сканирует несколько баз данных, включая `wpa-sec`, `onlinehashcrack` (OHC) и файлы локального брутфорса (`*.pcap.cracked`) от **better_quickdic**.
- **Умный выбор (mtime):** сравнивает время изменения файлов, чтобы *всегда* выводить на экран самый свежий взломанный пароль, независимо от того, каким инструментом он был получен.
- **Поддержка better_quickdic:** плагин умеет на лету вытаскивать имя сети (ESSID) прямо из названия файла (например, `MyWiFi_AA:BB:CC:DD.pcap.cracked`), так как внутри хранится только сам пароль.
- **Поддержка современных дисплеев:** полная совместимость с Waveshare v3, Waveshare v4 и стандартными экранами.
- **Чистый Python:** полный отказ от нестабильных bash-конвейеров `awk` и `tail` в пользу нативной обработки на Python. Это снижает нагрузку на CPU и повышает стабильность работы.
- **Чистый UI:** никаких ломающих верстку трейсбеков (`Error: file not found...`) на экране. Если паролей пока нет — выводится аккуратное "No cracked passwords".
- **Современные пути прошивок:** встроенный поиск файлов как в `/root/handshakes/`, так и в `/home/pi/handshakes/` (идеально для сборок Jayofelony / Aluminum-Ice).

## 🚀 Установка
```bash
ssh pi@10.0.0.2
cd /usr/local/share/pwnagotchi/custom-plugins/
sudo wget [https://raw.githubusercontent.com/Newfpv/display-password/main/display-password.py](https://raw.githubusercontent.com/Newfpv/display-password/main/display-password.py)
sudo nano /etc/pwnagotchi/config.toml
```
Добавьте конфиг плагина:
```toml
main.plugins.display-password.enabled = true
# Опционально: ориентация вывода текста (по умолчанию horizontal)
main.plugins.display-password.orientation = "horizontal"
```
Перезапустите сервис:
```bash
sudo systemctl restart pwnagotchi
```

## 🛠 Решение проблем (Troubleshooting)
### На экране висит надпись "No cracked passwords"
Убедитесь, что ваши файлы `.potfile` или пакапы с хэндшейками лежат в `/root/handshakes/` или `/home/pi/handshakes/`. Плагин проверяет эти директории автоматически.

### Текст вылезает за пределы экрана
Если пароль или название сети (ESSID) слишком длинные, плагин безопасно обрежет строку, чтобы не сломать отрисовку остальных элементов интерфейса на e-ink экране.

## 🤝 Благодарности
- **@nagy_craig**, **@vanshksingh** и **@avipars** — за оригинальную идею и базовый код плагина.
- **NewFPV** — за полную переработку архитектуры, поддержку better_quickdic и алгоритм сортировки по mtime.

## 📝 Лицензия
Этот проект распространяется под лицензией GPL3.

## ☕ Поддержка
<div align="left"><a href="https://www.donationalerts.com/r/newfpv"><img src="https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-yellow.svg" alt="Donate"></a></div>
