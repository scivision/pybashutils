% plots vmstat text dumps created by the two-liner from Bash Terminal:
%
% echo "date '+%F %T'" > ~/logs/load.log
% nohup vmstat --one-header 15 >> ~/logs/load.log&
%
% e.g. for Raspberry Pi. Don't let it run forever or you'll fill up the storage.
% 
% tested with Octave 4.0 and Matlab R2015b
% 
% Michael Hirsch 
% July 2013

function data = loadingLog(logfn,cadenceSec)
%% Initialize variables.
fid = fopen(logfn,'r');
t0 = datenum(fgetl(fid),31);
%% Read data
% Format string for each line of text
ncol = 17;
formatSpec = repmat('%u',1,ncol); %has to be %u, not %u32 for Octave

%throw away header
for i = 1:2
    fgetl(fid);
end

data = zeros(100000,ncol,'uint32'); %speculative preallocation
i = 0;
while ~feof(fid)
    i = i+1;
    c = fgetl(fid);
    c = textscan(c, formatSpec, 'Delimiter',' ','multipledelimsasOne',true);
    data(i,:) = cell2mat(c);
    if ~mod(i,1000), display([int2str(i),' lines read']), end
end

%single for plotting
data = double(data(1:i,:)); %trim off unused space from preallocation

fclose(fid);

%% handle timing estimation
day2sec = 86400;
Nt=size(data,1);
cadenceDN = cadenceSec/day2sec;

t = t0 + cadenceDN*(0:Nt-1);
t = t(:); %be sure it's a column vector
display(['Start: ',datestr(t(1)),' , End: ',datestr(t(end))])

%% Allocate imported array to column variable names
r = data(:, 1);
b = data(:, 2);
swpd = data(:, 3);
free = data(:, 4)/1000;
buffer = data(:, 5);
cache = data(:, 6);
si = data(:, 7);
so = data(:, 8);
bi = data(:, 9);
bo = data(:, 10);
in = data(:, 11);
cs = data(:, 12);
us = data(:, 13);
sy = data(:, 14);
id = data(:, 15);
wa = data(:, 16);
st = data(:,17);

avail = free+buffer+cache;
%% plot
try %octave 4.0 is buggy on these plots, with fltk and gnuplot, but gnuplot is less bac (xlabeltick doubling)
  graphics_toolkit('gnuplot') 
end

try
    figure(1),clf(1)
    ax=subplot(2,1,1);
    plot(t,avail,'parent',ax)
    datetick(ax,'x')
    title(ax,'CPU/RAM')
%    set(gca,'ylim',[0,inf],'xgrid','on','ygrid','on')
    ylabel(ax,'Avail. Memory (MB)'),%xlabel(' Time')

    ax=subplot(2,1,2);
    hold('on')
    plot(t,us,'color','b','DisplayName','USER')
    plot(t,sy,'color','g','DisplayName','SYSTEM')
    legend('show','location','best')
    datetick(ax,'x')
%    set(gca,'ylim',[0,100],'xgrid','on','ygrid','on')
    ylabel('CPU (%)'),%xlabel(' Time')
end

try
    figure(2),clf(2)
    subplot(2,1,1)
    plot(t,wa)
    datetick
    title('I/O')
%    set(gca,'ylim',[0,inf],'xgrid','on')
    ylabel('IO Wait (%)'),xlabel(' Time')

    subplot(2,1,2)
    plotyy(t,bi,t,bo)
    datetick
    legend('Blks In','Blks Out','location','best')
    ylabel('blocks/sec')
%    set(gca,'ylim',[0,inf],'xgrid','on')
end
    
try
    figure(3),clf(3)
    ax=plotyy(t,in,t,cs);
    legend('Intrpts/sec','ContxtSwtch/sec','location','best')
    datetick(ax(2),'x')
    set(ax(1),'xtick',[])
    title('Interrupts')
%    set(gca,'ylim',[0,inf],'xgrid','on')
    ylabel('/sec'),xlabel(' Time')
end

if ~nargout,clear,end
end %function
