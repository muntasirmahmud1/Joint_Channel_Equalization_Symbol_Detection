import torch
import yaml
import numpy
from glob import glob
import random
import numpy as np
from scipy.signal import butter,filtfilt
class uwdataset(torch.utils.data.Dataset):
    def __init__(self, path_list, config_file= 'config.yaml', data_type = '2d'):
        with open(path_list, "r") as file:
            self.path_list = file.readlines()
        with open(config_file, "r") as file:
            config = yaml.safe_load(file)
        self.label = config['label']
        self.data_type = data_type
    def butter_lowpass_filter(self, data, cutoff=400000, fs=100000000, order=3):
        nyq = 0.5 * fs  # Nyquist Frequency
        normal_cutoff = cutoff / nyq
        # Get the filter coefficients 
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        y = filtfilt(b, a, data)
        return y
    def __getitem__(self, index):
        data = np.genfromtxt('../'+self.path_list[index].split('\n')[0], delimiter=",", dtype=np.float16)
        data = self.butter_lowpass_filter(data)
        if (self.data_type == '2d'):
            data = data.reshape(1,-1,1)
        elif (self.data_type == '1d'):
            data = data.reshape(1,-1)
        label = self.path_list[index].split('/')[-2]
        label = np.array(self.label[label])
        return torch.as_tensor(data.copy()).to(torch.float32).contiguous(), torch.as_tensor(label)
    def __len__(self):
        return len(self.path_list)
        
