---
title: windows配置opengl 
date: 2021-03-02
author: zwx
tags: C++
---
## OpenGL
- vs已有，无需自行安装
- 添加opengl32.lib依赖项：属性 -> 配置属性 -> 链接器 -> 输入 -> 附加依赖项

## GLFW
### 下载链接
- [下载链接](https://www.glfw.org/download.html)，选取 *Source package*

### 编译
- 打开VS，cmake生成
- 生成解决方案

### 配置
- 添加include目录：属性 -> 配置属性 -> VC++ 目录 -> 包含目录（**"x:\xx\glfw\include"**）
- 添加glfw3.lib依赖项：属性 -> 配置属性 -> 链接器 -> 输入 -> 附加依赖项（**"x:\xx\glfw\out\build\x64-Debug\src"**）

## GLAD
- 管理OpenGL的函数指针

### 下载链接
- [在线服务](https://glad.dav1d.de/)
- Language: C/C++
- Specification: OpenGL
- API: gl: Version 3.3
- Profile: Core
- 勾选 *Generate a loader*
- 点击 *GENERATE*
- 生成glad.zip压缩文件，下载

### 配置
- 添加include目录：属性 -> 配置属性 -> VC++ 目录 -> 包含目录（**"x:\xx\glad\include"**）
- 将 **src\glad.c** 添加到工程中
















