# pyqt-scaffolding

Quickly build QT program framework.

## 项目说明

本项目为我的老师提供的一个软件设计结构的改进版，个人觉得这样的结构写 pyqt 项目会非常清晰而且代码耦合度非常低，所以在原来的基础上进行了改进。

## 项目结构

``` bash
├── HelloWorldManager.py
├── Main.py
├── README.md
├── script
│   └── pyuic.py
├── ui
│   ├── MainWindow.py
│   └── MainWindow.ui
└── view
    └── MainWindow.py
```

## 结构说明

- Manager:对主要逻辑功能进行封装，类似三层架构里的 Service。
- Main:程序启动入口，里面负责逻辑与视图层的中转。
- script:这是一个脚本文件夹，里面可以编写一些项目工具，例子里的脚本是将 ui 文件夹下的 ui 文件转化成 py 文件。
- ui:ui 文件夹负责存储通过可视化设计工具生成的 .ui 文件并通过 pyuic 将 .ui 转化成 .py 文件，注意，通过软件自动生成的任何东西都不能进行改动。
- view:主要目的是提供用户交互，也就是视图层。
