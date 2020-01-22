#!/bin/sh

trap 'kill $BGPID; exit' INT
cd hand-gesture
pipenv run python evaluate_pose.py &
BGPID=$!
cd ..
node index.js
