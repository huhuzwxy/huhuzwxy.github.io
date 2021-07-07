---
title: model-based 6d pose estimation
date: 2021-01-20
author: zwx
tags: 三维重建
---
## Rapid

## LineMod（2011）
- [作者个人主页](http://campar.in.tum.de/Main/StefanHinterstoisser)  
- [【PDF】Multimodal Templates for Real-Time Detection of Texture-less Objects in
Heavily Cluttered Scenes，ICCV，2011](http://far.in.tum.de/pub/hinterstoisser2011linemod/hinterstoisser2011linemod.pdf)  
- [【PDF】Model Based Training, Detection and Pose
Estimation of Texture-Less 3D Objects in
Heavily Cluttered Scenes，ACCV，2012](http://www.stefan-hinterstoisser.com/papers/hinterstoisser2012accv.pdf)

### 模版构造
![LineMODE算法特征](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/LineMOD%E7%89%B9%E5%BE%81.png)  

- 利用梯度和表面法向量构造特征

### 匹配
- 相似度衡量
- 算法加速

## PWP3D（2012）
- [【PDF】 PWP3D: Real-time segmentation and
tracking of 3D objects](https://pdfs.semanticscholar.org/caa1/5c52919ddbab8a5c5d99d35c70d877afac0d.pdf)  
- [【code】 github](https://github.com/lumark/PWP3D)  

### 分割 region-based cost function
- 

## ECCV 2018 He
- [【PDF】 Implicit 3D Orientation Learning for
6D Object Detection from RGB Images](https://openaccess.thecvf.com/content_ECCV_2018/papers/Martin_Sundermeyer_Implicit_3D_Orientation_ECCV_2018_paper.pdf)  
- [【code】 github](https://github.com/DLR-RM/AugmentedAutoencoder)  

## PVNet（2019）浙大
- [【PDF】 PVNet: Pixel-wise Voting Network for 6DoF Pose Estimation](https://openaccess.thecvf.com/content_CVPR_2019/papers/Peng_PVNet_Pixel-Wise_Voting_Network_for_6DoF_Pose_Estimation_CVPR_2019_paper.pdf)  
- [【code】 github](https://github.com/zju3dv/pvnet)

## 数据集
1. [Tango spacecraft，2019](https://kelvins.esa.int/satellite-pose-estimation-challenge/data/)  
2. [BOP数据](https://bop.felk.cvut.cz/datasets/)