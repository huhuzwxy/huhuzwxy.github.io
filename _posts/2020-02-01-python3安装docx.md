---
title: python3安装docx 
date: 2021-02-01
author: zwx
tags: python
---
## 直接安装docx
- 直接`pip3 install python-docx`
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
- 或者：删除python-docx-0.8.10\docx\templates中的default-docx-template文件夹，然后执行`python setup.py install`

## 安装xlrd和xlwt
- 直接`pip3 install xlrd`和`pip3 install xlwt`
- xlrd当前版本只支持xls文件，不支持xlsx文件，如需读取xlsx，安装1.2.0版本，`pip3 install xlrd==1.2.0`
- xlwt单个sheet最大行数是65535，如果有更大需要，建议使用openpyxl函数，最大行数达到1048576，`pip3 install openpyxl`