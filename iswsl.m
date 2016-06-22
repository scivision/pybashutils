function yeswsl = iswsl()
persistent wsl;

if isempty(wsl)
    if ispc || ismac
        wsl=false;
    elseif isunix
        fid = fopen('/proc/version');
        v = fscanf(fid,'%s');
        fclose(fid);
        wsl = ~isempty(strfind(v,'Microsoft'));
    end
end

yeswsl=wsl; % has to be a separate line/variable for matlab

end
