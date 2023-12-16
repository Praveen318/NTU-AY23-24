from capstone import *

CODE = b"\x37\x00\xa0\xe3\x03\x10\x42\xe0"

md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
for (address, size, mnemonic, op_str) in md.disasm_lite(CODE, 0x1000):
	print("0x%x:\t%s\t%s" %(address, mnemonic, op_str))