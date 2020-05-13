---
title: semantic segmentation of Medical Images
date: 2019-12-05
author: zwx
tags: segmentation
---

# semantic segmentation of Medical Images

- - -
## 发展流程
- edge detection filters and mathematical methods
- machine learning approaches extracting hand-crafted features
- deep learning techniques
- - -

## network structure

### CNN
- patch-wise prediction

### Fully Convolutional Network（FCN）
- pixel-wise prediction from the full-sized image
- up-sampling the output feature map
- 保护纹理信息，混合粗粒度层和细粒度层
- Cascaded FCN（以肝部问题为例，先分割肝，然后在肝上分割病灶）

### Encoder-decoder Network

1. U-Net
    - a contracting path to capture context
    - a symmetric expanding path that enables precise localization
    - skip connections
    - weighted BCE

2. DCAN

3. V-Net
    - Residual connections
    - dice loss

4. DenseNet-based

### Attention-based

### Adversarial-based

### Recurrent Neural Network-based

## Transfer Learning

## loss function

## challenges and limitations




