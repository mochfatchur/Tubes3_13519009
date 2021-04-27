@echo off
cd src
pytest -q DatabaseClassTest.py
pytest -q GetDueTodayTaskCommandTest.py
pytest -q AddTaskCommandTest.py
cd ..