@echo off
PUSHD "%~dp0doc"
CALL sphinx-build source build
rem CALL sphinx-build -b pdf source build
POPD
