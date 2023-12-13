clc;clear;close all

directory = 'C:\Users\Muntasir Mahmud\OneDrive - UMBC\3. My Papers\DL_paper\Plot';
data = readmatrix(fullfile(directory, 'original_tek0586CH1.csv'));
directory2 = 'C:\Users\Muntasir Mahmud\OneDrive - UMBC\3. My Papers\DL_paper\Plot';
data2 = 0.9*readmatrix(fullfile(directory2, 'original_tek0583CH1.csv'));
data2 = [data2(48301:50000); data2(1:48300)];
directory3 = 'C:\Users\Muntasir Mahmud\OneDrive - UMBC\3. My Papers\DL_paper\Plot';
data3 = readmatrix(fullfile(directory3, 'original_tek0534CH1.csv'));
data3 = [data3(47001:50000); data3(1:47000)];
t = 0.00001:0.00001:0.5;


nexttile
plot (t,data,'k','linewidth',1.5);
%legend('90 Degree')
title('90 Degree')
xlabel('Time (ms)', 'FontWeight', 'bold')
ylabel('Voltage (V)', 'FontWeight', 'bold')
ylim ([-7,7])
xlim ([0,0.5])
grid on

nexttile
plot (t,data2,'k','linewidth',1.5);
title('45 Degree')
xlabel('Time (ms)', 'FontWeight', 'bold')
ylabel('Voltage (V)', 'FontWeight', 'bold')
ylim ([-7,7])
xlim ([0,0.5])
grid on

nexttile
plot (t,data3,'k','linewidth',1.5);
title('0 Degree')
xlabel('Time (ms)', 'FontWeight', 'bold')
ylabel('Voltage (V)', 'FontWeight', 'bold')
ylim ([-7,7])
xlim ([0,0.51])
grid on


%Fs = 1/mean(diff(t_10ms))
dt = 1e-8; %sampling interval
Fs = 1/dt; %2.5e9 %1/dt
t_f_1 = fft(data);
t_f_90 = fftshift(abs(t_f_1));
m = length(t_f_1);
freq = (-m/2:(m/2-1))*Fs/(m-1);

t_f_2 = fft(data2);
t_f_45 = fftshift(abs(t_f_2));

t_f_3 = fft(data3);
t_f_0 = fftshift(abs(t_f_3));

nexttile
plot (freq,t_f_0,freq,t_f_45,freq,t_f_90,'k','lineWidth',1.5);
%title ('10 ms signal-FFT')
legend('0 Degree','45 Degree','90 Degree')
title('Frequency Spectrum')
xlabel('Frequenncy (Hz)', 'FontWeight', 'bold')
ylabel('Amplitude', 'FontWeight', 'bold')
xlim ([0,4.8e5])
grid on

%directory3 = '/Users/muntasirmahmud/Library/CloudStorage/OneDrive-UMBC/3. My Papers/DL_paper/Plot';
data4 = readmatrix(fullfile(directory3, 'tek0347CH1.csv'));
data4 = data4(15017:115016,2)+0.48;
t2 = 0.00001:0.00001:1;
f=figure;
axes1 = axes('Parent',f);
hold(axes1,'on');
box(axes1,'on');
set(axes1,'LineWidth',1.5);
plot (t2,0.97*data4,'linewidth',1.5);
ylim ([-6,10])
%title ('10 ms received signal')
xlabel('Time(ms)', 'FontWeight', 'bold')
ylabel('Voltage(V)', 'FontWeight', 'bold') 
grid on

% f2=figure;
% axes2 = axes('Parent',f2);
% hold(axes2,'on');
% box(axes2,'on');
% set(axes2,'LineWidth',1.5);
% plot (t,data,t,data2,t,data3,'linewidth',1.5);
% ylim ([-7,7])
% legend('90 Degree','45 Degree','0 Degree')
% xlabel('Time(ms)', 'FontWeight', 'bold')
% ylabel('Voltage(V)', 'FontWeight', 'bold') 
% grid on

f2=figure;
axes2 = axes('Parent',f2);
hold(axes2,'on');
box(axes2,'on');
set(axes2,'LineWidth',1.5);
set(gca,'YTickLabel',[],'YTick',[]);
plot (t,data+12,t,data2,t,data3-12,'linewidth',1.5);
%ylim ([-7,7])
legend('90 Degree','45 Degree','0 Degree', 'FontWeight', 'bold')
xlabel('Time(ms)', 'FontWeight', 'bold')
ylabel('Voltage(V)', 'FontWeight', 'bold') 
grid on
