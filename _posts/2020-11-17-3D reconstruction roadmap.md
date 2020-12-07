---
title: 3D reconstruction roadmap
date: 2020-11-17
author: zwx
tags: 三维重建
---
$$
\left\{\begin{aligned}
	&三维重建 \ \left\{\begin{aligned}
		&SfM(Stucture \ from \ Motion) \left\{\begin{aligned}
			&特征提取 \\
			&关键点匹配 + 过滤 \\
			&SfM \left\{\begin{aligned}
				&增量式(Incremental)：openMVS、COLMAP\\
				&全局式(Global) \\
				&混合式(Hybrid) \\
				&层次式(hierarchica) \\
			\end{aligned}
			\right. \\
			&BA(Bundle \ Adjustment)优化 \\
			&MVS(Multiple \ View \ Stereo) \left\{\begin{aligned}
				&基于体素 \\
				&基于点云扩散 \\
				&基于深度图 \\
			\end{aligned} \right. \\
		\end{aligned} \right. \\
		&立体视觉法 \left\{\begin{aligned}
				&双目\\
				&多目 \\
			\end{aligned}
			\right. \\
		&RGB-D \\
		\end{aligned} \right. \\
	&SLAM \ \left\{\begin{aligned}
				&前端-视觉里程计 \\
				&后端-非线性优化 \\
				&回环检测 \\
				&建图
			\end{aligned} \right. \\
	&Pose \ Estimation \ \left\{\begin{aligned}
				&坐标系(右手系) \left\{\begin{aligned}
					&目标世界坐标系：可辨识特征点的几何中心(通常选取3或4个)？？？ \\
					&本体世界坐标系：原点为质心(坐标轴根据几何形状确定 / X轴为与地球中心连线的反向，Y轴为运动方向) \\
					&相机坐标系 \\
					&像素坐标系 \\
				\end{aligned} \right. \\
				&初始化 \left\{\begin{aligned}
					&由已有3D模型生成层次视图库(利用3D模型+虚拟摄像机生成 / 实拍) \\
					&图像分割，提取二阶矩->估算质心、方向、面积 \\
					&粒子滤波+贝叶斯框架->完成输入图像与3D模型生成视图的匹配，得到初始位姿 \\
				\end{aligned} \right. \\
				&位姿解算+跟踪 \left\{\begin{aligned}
					&匹配点搜索(多假设) \\
					&减缓误匹配(全局优化 / GNN) \\
					&多特征融合(特征点 + 边缘) \\
				\end{aligned} \right. \\
			\end{aligned} \right. \\
\end{aligned}
\right.
$$

### 参考：
[openMVS](https://github.com/openMVG/openMVG)  
[CMVS-PMVS](https://github.com/pmoulon/CMVS-PMVS)   
[awesome 3D Reconstruction](https://github.com/openMVG/awesome_3DReconstruction_list)

![3D模型生成视图](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/%E7%94%B13D%E7%94%9F%E6%88%90%E8%A7%86%E5%9B%BE.png)






