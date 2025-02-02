clc;clear;close all

directory = 'E:\docker\updated_dataset\original_dataset\L7cm_22mJ_90d';
data = readmatrix(fullfile(directory, 'original_tek0501CH1.csv'));
directory2 = 'E:\docker\updated_dataset\original_dataset\L7cm_35mJ_90d';
data2 = readmatrix(fullfile(directory2, 'original_tek0501CH1.csv'));
directory3 = 'E:\docker\updated_dataset\original_dataset\L7cm_50mJ_90d';
data3 = readmatrix(fullfile(directory3, 'original_tek0501CH1.csv'));
directory4 = 'E:\docker\updated_dataset\original_dataset\L7cm_65mJ_90d';
data4 = readmatrix(fullfile(directory4, 'original_tek0501CH1.csv'));
t = 0.00001:0.00001:0.5;


f = figure;
axes1 = axes('Parent',f);
hold(axes1,'on');
box(axes1,'on');
set(axes1,'LineWidth',1.5);
plot (t,data4,t,data3,t,data2,t,data,'k','linewidth',1.5);
%xlim ([0,1e5])
%title ('10 ms received signal')
legend('E = 60mJ','E = 50mJ','E = 35mJ','E = 22mJ', 'FontWeight', 'bold')
xlabel('Time (ms)', 'FontWeight', 'bold')
ylabel('Voltage (V)', 'FontWeight', 'bold')
ylim ([-10,8]) 
grid on


%Fs = 1/mean(diff(t_10ms))
dt = 1e-8; %sampling interval
Fs = 1/dt; %2.5e9 %1/dt
t_f = fft(data4);
t_f_10ms = fftshift(abs(t_f));
m = length(t_f);
freq = (-m/2:(m/2-1))*Fs/(m-1);
figure;
plot (freq,t_f_10ms,'lineWidth',1);
title ('10 ms signal-FFT')
xlim ([0,4.8e5])
grid on