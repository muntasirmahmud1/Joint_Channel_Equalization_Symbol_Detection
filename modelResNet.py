import torch.nn as nn
import torch.nn.functional as F

class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=3, stride=1, padding=1):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, stride=stride, padding=padding)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=kernel_size, stride=stride, padding=padding)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride),
                nn.BatchNorm2d(out_channels)
            )

    def forward(self, x):
        residual = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        out = self.conv2(out)
        out = self.bn2(out)
        out += self.shortcut(residual)
        out = self.relu(out)
        return out

class ResNet(nn.Module):
    def __init__(self, num_classes=8):
        super(ResNet, self).__init__()
        self.conv = nn.Conv2d(1, 40, kernel_size=1, stride=1, padding=0)
        self.bn = nn.BatchNorm2d(40)
        self.layer1 = self.make_layer(40, 5)
        self.fc1 = nn.Linear(9360, 128)
        self.drop1 = nn.Dropout(p=0.5)
        self.fc2 = nn.Linear(128, 128)
        self.drop2 = nn.Dropout(p=0.5)
        self.fc3 = nn.Linear(128, num_classes)

    def make_layer(self, out_channels, num_blocks):
        layers = []
        layers.append(ResidualBlock(40, out_channels))
        for i in range(num_blocks-1):
            layers.append(ResidualBlock(out_channels, out_channels))
        return nn.Sequential(*layers)

    def forward(self, x):
        out = self.conv(x)
        out = self.bn(out)
        out = F.relu(out)
        out = self.layer1(out)
        out = F.max_pool2d(out, kernel_size=2, stride=2)
        out = out.view(out.size(0), -1)
        out = self.fc1(out)
        out = F.selu(out)
        out = self.drop1(out)
        out = self.fc2(out)
        out = F.selu(out)
        out = self.drop2(out)
        out = self.fc3(out)
        return out