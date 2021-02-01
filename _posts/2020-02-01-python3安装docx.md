---
title: python3安装docx 
date: 2021-02-01
author: zwx
tags: python
---
## 直接安装docx
`pip3 install python-docx`

- 出现`Successfully installed xxxx`即为安装成功
- 如果出现lxml安装报错，先安装lxml

## 安装lxml
- 直接`pip3 install lxml`
- 如果出现类似`ReadTimeoutError: HTTPSConnectionPool`错误，网站下载
- [lxml下载链接](https://pypi.org/project/lxml/#files)，选取合适版本whl
- `pip3 install xxxxx.whl`
- 出现`Successfully installed xxxxx`即为安装成功

## 通过tar装docx
- [docx下载链接](https://pypi.org/project/python-docx/#files)
- 安装lxml后，`pip3 install python-docx`