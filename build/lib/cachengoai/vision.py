from os import path, listdir
# from cachengoai.utils.rknn_utils import rknn_preprocess
# from cachengoai.utils.image_utils import get_frames
# from rknnlite.api import RKNNLite
# import rknnlite


# def rknpu(model_path=path.join(path.dirname(__file__), 'models/yolov5s-640-640.rknn')):
#     model = RKNNLite(verbose=False)
#     ret = model.load_rknn(model_path)
#     ret = model.init_runtime(core_mask=RKNNLite.NPU_CORE_0)
#     return ret

# def detect(model,video_path):

def test():
    print(listdir(path.dirname(__file__)))