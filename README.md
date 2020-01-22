# Spotify Hands Free

Based on [Prasad9/Classify-HandGesturePose](https://github.com/Prasad9/Classify-HandGesturePose) which is itself a fork of [lmb-freiburg/hand3d](https://github.com/lmb-freiburg/hand3d).

## How it works

The goal is to interact with Spotify, on MacOS, with gestures.

Each second, the webcam will take a photo using imagesnap (Objective-C), the client (Node.js) will send via a socket the image path to a Python script which will do the analyze. Once it's done, result is sent back to Node.js which will call appropriate AppleScript action.

## Machine Learning

**First Layer:** Hand3D library is used to extract 3D hand pose from a single RGB Image. The model is trained with more than 40.000 images.

**Second Layer:** Prasad9's work is used to interpret data extracted by Hand3D (for instance coordinates of the 21 hand's keypoints).

**Third Layer:** We wrap all this with Node.js to make it a real practical application.

## Requirements

- MacOS
- Spotify
- brew
- python, pipenv
- imagesnap
- Node.js

## First time install

```sh
brew install imagesnap
npm install
cd hand-gesture
pipenv install
```

## Each time running

```sh
./run.sh
```

Or if you prefer run it manually:

```sh
# run Spotify
# start hand gesture listening
cd hand-gesture
pipenv shell
python evaluate_pose.py
# start infinite nodejs loop
cd ..
node index.js
```
