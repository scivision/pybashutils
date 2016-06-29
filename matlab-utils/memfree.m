%% find free physical RAM on Windows (with or without Cygwin) and Linux systems
% currently Matlab doesn't support memory() on Linux/Mac systems
% This function is meant to give free memory using Matlab or Octave
%
% This function works on:
% Windows: Matlab, Octave with or without Cygwin
% Linux:   Matlab, Octave
% Android: untested
% Mac: untested
%
% Output:
% --------
% returns estimate of free physical RAM in bytes
%
% Michael Hirsch 2012

function freebytes = memfree()

try
    [err,freebytes]=system('python -c "import psutil; print(psutil.virtual_memory().available)"');
    if ~err
        freebytes=str2double(freebytes);
        disp([num2str(freebytes/1e9,'%0.2f'),' Gbyte available RAM via python psutil'])
    end
catch
    if ispc  % for Cygwin, isunix=true && ispc=false
        freebytes = memorywindows();
    elseif ismac % BSD
        freebytes = memorymac(); % we did not handle Macs yet (request if you want)
    else %isunix && ~ismac || iscygwin
        freebytes = memoryunix();
    end %if
    disp([num2str(freebytes/1e9,'%0.2f'),' Gbyte available RAM via Matlab fallback'])
end %try


if ~nargout,clear,end
end %function

function freebytes = memoryunix()
%% free + buffers + cached
[~,msg] = unix('free -mb | awk "NR==2"');

mems = cell2mat(textscan(msg,'%*s %f %f %f %f %f %f','delimiter',' ','collectoutput',true,'multipleDelimsAsOne',true));

freebytes = mems(1,3)+mems(1,5)+mems(1,6);

end %function

function freebytes = memorymac()
%% inactive + free
% TODO: looks like we could awk vm_stat to get it
%  "Pages inactive"   "Pages free"
freebytes=[];

end %function

function freebytes = memorywindows()

if isoctave % is windows (and not on Cygwin)
    [~,msg] = system('wmic OS get FreePhysicalMemory /Value');
    freebytes = str2double(msg(26:end))*1e3;
else % is matlab
    [~,s]=memory;
    freebytes = s.PhysicalMemory.Available;
end

end %function
