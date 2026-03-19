from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
import os
import glob

class DisplayPassword(plugins.Plugin):
    __author__ = '@vanshksingh (Modified by NewFPV)'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Displays recently cracked passwords from wpa-sec, OHC and better_quickdic'

    def on_loaded(self):
        logging.info("display-password loaded")

    def on_ui_setup(self, ui):
        if ui.is_waveshare_v2():
            h_pos = (0, 95)
            v_pos = (180, 61)
        elif ui.is_waveshare_v4():
            h_pos = (0, 95)
            v_pos = (180, 61)
        elif ui.is_waveshare_v3():
            h_pos = (0, 95)
            v_pos = (180, 61)  
        elif ui.is_waveshare_v1():
            h_pos = (0, 95)
            v_pos = (170, 61)
        elif ui.is_waveshare144lcd():
            h_pos = (0, 92)
            v_pos = (78, 67)
        elif ui.is_inky():
            h_pos = (0, 83)
            v_pos = (165, 54)
        elif ui.is_waveshare27inch():
            h_pos = (0, 153)
            v_pos = (216, 122)
        else:
            h_pos = (0, 91)
            v_pos = (180, 61)

        if self.options['orientation'] == "vertical":
            ui.add_element('display-password', LabeledValue(color=BLACK, label='', value='',
                                                   position=v_pos,
                                                   label_font=fonts.Bold, text_font=fonts.Small))
        else:
            ui.add_element('display-password', LabeledValue(color=BLACK, label='', value='',
                                                   position=h_pos,
                                                   label_font=fonts.Bold, text_font=fonts.Small))

    def on_unload(self, ui):
        with ui._lock:
            ui.remove_element('display-password')

    def on_ui_update(self, ui):
        # 1. Сначала проверяем стандартные pot-файлы (wpa-sec, OHC)
        potfiles = [
            '/root/handshakes/wpa-sec.cracked.potfile',
            '/root/handshakes/onlinehashcrack.cracked.potfile',
            '/home/pi/handshakes/wpa-sec.cracked.potfile'
        ]
        
        # 2. Ищем файлы от better_quickdic (*.pcap.cracked)
        # Они лежат там же, где и handshakes
        handshake_dirs = ['/root/handshakes/', '/home/pi/handshakes/']
        quickdic_files = []
        for d in handshake_dirs:
            if os.path.exists(d):
                quickdic_files.extend(glob.glob(os.path.join(d, '*.pcap.cracked')))

        last_cracked = ""
        last_timestamp = 0
        found_any = False

        # --- Обработка стандартных potfiles ---
        for p_file in potfiles:
            if os.path.exists(p_file):
                try:
                    mtime = os.path.getmtime(p_file)
                    # Читаем последнюю строку
                    line = os.popen(f'tail -n 1 {p_file}').read().strip()
                    if line:
                        parts = line.split(':')
                        if len(parts) >= 3:
                            pwd = parts[-1]
                            essid = parts[-2]
                            display_str = f"{essid}:{pwd}"
                            
                            if mtime > last_timestamp:
                                last_timestamp = mtime
                                last_cracked = display_str
                                found_any = True
                except Exception as e:
                    logging.debug(f"DisplayPassword Error reading {p_file}: {e}")

        # --- Обработка файлов better_quickdic ---
        for q_file in quickdic_files:
            try:
                mtime = os.path.getmtime(q_file)
                # Если этот файл старее, чем то, что мы уже нашли, пропускаем чтение (оптимизация)
                if mtime <= last_timestamp:
                    continue

                # Quickdic пишет только пароль внутрь файла
                with open(q_file, 'r') as f:
                    pwd = f.read().strip()
                
                if pwd:
                    # Имя файла обычно: ESSID_MAC.pcap.cracked
                    # Нам нужно вытащить ESSID из имени файла
                    filename = os.path.basename(q_file)
                    # Убираем расширение
                    name_no_ext = filename.replace('.pcap.cracked', '')
                    
                    # Разбиваем по подчеркиванию. Последняя часть - это MAC, всё до неё - ESSID
                    parts = name_no_ext.split('_')
                    if len(parts) > 1:
                        essid = "_".join(parts[:-1]) # Собираем обратно, если в ESSID были подчеркивания
                    else:
                        essid = name_no_ext # На всякий случай

                    display_str = f"{essid}:{pwd}"
                    
                    last_timestamp = mtime
                    last_cracked = display_str
                    found_any = True
            except Exception as e:
                logging.debug(f"DisplayPassword Error reading quickdic file {q_file}: {e}")

        if not found_any:
            ui.set('display-password', 'No cracked passwords')
        else:
            # Обрезаем строку, если она слишком длинная для экрана
            if len(last_cracked) > 20: 
                 # Показываем начало ESSID и пароль
                 # (можно настроить под себя)
                 pass
            ui.set('display-password', last_cracked)