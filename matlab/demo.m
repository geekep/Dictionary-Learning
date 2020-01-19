addpath('functions')
set_params;
H = int32(params.H);
W = int32(params.W);
BKH = int32(params.BKH);
BKW = int32(params.BKW);
tprLen = int32(params.tprLen);
patchW = int32(params.patchW);
patchH = int32(params.patchH);

%% training
filePath = 'data/train_feature';
fileList = dir(strcat(filePath, '/*.mat'));
fileNum = length(fileList);
vars = {'C3Dfeature', 'locationOfCube', 'numOfFrame'};

X = [];
for i = 1 : fileNum
    fileName = fileList(i).name;
    trainFeature = load(strcat(filePath, '/', fileName), '-mat', vars{:});
    C3Dfeature = getfield(trainFeature, {1}, vars{1});
    X = [X; C3Dfeature];
end

%%
opt = struct('K',128, 'samet','pinv','saopt',struct('tnz',32));
Ds = dictlearn_mb(struct('X', X'), opt);
figure(1);
clf;
plot(Ds.ptab(:, 1), Ds.ptab(:, 2), 'b-');
xlabel(Ds.ptc{1});
ylabel(Ds.ptc{2});
threshold = max(Ds.ptab(2:end, 2));
dic = Ds.D;
save(strcat('data', '/dictionary.mat'), 'dic');

%% testing
filePath = 'data/test_feature';
fileList = dir(strcat(filePath, '/*.mat'));
fileNum = length(fileList);

for i = 1 : fileNum
    
    fileName = fileList(i).name;
    testFeature = load(strcat(filePath, '/', fileName), '-mat', vars{:});
    C3Dfeature = getfield(testFeature, {1}, vars{1});
    locationOfCube = getfield(testFeature, {1}, vars{2});
    numOfFrame = getfield(testFeature, {1}, vars{3});
    
    op = struct('targetNonZeros',32, 'verbose',2);
    [Wpinv, ra] = sparseapprox(C3Dfeature', dic, 'pinv', op);
    Err = ra.norm2R;

    AbEvent = zeros(BKH, BKW, numOfFrame);
    for j = 1 : length(Err)
        for k = 1 : tprLen
            AbEvent(locationOfCube(int32(j), 2) + 1, ...
            locationOfCube(int32(j), 3) + 1, ...
            locationOfCube(int32(j), 1) * tprLen + k) = Err(int32(j));
        end
    end
%     AbEvent = smooth3(AbEvent, 'box',5);

    save(strcat('data/test_result', '/regionalRes_', fileName(1:7), '.mat'), 'AbEvent');

end

%%
for i = 1 : length(Err)

    AbEventPath = 'data/test_result';
    AbEventList = dir([AbEventPath, '/*.mat']);
    for j = 1 : length(AbEventList)
        load([AbEventPath, '/', AbEventList(j).name]);
        for 
            
        end
        find(AbEvent < err);
        idx = union(idx, AbEvent(j, 1) - 7 : AbEvent(j, 1) + 8, 'sorted');
         
        TestVideoFile{i}.predict_frame = idx';
        err = Err(i);
        TPR = find(Err < Err(i));
        FPR = ;
    end

end































