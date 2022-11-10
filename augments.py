import numpy
import math
import json
from PIL import Image
from io import BytesIO
from torch.utils.data import Dataset
from torchvision import transforms
import h5py
import json
import numpy as np
import torch
class augmentations():
    def __init__(self, dict):
        self.dict= dict
        aug_list = []
        for c,report in enumerate(self.dict['report'].values()):
            if report == 'True':
                aug_list.append(list(self.dict['report'].keys())[c])
        for item in aug_list:
            globals()[item]()
    def rotations():
        pass
    def scaling():
        pass
    def mirroring():
        pass
    def reflection():
        pass