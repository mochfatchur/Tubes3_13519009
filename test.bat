@echo off
cd src
pytest -q DatabaseClassTest.py
pytest -q GetDueTodayTaskCommandTest.py
cd ..