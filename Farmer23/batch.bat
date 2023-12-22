@echo off
cls
echo ************************
echo Batch file for creating new directories
echo Originally created by NMG Oct 23
echo ***********************

set /p CONFIRMATION= Do you want to create a new project? (Y/N) :
if /i "%CONFIRMATION%"=="N" (
    echo Exiting
    timeout /t 5 
    exit
) else (
    echo Creating new project...
)
echo ****************

set /p NAME= Enter new project name, then press [return] 
echo New project %NAME% is being created
md %NAME%
cd %NAME%
md Documentation
md Tests
md Examples
md Templates
md Source
echo Folders successfully created
dir  /ad

echo ****************

cd ..

echo ****************




echo checking items in %CD%
FOR %%I IN (*) DO @ECHO %%I


echo *******************




cd %NAME%
echo Working directory changed to %Name%
echo Please pick 1 of the following 2 options

echo **********************


echo Option 1= Create readme.md and main.py


echo Option 2= Exit

echo ************************

set /p Option= Please choose (1) (2) :

    

if /i "%Option%"=="1" (
    copy nul main.py
    copy nul readme.md
    

)
if /i "%Option%"=="2" (
    echo Exiting
    timeout /t 5 
    exit

)