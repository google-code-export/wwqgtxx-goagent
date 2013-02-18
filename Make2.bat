@echo off
cd /D "%~dp0"
cls
cd wwqgtxx-wallproxy
del /f /s /q wallproxy-local\cert\certs\*.crt
del /f /s /q wallproxy-local\cert\certs\*.key
echo Generating hash table...
del hash.dat
if %PROCESSOR_ARCHITECTURE%==x86 (
	utility\md5deep.exe -rl . > hash.dat
) else (
	utility\md5deep64.exe -rl . > hash.dat
)

if exist hash.dat (
	echo  DONE generate hash table!
) else (
	echo  FAIL to generate hash table!
	pause
	exit
)

utility\php\php.exe cleanhash.php

utility\php\php.exe ..\sign2.php
pause

git config --global push.default matching
git config core.autocrlf false
git init
git add .
git commit -m"bat"
git push https://code.google.com/p/wwqgtxx-goagent.wallproxy/ +master
start /min git push https://code.google.com/p/wwqgtxx-wallproxy.wallproxy/ +master
pause
cd ..
rmdir /S /Q wwqgtxx-wallproxy-Release
mkdir wwqgtxx-wallproxy-Release
xcopy wwqgtxx-wallproxy\* wwqgtxx-wallproxy-Release /s /e
pause
del /f /s /q wwqgtxx-wallproxy-Release\wallproxy-local\cert\certs\*.crt
del /f /s /q wwqgtxx-wallproxy-Release\wallproxy-local\cert\certs\*.key
rmdir /S /Q wwqgtxx-wallproxy-Release\.settings
del /f /s /q wwqgtxx-wallproxy-Release\.project
del /f /s /q wwqgtxx-wallproxy-Release\wwqgtxx-wallproxy.nsi
del /f /s /q wwqgtxx-wallproxy-Release\data\last-known-good
del /f /s /q wwqgtxx-wallproxy-Release\data\host
rmdir /S /Q wwqgtxx-wallproxy-Release\.git
rmdir /S /Q wwqgtxx-goagent-Release\FirefoxPortable
pause