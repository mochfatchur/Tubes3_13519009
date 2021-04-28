@echo off
cd src
pytest -q DatabaseClassTest.py
pytest -q GetDueTodayTaskCommandTest.py
pytest -q AddTaskCommandTest.py
pytest -q DeleteTaskCommandTest.py
pytest -q GetAllTaskCommandTest.py
pytest -q GetSpesificTimeLeftTaskCommandTest.py
pytest -q ExtractorTest.py
cd ..