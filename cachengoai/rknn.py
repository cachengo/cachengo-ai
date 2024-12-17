from os import path
from rknnlite.api import RKNNLite
from cachengoai.rknn_utils import perform_inference
import rknnlite

def model(model_path=path.join(path.dirname(__file__), 'yolov5s-640-640.rknn')):
    if model_path[-4:] != "rknn":
        print("Invalid model. Please provide valid rknn model")
        return
    rknn_model = RKNNLite(verbose=False)
    ret = rknn_model.load_rknn(model_path)
    if ret != 0:
        return 'Load RKNN model failed'
    try:
        ret = rknn_model.init_runtime(core_mask=RKNNLite.NPU_CORE_ALL)
        return rknn_model
    except Exception as e:
        print(e)
        return "Model could not be loaded"

def detect(model,video_path="",conf_thresh=0.7,frames=[]):
    try:
        preds,dets,objs =  perform_inference(video_path,model,conf_thresh,frames)
        return preds,dets,objs
    except Exception as e:
        print(e)
        return "Couldn't perform inference."
