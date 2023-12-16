from emu import Emulator

em = Emulator(r'rootfs/arm_linux/bin/pass', r'rootfs/arm_linux/')

skip_instruction = 0x000105c8 #instruction to skip here

print( "Instruction skipped : 0x%x" % skip_instruction )
try:
    em.setup_skip_instruction( inst= skip_instruction, debug=True )
except Exception as e:
    print("ERROR: %s" % e)
