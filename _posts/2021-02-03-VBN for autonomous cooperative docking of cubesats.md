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
- 导航滤波使用了线性耦合动力学，描述运动过程

## Introduction
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

## 交会场景 + 对接需求
![交会场景](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/%E4%BA%A4%E4%BC%9A%E5%9C%BA%E6%99%AF.png)

- S24处：chaser body frame和LVLH frame对准。位置由CDGPS获得，角度依赖于恒星追踪器、6个太阳传感器、磁力计、三轴陀螺仪。
- S3处：CDGPS导航和VBN第一次切换（航天器尺寸较小，GNSS多径效应可忽略不计），在5m-2.5m范围内强制直线运动

## Cooperative VBN
### 符号 + 参考系
#### 参考系
- 惯性坐标系I：Earth-centred Inertial（ECI）frame（J2000定义）
- 轨道坐标系o：LVLH frame(orbital frame)

#### 动力学相关参考系
- 几何坐标系g：geometrical frame，固定在立方星上，通常位于顶点处
- 本体坐标系b：body frame，位于g中，原点在立方星质心，与卫星主惯性轴对齐
- d：docking port frame，位于g中，其位置由平移和旋转定义
- n：the frame used for the VBN，类似于d
![参考系](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/%E5%8F%82%E8%80%83%E6%A1%86%E6%9E%B6.png)

#### 转换关系
- r bd：目标中，d在b参考系中位置

### 相对动力学
- 推导耦合旋转/平移系统的非线形动力学方程，并将其线性化
- [[paper](http://refhub.elsevier.com/S0094-5765(17)30908-6/sref26)]：线性耦合动力学，用于ATV和ISS的对接（由于在o参考系下，ISS的对齐和稳定性，其运动可通过谐波振荡器估算，该假设在立方星上无法应用，且不可能像ISS一样稳定）

#### 姿态耦合
- 得到相对姿态空间状态模型
- 在o参考系下导出及线性化
- b相对于o参考系的角速度，表示为b相对惯性框架的旋转

#### 位置耦合
- 得到相对位置空间状态模型

### 测量方程
- 推导测量方程

















