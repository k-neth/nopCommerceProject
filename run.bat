@REM pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
pytest  -v -s testCases\test_jumia.py --browser=chrome --html=./Reports/myreport.html --log-cli-level=debug