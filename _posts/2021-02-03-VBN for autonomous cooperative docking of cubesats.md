---
title: Vision Based Navigation for Autonomous Cooperative Docking of CubeSats 
date: 2021-02-03
author: zwx
tags: 论文阅读
---
## notes
- **地心惯性系（i）**：原点为地心，基准平面是历元J2000.0时的地球平赤道面。X轴指向此历元时的平春分点方向；Z轴指向平北极；y轴由右手定则确定。该坐标系用于描述航天器的轨道状态及绝对姿态。
- **轨道坐标系（o）**：原点在轨道上与航天器质心重合，Z轴指向地心，Y轴与轨道平面垂直，X按右手法则指向飞行方向。主星轨道坐标系为基准坐标系。
- **本体坐标系（b）**：原点与航天器的质心重合，三条正交的本体坐标轴分别与星体的本体特征轴平行。俯仰角（pitch），偏航角（yaw），翻滚角（roll）。姿态为0时，本体坐标系与轨道坐标系重合。
- **RVD**：rendezvous & docking 交会对接
- **VBN**：vision-based navigation 
- **ATV**：automated transfer vehicle 自动运载飞船
- **LoS**：Line of Sight
- **CDGPS**：Carrier Phase Differential GPS
- **ISS**：International Space Station
- **横向控制**：根据上层运动规划输出的路径、曲率等信息进行跟踪控制，以减少跟踪误差，同时保证稳定性。

## Highlights
- 系统由**camera + LED**组成，对接时导航精度优于1mm
-  线性旋转-平移耦合动力学系统(coupled dynamics)
-  可同时优化旋转和平移
-  对运动和传感器噪声不确定性均具备鲁棒性

## Abstract
- 适用于**立方星**的交会、对接导航方案
- **为什么应用VBN**：
	- 通过对ESA自动运载飞船GCN和俄罗斯对接系统的分析，得出两颗立方星的对接需要大约1cm的横向控制性能
	- 近距离时，视距限制和多径效应影响GNSS的测量，无法使用GNSS
	- GNSS的限制和对高控制精度的需求，交会、对接过程中最后10m使用视觉传感器
- **硬件系统组成**：卫星上单目相机 + 目标上的成组LEDs
- **算法优势**：
	- 测量方程可将旋转和平移分开，在对接时导航性能优于1mm
	- 测量方程可求得解析解，提供可分析的导航方案
	- 改方案可用于监视导航滤波，确保其稳定性，为自主交会对接增加保障
- 导航滤波初始化
- 实验证明，该方案能区分LED信号和太阳反射

## Introduction
![交会对接过程](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/%E4%BA%A4%E4%BC%9A%E5%AF%B9%E6%8E%A5%E8%BF%87%E7%A8%8B.jpg)

$$
RVD\ \left\{\begin{aligned}
	&Phasing：几十公里处 \\
	&Homing：十米至几百米内 \\
	&Docking \\
\end{aligned}
\right.
$$

### Methods
#### RVD
- 俄罗斯：RF-sensors [[paper. p245](https://www.sciencedirect.com/science/refhub/S0094-5765(17)30908-6/sref1)]
- 美国：Line of Sight [[paper](https://www.sciencedirect.com/science/refhub/S0094-5765(17)30908-6/sref2)]
- Today：GNSS + CDGPS（～10cm精度，最高达～1cm） + VBN

#### VBN
1. pnp -> 6DoF
	- 有源照明信标(LEDs)：4个共面可见LED + 1个红外
	- 无源：
	- $$
问题\ \left\{\begin{aligned}
	&EKF：视觉传感器存在噪声 \\
	&计算量大\\
\end{aligned}
\right.
$$

2. TRIAD / QUEST算法
	- ATV方案限制：相对姿态和LoS角很小

### proposed method
- 十字LED图案
- 可直接用于EKF，无需非线性求解/TRIAD/QUEST算法
- 可求解析解，获得确定解
- 适用于任何相对旋转/平移

## Rendezvous scenario and docking requirements
![交会场景](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/%E4%BA%A4%E4%BC%9A%E5%9C%BA%E6%99%AF.png)

- S24处：本体坐标系与轨道坐标系对准。位置由CDGPS获得，角度依赖于恒星追踪器、6个太阳传感器、磁力计、三轴陀螺仪。
- S3处：CDGPS导航和VBN第一次切换（航天器尺寸较小，GNSS多径效应可忽略不计），在5m-2.5m范围内强制直线运动

## Cooperative VBN
### 符号 + 参考系
#### 参考系
- 惯性坐标系I：Earth-centred Inertial（ECI）frame
- 轨道坐标系o：LVLH frame(orbital frame)

#### 动力学相关参考系
- 几何坐标系g：geometrical frame，固定在立方星上，通常位于顶点处
- 本体坐标系b：body frame，位于g中，原点在立方星质心，与卫星主惯性轴对齐
- d：docking port frame，位于g中，其位置由平移和旋转定义
- n：the frame used for the VBN，类似于d
![参考系](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/%E5%8F%82%E8%80%83%E6%A1%86%E6%9E%B6.png)

### 相对动力学模型
- 推导耦合旋转/平移系统的非线形动力学模型，并将其线性化
- [[paper](http://refhub.elsevier.com/S0094-5765(17)30908-6/sref26)]：线性耦合动力学，用于ATV和ISS的对接（由于在o参考系下，ISS的对齐和稳定性，其运动可通过谐波振荡器估算，该假设在立方星上无法应用，且不可能像ISS一样稳定）

#### 姿态耦合
- 得到相对姿态状态空间模型
- 在轨道系下导出，并将其线性化

#### 位置耦合
- 得到相对位置状态空间模型

### 测量方程
- 推导测量方程
- 对旋转、平移进行检测和校正

### 解析解
- LED1 LED2 LED3 LED4的对称性 -> 可得解析解

### EKF
- 两种EKF：
	- 10m - 5m处：外部LED + 中心LED + 星敏
	- 5m - 对接：5个中心对称LED

### VBN硬件
![LED2](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/LED2.png)
#### LED位置设计
- 外部LED尺寸应满足的需求：
	- 适合于立方星表面（10cm x 10cm）
	- 满足D1 = 5cm
- 内部LED尺寸应满足的需求：
	- 5m处进行模式切换时，有足够高的精度
	- 从5m至对接时，能观测到图案，且精度够高	
-  不用鱼眼镜头
-  上述制约使得D = 2cm
-  内部LED放置在立方星内部3cm处
![LED1](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/LED1.png)

#### 相机：
- 商业现货（COTS）硬件：COTS mono-chromatic Basler ACE camera acA3800-10 gm 
- [[官网链接](https://www.baslerweb.com/en/products/cameras/area-scan-cameras/ace/aca3800-10gm/)]
- 分辨率：2764 x 3856 pixels
- 1 pixel size = 1.67um
- focal length = 4mm
- FoV约为60deg
- 放置在立方星内部4cm处

#### 其它：
- 相机峰值量子效率 = 460nm，故选用蓝光LED（The camera sensor has its peak quantum efficiency at 460 nm. LEDs emitting in the blue part of the spectrum were thus selected. ）
- 所选LED：峰值发射 = 470nm，视角 = 80deg，发光强度 = 1.2cd
- 相机上使用带通滤波片，使来自太阳的杂散光（stray light）最小
- 滤波片的峰值透射率 = 470nm
- 建议用单色相机
![实验所用](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/LED3.png)

### LED检测和跟踪
- 唯一视觉算法：MATLAB Blob analysis
	- 在二进制图像上检测联通区域，提取质心
- 利用测量方程和导航滤波对LED进行主动跟踪（可定义ROI）
- 两种情况：
	- VBN已收敛，其精度可以进行初始跟踪。n个LED，检测到m个连通区域（m > n），此时可利用EKF提供的每个LED的估计位置，计算该估计位置与连通区域位置的范数，选取最接近的连通区域。
	- VBN未初始化或精度不达标。此时无法利用EKF进行主动跟踪，利用几何特征来解决。

### 几何特征
- 几何特征算法较简单，始终与EKF并行，提供LED检测的鲁棒性
![几何特征](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/%E5%87%A0%E4%BD%95%E7%89%B9%E5%BE%81.png)

#### 外部模式
- 角度：a接近180度；beta趋于0度
- 距离比：d1 / d2 = 1
- 额外特征：两个外部LED之间的像素距离（在5m处最大，10m最小）

#### 内部模式
- 距离比：d1 / d2， d1 / d3， d2 / d4， d3 / d4
- 角度：a1， a2， a3， a4
- 最后采用(d1 + d2) / (d3 + d4) = 1

















