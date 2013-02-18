@echo off
cd /D "%~dp0"
cls
cd wwqgtxx-goagent
del /f /s /q goagent-local\certs\*.crt
del /f /s /q goagent-local\certs\*.key
del /f /s /q goagent-local\ip.txt
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

utility\php\php.exe ..\sign.php
pause

git config --global push.default matching
git config core.autocrlf false
git init
git add .
git commit -m"bat"
git push https://code.google.com/p/wwqgtxx-goagent.goagent/ +master
start /min git push https://code.google.com/p/wwqgtxx-wallproxy.goagent/ +master
pause
cd ..
rmdir /S /Q wwqgtxx-goagent-Release
mkdir wwqgtxx-goagent-Release
xcopy wwqgtxx-goagent\* wwqgtxx-goagent-Release /s /e
pause
del /f /s /q wwqgtxx-goagent-Release\goagent-local\certs\*.crt
del /f /s /q wwqgtxx-goagent-Release\goagent-local\certs\*.key
rmdir /S /Q wwqgtxx-goagent-Release\.settings
del /f /s /q wwqgtxx-goagent-Release\.project
del /f /s /q wwqgtxx-goagent-Release\wwqgtxx-goagent.nsi
del /f /s /q wwqgtxx-goagent-Release\data\last-known-good
del /f /s /q wwqgtxx-goagent-Release\data\host
rmdir /S /Q wwqgtxx-goagent-Release\.git
rmdir /S /Q wwqgtxx-goagent-Release\FirefoxPortable
pause