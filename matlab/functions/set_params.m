params.H = 160;       % loaded video height size
params.W = 240;       % loaded video width size

params.patchH = 40;   % height of 3D patch
params.patchW = 40;   % width of 3D patch
params.tprLen = 16;    % 3D patch temporal length

params.BKH = params.H / params.patchWin;      % region number in height
params.BKW = params.W / params.patchWin;      % region number in width

params.srs = 40;       % spatial sampling rate in training video volume
params.trs = 16;       % temporal sampling rate in training video volume

params.PCAdim = 100;  % PCA Compression dimension

params.MT_thr = 5;    % 3D patch selecting threshold