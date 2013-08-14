# vim:fileencoding=utf-8:noet
import subprocess, re

def osx_battery(pl, steps=4, gamify=True):
    full_heart = '♥ '
    empty_heart = '♡ '
    battery_summary = subprocess.check_output(['pmset', '-g', 'batt']).decode('utf8')
    if 'AC Power' in battery_summary:
        return None
    else:
        batt_percent = re.search(r'\d+%', battery_summary).group(0)
        batt_level = int(batt_percent.replace('%', ''))
        step_size = 100.0/steps
        num_of_full_hearts = min(int(batt_level/step_size) + 1, steps)
        if gamify:
            return [
                {
                    'contents': full_heart * num_of_full_hearts,
                    'highlight_group': ['osx_battery'],
                    'draw_soft_divider': False,
                },
                {
                    'contents': empty_heart * (steps - num_of_full_hearts),
                    'highlight_group': ['osx_battery'],
                    'draw_soft_divider': False,
                }
            ]
        else:
            return [{
                'contents': batt_percent,
                'highlight_group': ['osx_battery'],
            }]
