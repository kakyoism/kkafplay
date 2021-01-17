#! /bin/sh


ScriptDir="$( cd "$( dirname "$0" )" && pwd )"
cd - &> /dev/null

RootDir="$ScriptDir"/..
SrcDir="$RootDir"/src

poetry run pyinstaller "$SrcDir"/main.py --onefile --osx-bundle-identifier com.example.app
