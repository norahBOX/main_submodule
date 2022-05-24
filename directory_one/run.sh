#!/bin/bash
BASEDIR=`dirname "$(realpath $0)"` 
PYTHON="$HOME/.pyenv/shims/python"
cd $BASEDIR/..
$PYTHON -m directory_one.main_test