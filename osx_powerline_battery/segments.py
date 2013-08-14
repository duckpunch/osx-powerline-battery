# vim:fileencoding=utf-8:noet
import subprocess, re

def osx_battery(pl, steps=4, gamify=True):
    full_heart = '♥ '
    empty_heart = '♡ '
    power_type, charge, _ = subprocess.check_output(['pmset', '-g', 'batt']).decode('utf8').split('\n')
    if 'AC Power' in power_type:
        return None
    else:
        batt_percent = re.search(r'\d+%', charge).group(0)
        batt_level = int(batt_percent.replace('%', ''))
        step_size = 100.0/steps
        num_of_full_hearts = int(batt_level/step_size) + 1
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
