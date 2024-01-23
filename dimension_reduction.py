from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt
import config as cfg
import dvc.api

params = dvc.api.params_show()
random_state = params['reducer']['random_state']


X= np.load(cfg.WINDOWED_DATA)

tsne = TSNE(n_components=2, random_state=random_state)

X_tsne = tsne.fit_transform(X)

fig = plt.figure()
plt.plot(X_tsne[:,0], X_tsne[:,1], 'o')
fig.savefig(cfg.PLOT_FILE)