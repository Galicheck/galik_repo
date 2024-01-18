import dvc.api
import numpy as np
import config as cfg
import dvc.api

params = dvc.api.params_show()
print(params)
windows_size = params['windower']['windows_size']
step = params['windower']['step']

X = np.genfromtxt(cfg.RAW_DATA, delimiter=',',skip_header=True)

print(X.shape)
print(X[:10, :])

acc_x = np.lib.stride_tricks.sliding_window_view(X[:,0],window_shape=windows_size)

acc_y = np.lib.stride_tricks.sliding_window_view(X[:,1],window_shape=windows_size)
Y = np.concatenate([acc_x[::step], acc_y[::step]], axis=1)

np.save(cfg.WINDOWED_DATA, Y)