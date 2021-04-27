cd test
ln -s ../src src
pytest -q DatabaseClassTest.py
rm -r src
cd ..
echo "Will be closed in 100 seconds ..."
sleep 100s