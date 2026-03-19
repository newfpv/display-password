# Display Password (Advanced Fork)  
**Ультимативный агрегатор взломанных паролей для Pwnagotchi**

Мощный, полностью переработанный плагин для отображения недавно взломанных паролей прямо на e-ink экране вашего Pwnagotchi.  
Поддерживает несколько источников, умную сортировку по времени, интеграцию с better_quickdic и современные дисплеи без поломки интерфейса.

[🇬🇧 View in English](https://github.com/Newfpv/display-password/blob/main/README.md)

![image](https://github.com/Newfpv/display-password/blob/main/image.webp)

## ⚡ Главные отличия от оригинала
Этот форк — глубокий рефакторинг кода `@nagy_craig` и `@vanshksingh`:
- **Модульность:** в отличие от оригинала, вы можете включать/выключать конкретные источники (`wpa_sec`, `ohc`, `better_quickdic`) в конфиге.
- **Умный выбор (mtime):** оригинал читает одну строку одного файла. Этот форк сравнивает время изменения ВСЕХ файлов, чтобы показать **самый свежий** результат.
- **Поддержка Better_quickdic:** встроенная работа с файлами `.pcap.cracked`. Плагин сам достает имя сети из названия файла.
- **Умная обрезка:** если строка не влезает, плагин обрезает только имя сети и ставит точку (`.`), оставляя пароль полностью видимым (например, `MySuperLongWifi.:password123`).
- **Чистый Python:** отказ от вызовов `awk` и `tail`. Весь парсинг нативный, что экономит ресурсы CPU и исключает ошибки отрисовки.

## ✨ Возможности
- **Мульти-источники:** сканирует `wpa-sec`, `onlinehashcrack` (OHC) и `better_quickdic`.
- **Поддержка дисплеев:** Waveshare v2/v3/v4, Inky и другие.
- **Пути прошивок:** автоматически ищет в `/root/handshakes/` и `/home/pi/handshakes/`.

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
main.plugins.display-password.orientation = "horizontal"

# Опционально: переключатели источников (по умолчанию true)
main.plugins.display-password.wpa_sec = true
main.plugins.display-password.ohc = true
main.plugins.display-password.better_quickdic = true

# Лимит символов на экране до обрезки
main.plugins.display-password.max_length = 22
```

## 🛠 Решение проблем
### На экране висит надпись "No cracked passwords"
Убедитесь, что ваши `.potfile` или `.pcap.cracked` лежат в папках `/root/handshakes/` или `/home/pi/handshakes/`.

## 🤝 Благодарности
- **@nagy_craig**, **@vanshksingh** и **@avipars** — за идею и базовый код.
- **NewFPV** — за рефакторинг, умную сортировку и модульность.

## 📝 Лицензия
GPL3 License.

## ☕ Поддержка
<div align="left"><a href="https://www.donationalerts.com/r/newfpv"><img src="https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-yellow.svg" alt="Donate"></a></div>
