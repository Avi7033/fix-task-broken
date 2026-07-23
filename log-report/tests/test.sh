#!/bin/bash

#run the verifier tests and write the results to /logs/verifier/ctrf.json and /logs/verifier/reward.txt
# pytest and pytest-json-ctrf are baked into the environment image (environment/Dockerfile).
mkdir -p /logs/verifier
pytest --rootdir /app /app/tests/test_outputs.py -rA --ctrf=/logs/verifier/ctrf.json 

status=$?

if [ "$status" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi


# the script itself always exits clean.Pass or fail lives in reward.txt
exit 0