H = 160                   # loaded video height size
W = 240                   # loaded video width size

patchH = 40               # height of 3D patch
patchW = 40               # width of 3D patch
tprLen = 16               # temporal length of 3D patch

BKH = H / patchH          # region number in height
BKW = W / patchW          # region number in width

srs = 40                  # spatial sampling rate in training video volume
trs = 16                  # temporal sampling rate in training video volume

PCAdim = 32               # PCA Compression dimension

MT_thr = 5                # 3D patch selecting threshold

k = 128                   # number of atoms in the dictionary, if k is None, select k = round(0.2 * n_samples)
