import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class ConvNet1d(nn.Module):
    def __init__(self):
        super(ConvNet2d, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.pool1 = nn.MaxPool1d(kernel_size=3, stride=2, padding=1)
        self.bn1 = nn.BatchNorm1d(32)
        
        self.conv2 = nn.Conv1d(in_channels=32, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.pool2 = nn.MaxPool1d(kernel_size=3, stride=2, padding=1)
        self.bn2 = nn.BatchNorm1d(32)
        
        self.conv3 = nn.Conv1d(in_channels=32, out_channels=32, kernel_size=2, stride=1, padding=0)
        self.pool3 = nn.MaxPool1d(kernel_size=2, stride=2, padding=0)
        self.bn3 = nn.BatchNorm1d(32)
        
        self.fc1 = nn.Linear(119968, 64)
        self.dropout = nn.Dropout(0.3)
        self.fc2 = nn.Linear(64, 8)
        
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool1(x)
        x = self.bn1(x)
        
        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        x = self.bn2(x)
        
        x = F.relu(self.conv3(x))
        x = self.pool3(x)
        x = self.bn3(x)
        
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        x = F.softmax(x)
        return x

class ConvNet2d(nn.Module):
    def __init__(self):
        super(ConvNet2d, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=(3,1), stride=1, padding=(1,0))
        self.pool1 = nn.MaxPool2d(kernel_size=(3,1), stride=(2,1), padding=(1,0))
        self.bn1 = nn.BatchNorm2d(32)
        
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3,1), stride=1, padding=(1,0))
        self.pool2 = nn.MaxPool2d(kernel_size=(3,1), stride=(2,1), padding=(1,0))
        self.bn2 = nn.BatchNorm2d(32)
        
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(2,1), stride=1, padding=0)
        self.pool3 = nn.MaxPool2d(kernel_size=(2,1), stride=(2,1), padding=0)
        self.bn3 = nn.BatchNorm2d(32)
        
        self.fc1 = nn.Linear(199968, 64)
        self.dropout = nn.Dropout(0.3)
        self.fc2 = nn.Linear(64, 8)
        
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool1(x)
        x = self.bn1(x)
        
        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        x = self.bn2(x)
        
        x = F.relu(self.conv3(x))
        x = self.pool3(x)
        x = self.bn3(x)
        
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        x = F.softmax(x) 
        return x