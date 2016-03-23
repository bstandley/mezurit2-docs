# script_example.py

# Copy following lines into /usr/share/mezurit2/script.py right before the definition of reset_gpib():

tau_table = [10e-6, 30e-6, 100e-6, 300e-6, 1e-3, 3e-3, 10e-3, 30e-3, 100e-3, 300e-3, 1.0, 3.0, 10.0, 30.0, 100.0, 300.0, 1e3, 3e3, 10e3, 30e3]
SRS_SR830_OFLT = GPIB_Device(2.0, "*IDN?", 'OFLT?', '%lf', '')  # SR830 time constant in seconds (refresh: 2s, write not supported)
def SR830_Tau (brd, pad) : return tau_table[int(SRS_SR830_OFLT.read(brd, pad))]

# Add the following line to reset_gpib():

	SRS_SR830_OFLT.reset()
