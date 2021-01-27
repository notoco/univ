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
            control.send_notification("Ambilight", "Wyłączono podświetlenie")
        else:
            control.turn_on()
            control.send_notification("Ambilight", "Włączono podświetlenie")

#ESC
    elif arg == "esc":
        xbmc.executebuiltin("Action(Stop)")
        xbmc.executebuiltin("Dialog.Close(all, true)")
        xbmc.executebuiltin("xbmc.ActivateWindow(home)")
#EPG
    elif arg == "epg":
        playing = xbmc.Player().isPlayingVideo()
        if (playing == True):  
            xbmc.executebuiltin("xbmc.ActivateWindow(fullscreenvideo)")
        else:
            xbmc.executebuiltin("Action(back)")
#CPU
    elif arg == "cpu":
        control.cpu()
        

