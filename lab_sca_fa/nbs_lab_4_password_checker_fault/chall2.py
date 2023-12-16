from emu import Emulator

em = Emulator(r'rootfs/arm_linux/bin/pass', r'rootfs/arm_linux/')

delay_value = None #Enter delay Value here
try:
    em.setup_skip_delay( delay = delay_value , debug=False )
except Exception as e:
    print("ERROR: %s" % e)