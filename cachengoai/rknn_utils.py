import cv2
import torch
import numpy as np
from cachengoai.image_utils import get_frames
from cachengoai.yolov5_utils import yolov5_post_process

IMG_SIZE = 640

def rknn_preprocess(frame):
    frame = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
    frame = np.expand_dims(frame,0)
    return frame

def perform_inference(video_path,model,conf_thresh):
    preds = []
    dets = 0
    objs = []
    for frame in get_frames(video_path):
        frame_preds = []
        if frame is not None:
        # Resize
            frame2 = rknn_preprocess(frame)
        # Inference
            outputs = model.inference(inputs=[frame2], data_format=['nhwc'])
        # post process
            input0_data = outputs[0]
            input1_data = outputs[1]
            input2_data = outputs[2]

            input0_data = input0_data.reshape([3, -1]+list(input0_data.shape[-2:]))
            input1_data = input1_data.reshape([3, -1]+list(input1_data.shape[-2:]))
            input2_data = input2_data.reshape([3, -1]+list(input2_data.shape[-2:]))

            input_data = list()
            input_data.append(np.transpose(input0_data, (2, 3, 0, 1)))
            input_data.append(np.transpose(input1_data, (2, 3, 0, 1)))
            input_data.append(np.transpose(input2_data, (2, 3, 0, 1)))

            boxes, classes, scores = yolov5_post_process(input_data,frame)
            for obj in classes:
                objs.append(obj)

            if boxes is not None and boxes[0] is not None:
                for i,box in enumerate(boxes[0]):
                    if scores[i] >= conf_thresh:
                        dets+=1
                        box = list(box)
                        box.append(scores[i])
                        box.append(classes[i])
                        frame_preds.append(box)
        preds.append(torch.Tensor([frame_preds]))

    return preds,dets,list(set(objs))
