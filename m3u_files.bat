@echo off
setlocal enabledelayedexpansion

:: ==========================================================
:: Batch Script to parse a directory for files with extensions
:: .cue, .chd, .iso, .img, and group related files (e.g., "disk 1", 
:: "side A", etc.) into a single .m3u playlist file.
:: ==========================================================

:: Set the file extensions to search for.
:: You can add more extensions if needed by modifying the list.
set extensions=*.cue *.chd *.iso *.img

:: Loop through each of the specified extensions.
for %%E in (%extensions%) do (
    :: Search for all files matching the current extension (%%E)
    :: in the current directory and all subdirectories.
    :: /B - bare format (just the filenames)
    :: /S - search recursively in all subdirectories
    :: 2^>nul - suppress error messages if no files are found
    for /F "delims=" %%F in ('dir /B /S "%%E" 2^>nul') do (
        :: Extract the base name of the file without the extension
        :: %%~nF gives us the filename only (without the path or extension).
        set "filename=%%~nF"
        
        :: Extract the directory path where the file is located
        :: %%~dpF gives us the directory path.
        set "directory=%%~dpF"

        :: Create the name of the .m3u file by stripping off the part
        :: of the filename that denotes "disk 1", "side A", etc.
        :: The !filename:~0,-8! trims off the last 8 characters (e.g., "(disk 1)").
        set "m3uFile=!directory!!filename:~0,-8!.m3u"

        :: Now check if the filename contains patterns like (disk 1),
        :: (side A), etc. using "findstr".
        :: The /I makes the match case-insensitive.
        :: The /R tells "findstr" to use a regular expression.
        :: The pattern looks for "(disk X)" or "(side X)" where X can be a digit or a letter.
        echo %%F | findstr /I /R ".*(disk.*[1-9A-Z]).* .*([1-9A-Z]).*" >nul

        :: If the pattern is found, the file is part of a set.
        :: We check if the findstr command found a match by using "errorlevel".
        if !errorlevel! == 0 (
            :: If this is the first file in the set, we create a new .m3u file.
            :: If the .m3u file already exists, this step is skipped.
            if not exist "!m3uFile!" (
                echo Creating M3U file: !m3uFile!
            )
            :: Append the current file's name (with extension) to the .m3u file.
            :: %%~nxF provides the file name with the extension.
            echo %%~nxF>>"!m3uFile!"
        )
    )
)

:: End of script
endlocal
