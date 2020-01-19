params.H = 160;       % loaded video height size
params.W = 240;       % loaded video width size

params.patchW = 40;   % 3D patch spatial width
params.patchH = 40;   % 3D patch spatial height
params.tprLen = 16;   % 3D patch temporal length

params.BKH = params.H / params.patchH;      % region number in height
params.BKW = params.W / params.patchW;      % region number in width

params.srs = 40;       % spatial sampling rate in video volume
params.trs = 16;       % temporal sampling rate in video volume

params.MT_thr = 5;    % 3D patch selecting threshold