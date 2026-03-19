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
    __version__ = '2.0.1'
    __license__ = 'GPL3'
    __description__ = 'Displays recently cracked passwords from wpa-sec, OHC and better_quickdic'

    __defaults__ = {
        'enabled': False,
        'orientation': 'horizontal',
        'wpa_sec': True,
        'ohc': True,
        'better_quickdic': True,
        'max_length': 22
    }

    def on_loaded(self):
        logging.info("display-password loaded")

    def on_ui_setup(self, ui):
        is_v2 = getattr(ui, 'is_waveshare_v2', lambda: False)()
        is_v3 = getattr(ui, 'is_waveshare_v3', lambda: False)()
        is_v4 = getattr(ui, 'is_waveshare_v4', lambda: False)()

        if is_v2 or is_v3 or is_v4:
            h_pos = (0, 95)
            v_pos = (180, 61)
        elif getattr(ui, 'is_waveshare_v1', lambda: False)():
            h_pos = (0, 95)
            v_pos = (170, 61)
        elif getattr(ui, 'is_waveshare144lcd', lambda: False)():
            h_pos = (0, 92)
            v_pos = (78, 67)
        elif getattr(ui, 'is_inky', lambda: False)():
            h_pos = (0, 83)
            v_pos = (165, 54)
        elif getattr(ui, 'is_waveshare27inch', lambda: False)():
            h_pos = (0, 153)
            v_pos = (216, 122)
        else:
            h_pos = (0, 91)
            v_pos = (180, 61)

        orientation = self.options.get('orientation', 'horizontal')

        if orientation == "vertical":
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
        potfiles = []
        if self.options.get('wpa_sec', True):
            potfiles.extend([
                '/root/handshakes/wpa-sec.cracked.potfile',
                '/home/pi/handshakes/wpa-sec.cracked.potfile'
            ])
            
        if self.options.get('ohc', True):
            potfiles.append('/root/handshakes/onlinehashcrack.cracked.potfile')
        
        quickdic_files = []
        if self.options.get('better_quickdic', True):
            handshake_dirs = ['/root/handshakes/', '/home/pi/handshakes/']
            for d in handshake_dirs:
                if os.path.exists(d):
                    quickdic_files.extend(glob.glob(os.path.join(d, '*.pcap.cracked')))

        last_essid = ""
        last_pwd = ""
        last_timestamp = 0
        found_any = False

        for p_file in potfiles:
            if os.path.exists(p_file):
                try:
                    mtime = os.path.getmtime(p_file)
                    line = os.popen(f'tail -n 1 {p_file}').read().strip()
                    if line:
                        parts = line.split(':')
                        if len(parts) >= 3:
                            pwd = parts[-1]
                            essid = parts[-2]
                            
                            if mtime > last_timestamp:
                                last_timestamp = mtime
                                last_essid = essid
                                last_pwd = pwd
                                found_any = True
                except Exception as e:
                    logging.debug(f"DisplayPassword Error reading {p_file}: {e}")

        for q_file in quickdic_files:
            try:
                mtime = os.path.getmtime(q_file)
                if mtime <= last_timestamp:
                    continue

                with open(q_file, 'r') as f:
                    pwd = f.read().strip()
                
                if pwd:
                    filename = os.path.basename(q_file)
                    name_no_ext = filename.replace('.pcap.cracked', '')
                    parts = name_no_ext.split('_')
                    if len(parts) > 1:
                        essid = "_".join(parts[:-1])
                    else:
                        essid = name_no_ext
                    
                    last_timestamp = mtime
                    last_essid = essid
                    last_pwd = pwd
                    found_any = True
            except Exception as e:
                logging.debug(f"DisplayPassword Error reading quickdic file {q_file}: {e}")

        if not found_any:
            ui.set('display-password', 'No cracked passwords')
        else:
            max_len = self.options.get('max_length', 22)
            display_str = f"{last_essid}:{last_pwd}"
            
            if len(display_str) > max_len:
                avail_len = max_len - len(last_pwd) - 2
                if avail_len > 0:
                    display_str = f"{last_essid[:avail_len]}.:{last_pwd}"
                else:
                    display_str = f"{last_essid[:1]}.:{last_pwd[:max_len-4]}."
            
            ui.set('display-password', display_str)
