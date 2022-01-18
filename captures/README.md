If you open this file in Logic software it should have the full program + readback sequence.

**NOTE**: The readback is done without a CS line. So you'll have to turn the CS off on the logic decoder.

To deal with this just right click where you need decoding to start and say "Delete Data --> Before Marker".

Watch out - for some reason some of the readback commands have an extra **5 cycles** of SCK line. You **MUST**
chop off stuff after that or the SPI decoder in Salae will get messed up.