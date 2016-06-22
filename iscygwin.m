function iscyg = iscygwin()
persistent cyg;

if isempty(cyg)
    if ispc || ismac
        cyg=false;
    elseif isunix
        fid = fopen('/proc/version');
        v = fscanf(fid,'%s');
        fclose(fid);
        cyg = ~isempty(strfind(v,'CYGWIN'));
    end
end

iscyg=cyg; % has to be a separate line/variable for matlab

end
