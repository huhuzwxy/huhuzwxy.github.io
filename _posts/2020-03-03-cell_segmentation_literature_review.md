---
title: cell segmentation
date: 2020-03-03
author: zwx
tags: segmentation
---

## 典型网络

### [FCN](https://arxiv.org/pdf/1605.06211.pdf) 2015年

### [U-Net](https://arxiv.org/pdf/1505.04597.pdf) 2015年

### [SegNet](https://arxiv.org/pdf/1511.00561.pdf) 2016年

### [FusionNet](https://arxiv.org/pdf/1612.05360.pdf) 2016年

    -将分割网络和残差网络相结合，用于细胞分割。
    -引入了基于求和的特征层连接，从而可以提供更深的网络架构来实现更精确的分割。

### [attention-UNet]<https://github.com/ozan-oktay/Attention-Gated-Networks>

    - Adam + BN + data augmentation
    - Dice loss


### [MIMO-Net](http://www.bioimageanalysis.org/wp/wp-content/uploads/formidable/6/MIMO-Net_Isbi2017.pdf) 2017年

    - 多输入多输出卷积神经网络，用于荧光显微镜图像中的细胞分割。
    - 网络使用输入图像的多种分辨率训练网络参数，连接中间层以获得更好的定位和上下文，并使用多分辨率反卷积滤波器生成输出。
    - 通过添加绕过最大池化操作的额外卷积层，使得网络可处理可变强度的细胞边界和可变高度的细胞大小。

### [FCNG](https://ieeexplore.ieee.org/abstract/document/7950548) 2017年

    - 提出了一种将全卷积网络和基于图的方法相结合的宫颈细胞分割方法。
    - FCN通过训练，可以学习宫颈细胞的高级特征，以生成细胞标签掩膜和细胞概率图。
    - 标签掩膜用于通过图像变换构造图；细胞概率图被公式化为图损失函数。
    - 通过动态编程找出全局最优路径。

### [CNN+RNN](https://ieeexplore.ieee.org/abstract/document/8402091) 2018年

    - 提出了CNN-RNN框架，该框架将CNN和RNN结合，加深了对图像内容的理解并了解了图像的结构化特征，用于血细胞分割。

### [R2U-Net](https://ieeexplore.ieee.org/abstract/document/8556686) 2018年

    - 提出了一种基于U-Net模型的递归残差卷积神经网络，用于细胞分割。
    - 残余单元在训练深度架构时有帮助。
    - 具有递归残差卷积层的特征累积可确保对分割任务进行更好的特征表示。

### <https://arxiv.org/pdf/1901.10170.pdf> 2019年

    - 提出了一个集成模型，将U-Net和Mask-RCNN的预测相结合，用于细胞分割。

### [GRUU-Net](https://www.sciencedirect.com/science/article/abs/pii/S1361841518306753#fig0009) 2019年

    - 提出了一种将卷积神经网络和门控递归神经网络集成在多个图像尺度上的分割算法，用于胶质母细胞瘤细胞核分割。
    - 为了提高训练的鲁棒性并改善分割效果，引入了focal loss。
    - 提出了一种用于优化集成神经网络训练的分布式方案。

### [LSTM-UNet](https://ieeexplore.ieee.org/abstract/document/8759447) 2019年

    - 将卷积长短期记忆（C-LSTM）与U-Net集成在一起。
    - 该网络的独特体系结构使其能够在C-LSTM存储单元中捕获多尺度，紧凑的时空编码。

### [attention-UNet](https://www.sciencedirect.com/science/article/abs/pii/S1361841518308442) 2019年

    - 用于神经细胞实例分割。
    - 将SSD和U-Net结合在一起，并在检测和分割模块中采用注意力机制，以将模型重点放在与任务相关的特征上。


## 光照校正

## [伪平场校正]<https://jcp.bmj.com/content/56/8/619>

    - 用高斯滤波图像代替平场图像。

## 去噪
- - -

- 空域滤波（线形+非线性）
- 频域滤波
- 形态学滤波

- - -

## [小波变换]<https://digital-library.theiet.org/content/journals/10.1049/el.2010.2063>

    - 使用小波变换和Haar变换，增强图像的细节，并有效地保留其边缘特征。
    - 首先，用小波变换分解医学图像。
    - 其次，对所有高频子图像进行Haar变换分解。
    - 第三，通过软阈值方法降低了频率场中的噪声。
    - 第四，通过在不同的子图像中使用不同的权重值来增强高频系数。
    - 然后，通过逆小波变换和逆Haar变换获得增强图像。
    - 最后，通过非线性直方图均衡化来拉伸图像的直方图。