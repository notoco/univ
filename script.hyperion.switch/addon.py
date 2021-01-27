# -*- coding: utf-8 -*-
import xbmc
import control
state = control.get_setting('state')
if __name__ == '__main__':
    arg = None

    try:
       arg = sys.argv[1].lower()
    except Exception:
       pass
# AMBILIGHT
    if arg == "amb_on":
        control.turn_on()
    elif arg == "amb_off":
        control.turn_off()
    elif arg == "amb_switch":
        if state == 'true':
            control.turn_off()
            control.send_notification("Ambilight", "Off")
        else:
            control.turn_on()
            control.send_notification("Ambilight", "On")
