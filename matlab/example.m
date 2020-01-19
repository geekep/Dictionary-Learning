addpath('functions')
addpath('C:/Users/admin/Downloads/DICTOL-master/build_spams')

%% sparseapprox.m 
L = 400;
N = 16;
K = 32;
D = randn(N,K);
X = randn(N,L);
% or
% Wi = zeros(K, L);
% for i = 1 : L
%   Wi(:, i) = randperm(K);
% end
% Wt = zeros(K, L);
% Wt(Wi <= 5) = randn(5 * L, 1);
% X = D * Wt + 0.01 * randn(N, L);
op = struct('targetNonZeros',5, 'verbose',2);
% [WbackSlash, rb] = sparseapprox(X, D, '\', op);
[Wpinv, ra] = sparseapprox(X, D, 'pinv', op);
% [Wlp, rc] = sparseapprox(X, D, 'linprog', op); 

% [Wf, rd] = sparseapprox(X, D, 'FOCUSS', op, 'p', 0.8, 'l', 0.4, 'nIt', 100);
% [Wmomp, rm] = sparseapprox(X, D, 'mexOMP', op);      % like ORMP
% [Wlasso, rl] = sparseapprox(X, D, 'mexLasso', op);  
% [Wgmp, ri] = sparseapprox(X, D, 'GMP', 'tnz', 5*L, 'v',2); 

% [Womp, rf] = sparseapprox(X, D, 'javaOMP', op); 
% [Wormp, rg] = sparseapprox(X, D, 'javaORMP', op); 
% [Wps100, rh] = sparseapprox(X, D, 'javaPS', 'nComb',100, op);
% [Wps, rih] = sparseapprox(X, D, 'javaPS', 'tnz',sum(Wgmp~=0), 'nComb',100);

% fs = ' %5.2f  %5.2f  %5.2f  %5.2f  %5.2f  %5.2f  %5.2f  %5.2f \n';
% fprintf('\n       pinv  linprog FOCUSS  OMP   ORMP   PS     GMP   GMP+PS \n'); 
% fprintf(['SNR  ',fs], ra.snr,rc.snr,rd.snr,rf.snr,rg.snr,rh.snr,ri.snr,rih.snr);  
% fprintf(['time ',fs], ra.time,rc.time,rd.time,rf.time,rg.time,rh.time,ri.time,rih.time);  

% to show the coefficients for a selected vector
% i = 11;
% [Wt(:,i), Womp(:,i), Wormp(:,i), Wmomp(:,i), Wlasso(:,i), Wps100(:,i)]

%% dlfun.m (using 7-12 sec per iteration)
% clear all;
% load('data/dataXforAR1.mat');
% [N, L] = size(X);
% K = 50;
% D0 = dictnormalize(X(:, 3000 + (1 : K)));
% nofIt = 10;
% 
% dlsMOD = struct('D',D0, 'Met','MOD', 'vsMet','ORMP', 'vsArg',struct('tnz',4));
% dlsMOD.snr = zeros(1,nofIt);
% tic;
% for i = 1 : nofIt
%     dlsMOD = dlfun(dlsMOD, X, 1);
% end
% toc;  
% 
% dlsKSVD = struct('D',D0, 'Met','K-SVD', 'vsMet','ORMP', 'vsArg',struct('tnz',4));
% dlsKSVD.snr = zeros(1,nofIt);
% tic;
% for i = 1 : nofIt
%     dlsKSVD = dlfun(dlsKSVD, X, 1);
% end
% toc;
% 
% dlsODL = struct('D',D0, 'Met','ODL', 'vsMet','ORMP', 'vsArg',struct('tnz',4));
% dlsODL.lamStep = 20;
% dlsODL.ndStep = 50;
% dlsODL.A = eye(K);
% dlsODL.B = dlsODL.D;
% dlsODL.snr = zeros(1, nofIt);          
% tic;
% for i = 1 : nofIt
%     dlsODL.lam = lambdafun(i, 'C', nofIt, 0.99, 1);
%     dlsODL = dlfun(dlsODL, X, 1);
% end
% toc;
% 
% dlsRLS = struct('D',D0, 'Met','RLS', 'vsMet','ORMP', 'vsArg',struct('tnz',4));
% dlsRLS.lamStep = 20;
% dlsRLS.ndStep = 50;
% dlsRLS.C = eye(K);
% dlsRLS.snr = zeros(1,nofIt);          
% tic;
% for i = 1 : nofIt
%     dlsRLS.lam = lambdafun(i, 'C', nofIt, 0.99, 1);
%     dlsRLS = dlfun(dlsRLS, X, 1);
% end
% toc;

%% dictlearn_mb.m
% X = load('data/dataXforAR1.mat');
% opt = struct('K',32, 'samet','pinv','saopt',struct('tnz',4));
% Ds = dictlearn_mb(X, opt);    
% figure(1);
% clf;
% plot(Ds.ptab(:, 1), Ds.ptab(:, 2), 'b-');
% xlabel(Ds.ptc{1});
% ylabel(Ds.ptc{2}); 

%% 


































