clc;clear;close all

directory = 'C:\Users\Muntasir Mahmud\OneDrive - UMBC\3. My Papers\DL_paper\Plot';
data = readmatrix(fullfile(directory, 'echo_tek0627CH1.csv'));
directory2 = 'C:\Users\Muntasir Mahmud\OneDrive - UMBC\3. My Papers\DL_paper\Plot';
data2 = readmatrix(fullfile(directory2, 'echo_tek0652CH1.csv'));
directory3 = 'C:\Users\Muntasir Mahmud\OneDrive - UMBC\3. My Papers\DL_paper\Plot';
data3 = readmatrix(fullfile(directory3, 'echo_tek0680CH1.csv'));
directory4 = 'C:\Users\Muntasir Mahmud\OneDrive - UMBC\3. My Papers\DL_paper\Plot';
data4 = readmatrix(fullfile(directory4, 'echo_tek0682CH1.csv'));
data5 = readmatrix(fullfile(directory4, 'val2_tek0545CH1.csv'));
t = 0.00001:0.00001:0.5;


nexttile
plot (t,data4,'linewidth',1.5);
%legend('90 Degree')
%title('90 Degree')
xlabel('Time (ms)', 'FontWeight', 'bold')
ylabel('Voltage (V)', 'FontWeight', 'bold')
ylim ([-7,7])
xlim ([0,0.5])
grid on

nexttile
plot (t,data3,'linewidth',1.5);
%title('45 Degree')
xlabel('Time (ms)', 'FontWeight', 'bold')
ylabel('Voltage (V)', 'FontWeight', 'bold')
ylim ([-7,7])
xlim ([0,0.5])
grid on

nexttile
plot (t,data2,'linewidth',1.5);
%title('0 Degree')
xlabel('Time (ms)', 'FontWeight', 'bold')
ylabel('Voltage (V)', 'FontWeight', 'bold')
ylim ([-7,7])
xlim ([0,0.51])
grid on

nexttile
plot (t,data,'linewidth',1.5);
%title('45 Degree')
xlabel('Time (ms)', 'FontWeight', 'bold')
ylabel('Voltage (V)', 'FontWeight', 'bold')
ylim ([-7,7])
xlim ([0,0.5])
grid on

% nexttile
% plot (t,data5,'linewidth',1.5);
% %title('45 Degree')
% xlabel('Time (ms)', 'FontWeight', 'bold')
% ylabel('Voltage (V)', 'FontWeight', 'bold')
% ylim ([-7,7])
% xlim ([0,0.5])
% grid on


