# Cachengo-ai

Tools for running AI workloads on Cachengo symbiotes

## Package

Basic structure of package is

```
├── README.md
├── cachengoai
│   ├── __init__.py
│   ├── rknn.py
│   └── rknn_utils.py
│   └── bbox_utils.py
│   └── yolov5_utils.py
│   └── image_utils.py
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
```

## Installation
Package can be installed by running
```
pip install git+https://github.com/cachengo/cachengo-ai.git
```

Package can also be installed by running the following command inside the repo directory
```
pip install .
```
## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

## Tests

Coming soon...

## Examples

### Run inference on video file
```py
from cachengoai import rknn

# Initialize default yolov5 model with COCO classes
model = rknn.model()
# Run inference on video file and return list of detected classes
# Output is array of detected classes
_,_,objs = rknn.detect(model,"./TestVideo.mp4",conf_thresh=0.6)
```

### Run inference on raw frames
```py
from cachengoai import rknn
import cv2

# Convert video to raw frames
def video_to_frames(video_path):
    """Converts a video to a list of raw frames using OpenCV."""

    cap = cv2.VideoCapture(video_path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    return frames

# Initialize local model
model = rknn.model("./yolov5s-640-640.rknn")
# Run inference on video file and return list of detected classes
raw_frames = video_to_frames('./TestVideo.mp4')

_,_,objs = rknn.detect(model,conf_thresh=0.6,frames=raw_frames)
```