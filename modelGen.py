import torch.nn as nn
import torch.nn.functional as F
import torch

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        size_filter_in = 16
        self.conv1_1 = nn.Conv2d(1, size_filter_in, kernel_size=3, padding=1)
        nn.init.kaiming_normal_(self.conv1_1.weight, mode='fan_out', nonlinearity='leaky_relu')
        self.conv1_2 = nn.Conv2d(size_filter_in, size_filter_in, kernel_size=3, padding=1)
        nn.init.kaiming_normal_(self.conv1_2.weight, mode='fan_out', nonlinearity='leaky_relu')
        # self.pool1 = nn.MaxPool2d(kernel_size=2)
        
        self.conv2_1 = nn.Conv2d(size_filter_in, size_filter_in*2, kernel_size=3, padding=1)
        nn.init.kaiming_normal_(self.conv2_1.weight, mode='fan_out', nonlinearity='leaky_relu')
        self.conv2_2 = nn.Conv2d(size_filter_in*2, size_filter_in*2, kernel_size=3, padding=1)
        nn.init.kaiming_normal_(self.conv2_2.weight, mode='fan_out', nonlinearity='leaky_relu')
        # self.pool2 = nn.MaxPool2d(kernel_size=2)

        self.conv3_1 = nn.Conv2d(size_filter_in*2, size_filter_in*4, kernel_size=3, padding=1)
        nn.init.kaiming_normal_(self.conv3_1.weight, mode='fan_out', nonlinearity='leaky_relu')
        self.conv3_2 = nn.Conv2d(size_filter_in*4, size_filter_in*4, kernel_size=3, padding=1)
        nn.init.kaiming_normal_(self.conv3_2.weight, mode='fan_out', nonlinearity='leaky_relu')
        # self.pool3 = nn.MaxPool2d(kernel_size=2)

        # self.conv4_1 = nn.Conv2d(size_filter_in*4, size_filter_in*8, kernel_size=3, padding=1)
        # self.conv4_2 = nn.Conv2d(size_filter_in*8, size_filter_in*8, kernel_size=3, padding=1)
        # self.drop4 = nn.Dropout(p=0.5)
        
        # self.conv5_1 = nn.Conv2d(size_filter_in*8, size_filter_in*16, kernel_size=3, padding=1)
        # self.conv5_2 = nn.Conv2d(size_filter_in*16, size_filter_in*16, kernel_size=3, padding=1)
        # # self.drop5 = nn.Dropout(p=0.5)

        # self.up6 = nn.ConvTranspose2d(size_filter_in*16 , size_filter_in*8 , kernel_size= 2 , stride= 2 , padding= 0 )
        # self.conv6_1 = nn.Conv2d(size_filter_in*16 , size_filter_in*8 , kernel_size= 3 , padding= 1 )
        # self.conv6_2 = nn.Conv2d(size_filter_in*8 , size_filter_in*8 , kernel_size= 3 , padding= 1 )
        # # self.drop6 = nn.Dropout(p=0.5) # may consider this drop but no there in code

        # self.up7 = nn.ConvTranspose2d(size_filter_in*8 , size_filter_in*4 , kernel_size= 2 , stride= 2 , padding= 0 )
        # self.conv7_1 = nn.Conv2d(size_filter_in*8 , size_filter_in*4 , kernel_size= 3 , padding= 1 )
        # self.conv7_2 = nn.Conv2d(size_filter_in*4 , size_filter_in*4 , kernel_size= 3 , padding= 1 )
        # self.drop7 = nn.Dropout(p=0.5) # may consider this drop but no there in code

        self.up8 = nn.ConvTranspose2d(size_filter_in*4 , size_filter_in*2 , kernel_size= 2 , stride= 2 , padding= 0 )
        nn.init.kaiming_normal_(self.up8.weight, mode='fan_out', nonlinearity='leaky_relu')
        self.conv8_1 = nn.Conv2d(size_filter_in*4 , size_filter_in*2 , kernel_size= 3 , padding= 1 )
        nn.init.kaiming_normal_(self.conv8_1.weight, mode='fan_out', nonlinearity='leaky_relu')
        self.conv8_2 = nn.Conv2d(size_filter_in*2 , size_filter_in*2 , kernel_size= 3 , padding= 1 )
        nn.init.kaiming_normal_(self.conv8_2.weight, mode='fan_out', nonlinearity='leaky_relu')

        self.up9 = nn.ConvTranspose2d(size_filter_in*2 , size_filter_in , kernel_size= 2 , stride= 2 , padding= 0 )
        nn.init.kaiming_normal_(self.up9.weight, mode='fan_out', nonlinearity='leaky_relu')
        self.conv9_1 = nn.Conv2d(size_filter_in * 2, size_filter_in, kernel_size=3, stride=1, padding=1)
        nn.init.kaiming_normal_(self.conv9_1.weight, mode='fan_out', nonlinearity='leaky_relu')
        self.conv9_2 = nn.Conv2d(size_filter_in, size_filter_in, kernel_size=3, stride=1, padding=1)
        nn.init.kaiming_normal_(self.conv9_2.weight, mode='fan_out', nonlinearity='leaky_relu')
        self.conv9_3 = nn.Conv2d(size_filter_in, 2, kernel_size=3, stride=1, padding=1)
        nn.init.kaiming_normal_(self.conv9_3.weight, mode='fan_out', nonlinearity='leaky_relu')
        
        self.conv10 = nn.Conv2d(2, 1, kernel_size=1)
        nn.init.kaiming_normal_(self.conv10.weight, mode='fan_out', nonlinearity='tanh')
        # nn.init.kaiming_normal_(self.conv1.weight, mode='fan_out', nonlinearity='linear')
    def forward(self,x):
        conv1_out = F.leaky_relu(self.conv1_1(x))
        conv1_out = F.leaky_relu(self.conv1_2(conv1_out))
        pool1_out = F.max_pool2d(conv1_out, kernel_size=2)
        
        conv2_out = F.leaky_relu(self.conv2_1(pool1_out))
        conv2_out = F.leaky_relu(self.conv2_2(conv2_out))
        pool2_out = F.max_pool2d(conv2_out, kernel_size=2)
        
        conv3_out = F.leaky_relu(self.conv3_1(pool2_out))
        conv3_out = F.leaky_relu(self.conv3_2(conv3_out))
        drop3_out = F.dropout(conv3_out, p = 0.5)
        # pool3_out = F.max_pool2d(conv3_out, kernel_size=2)

        
        # conv4_out = F.leaky_relu(self.conv4_1(pool3_out))
        # conv4_out = F.leaky_relu(self.conv4_2(conv4_out))
        # drop4_out = F.dropout(conv4_out, p = 0.5)
        # pool4_out = F.max_pool2d(drop4_out, kernel_size=2)
        
        # conv5_out = F.leaky_relu(self.conv5_1(pool4_out))
        # conv5_out = F.leaky_relu(self.conv5_2(conv5_out))
        # drop5_out = F.dropout(conv5_out, p = 0.5)
        
        # up6_out = F.leaky_relu(self.up6(drop5_out))
        # print(up6_out.shape)
        # print(drop4_out.shape)
        # merge6_out = torch.cat((up6_out,drop4_out), dim = 1)
        # conv6_out = F.leaky_relu(self.conv6_1(merge6_out))
        # conv6_out = F.leaky_relu(self.conv6_2(conv6_out))
        
        # up7_out = F.leaky_relu(self.up7(drop4_out, output_size=(conv3_out.shape[2],conv3_out.shape[3])))
        # merge7_out = torch.cat([up7_out,conv3_out], dim = 1)
        # conv7_out = F.leaky_relu(self.conv7_1(merge7_out))
        # conv7_out = F.leaky_relu(self.conv7_2(conv7_out))
        
        up8_out = F.leaky_relu(self.up8(drop3_out, output_size=(conv2_out.shape[2],conv2_out.shape[3])))
        merge8_out = torch.cat([up8_out,conv2_out], dim = 1)
        conv8_out = F.leaky_relu(self.conv8_1(merge8_out))
        conv8_out = F.leaky_relu(self.conv8_2(conv8_out))
        
        up9_out = F.leaky_relu(self.up9(conv8_out, output_size=(conv1_out.shape[2],conv1_out.shape[3])))
        merge9_out = torch.cat([up9_out,conv1_out], dim = 1)
        conv9_out = F.leaky_relu(self.conv9_1(merge9_out))
        conv9_out = F.leaky_relu(self.conv9_2(conv9_out))
        conv9_out = F.leaky_relu(self.conv9_3(conv9_out))
        
        # out = self.conv10(conv9_out)
        out = F.tanh(self.conv10(conv9_out))
        return out