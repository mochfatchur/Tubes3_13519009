@echo off
cd src
pytest -q DatabaseClassTest.py
pytest -q GetDueTodayTaskCommandTest.py
pytest -q AddTaskCommandTest.py
pytest -q DeleteTaskTest.py
pytest -q GetAllTaskCommandTest.py
pytest -q GetSpecificTimeLeftTaskTest.py
pytest -q ExtractorTest.py
cd ..