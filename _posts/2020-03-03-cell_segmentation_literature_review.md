---
title: cell segmentation
date: 2020-03-03
author: zwx
tags: segmentation
---

# 典型网络

###1. [FCN](https://arxiv.org/pdf/1605.06211.pdf) 2015年
![](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/fcn.png)

###2. [U-Net](https://arxiv.org/pdf/1505.04597.pdf) 2015年
![](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/unet.png)

3. [SegNet](https://arxiv.org/pdf/1511.00561.pdf) 2016年
![](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/segnet.png)

4. [FusionNet Res-UNet](https://arxiv.org/pdf/1612.05360.pdf) 2016年
    - 将分割网络和残差网络相结合，用于细胞分割。
    - 引入了基于求和的特征层连接，从而可以提供更深的网络架构来实现更精确的分割。

5. [DilatedNet](https://arxiv.org/pdf/1511.07122.pdf) 2016年

6. [Tiramisu Dense-UNet](https://arxiv.org/pdf/1611.09326.pdf) 2017年
    - 将分割网络和残差网络相结合，用于细胞分割。
    - 引入了基于求和的特征层连接，从而可以提供更深的网络架构来实现更精确的分割。

7. [MIMO-Net](http://www.bioimageanalysis.org/wp/wp-content/uploads/formidable/6/MIMO-Net_Isbi2017.pdf) 2017年
    - 多输入多输出卷积神经网络，用于荧光显微镜图像中的细胞分割。
    - 网络使用输入图像的多种分辨率训练网络参数，连接中间层以获得更好的定位和上下文，并使用多分辨率反卷积滤波器生成输出。
    - 通过添加绕过最大池化操作的额外卷积层，使得网络可处理可变强度的细胞边界和可变高度的细胞大小。

8. [Attention-UNet](https://arxiv.org/pdf/1804.03999.pdf) 2018年
    - Adam + BN + data augmentation
    - Dice loss

9. [R2UNet](https://arxiv.org/ftp/arxiv/papers/1802/1802.06955.pdf) 2018年
    - 提出了一种基于U-Net模型的递归残差卷积神经网络，用于细胞分割。
    - 残余单元在训练深度架构时有帮助。
    - 具有递归残差卷积层的特征累积可确保对分割任务进行更好的特征表示。

10. [UNet++](https://arxiv.org/pdf/1807.10165.pdf) 2018年

# cell image analysis

1. [Cell Image Analysis](http://www.cs.cmu.edu/~zhaozhen/Papers/WACV2011_CellImageAnalysis.pdf) 2011年

2. [Fundamentals of Biomedical Image Processing](https://elearning.uniroma1.it/pluginfile.php/509402/mod_resource/content/1/9783642158155-c1.pdf) 2011年

3. [Data-analysis strategies for image-based cell profiling](https://www.nature.com/articles/nmeth.4397) 2017年

# 分割综述

1. [Deep Semantic Segmentation of Natural and Medical Images: A Review](https://arxiv.org/pdf/1910.07655.pdf) 2019年

2. [Phase Contrast Microscopy Cell Population Segmentation: A Survey](https://arxiv.org/pdf/1911.11111.pdf) 2019年

# 显微镜

1. [利用光学原理恢复细胞图像](https://arxiv.org/pdf/1910.07655.pdf) 2019年

