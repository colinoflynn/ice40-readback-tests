This repository contains some bonus data related to the ice40 "Readback" implementation available in [ChipWhisperer](https://github.com/newaetech/chipwhisperer/blob/develop/software/chipwhisperer/hardware/naeusb/programmer_targetfpga.py#L169).

The `example` directory has the code sequence used to check this. It's not complete yet as the full contents of various BRAMs aren't actually validated since they were loaded with 0's, but some minimal checks worked.

**WARNING**: If you are trying to use ChipWhisperer for this, be aware you need to install beta firmware currently for ice40 programming to work.