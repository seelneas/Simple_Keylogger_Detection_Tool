import psutil

def scan_processes(suspicious_keywords=["pynput", "keyboard", "keylog"]):
    flagged = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            name = proc.info.get('name', '')
            cmdline_list = proc.info.get('cmdline') or []
            if isinstance(cmdline_list, list):
                cmdline = ' '.join(cmdline_list)
            else:
                cmdline = ''
            
            for keyword in suspicious_keywords:
                if keyword.lower() in cmdline.lower():
                    flagged.append((proc.info['pid'], name, cmdline))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return flagged

