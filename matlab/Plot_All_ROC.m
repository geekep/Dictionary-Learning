clc
clear all
close all

ROC_PathAL = 'C:/Users/admin/PycharmProjects/Real-worldAnomalyDetection/Paper_Results';
All_files = dir([ROC_PathAL, '/*.mat']);
Colors = {'b', 'c', 'k', 'r'};

AUC_ALL = [];
for i = 1: length(All_files)
   FilePath = [ROC_PathAL, '/', All_files(i).name];
   load(FilePath)
   plot(X, Y, 'Color',Colors{i}, 'LineWidth',3.5);
   hold on;
   AUC_ALL = [AUC_ALL; AUC];
   clear X Y
end

AUC_ALL * 100

legend({'Binary classifier', 'Lu et al.', 'Hasan et al.', 'Proposed with constraints'}, 'FontSize', 16, 'Location', 'southeast');
xlabel('False Positive Rate', 'FontWeight', 'normal', 'FontSize', 18);
ylabel('True Positive Rate', 'FontWeight', 'normal', 'FontSize', 18);
set(gca, 'FontWeight', 'normal', 'FontSize',12);

grid on
