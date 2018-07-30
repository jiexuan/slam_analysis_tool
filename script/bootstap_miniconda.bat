@echo off
setlocal
rem set "env_file=%~dp0..\ts_detection.yml"
rem set "env_name=ts_detection"
rem if NOT "%~1"=="" set "env_file=%~1"
rem if NOT "%~2"=="" set "env_name=%~2"


set "mini_conda=%USERPROFILE%\.miniconda"
set "mini_conda_path=%mini_conda%\Scripts"

call :install_mini_conda

if exist "%mini_conda_path%" (
    echo "%env_file%"
	rem call %mini_conda_path%\conda env create -f %env_file%
)

endlocal & ^
set "mini_conda=%mini_conda_path%" & ^
set "env_name=%env_name%" & ^

goto :eof

:install_mini_conda
    set "Download_path=%mini_conda%\download"
	set "miniconda_app=Miniconda3-latest-Windows-x86_64.exe"
	set "miniconda_app_path=%Download_path%\Miniconda3-latest-Windows-x86_64.exe"	
	if not exist "%mini_conda%" ( 	
        mkdir %Download_path%
        echo "downloading miniconda"
		powershell -Command "Invoke-WebRequest https://repo.continuum.io/miniconda/%miniconda_app% -OutFile %miniconda_app_path%"		
		echo "downloading miniconda completed"

		if exist "%miniconda_app_path%" (
			echo "installing miniconda"
			start /wait "" %miniconda_app_path% /InstallationType=JustMe /RegisterPython=0 /S /D=%mini_conda%
			echo "installing miniconda completed"
		)
	)
goto :eof
