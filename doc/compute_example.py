# compute_example.py

tau_table = [10e-6, 30e-6, 100e-6, 300e-6, 1e-3, 3e-3, 10e-3, 30e-3, 100e-3, 300e-3, 1.0, 3.0, 10.0, 30.0, 100.0, 300.0, 1e3, 3e3, 10e3, 30e3]
SR830_Tau = GPIB_Device('OFLT?', 2.0, 6, '%lf', 'OFLT %0.0f')  # SR830 time constant in seconds (refresh: 2s, dummy: 10e-3s)
SR830_Tau.noninverse_fn = lambda x : tau_table[int(x)]
SR830_Tau.inverse_fn = lambda x : nearest_index(tau_table, x)
