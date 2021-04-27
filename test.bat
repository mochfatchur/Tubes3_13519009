@echo off
cd test
ln -s ../src src
pytest -q DatabaseClassTest.py
rm -r src
cd ..