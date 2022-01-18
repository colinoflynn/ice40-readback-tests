import chipwhisperer as cw
from chipwhisperer.hardware.naeusb.programmer_targetfpga import LatticeICE40

# Connect to scope
scope = cw.scope()
lattice = LatticeICE40(scope)

lattice.erase_and_init()
#Program but don't run final start command
lattice.program(r"hardware.bin", sck_speed=20E6, start=False)

#Readback
cram, bram = lattice.readback()

#Start program
lattice.start()

# Read the "known good" readback file (created with diamond)
readback_lattice_crams = []
readback_lattice_brams = []

with open('hardware_rbk.hex') as fp:
    line = fp.readline()
    
    while line:
        if line == "01 01\n":
            data = []
            line = fp.readline()
            while len(line) > 30:
                data += [int(a, 16) for a in line.rstrip().split()]
                line = fp.readline()
            readback_lattice_crams.append(data)
        elif line == "01 03\n":
            data = []
            line = fp.readline()
            while len(line) > 30:
                data += [int(a, 16) for a in line.rstrip().split()]
                line = fp.readline()
            readback_lattice_brams.append(data)
        else:
            line = fp.readline()
            

def compare_arrays(a, b, show=False):
    ok = 0
    diff = 0
    
    if len(a) != len(b):
        print("WARNING: len %d != len %d, using smaller value"%(len(a), len(b)))
    
    for i in range(0, min(len(a), len(b))):
        if a[i] != b[i]:
            diff += 1
            if show:
                print("%06d: %02x != %02x"%(i, a[i], b[i]))
        else:
            ok += 1
    
    print("Diff: %d, same %d"%(diff, ok))

for i in range(0, 4):
    compare_arrays(readback_lattice_crams[i], cram[i], True)
for i in range(0, 8):
    compare_arrays(readback_lattice_brams[i], bram[i])