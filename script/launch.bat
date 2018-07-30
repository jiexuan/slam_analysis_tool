@echo off

call "%~dp0bootstap_miniconda.bat" %*
set "Path=%mini_conda%;%Path%"
cd "%~dp0..\tools" && activate slam_plot