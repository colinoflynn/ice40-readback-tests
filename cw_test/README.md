This test checks the readback file that was created with Lattice Diamond Programmer.

The readback `.hex` file is really just data that si read back, interspliced with what lattice knows should be
there to "make" a bitstream. The parser just finds the readback areas and compares it with what we read back.

For some reason the sizes are slightly different, but the overlaping ones DO agree. For my purpose this doesn't matter.

```
WARNING: len 29066 != len 29064, using smaller value
Diff: 0, same 29064
WARNING: len 15222 != len 15224, using smaller value
Diff: 0, same 15222
WARNING: len 29066 != len 29064, using smaller value
Diff: 0, same 29064
WARNING: len 15222 != len 15224, using smaller value
Diff: 0, same 15222
Diff: 0, same 2560
Diff: 0, same 2560
Diff: 0, same 1280
Diff: 0, same 1280
Diff: 0, same 2560
Diff: 0, same 2560
Diff: 0, same 1280
Diff: 0, same 1280
```