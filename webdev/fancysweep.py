# fancysweep.py for mezurit2 0.74b

basefile='devX_runY'
sweep_ch1 = 1
sweep_ch2 = 2
step_ch   = 3

def adj_sweep (V) :
	fmin = 100 + V**2
	set_var('panel{0:d}_sweep{1:d}_scaled_down={2:f}'.format(get_panel(), get_sweep_id(sweep_ch1), fmin)
	set_var('panel{0:d}_sweep{1:d}_scaled_up={2:f}'.format  (get_panel(), get_sweep_id(sweep_ch1), fmin + 10.0)
	set_var('panel{0:d}_sweep{1:d}_scaled_down={2:f}'.format(get_panel(), get_sweep_id(sweep_ch2), fmin + 0.01)
	set_var('panel{0:d}_sweep{1:d}_scaled_up={2:f}'.format  (get_panel(), get_sweep_id(sweep_ch2), fmin + 10.01)

clear_buffer(True, False)
set_recording(True)
V_last = channel_value(step_ch)

for V_cur in make_range(-5.0, 5.0, 20) :

	for V_x in make_range(V_last, V_cur, 10) :
		set_dac(step_ch, V_x)  # set voltage is 10 steps to reduce transients
	V_last = V_cur
	adj_sweep(V_cur)

	sweep_up(sweep_ch)
	sweep_catch('max_posthold', sweep_ch)  # change to catch_sweep() in v0.81
	save_data(basefile + '_up.dat')
#	clear_buffer(False, False)

	sweep_down(sweep_ch)
	sweep_catch('min_posthold', sweep_ch)  # change to catch_sweep() in v0.81
	save_data(basefile + '_down.dat')
#	clear_buffer(False, False)

set_recording(False)
