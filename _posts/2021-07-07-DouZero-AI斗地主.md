---
title: DouZero: AI斗地主
date: 2021-07-07
author: zwx
tags: 论文阅读
---
DouZero:Mastering DouDizhu with Self-Play Deep Reinforcement Learning

## Demo
[DouZero demo](https://douzero.org/)

## background
### reinforcement learning（强化学习）
- **定义**：对于某一任务，如果某一策略可以得到较好的效果，则不断强化该策略
- **状态**：某一策略在某一时刻所能看到的全部信息
- **动作**：某一状态下做出的一个行为
- **算法分类**：Q-Learning、Policy Optimization（策略优化）

## algorithm
### 编码
![DouZero编码方式](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/DouZero-%E7%BC%96%E7%A0%81.png)

- 4x15矩阵（15表示1-K和Joker，每列代表一种牌；4表示每种牌的数量）
- 0/1编码
- 花色？？？

### Deep Monte-Carlo
![DouZero网络](https://raw.githubusercontent.com/huhuzwxy/huhuzwxy.github.io/master/assets/images/douzero-dmc%E7%BD%91%E7%BB%9C.png)

- Input: 状态（过去的出牌用LSTM编码 / 当前信息编码） + 动作（当前出去）
- Output: 输出价值