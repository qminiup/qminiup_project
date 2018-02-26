# -*- coding: utf-8 -*-

# 2017.11.10 ：XDsscom V1.1
#                       1）统一Class initial 参数，均携带实例调用主Class信息，以便各个window间可相互调用其中的成员变量及成员函数
#
# 2017.11.10 ：XDsscom V1.2
#                       1) button/slider功能实现，并实现颜色状态显示
#
# 2017.11.14 ：XDsscom V1.3
#                       1) 自动插拔盘测试，上下电控制逻辑测试ok，磁盘显示和抓取功能还未实现
#
# 2017.11.16 ：XDsscom V1.4
#                       1) 添加全局自动插拔盘测试，全局复位计数，全局选盘（匹配功能受限）
#                       2) 自动拔盘测试功能基本实现，有待进一步测试完善
#
# 2017.11.17 ：XDsscom V1.5
#                       1) 优化串口打开无设备异常，弹出提升对话框
#                       2）优化USB设备无法读取 wwid 异常
#                       3）发布该版本实际应用
#
# 2017.11.17 ：XDsscom V1.6
#                       1) 优化自动拔插盘测试，当对应槽位的盘插入其它槽位时，判定为未上盘（根据槽位电流附加条件判定）
#
# 2017.11.20 ：XDsscom V1.7
#                       1) 根据 scsi id 物理编号 和 slotnum 绑定关系，判断磁盘位置，精准解决 slot定位问题，
#                           局限性：需要核实计算机本地scsi id物料编号是 0:0:0:0,1:0:0:0,2:0:0:0,3:0:0:0,4:0:0:0,5:0:0:0,6:0:0:0
#                           通常 6个物理SATA口的计算机，是按该scsi物料编号固定，SATA线接到STB板，需要按该物料顺序连接
#
# 2017.11.22 ：XDsscom V1.8
#                       1) 优化自动拔插盘测试，当对应槽位的盘要下电前，主动删除系统设备，以便实现盘体信息显示快速更新
#                       2) 增加随机设置滑动条
#
# 2017.11.24 ：XDsscom V1.9
#                       1) 增加 Slot<->SATA S.M.A.R.T 显示页面
#                       2) 优化主动删除系统设备逻辑，确保删除的系统盘符和槽位对应
#
# 2017.11.28 ：XDsscom V2.0
#                       1) 修改系统主动删盘策略，自动掉电前10秒主动offline, 随后1秒主动delete，（若掉电前1秒进行delete，270cycle后，系统固定会卡死）
#
# 2017.12.04 ：XDsscom V2.1
#                       1) 删除主动删盘策略（约270cycle后，系统固定会卡死）
#                       2) 添加"测试硬盘"显示页面，基本实现 TH0.2/TH3/TH10 同屏选择基础读写测试功能
#
# 2017.12.05 ：XDsscom V2.2
#                       1) 添加完成状态判断，使用bar条的颜色来指示本次测试状态
#                       2) 添加TH1测试按键
#
# 2017.12.06 ：XDsscom V2.3
#                       1) 测试结果状态显示功能基本ok
#                       2) 添加TH0，TH5，RO1，VY1 测试功能
#
# 2017.12.07 ：XDsscom V2.4
#                       1) 添加硬盘版本信息
#                       2) 没有在系统中显盘的槽位，自动不参与测试
#
# 2017.12.08 ：XDsscom V2.5
#
# 2017.12.11 ：XDsscom V2.6
#                       1) 修正结果显示bar颜色状态，仅在关键smart信息状态有变化的条件下，才变色
#                       2) 优化“删除硬盘”和“手动刷新”对显示结果的处理
#                       3) 优化“测试按键”的变化状态，确保状态会刷新变化
#                       4) 修改tab页面title信息，修改软件名字为 “STBTestBoard”
#
# 2017.12.13 ：XDsscom V2.7
#                       1) 优化bar颜色显示，确保完成后bar条颜色状态一致
#                       2) 优化STB半LED故障状态显示时机，启动测试就判断smart状态显示LED是否闪烁
#                       3) 优化读写速度显示颜色
#                       4) 优化窗口大小
#
# 2017.12.13 ：XDsscom V2.8
#                       1) 增加加密狗判断，加密狗不再位，或加密狗次数超过10000次，分别报 UA 和 OV 错误
#
# 2017.12.14 ：XDsscom V2.81
#                       1) 修改重复测试，硬盘测试界面SMART信息没清理干净问题
#                       2) 增加加热控制bar，默认100%加热，可手动调整加热比例
#                       3) tab2界面增加每个槽位的单独的删盘和独立刷新按键，方便单独操作
#                       4) tab2界面不再控制LED灯，不再需要串口通讯
#
# 2017.12.15 ：XDsscom V2.82
#                       1) tab3界面增加每个槽位的单独的删盘和独立刷新按键，方便单独操作
#
# 2017.12.15 ：XDsscom V2.83
#                       1) 修改 disk name不完整问题
#                       2) 修改 samrt 信息可能无法显示问题
#
# 2018.01.16 ：XDsscom V2.84
#                       1) 添加tab4(克隆校验)功能页面
#
# 2018.01.17 ：XDsscom V2.85
#                       1) 添加tab5(硬盘测试+)功能页面
#
# 2018.01.18 ：XDsscom V2.86
#                       1) tab4(克隆校验)功能页面添加“开启4.5~5.5V测试”功能，默认关闭
#
# 2018.01.18 ：XDsscom V2.87
#                       1) tab3 和 tab5 功能页面加热功能在使能条件下，将根据是否正在测试而自动起停，以便节能
#
# 2018.01.30 ：XDsscom V2.88
#                       1)  tab4(克隆校验)功能页面，全局“删除硬盘”按键，不删除Slot 1，Slot 1自身的“删除硬盘”才能删除自身硬盘
#
# 2018.01.31 ：XDsscom V2.89
#                       1)  修改linux sdx 读写超时时间，从1s修改为2s，为了兼容 2246xt+L06B 写入WE错误（“Write DMA Ext”命令超时)
#
# 2018.02.01 ：XDsscom V2.90
#                       1)  修改linux sdx 读写超时时间，从1s修改为2s，修改一处没有同步修改的bug
#                       2)  修改自动拔插盘测试ON、OFF时间设置
#
# 2018.02.09 ：XDsscom V2.91
#                       1) 添加tab6(硬盘测试++)功能页面
#                       2) 修改SMART显示之前ID未清除问题
#

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import datetime
import serial
import serial.tools.list_ports
import threading
import random

diskid = {'sda':0, 'sdb':1, 'sdc':2, 'sdd':3, 'sde':4, 'sdf':5, 'sdg':6, 'sfh':7, 'sdi':8 }

sid_to_slotnum = {'0:0:0:0':1, '1:0:0:0':2, '2:0:0:0':3, '3:0:0:0':4, '4:0:0:0':5, '5:0:0:0':6 }

# tab_1 ################################################################################################################

'''
tab "Monitor"
'''
class UartControl(object):
    def __init__(self, parent, widget, position):

        self.serial = parent.serial
        self.serialThread = parent.serialThread
        self.parent = parent

        # do not set the timeout, let the serail.read() block
        self.serial.timeout = 0.3  # make sure that the alive event can be checked from time to time

        self.frame = QtWidgets.QFrame(widget)
        self.frame.setGeometry(position)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("UartControl")

        self.label_UartPort = QtWidgets.QLabel(self.frame)
        self.label_UartPort.setGeometry(QtCore.QRect(10, 7, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_UartPort.setFont(font)
        self.label_UartPort.setObjectName("label_UartPort")
        self.label_UartPort.setText("UART Port:")

        self.comboBox_UartPort = QtWidgets.QComboBox(self.frame)
        self.comboBox_UartPort.setGeometry(QtCore.QRect(85, 5, 231, 20))
        self.comboBox_UartPort.setObjectName("comboBox_UartPort")

        self.pushButton_UartPortFlash = QtWidgets.QPushButton(self.frame)
        self.pushButton_UartPortFlash.setGeometry(QtCore.QRect(320, 3, 80, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_UartPortFlash.setFont(font)
        self.pushButton_UartPortFlash.setObjectName("pushButton_UartPortFlash")
        self.pushButton_UartPortFlash.setText("设备刷新")

        self.pushButton_UartPortOpen = QtWidgets.QPushButton(self.frame)
        self.pushButton_UartPortOpen.setGeometry(QtCore.QRect(402, 3, 80, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_UartPortOpen.setFont(font)
        self.pushButton_UartPortOpen.setObjectName("pushButton_UartPortOpen")
        self.pushButton_UartPortOpen.setText("打开串口")

        self.checkBox_backMonitor = QtWidgets.QCheckBox(self.frame)
        self.checkBox_backMonitor.setGeometry(QtCore.QRect(600, 3, 115, 23))
        self.checkBox_backMonitor.setObjectName("checkBox_backMonitor")
        self.checkBox_backMonitor.setText("背景监测")

        self.checkBox_autoPowerOnOffTestAll = QtWidgets.QCheckBox(self.frame)
        self.checkBox_autoPowerOnOffTestAll.setGeometry(QtCore.QRect(688, 3, 115, 23))
        self.checkBox_autoPowerOnOffTestAll.setObjectName("checkBox_autoPowerOnOffTestAll")
        self.checkBox_autoPowerOnOffTestAll.setText("自动拔插盘测试")

        self.pushButton_resetCountAll = QtWidgets.QPushButton(self.frame)
        self.pushButton_resetCountAll.setGeometry(QtCore.QRect(802, 3, 77, 23))
        self.pushButton_resetCountAll.setObjectName("pushButton_resetCountAll")
        self.pushButton_resetCountAll.setText("复位计数")

        self.pushButton_refreshDiskList = QtWidgets.QPushButton(self.frame)
        self.pushButton_refreshDiskList.setGeometry(QtCore.QRect(881, 3, 77, 23))
        self.pushButton_refreshDiskList.setObjectName("pushButton_refreshDiskList")
        self.pushButton_refreshDiskList.setText("扫描硬盘")

        self.__attach_events()

    def __attach_events(self):
        self.pushButton_UartPortFlash.clicked.connect(self.On_UartPortFlash)
        self.pushButton_UartPortOpen.clicked.connect(self.On_UartPortOpen)
        self.pushButton_resetCountAll.clicked.connect(self.On_ResetCountAll)
        self.pushButton_refreshDiskList.clicked.connect(self.On_RefreshDiskList)
        self.checkBox_autoPowerOnOffTestAll.stateChanged.connect(self.On_AutoPowerOnOffTestAll)

    def On_UartPortOpen(self):
        #print(self.pushButton_UartPortOpen.text())
        #print(self.comboBox_UartPort.currentIndex())
        #print(self.ports[self.comboBox_UartPort.currentIndex()])
        if self.pushButton_UartPortOpen.text() == "打开串口":
            #print(self.ports[self.comboBox_UartPort.currentIndex()])
            try:
                self.serial.port = self.ports[self.comboBox_UartPort.currentIndex()]

                self.serial.baudrate = 115200
                self.serial.bytesize = 8
                #self.serial.stopbits = self.serial.STOPBITS[0]
                self.serial.stopbits = 1
                #self.serial.parity = self.serial.PARITIES[0]
                self.serial.parity = 'N'

                self.serial.open()
                print(self.serial)
                print("serial is opened")

                self.pushButton_UartPortOpen.setText("关闭串口")
                self.serialThread.start()
                self.serialThread.serial_open_flag = 1

                time.sleep(0.01)
                self.serial.flushInput()
                self.serial.write("$S1\n".encode('ascii'))
                time.sleep(0.01)
            except:
                #print("!!!!!!!!!!")
                #QMessageBox.question(self.parent, 'Message', 'You sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                QMessageBox.warning(self.parent, 'Message', '打开串口失败：请选择正确的串口', QMessageBox.Cancel)
                #QMessageBox.critical(self.parent, 'Message', '打开串口失败：请选择正确的串口', QMessageBox.Yes)
                self.On_UartPortFlash()
                pass

        else:
            try:
                self.serialThread.__del__()
                self.serial.close()
            except:
                pass

            self.pushButton_UartPortOpen.setText("打开串口")
            #print("On_CloseCom")
            print("serial is closed")

    def On_UartPortFlash(self):
        #print("in On_ComFresh")
        # fill in ports and select current setting
        preferred_index = 0
        self.comboBox_UartPort.clear()
        self.ports = []
        for n, (portname, desc, hwid) in enumerate(sorted(serial.tools.list_ports.comports())):
            #self.comboBox_UartPort.addItem("{} - {}".format(portname, desc))
            #self.comboBox_UartPort.addItem("{portname} - {desc} - {hwid}".format(portname=portname, desc=desc, hwid=hwid))
            self.comboBox_UartPort.addItem("{portname} - {desc}".format(portname=portname, desc=desc))
            self.ports.append(portname)
            #print(n)
            #print(portname)

        preferred_index = n
        self.comboBox_UartPort.setCurrentIndex(preferred_index)

    def On_ResetCountAll(self):
        #print("in On_ResetCountAll")
        for i in (1, 2, 3, 4, 5, 6):
            self.parent.tab1_frame[i].auto_power_on_count = 0
            self.parent.tab1_frame[i].lineEdit_powerOnCount.setText("0")
            self.parent.tab1_frame[i].auto_disk_on_count = 0
            self.parent.tab1_frame[i].lineEdit_diskOnCount.setText("0")

    def On_RefreshDiskList(self):
        #print("in On_RefreshDiskList")
        if self.checkBox_autoPowerOnOffTestAll.isChecked():
            pass
        else:
            isCk = 0
            for i in (1, 2, 3, 4, 5, 6):
                if self.parent.tab1_frame[i].checkBox_autoPowerOnOffTest.isChecked():
                    isCk = isCk + 1

            if isCk == 0:
                for i in (1, 2, 3, 4, 5, 6):
                    self.parent.tab1_frame[i].comboBox_diskListAutoSelect()
            else:
                #print("Refresh none")
                pass

    def On_AutoPowerOnOffTestAll(self):
        if self.checkBox_autoPowerOnOffTestAll.isChecked():
            self.pushButton_refreshDiskList.setDisabled(True)
            for i in (1, 2, 3, 4, 5, 6):
                self.parent.tab1_frame[i].Checkbox_AutoPowerAutoSelect()
        else:
            self.pushButton_refreshDiskList.setEnabled(True)
            for i in (1, 2, 3, 4, 5, 6):
                self.parent.tab1_frame[i].Checkbox_AutoPowerAutoDeSelect()


class SlotVIW(object):
    def __init__(self, parent, widget, position, slotnum):
        self.mutex = parent.mutex
        self.serial = parent.serial
        self.slotnum = slotnum
        self.parent = parent
        self.scsi_id = "{}:0:0:0".format(slotnum - 1)
        self.sdxx = ""
        self.secSize = 0
        self.slot_V_min = 0
        self.slot_V_now = 0
        self.slot_V_max = 0
        self.slot_I_min = 0
        self.slot_I_now = 0
        self.slot_I_max = 0
        self.slot_W_min = 0
        self.slot_W_now = 0
        self.slot_W_max = 0

        self.slot_V_min_old = 0
        self.slot_V_now_old = 0
        self.slot_V_max_old = 0
        self.slot_I_min_old = 0
        self.slot_I_now_old = 0
        self.slot_I_max_old = 0
        self.slot_W_min_old = 0
        self.slot_W_now_old = 0
        self.slot_W_max_old = 0

        self.auto_power_run_flag = 0
        self.disk_fix_check = 0
        self.disk_fix_SN = 0
        self.catch_disk_flag = 0
        self.catch_disk_timecount = 0
        self.catch_disk_min_time = 0
        self.catch_disk_max_time = 0
        self.catch_disk_now_time = 0

        self.auto_power_on_count = 0
        self.auto_disk_on_count = 0
        self.check_disk_on_flag = 0
        self.check_disk_off_flag = 0
        self.check_disk_validate = 0

        self.frame = QtWidgets.QFrame(widget)
        self.frame.setGeometry(position)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame"+"slotnum")

        self.line_0 = QtWidgets.QFrame(self.frame)
        self.line_0.setGeometry(QtCore.QRect(0, 0, 160, 2))
        self.line_0.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_0.setObjectName("line_0")

        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 4, 40, 60))
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setStyleSheet("color:white;background:gray")
        self.lcdNumber.setProperty("value", slotnum)
        self.lcdNumber.setObjectName("lcdNumber")

        self.label_V = QtWidgets.QLabel(self.frame)
        self.label_V.setGeometry(QtCore.QRect(0, 80, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_V.setFont(font)
        self.label_V.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_V.setAutoFillBackground(False)
        self.label_V.setStyleSheet("color:#0044FF;")
        self.label_V.setAlignment(QtCore.Qt.AlignCenter)
        self.label_V.setObjectName("label_V")
        self.label_V.setText("0.00<0.00V<0.00")
        
        self.label_I = QtWidgets.QLabel(self.frame)
        self.label_I.setGeometry(QtCore.QRect(0, 110, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_I.setFont(font)
        self.label_I.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_I.setAutoFillBackground(False)
        self.label_I.setStyleSheet("color:green;")
        self.label_I.setAlignment(QtCore.Qt.AlignCenter)
        self.label_I.setObjectName("label_I")
        self.label_I.setText("0.00<0.00A<0.00")

        self.label_W = QtWidgets.QLabel(self.frame)
        self.label_W.setGeometry(QtCore.QRect(0, 140, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_W.setFont(font)
        self.label_W.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_W.setAutoFillBackground(False)
        self.label_W.setStyleSheet("color:#446611;")
        self.label_W.setAlignment(QtCore.Qt.AlignCenter)
        self.label_W.setObjectName("label_W")
        self.label_W.setText("0000<0000mW<0000")

        self.pushButton_clear = QtWidgets.QPushButton(self.frame)
        self.pushButton_clear.setGeometry(QtCore.QRect(50, 180, 60, 20))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_clear.setText("retrace")

        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 210, 160, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.verticalSlider_V = QtWidgets.QSlider(self.frame)
        self.verticalSlider_V.setGeometry(QtCore.QRect(30, 240, 22, 100))
        self.verticalSlider_V.setMinimum(3300)
        self.verticalSlider_V.setMaximum(6000)
        self.verticalSlider_V.setProperty("value", 5100)
        self.verticalSlider_V.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_V.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_V.setTickInterval(100)
        self.verticalSlider_V.setSingleStep(10)
        self.verticalSlider_V.setPageStep(10)
        self.verticalSlider_V.setObjectName("verticalSlider_V")
        self.slider_power_now = self.verticalSlider_V.value()
        self.slider_power_old = self.slider_power_now

        self.label_voltValue_max = QtWidgets.QLabel(self.frame)
        self.label_voltValue_max.setGeometry(QtCore.QRect(20, 220, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        self.label_voltValue_max.setFont(font)
        self.label_voltValue_max.setObjectName("label_voltValue_max")
        self.label_voltValue_max.setText("6.00V")

        self.label_voltValue_min = QtWidgets.QLabel(self.frame)
        self.label_voltValue_min.setGeometry(QtCore.QRect(20, 340, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        self.label_voltValue_min.setFont(font)
        self.label_voltValue_min.setObjectName("label_voltValue_min")
        self.label_voltValue_min.setText("3.30V")

        self.label_voltValue = QtWidgets.QLabel(self.frame)
        self.label_voltValue.setGeometry(QtCore.QRect(70, 240, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_voltValue.setFont(font)
        self.label_voltValue.setAutoFillBackground(False)
        self.label_voltValue.setStyleSheet("color:#0044FF;")
        self.label_voltValue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_voltValue.setObjectName("label_voltValue")
        self.label_voltValue.setText("{0:.2f}".format(self.slider_power_now / 1000))

        self.pushButton_PowerOnOff = QtWidgets.QPushButton(self.frame)
        self.pushButton_PowerOnOff.setGeometry(QtCore.QRect(75, 270, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_PowerOnOff.setFont(font)
        self.pushButton_PowerOnOff.setStyleSheet("color:white;background:#666666")
        self.pushButton_PowerOnOff.setObjectName("pushButton_PowerOnOff")
        self.pushButton_PowerOnOff.setText("Power\nOn")

        self.label_scsi_id = QtWidgets.QLabel(self.frame)
        self.label_scsi_id.setGeometry(QtCore.QRect(60, 320, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Arial")
        #font.setBold(True)
        self.label_scsi_id.setFont(font)
        self.label_scsi_id.setAutoFillBackground(False)
        self.label_scsi_id.setStyleSheet("color:red;")
        self.label_scsi_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_scsi_id.setObjectName("label_scsi_id")
        #self.label_scsi_id.setText("{}:0:0:0".format(slotnum - 1))
        self.label_scsi_id.setText("-:-:-:-")

        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 365, 160, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 2, 700))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(159, 0, 2, 700))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.checkBox_autoPowerOnOffTest = QtWidgets.QCheckBox(self.frame)
        self.checkBox_autoPowerOnOffTest.setGeometry(QtCore.QRect(20, 370, 111, 20))
        self.checkBox_autoPowerOnOffTest.setObjectName("checkBox_autoPowerOnOffTest")
        self.checkBox_autoPowerOnOffTest.setText("自动拔插盘测试")

        self.label_OnTime = QtWidgets.QLabel(self.frame)
        self.label_OnTime.setGeometry(QtCore.QRect(20, 395, 30, 20))
        self.label_OnTime.setAlignment(QtCore.Qt.AlignLeft)
        self.label_OnTime.setObjectName("label_OnTime")
        self.label_OnTime.setText("ON:")

        self.horizontalSlider_OnTime = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_OnTime.setGeometry(QtCore.QRect(10, 405, 60, 20))
        self.horizontalSlider_OnTime.setMinimum(1)
        self.horizontalSlider_OnTime.setMaximum(600)
        self.horizontalSlider_OnTime.setProperty("value", 50 + 10*self.slotnum)
        self.horizontalSlider_OnTime.setTickInterval(1)
        self.horizontalSlider_OnTime.setSingleStep(1)
        self.horizontalSlider_OnTime.setPageStep(1)
        self.horizontalSlider_OnTime.setInvertedAppearance(False)
        self.horizontalSlider_OnTime.setInvertedControls(True)
        self.horizontalSlider_OnTime.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_OnTime.setObjectName("horizontalSlider_OnTime")

        self.horizontalSlider_OnTime_Random = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_OnTime_Random.setGeometry(QtCore.QRect(80, 405, 60, 20))
        self.horizontalSlider_OnTime_Random.setMinimum(0)
        self.horizontalSlider_OnTime_Random.setMaximum(600)
        self.horizontalSlider_OnTime_Random.setProperty("value", 30)
        self.horizontalSlider_OnTime_Random.setTickInterval(1)
        self.horizontalSlider_OnTime_Random.setSingleStep(1)
        self.horizontalSlider_OnTime_Random.setPageStep(1)
        self.horizontalSlider_OnTime_Random.setInvertedAppearance(False)
        self.horizontalSlider_OnTime_Random.setInvertedControls(True)
        self.horizontalSlider_OnTime_Random.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_OnTime_Random.setObjectName("horizontalSlider_OnTime_Random")

        self.label_OnTimeValue = QtWidgets.QLabel(self.frame)
        self.label_OnTimeValue.setGeometry(QtCore.QRect(48, 395, 70, 12))
        self.label_OnTimeValue.setAlignment(QtCore.Qt.AlignLeft)
        self.label_OnTimeValue.setObjectName("label_OnTimeValue")
        self.label_OnTimeValue.setText("{}-{}s".format(self.horizontalSlider_OnTime.value(), (self.horizontalSlider_OnTime_Random.value() + self.horizontalSlider_OnTime.value())))

        self.label_OnTimeValue_DownCount = QtWidgets.QLabel(self.frame)
        self.label_OnTimeValue_DownCount.setGeometry(QtCore.QRect(110, 395, 30, 20))
        font = QtGui.QFont()
        #font.setPointSize(12)
        #font.setFamily("Arial")
        font.setBold(True)
        self.label_OnTimeValue_DownCount.setFont(font)
        self.label_OnTimeValue_DownCount.setAlignment(QtCore.Qt.AlignRight)
        self.label_OnTimeValue_DownCount.setStyleSheet("color:red;")
        self.label_OnTimeValue_DownCount.setObjectName("label_OnTimeValue_DownCount")
        self.label_OnTimeValue_DownCount.setText("")

        self.label_OffTime = QtWidgets.QLabel(self.frame)
        self.label_OffTime.setGeometry(QtCore.QRect(20, 430, 30, 20))
        self.label_OffTime.setAlignment(QtCore.Qt.AlignLeft)
        self.label_OffTime.setObjectName("label_OffTime")
        self.label_OffTime.setText("OFF:")

        self.horizontalSlider_OffTime = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_OffTime.setGeometry(QtCore.QRect(10, 440, 60, 20))
        self.horizontalSlider_OffTime.setMinimum(1)
        self.horizontalSlider_OffTime.setMaximum(600)
        self.horizontalSlider_OffTime.setProperty("value", 2)
        self.horizontalSlider_OffTime.setTickInterval(1)
        self.horizontalSlider_OffTime.setSingleStep(1)
        self.horizontalSlider_OffTime.setPageStep(1)
        self.horizontalSlider_OffTime.setInvertedAppearance(False)
        self.horizontalSlider_OffTime.setInvertedControls(True)
        self.horizontalSlider_OffTime.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_OffTime.setObjectName("horizontalSlider_OffTime")

        self.horizontalSlider_OffTime_Random = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_OffTime_Random.setGeometry(QtCore.QRect(80, 440, 60, 20))
        self.horizontalSlider_OffTime_Random.setMinimum(0)
        self.horizontalSlider_OffTime_Random.setMaximum(600)
        self.horizontalSlider_OffTime_Random.setProperty("value", 3)
        self.horizontalSlider_OffTime_Random.setTickInterval(1)
        self.horizontalSlider_OffTime_Random.setSingleStep(1)
        self.horizontalSlider_OffTime_Random.setPageStep(1)
        self.horizontalSlider_OffTime_Random.setInvertedAppearance(False)
        self.horizontalSlider_OffTime_Random.setInvertedControls(True)
        self.horizontalSlider_OffTime_Random.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_OffTime_Random.setObjectName("horizontalSlider_OffTime_Random")

        self.label_OffTimeValue = QtWidgets.QLabel(self.frame)
        self.label_OffTimeValue.setGeometry(QtCore.QRect(48, 430, 70, 12))
        self.label_OffTimeValue.setAlignment(QtCore.Qt.AlignLeft)
        self.label_OffTimeValue.setObjectName("label_OffTimeValue")
        self.label_OffTimeValue.setText("{}-{}s".format(self.horizontalSlider_OffTime.value(), (self.horizontalSlider_OffTime_Random.value() + self.horizontalSlider_OffTime.value())))

        self.label_OffTimeValue_DownCount = QtWidgets.QLabel(self.frame)
        self.label_OffTimeValue_DownCount.setGeometry(QtCore.QRect(110, 430, 30, 20))
        font = QtGui.QFont()
        #font.setPointSize(12)
        #font.setFamily("Arial")
        font.setBold(True)
        self.label_OffTimeValue_DownCount.setFont(font)
        self.label_OffTimeValue_DownCount.setAlignment(QtCore.Qt.AlignRight)
        self.label_OffTimeValue_DownCount.setStyleSheet("color:red;")
        self.label_OffTimeValue_DownCount.setObjectName("label_OffTimeValue_DownCount")
        self.label_OffTimeValue_DownCount.setText("")

        self.label_sn_fix = QtWidgets.QLabel(self.frame)
        self.label_sn_fix.setGeometry(QtCore.QRect(0, 460, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        #font.setFamily("Arial")
        #font.setBold(True)
        self.label_sn_fix.setFont(font)
        self.label_sn_fix.setStyleSheet("color:blue;")
        self.label_sn_fix.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sn_fix.setFont(font)
        self.label_sn_fix.setObjectName("label_sn_fix")
        self.label_sn_fix.setText("")

        self.comboBox_diskList = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial")
        font.setBold(True)
        self.comboBox_diskList.setFont(font)
        self.comboBox_diskList.setGeometry(QtCore.QRect(5, 480, 150, 20))
        self.comboBox_diskList.setObjectName("comboBox_diskList")

        self.lineEdit_sn = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_sn.setGeometry(QtCore.QRect(5, 503, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        #font.setFamily("Arial")
        #font.setBold(True)
        self.lineEdit_sn.setFont(font)
        self.lineEdit_sn.setReadOnly(True)
        self.lineEdit_sn.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sn.setFont(font)
        self.lineEdit_sn.setObjectName("lineEdit_sn")
        self.lineEdit_sn.setText("")

        self.lineEdit_size = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_size.setGeometry(QtCore.QRect(5, 525, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        # font.setFamily("Arial")
        # font.setBold(True)
        self.lineEdit_size.setFont(font)
        self.lineEdit_size.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_size.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_size.setReadOnly(True)
        self.lineEdit_size.setObjectName("lineEdit_size")
        self.lineEdit_size.setText("")

        self.pushButton_updateDiskList = QtWidgets.QPushButton(self.frame)
        self.pushButton_updateDiskList.setGeometry(QtCore.QRect(90, 525, 65, 20))
        self.pushButton_updateDiskList.setObjectName("pushButton_updateDiskList")
        self.pushButton_updateDiskList.setText("Refresh")

        self.label_powerOffCount = QtWidgets.QLabel(self.frame)
        self.label_powerOffCount.setGeometry(QtCore.QRect(5, 550, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        #font.setBold(True)
        self.label_powerOffCount.setFont(font)
        #self.label_powerOffCount.setStyleSheet("color:#123456;")
        self.label_powerOffCount.setObjectName("label_powerOffCount")
        self.label_powerOffCount.setText("上电次数")

        self.lineEdit_powerOnCount = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_powerOnCount.setGeometry(QtCore.QRect(60, 550, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        #font.setBold(True)
        self.lineEdit_powerOnCount.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_powerOnCount.setReadOnly(True)
        self.lineEdit_powerOnCount.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_powerOnCount.setFont(font)
        self.lineEdit_powerOnCount.setObjectName("lineEdit_powerOnCount")
        self.lineEdit_powerOnCount.setText("0")

        self.label_diskOnCount = QtWidgets.QLabel(self.frame)
        self.label_diskOnCount.setGeometry(QtCore.QRect(5, 575, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        #font.setBold(True)
        self.label_diskOnCount.setFont(font)
        # self.label_diskOnCount.setStyleSheet("color:#123456;")
        self.label_diskOnCount.setObjectName("label_diskOnCount")
        self.label_diskOnCount.setText("上盘次数")

        self.lineEdit_diskOnCount = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_diskOnCount.setGeometry(QtCore.QRect(60, 575, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        #font.setBold(True)
        self.lineEdit_diskOnCount.setFont(font)
        self.lineEdit_diskOnCount.setReadOnly(True)
        self.lineEdit_diskOnCount.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_diskOnCount.setFont(font)
        self.lineEdit_diskOnCount.setObjectName("lineEdit_diskOnCount")
        self.lineEdit_diskOnCount.setText("0")

        self.pushButton_resetCount = QtWidgets.QPushButton(self.frame)
        self.pushButton_resetCount.setGeometry(QtCore.QRect(59, 600, 95, 20))
        self.pushButton_resetCount.setObjectName("pushButton_resetCount")
        self.pushButton_resetCount.setText("Reset Count")


        # 创建定时器
        self.timer_autoPowerOn = QtCore.QTimer(self.parent)
        self.timer_autoPowerOff = QtCore.QTimer(self.parent)

        self.__attach_events()

    def __attach_events(self):
        self.pushButton_clear.clicked.connect(self.On_ClearVIW)
        self.pushButton_PowerOnOff.clicked.connect(self.On_PowerOnOff)
        self.verticalSlider_V.valueChanged.connect(self.On_PowerSlider)
        self.horizontalSlider_OnTime.valueChanged.connect(self.On_OnTimeSlider)
        self.horizontalSlider_OnTime_Random.valueChanged.connect(self.On_OnTimeSlider)
        self.horizontalSlider_OffTime.valueChanged.connect(self.On_OffTimeSlider)
        self.horizontalSlider_OffTime_Random.valueChanged.connect(self.On_OffTimeSlider)

        self.timer_autoPowerOn.timeout.connect(self.OnPowerOnTimer)
        self.timer_autoPowerOff.timeout.connect(self.OnPowerOffTimer)

        self.pushButton_updateDiskList.clicked.connect(self.On_DiskFresh)
        #self.comboBox_diskList.currentIndexChanged.connect(self.On_DiskChoise)
        self.checkBox_autoPowerOnOffTest.stateChanged.connect(self.On_Checkbox_AutoPower)

        self.pushButton_resetCount.clicked.connect(self.On_ResetCount)

    def SlotShowToBuffer(self, slotstr):
        try:
            if slotstr:
                slot_split = str(slotstr).split(", ")
                V_min = slot_split[0].split("<[")[0].split(" ")[1].split("V")[0]
                V_now = slot_split[0].split("<[")[1].split("]<")[0].split("V")[0]
                V_max = slot_split[0].split("<[")[1].split("]<")[1].split("V")[0]
                #print("Slot",slotnum, "V:", V_min, V_now, V_max)

                I_min = slot_split[1].split("<[")[0].split("A")[0]
                I_now = slot_split[1].split("<[")[1].split("]<")[0].split("A")[0]
                I_max = slot_split[1].split("<[")[1].split("]<")[1].split("A")[0]
                #print("Slot",slotnum, "I:", I_min, I_now, I_max)

                W_min = slot_split[3].split("<[")[0].split("mW")[0]
                W_now = slot_split[3].split("<[")[1].split("]<")[0].split("mW")[0]
                W_max = slot_split[3].split("<[")[1].split("]<")[1].split("'")[0].split("mW")[0]
                #print("Slot",slotnum, "W:", W_min, W_now, W_max)

                self.slot_V_min = V_min
                self.slot_V_now = V_now
                self.slot_V_max = V_max

                self.slot_I_min = I_min
                self.slot_I_now = I_now
                self.slot_I_max = I_max

                self.slot_W_min = W_min
                self.slot_W_now = W_now
                self.slot_W_max = W_max
        except:
            pass

    def SlotShowOnUpdate(self):
        try:
            if self.slot_V_min != self.slot_V_min_old or self.slot_V_now != self.slot_V_now_old or self.slot_V_max != self.slot_V_max_old:
                self.label_V.setText("{}<{}V<{}".format(self.slot_V_min, self.slot_V_now, self.slot_V_max))
                self.slot_V_min_old = self.slot_V_min
                self.slot_V_now_old = self.slot_V_now
                self.slot_V_max_old = self.slot_V_max

            if self.slot_I_min != self.slot_I_min_old or self.slot_I_now != self.slot_I_now_old or self.slot_I_max != self.slot_I_max_old:
                self.label_I.setText("{}<{}A<{}".format(self.slot_I_min, self.slot_I_now, self.slot_I_max))
                self.slot_I_min_old = self.slot_I_min
                self.slot_I_now_old = self.slot_I_now
                self.slot_I_max_old = self.slot_I_max

            if self.slot_W_min != self.slot_W_min_old or self.slot_W_now != self.slot_W_now_old or self.slot_W_max != self.slot_W_max_old:
                self.label_W.setText("{}<{}mW<{}".format(self.slot_W_min, self.slot_W_now, self.slot_W_max))
                self.slot_W_min_old = self.slot_W_min
                self.slot_W_now_old = self.slot_W_now
                self.slot_W_max_old = self.slot_W_max

            if self.slot_I_now == "0.00":
                self.lcdNumber.setStyleSheet("color:white;background:#DDDDDD")
            else:
                self.lcdNumber.setStyleSheet("color:red;background:#888888")

        except:
            pass

    def On_ClearVIW(self):
        if 1:
            self.slot_V_min_old = self.slot_V_min = self.slot_V_max_old = self.slot_V_max = self.slot_V_now_old = self.slot_V_now
            self.slot_I_min_old = self.slot_I_min = self.slot_I_max_old = self.slot_I_max = self.slot_I_now_old = self.slot_I_now
            self.slot_W_min_old = self.slot_W_min = self.slot_W_max_old = self.slot_W_max = self.slot_W_now_old = self.slot_W_now
            self.label_V.setText("{}<{}V<{}".format(self.slot_V_min, self.slot_V_now, self.slot_V_max))
            self.label_I.setText("{}<{}A<{}".format(self.slot_I_min, self.slot_I_now, self.slot_I_max))
            self.label_W.setText("{}<{}mW<{}".format(self.slot_W_min, self.slot_W_now, self.slot_W_max))

            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.01)
                self.serial.flushInput()
                self.serial.write(("$C" + str(self.slotnum) + "\n").encode('ascii'))
                time.sleep(0.1)
                self.serial.flushInput()
                self.mutex.release()

        else:
            #print("in On_ClearVIW")
            pass

    def On_PowerOnOff(self):
        if 1:
            if self.pushButton_PowerOnOff.text() == "Power\nOn":

                if self.serial.isOpen():
                    self.mutex.acquire()
                    time.sleep(0.01)
                    self.serial.flushInput()
                    self.serial.write(("$p" + str(self.slotnum) + "-0\n").encode('ascii'))
                    time.sleep(0.01)
                    self.serial.flushInput()
                    self.mutex.release()

                self.check_disk_off_flag = 1
                self.pushButton_PowerOnOff.setText("Power\nOff")
                self.pushButton_PowerOnOff.setStyleSheet("color:white;background:#BBBBBB")

            elif self.pushButton_PowerOnOff.text() == "Power\nOff":
                if self.serial.isOpen():
                    self.mutex.acquire()
                    time.sleep(0.01)
                    self.serial.flushInput()
                    self.serial.write(("$p" + str(self.slotnum) + "-1\n").encode('ascii'))
                    time.sleep(0.01)
                    self.serial.flushInput()
                    self.mutex.release()

                self.check_disk_on_flag = 1
                self.pushButton_PowerOnOff.setText("Power\nOn")
                self.pushButton_PowerOnOff.setStyleSheet("color:red;background:#666666")

        else:
            #print("in On_PowerOnOff")
            pass

    def On_PowerSlider(self):
        if 1:
            self.slider_power_now = self.verticalSlider_V.value()
            #self.label_voltValue.setText("{0:.2f}".format(self.slider_power_now / 1000))
            if self.slider_power_now != self.slider_power_old:
                self.slider_power_old = self.slider_power_now

                if self.serial.isOpen():
                    self.mutex.acquire()
                    time.sleep(0.01)
                    self.serial.flushInput()
                    self.serial.write(("$v" + str(self.slotnum) + "-" + str(self.slider_power_now) + "\n").encode('ascii'))
                    time.sleep(0.01)
                    self.serial.flushInput()
                    self.mutex.release()

                self.label_voltValue.setText("{0:.2f}".format(self.slider_power_now / 1000))
        else:
            #print("in On_PowerSlider")
            #print(self.verticalSlider_V.value())
            pass

    def On_OnTimeSlider(self):
        if 1:
            self.label_OnTimeValue.setText("{}-{}s".format(self.horizontalSlider_OnTime.value(), (self.horizontalSlider_OnTime.value() + self.horizontalSlider_OnTime_Random.value())))
            self.label_OnTimeValue_DownCount.setText("")
        else:
            #print("in On_OnTimeSlider")
            #print(self.horizontalSlider_OnTime.value())
            pass

    def On_OffTimeSlider(self):
        if 1:
            self.label_OffTimeValue.setText("{}-{}s".format(self.horizontalSlider_OffTime.value(), (self.horizontalSlider_OffTime_Random.value() + self.horizontalSlider_OffTime.value())))
            self.label_OffTimeValue_DownCount.setText("")
        else:
            #print("in On_OffTimeSlider")
            #print(self.horizontalSlider_OffTime.value())
            pass

    def restoreStatus(self):
        if 1:
            if self.pushButton_PowerOnOff.text() == "Power\nOn":
                if self.serial.isOpen():
                    self.mutex.acquire()
                    time.sleep(0.01)
                    self.serial.flushInput()
                    self.serial.write(("$p" + str(self.slotnum) + "-1\n").encode('ascii'))
                    time.sleep(0.01)
                    self.serial.flushInput()
                    self.mutex.release()
                    self.pushButton_PowerOnOff.setStyleSheet("color:red;background:#888888")
            elif self.pushButton_PowerOnOff.text() == "Power\nOff":
                if self.serial.isOpen():
                    self.mutex.acquire()
                    time.sleep(0.01)
                    self.serial.flushInput()
                    self.serial.write(("$p" + str(self.slotnum) + "-0\n").encode('ascii'))
                    time.sleep(0.01)
                    self.serial.flushInput()
                    self.mutex.release()
                    self.pushButton_PowerOnOff.setStyleSheet("color:white;background:#DDDDDD")

            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.01)
                self.serial.flushInput()
                self.serial.write(("$v" + str(self.slotnum) + "-" + str(self.slider_power_now) + "\n").encode('ascii'))
                time.sleep(0.01)
                self.serial.flushInput()
                self.mutex.release()

    def On_Checkbox_AutoPower(self):
        if self.checkBox_autoPowerOnOffTest.isChecked():
            self.power_on_time = self.horizontalSlider_OnTime.value() + random.randint(0, self.horizontalSlider_OnTime_Random.value())
            self.power_off_time = self.horizontalSlider_OffTime.value() + random.randint(0, self.horizontalSlider_OffTime_Random.value())
            self.label_OffTimeValue_DownCount.setText("")
            self.label_OnTimeValue_DownCount.setText("{}".format(self.power_on_time))
            self.label_sn_fix.setText("[{}]".format(self.lineEdit_sn.text()))

            self.timer_autoPowerOn.start(1000)

            self.horizontalSlider_OnTime.setDisabled(True)
            self.horizontalSlider_OffTime.setDisabled(True)
            self.pushButton_PowerOnOff.setDisabled(True)

        else:
            self.timer_autoPowerOn.stop()
            self.timer_autoPowerOff.stop()

            self.label_sn_fix.setText("")
            self.horizontalSlider_OnTime.setEnabled(True)
            self.horizontalSlider_OffTime.setEnabled(True)
            self.pushButton_PowerOnOff.setEnabled(True)

    def OnPowerOnTimer(self):
        if self.power_on_time:
            self.power_on_time = self.power_on_time - 1
            self.label_OnTimeValue_DownCount.setText("{}".format(self.power_on_time))
            self.checkDiskStatus()
            #try:
            #    self.check_disk_validate = 1
            #    self.checkDiskStatus()
            #    if self.sdxx != "":
            #        if self.power_on_time == 10:
            #            os.system("echo offline > /sys/block/{}/device/state".format(self.sdxx))
            #        if self.power_on_time == 9:
            #            os.system("echo 1 > /sys/block/{}/device/delete".format(self.sdxx))
            #except:
            #    pass
        else:
            self.label_OnTimeValue_DownCount.setText("")
            self.power_on_time = self.horizontalSlider_OnTime.value() + random.randint(0, self.horizontalSlider_OnTime_Random.value())

            if self.serial.isOpen():
                #try:
                #    self.check_disk_validate = 1
                #    self.checkDiskStatus()
                #    if self.sdxx != "":
                #        #print("slot-{} {}".format(self.slotnum, self.sdx))
                #        #os.system("echo offline > /sys/block/{}/device/state &".format(self.sdxx))
                #        os.system("echo 1 > /sys/block/{}/device/delete".format(self.sdxx))
                #except:
                #    pass
                
                self.mutex.acquire()
                time.sleep(0.01)
                self.serial.flushInput()
                self.serial.write(("$p" + str(self.slotnum) + "-0\n").encode('ascii'))
                time.sleep(0.01)
                self.serial.flushInput()
                self.mutex.release()

                self.check_disk_off_flag = 1
                self.pushButton_PowerOnOff.setText("Power\nOff")
                self.pushButton_PowerOnOff.setStyleSheet("color:white;background:#BBBBBB")

            self.timer_autoPowerOn.stop()
            self.timer_autoPowerOff.start(1000)
            self.label_OffTimeValue_DownCount.setText("{}".format(self.power_off_time))

        #print("in OnPowerOnTimer {}".format(self.slotnum))

    def OnPowerOffTimer(self):
        if self.power_off_time:
            self.power_off_time = self.power_off_time - 1
            self.label_OffTimeValue_DownCount.setText("{}".format(self.power_off_time))
            self.checkDiskStatus()
        else:
            self.label_OffTimeValue_DownCount.setText("")
            self.power_off_time = self.horizontalSlider_OffTime.value() + random.randint(0, self.horizontalSlider_OffTime_Random.value())

            self.auto_power_on_count = self.auto_power_on_count + 1
            self.lineEdit_powerOnCount.setText("{}".format(self.auto_power_on_count))

            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.01)
                self.serial.flushInput()
                self.serial.write(("$p" + str(self.slotnum) + "-1\n").encode('ascii'))
                time.sleep(0.01)
                self.serial.flushInput()
                self.mutex.release()

                self.check_disk_on_flag = 1
                self.pushButton_PowerOnOff.setText("Power\nOn")
                self.pushButton_PowerOnOff.setStyleSheet("color:red;background:#666666")

            self.timer_autoPowerOff.stop()
            self.timer_autoPowerOn.start(1000)
            self.label_OnTimeValue_DownCount.setText("{}".format(self.power_on_time))

        #print("in OnPowerOffTimer {}".format(self.slotnum))

    def get_disk_info(self):
        #print("in get_disk_info {}".format(self.slotnum))

        """
        获取物理磁盘信息。
        """
        tmplist = []

        f = os.popen('ls /sys/block')
        dl = f.readlines()
        for dev in dl:
            dlsdx = []
            iloop = dev[0:4]
            if iloop != 'loop':
                xsdx = dev.replace('\n', '')
                with open("/sys/block/{}/device/wwid".format(xsdx), 'r') as sno:
                    try:
                        line = sno.readline()
                        ata = line[4:7]
                        if ata == "ATA":
                            sn = line[-22:-1].replace('\n', '').strip()

                            dlsdx.append(xsdx)
                            dlsdx.append(sn)

                            with open("/sys/block/{}/size".format(xsdx), 'r') as ss:
                                size = ss.readline().replace('\n', '').strip()
                                secSize = int(size)
                                size = int(size) * 512 / 1000 / 1000 / 1000
                                size = "{0:.1f}GB".format(size)
                                dlsdx.append(size)

                            with open("/sys/block/{}/device/model".format(xsdx), 'r') as nn:
                                name = nn.readline().replace('\n', '').strip()
                                dlsdx.append(name)

                            f = os.popen("ls /sys/block/{}/device/scsi_device".format(xsdx))
                            scsi_id = f.readline().replace('\n', '').strip()
                            dlsdx.append(scsi_id)
                            dlsdx.append(secSize)

                            tmplist.append(dlsdx)
                    except:
                        pass


        # pad a null device
        dlsdx = []
        dlsdx.append("---")
        dlsdx.append("---")
        dlsdx.append("---")
        dlsdx.append("-")
        dlsdx.append("")
        dlsdx.append("")
        tmplist.append(dlsdx)

        return tmplist

    def checkDiskStatus(self):
        try:
            self.disklist = self.get_disk_info()
            if self.check_disk_on_flag:
                for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                    # if scsiid == "{}:0:0:0".format(self.slotnum - 1):
                    if scsiid == self.scsi_id:
                        if "[{}]".format(sn) == self.label_sn_fix.text():
                            self.check_disk_on_flag = 0
                            self.auto_disk_on_count = self.auto_disk_on_count + 1
                            self.lineEdit_diskOnCount.setText("{}".format(self.auto_disk_on_count))

                            self.lineEdit_sn.setText(sn)
                            self.lineEdit_size.setText(size_GB)
                            self.label_scsi_id.setText("{}={}".format(scsiid, sdxx))
                            try:
                                os.system("echo 2 > /sys/block/{}/device/eh_timeout".format(sdxx))
                                os.system("echo 2 > /sys/block/{}/device/timeout".format(sdxx))
                                os.system("echo 1 > /sys/block/{}/device/queue_depth".format(sdxx))
                            except:
                                pass

                            self.comboBox_diskList.clear()
                            for (sdxx, sn, size_GB, deviceName, scsiid) in self.disklist:
                                self.comboBox_diskList.addItem("{}-{size}-{name}".format(sdxx, size=size_GB, name=deviceName))

                            self.comboBox_diskList.setCurrentIndex(n)

                            break

                if n == (len(self.disklist) - 1):
                    self.comboBox_diskList.clear()
                    self.comboBox_diskList.setCurrentIndex(0)
                    self.lineEdit_sn.setText("")
                    self.lineEdit_size.setText("")

            if self.check_disk_off_flag:
                d = 0
                for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                    # if scsiid == "{}:0:0:0".format(self.slotnum - 1):
                    d = n
                    if scsiid == self.scsi_id:
                        break

                if d == (len(self.disklist) - 1):
                    self.check_disk_off_flag = 0
                    self.comboBox_diskList.clear()
                    self.comboBox_diskList.setCurrentIndex(0)
                    self.lineEdit_sn.setText("")
                    self.lineEdit_size.setText("")

            if self.check_disk_validate:
                self.sdxx = ""
                for (sdxx, sn, size_GB, deviceName, scsiid, secSize) in self.disklist:
                    if scsiid == self.scsi_id:
                        if "[{}]".format(sn) == self.label_sn_fix.text():
                            self.sdxx = sdxx
                            self.secSize = secSize
                self.check_disk_validate = 0
        except:
            pass

    def On_DiskFresh(self):
        #print("in On_DiskFresh {}".format(self.slotnum))
        self.comboBox_diskListAutoSelect()

    def comboBox_diskListAutoSelect(self):
        try:
            self.comboBox_diskList.clear()
            self.disklist = self.get_disk_info()
            for (sdx, sn, size_GB, deviceName, scsiid, secSize) in self.disklist:
                self.comboBox_diskList.addItem("{}-{size}-{name}".format(sdx, size=size_GB, name=deviceName))

            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                #if scsiid == "{}:0:0:0".format(self.slotnum - 1):
                if scsiid == self.scsi_id:
                    self.comboBox_diskList.setCurrentIndex(n)
                    self.lineEdit_sn.setText(sn)
                    self.lineEdit_size.setText(size_GB)
                    self.label_scsi_id.setText("{}={}".format(scsiid, sdxx))
                    try:
                        os.system("echo 2 > /sys/block/{}/device/eh_timeout".format(sdxx))
                        os.system("echo 2 > /sys/block/{}/device/timeout".format(sdxx))
                        os.system("echo 1 > /sys/block/{}/device/queue_depth".format(sdxx))
                    except:
                        pass
                    
                    break

            if n == (len(self.disklist) - 1):
                self.sdxx = ""
                self.comboBox_diskList.setCurrentIndex(n)
                self.lineEdit_sn.setText("")
                self.lineEdit_size.setText("")
        except:
            pass

    def Checkbox_AutoPowerAutoSelect(self):
        if len(self.lineEdit_sn.text()) != 0:
            self.checkBox_autoPowerOnOffTest.setChecked(True)

    def Checkbox_AutoPowerAutoDeSelect(self):
        if self.checkBox_autoPowerOnOffTest.isChecked():
            self.checkBox_autoPowerOnOffTest.setChecked(False)

    '''
    def On_DiskChoise(self):
        #print("in On_DiskChoise {}".format(self.slotnum))
        if len(self.disklist) > 1:
            id = self.comboBox_diskList.currentIndex()
            self.lineEdit_sn.setText(self.disklist[id][1])
            self.lineEdit_size.setText(self.disklist[id][2])
        else:
            self.lineEdit_sn.setText("")
            self.lineEdit_size.setText("")
    '''

    def On_ResetCount(self):
        self.check_disk_on_flag = 0
        self.auto_power_on_count = 0
        self.auto_disk_on_count = 0
        self.lineEdit_powerOnCount.setText("{}".format(self.auto_power_on_count))
        self.lineEdit_diskOnCount.setText("{}".format(self.auto_disk_on_count))

        #print("in On_ResetCount {}".format(self.slotnum))

# tab_2 ################################################################################################################
'''
tab "S.M.A.R.T"
'''
def get_disk_info():
    # print("in get_disk_info {}".format(self.slotnum))

    """
    获取物理磁盘信息。
    """
    tmplist = []

    f = os.popen('ls /sys/block')
    dl = f.readlines()
    for dev in dl:
        dlsdx = []
        iloop = dev[0:4]
        if iloop != 'loop':
            xsdx = dev.replace('\n', '')
            with open("/sys/block/{}/device/wwid".format(xsdx), 'r') as sno:
                try:
                    line = sno.readline()
                    ata = line[4:7]
                    if ata == "ATA":
                        sn = line[-22:-1].replace('\n', '').strip()

                        dlsdx.append(xsdx)
                        dlsdx.append(sn)

                        with open("/sys/block/{}/size".format(xsdx), 'r') as ss:
                            size = ss.readline().replace('\n', '').strip()
                            secSize = int(size)
                            size = int(size) * 512 / 1000 / 1000 / 1000
                            size = "{0:.1f}GB".format(size)
                            dlsdx.append(size)

                        with open("/sys/block/{}/device/model".format(xsdx), 'r') as nn:
                            name = nn.readline().replace('\n', '').strip()
                            dlsdx.append(name)

                        f = os.popen("ls /sys/block/{}/device/scsi_device".format(xsdx))
                        scsi_id = f.readline().replace('\n', '').strip()
                        dlsdx.append(scsi_id)
                        dlsdx.append(secSize)

                        tmplist.append(dlsdx)
                except:
                    pass

    # pad a null device
    dlsdx = []
    dlsdx.append("---")
    dlsdx.append("---")
    dlsdx.append("---")
    dlsdx.append("-")
    dlsdx.append("")
    dlsdx.append("")
    tmplist.append(dlsdx)

    return tmplist


class ShowSlotScsiID_Header(object):
    def __init__(self, parent, widget, position):

        self.parent = parent

        self.frame = QtWidgets.QFrame(widget)
        self.frame.setGeometry(position)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("HeadControl")

        self.checkBox_autoUpdate = QtWidgets.QCheckBox(self.frame)
        self.checkBox_autoUpdate.setGeometry(QtCore.QRect(688, 3, 115, 23))
        self.checkBox_autoUpdate.setObjectName("checkBox_autoUpdate")
        self.checkBox_autoUpdate.setText("自动刷新")

        self.pushButton_deleteDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_deleteDisk.setGeometry(QtCore.QRect(802, 3, 77, 23))
        self.pushButton_deleteDisk.setObjectName("pushButton_deleteDisk")
        self.pushButton_deleteDisk.setText("删除硬盘")

        self.pushButton_manualUpdate = QtWidgets.QPushButton(self.frame)
        self.pushButton_manualUpdate.setGeometry(QtCore.QRect(881, 3, 77, 23))
        self.pushButton_manualUpdate.setObjectName("pushButton_manualUpdate")
        self.pushButton_manualUpdate.setText("手动刷新")

        # 创建定时器
        self.timer_autoUpdate = QtCore.QTimer(self.parent)

        self.__attach_events()

    def __attach_events(self):
        self.pushButton_manualUpdate.clicked.connect(self.On_manualUpdate)
        self.pushButton_deleteDisk.clicked.connect(self.On_deleteDisk)
        self.checkBox_autoUpdate.stateChanged.connect(self.On_autoUpdate)
        self.timer_autoUpdate.timeout.connect(self.OnAutoUpdateTimer)

    def On_manualUpdate(self):
        #print("in On_manualUpdate")
        for i in (1, 2, 3, 4, 5, 6):
            self.parent.tab2_frame[i].SlotIDtoScsiID()

    def On_deleteDisk(self):
        #print("in On_deleteDisk")
        for i in (1, 2, 3, 4, 5, 6):
            self.parent.tab2_frame[i].SlotDeleteDisk()

    def On_autoUpdate(self):
        #print("in On_autoUpdate")
        if self.checkBox_autoUpdate.isChecked():
            self.pushButton_manualUpdate.setDisabled(True)
            self.timer_autoUpdate.start(500)

        else:
            self.pushButton_manualUpdate.setEnabled(True)
            self.timer_autoUpdate.stop()

    def OnAutoUpdateTimer(self):
        #print("in OnAutoUpdateTimer")
        self.On_manualUpdate()
        self.timer_autoUpdate.start(500)


class ShowSlotScsiID(object):
    def __init__(self, parent, widget, position, slotnum):
        self.slotnum = slotnum
        self.parent = parent
        self.scsi_id = "{}:0:0:0".format(slotnum - 1)
        self.sdxx = ""
        self.secSize = 0
        self.frame = QtWidgets.QFrame(widget)
        self.frame.setGeometry(position)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame" + "slotnum")

        self.line_0 = QtWidgets.QFrame(self.frame)
        self.line_0.setGeometry(QtCore.QRect(0, 0, 160, 2))
        self.line_0.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_0.setObjectName("line_0")

        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 2, 700))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(159, 0, 2, 700))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 4, 40, 60))
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setStyleSheet("color:white;background:gray")
        self.lcdNumber.setProperty("value", slotnum)
        self.lcdNumber.setObjectName("lcdNumber")

        self.label_scsi_id = QtWidgets.QLabel(self.frame)
        self.label_scsi_id.setGeometry(QtCore.QRect(40, 70, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_scsi_id.setFont(font)
        self.label_scsi_id.setAutoFillBackground(False)
        self.label_scsi_id.setStyleSheet("color:#00C78C;")
        self.label_scsi_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_scsi_id.setObjectName("label_scsi_id")
        self.label_scsi_id.setText("-:-:-:-")

        self.label_sdx = QtWidgets.QLabel(self.frame)
        self.label_sdx.setGeometry(QtCore.QRect(40, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_sdx.setFont(font)
        self.label_sdx.setAutoFillBackground(False)
        self.label_sdx.setStyleSheet("color:blue;")
        self.label_sdx.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sdx.setObjectName("label_sdx")
        self.label_sdx.setText("")

        self.label_fwVersion = QtWidgets.QLabel(self.frame)
        self.label_fwVersion.setGeometry(QtCore.QRect(5, 115, 150, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        # font.setFamily("Arial")
        # font.setBold(True)
        self.label_fwVersion.setFont(font)
        self.label_fwVersion.setStyleSheet("color:black;")
        self.label_fwVersion.setAlignment(QtCore.Qt.AlignLeft)
        self.label_fwVersion.setFont(font)
        self.label_fwVersion.setObjectName("label_fwVersion")
        self.label_fwVersion.setText("FW Version:")

        self.label_fwVersionValue = QtWidgets.QLabel(self.frame)
        self.label_fwVersionValue.setGeometry(QtCore.QRect(5, 130, 150, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        # font.setFamily("Arial")
        font.setBold(True)
        self.label_fwVersionValue.setFont(font)
        self.label_fwVersionValue.setStyleSheet("color:blue;")
        self.label_fwVersionValue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fwVersionValue.setFont(font)
        self.label_fwVersionValue.setObjectName("label_fwVersionValue")
        #self.label_fwVersionValue.setText("{}".format("Q0525A"))
        self.label_fwVersionValue.setText("")

        self.label_diskname = QtWidgets.QLabel(self.frame)
        self.label_diskname.setGeometry(QtCore.QRect(5, 145, 150, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        #font.setBold(True)
        self.label_diskname.setFont(font)
        self.label_diskname.setStyleSheet("color:black;")
        self.label_diskname.setAlignment(QtCore.Qt.AlignLeft)
        self.label_diskname.setFont(font)
        self.label_diskname.setObjectName("label_diskname")
        self.label_diskname.setText("Model Name:")

        self.label_disknameValue = QtWidgets.QLabel(self.frame)
        self.label_disknameValue.setGeometry(QtCore.QRect(5, 159, 150, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        font.setBold(True)
        self.label_disknameValue.setFont(font)
        self.label_disknameValue.setStyleSheet("color:blue;")
        self.label_disknameValue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disknameValue.setFont(font)
        self.label_disknameValue.setObjectName("label_disknameValue")
        #self.label_disknameValue.setText("FASPEED K6-120G")
        self.label_disknameValue.setText("")

        self.label_sn = QtWidgets.QLabel(self.frame)
        self.label_sn.setGeometry(QtCore.QRect(5, 175, 155, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        #font.setBold(True)
        self.label_sn.setFont(font)
        self.label_sn.setStyleSheet("color:black;")
        self.label_sn.setAlignment(QtCore.Qt.AlignLeft)
        self.label_sn.setFont(font)
        self.label_sn.setObjectName("label_sn")
        self.label_sn.setText("Model SNo.:")

        self.label_snValue = QtWidgets.QLabel(self.frame)
        self.label_snValue.setGeometry(QtCore.QRect(2, 190, 156, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_snValue.setFont(font)
        self.label_snValue.setStyleSheet("color:blue;")
        self.label_snValue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_snValue.setFont(font)
        self.label_snValue.setObjectName("label_snValue")
        #self.label_snValue.setText("12345678900987654321")
        self.label_snValue.setText("")

        self.label_size = QtWidgets.QLabel(self.frame)
        self.label_size.setGeometry(QtCore.QRect(5, 208, 75, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        #font.setBold(True)
        self.label_size.setFont(font)
        self.label_size.setStyleSheet("color:black;")
        self.label_size.setAlignment(QtCore.Qt.AlignLeft)
        self.label_size.setFont(font)
        self.label_size.setObjectName("label_size")
        self.label_size.setText("Model Size:")

        self.label_sizeValue = QtWidgets.QLabel(self.frame)
        self.label_sizeValue.setGeometry(QtCore.QRect(80, 208, 78, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        font.setBold(True)
        self.label_sizeValue.setFont(font)
        self.label_sizeValue.setStyleSheet("color:blue;")
        self.label_sizeValue.setAlignment(QtCore.Qt.AlignLeft)
        self.label_sizeValue.setFont(font)
        self.label_sizeValue.setObjectName("label_sizeValue")
        #self.label_sizeValue.setText("{}GB".format("120"))
        self.label_sizeValue.setText("")

        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(0, 225, 160, 2))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        #font.setBold(True)
        self.pushButton_DeleteDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_DeleteDisk.setFont(font)
        self.pushButton_DeleteDisk.setGeometry(QtCore.QRect(4, 227, 75, 22))
        self.pushButton_DeleteDisk.setObjectName("pushButton_DeleteDisk")
        self.pushButton_DeleteDisk.setText("删除硬盘")

        self.pushButton_ReflashDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_ReflashDisk.setFont(font)
        self.pushButton_ReflashDisk.setGeometry(QtCore.QRect(81, 227, 75, 22))
        self.pushButton_ReflashDisk.setObjectName("pushButton_ReflashDisk")
        self.pushButton_ReflashDisk.setText("手动刷新")

        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 250, 160, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.label_snValueOld = QtWidgets.QLabel(self.frame)
        self.label_snValueOld.setGeometry(QtCore.QRect(0, 250, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_snValueOld.setFont(font)
        self.label_snValueOld.setStyleSheet("color:gray;")
        self.label_snValueOld.setAlignment(QtCore.Qt.AlignCenter)
        self.label_snValueOld.setFont(font)
        self.label_snValueOld.setObjectName("label_snValueOld")
        self.label_snValueOld.setText("[]")
        self.snold = ""

        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(0, 270, 160, 2))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.label_smartName = [0 for x in range(0, 20)]
        self.label_smartValue = [0 for x in range(0, 20)]
        for i in range(0,17):
            self.label_smartName[i] = QtWidgets.QLabel(self.frame)
            self.label_smartName[i].setGeometry(QtCore.QRect(5, 275 + i*20, 80, 16))
            font = QtGui.QFont()
            font.setPointSize(10)
            #font.setFamily("Arial")
            font.setFamily("Mono")
            #font.setBold(True)
            self.label_smartName[i].setFont(font)
            self.label_smartName[i].setStyleSheet("color:black;")
            self.label_smartName[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_smartName[i].setFont(font)
            self.label_smartName[i].setObjectName("label_smartName{}".format(i))
            self.label_smartName[i].setText("")
            #self.label_smartName[i].setText("{:02X}:".format(i))

            self.label_smartValue[i] = QtWidgets.QLabel(self.frame)
            self.label_smartValue[i].setGeometry(QtCore.QRect(88, 276 + i*20, 67, 16))
            font = QtGui.QFont()
            font.setPointSize(10)
            # font.setFamily("Arial")
            font.setFamily("Mono")
            font.setBold(True)
            self.label_smartValue[i].setFont(font)
            self.label_smartValue[i].setStyleSheet("color:blue;")
            self.label_smartValue[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_smartValue[i].setFont(font)
            self.label_smartValue[i].setObjectName("label_smartValue{}".format(i))
            self.label_smartValue[i].setText("")
            #self.label_smartValue[i].setText("{:02X}:".format(i))

        self.__attach_events()

    def __attach_events(self):
        self.pushButton_DeleteDisk.clicked.connect(self.On_DeleteDisk)
        self.pushButton_ReflashDisk.clicked.connect(self.On_ReflashDisk)


    def On_DeleteDisk(self):
        self.SlotDeleteDisk()

    def On_ReflashDisk(self):
        for i in range(0, 17):
            self.label_smartName[i].setText("")
            self.label_smartValue[i].setText("")
            self.label_smartValue[i].setStyleSheet("color:blue;")

        self.SlotIDtoScsiID()

    def GetSmartInfo(self, sdxx):
        ID01_raw_read_error_rate       = 1
        ID05_reallocated_sectors_count = 5
        ID09_power_on_hours            = 9
        ID0C_power_cycle_count         = 12
        IDA3_original_bad_count        = 163
        IDA7_average_erase_count       = 167
        IDC2_temperature               = 194
        IDC3_read_retry                = 195
        IDC4_reallocation_event_count  = 196
        IDC7_ultraDMA_CRC_error_count  = 199
        IDF1_total_host_written        = 241
        IDF2_total_host_read           = 242

        small = []
        sml = []

        try:
            f = os.popen("smartctl -i /dev/{} | grep 'Firmware'".format(sdxx))
            sm = f.readlines()
            ver = sm[0].replace('Firmware Version:', '').replace('\n', '').strip()
            self.label_fwVersionValue.setText(ver)

            f = os.popen("smartctl -i /dev/{} | grep 'Device Model:'".format(sdxx))
            sm = f.readlines()
            name = sm[0].replace('Device Model:', '').replace('\n', '').strip()
            self.label_disknameValue.setText(name)

            f = os.popen("smartctl -s on -A /dev/{} | grep 0x0".format(sdxx))
            sm =  f.readlines()
            for i in sm:
                smll = []
                sml = i.replace('\n', '').strip()
                sm_1space = sml.replace('   ', ' ').replace('   ', ' ').replace('  ', ' ').replace('  ', ' ')
                smlist = sm_1space.split(' ')

                smll.append(smlist[0])
                smll.append(smlist[1])
                smll.append(smlist[9])

                small.append(smll)

            n = 0
            sncolor = "green"
            for (id, name, value) in small:
                if int(id) == ID01_raw_read_error_rate:
                    self.label_smartName[n].setText("{:02X}:读错误率".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    if int(value) != 0:
                        self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                        sncolor = "red"
                    else:
                        self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

                elif int(id) == ID05_reallocated_sectors_count:
                    self.label_smartName[n].setText("{:02X}:新增坏块".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    if int(value) != 0:
                        self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                        sncolor = "red"
                    else:
                        self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

                elif int(id) == ID09_power_on_hours:
                    self.label_smartName[n].setText("{:02X}:上电时间".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

                elif int(id) == ID0C_power_cycle_count:
                    self.label_smartName[n].setText("{:02X}:上电次数".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

                elif int(id) == IDA3_original_bad_count:
                    self.label_smartName[n].setText("{:02X}:原始坏块".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

                elif int(id) == IDA7_average_erase_count:
                    self.label_smartName[n].setText("{:02X}:平均磨损".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

                elif int(id) == IDC2_temperature:
                    self.label_smartName[n].setText("{:02X}:主控温度".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    if int(value) > 40:
                        self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                        if sncolor != "red":
                            sncolor = "orange"
                    else:
                        self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

                elif int(id) == IDC3_read_retry:
                    self.label_smartName[n].setText("{:02X}:重读次数".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    if int(value) != 0:
                        self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                        if sncolor != "red":
                            sncolor = "orange"
                    else:
                        self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

                elif int(id) == IDC4_reallocation_event_count:
                    self.label_smartName[n].setText("{:02X}:读取失败".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    if int(value) != 0:
                        self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                        sncolor = "red"
                    else:
                        self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

                elif int(id) == IDC7_ultraDMA_CRC_error_count:
                    self.label_smartName[n].setText("{:02X}:链路重传".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    if int(value) != 0:
                        self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                        if sncolor != "red":
                            sncolor = "orange"
                    else:
                        self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

                elif int(id) == IDF1_total_host_written:
                    self.label_smartName[n].setText("{:02X}:主机写入".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

                elif int(id) == IDF2_total_host_read:
                    self.label_smartName[n].setText("{:02X}:主机读取".format(int(id)))
                    self.label_smartValue[n].setText("{}".format(value))
                    self.label_smartValue[n].setStyleSheet("color:blue;")
                    n = n + 1

            if sncolor == "red":
                self.label_snValueOld.setStyleSheet("color:white;""background:red;")
            elif sncolor == "orange":
                self.label_snValueOld.setStyleSheet("color:white;""background:orange;")
            elif sncolor == "green":
                self.label_snValueOld.setStyleSheet("color:white;""background:green;")

        except:
            pass

    def SlotIDtoScsiID(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                # print("[{}] {} {} {} {} {}".format(self.slotnum, scsiid, sdxx, size_GB, deviceName, sn))
                if self.scsi_id == scsiid:
                    self.label_scsi_id.setText("{}".format(scsiid))
                    self.label_sdx.setText("{}".format(sdxx))
                    #self.label_disknameValue.setText(deviceName)
                    self.label_snValue.setText(sn)
                    self.label_snValueOld.setText("[{}]".format(sn))
                    self.label_sizeValue.setText(size_GB)
                    try:
                        os.system("echo 2 > /sys/block/{}/device/eh_timeout".format(sdxx))
                        os.system("echo 2 > /sys/block/{}/device/timeout".format(sdxx))
                        os.system("echo 1 > /sys/block/{}/device/queue_depth".format(sdxx))
                    except:
                        pass

                    self.lcdNumber.setStyleSheet("color:red;background:#888888")
                    self.GetSmartInfo(sdxx)
                    self.sdxx = sdxx
                    self.secSize = secSize

                    # 不控制LED
                    #shownum = sid_to_slotnum[self.scsi_id]
                    #self.pp.STB_LED_Show(shownum, shownum)

                    break

            if n == (len(self.disklist) - 1):
                self.lcdNumber.setStyleSheet("color:white;background:#DDDDDD")
                self.label_scsi_id.setText("-:-:-:-")
                self.label_sdx.setText("")
                self.label_fwVersionValue.setText("")
                self.label_disknameValue.setText("")
                self.label_snValue.setText("")
                self.label_sizeValue.setText("")
                for i in range(0, 17):
                    self.label_smartName[i].setText("")
                    self.label_smartValue[i].setText("")
                    self.label_smartValue[i].setStyleSheet("color:blue;")

                # 不控制LED
                #shownum = sid_to_slotnum[self.scsi_id]
                #self.pp.STB_LED_Show(shownum, 20)
        except:
            pass

    def SlotDeleteDisk(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                if self.scsi_id == scsiid:
                    os.system("echo 1 > /sys/block/{}/device/delete".format(sdxx))
        except:
            pass


class MonitorVIW_Thread(QtCore.QThread):

    def __init__(self, parent):
        self.sin = parent.sinUpdateVIW
        self.mutex = parent.mutex
        super(MonitorVIW_Thread, self).__init__()
        self.serial = parent.serial
        self.working = True
        self.pp = parent
        self.serial_open_flag = 0
        self.volt_now = 5100
        self.kKcount = 0
        self.heating_flag = 0
        self.heating_clore = ""

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        try:
            self.working = True
            time.sleep(0.01)
            self.serial.flushInput()
            self.serial.write("$S1\n".encode('ascii'))
            time.sleep(0.01)
            self.serial.write("$d11\n".encode('ascii'))
            time.sleep(0.01)
            self.serial.write("$d22\n".encode('ascii'))
            time.sleep(0.01)
            self.serial.write("$d33\n".encode('ascii'))
            time.sleep(0.01)
            self.serial.write("$d44\n".encode('ascii'))
            time.sleep(0.01)
            self.serial.write("$d55\n".encode('ascii'))
            time.sleep(0.01)
            self.serial.write("$d66\n".encode('ascii'))
            time.sleep(0.01)
            self.serial.write("$v\n".encode('ascii'))
            time.sleep(0.01)
            # 设置max,min = now
            self.serial.write(("$C0\n").encode('ascii'))
            self.lock.release()
        except:
            pass

        # if self.setupUI.tab1_frame[0].serial.isOpen():
        while self.working == True:
            if self.serial.isOpen():
                try:
                    if self.pp.tab1_frame[0].checkBox_backMonitor.isChecked() or self.pp.tabWidget.currentIndex() == 0:
                        time.sleep(0.1)

                        self.mutex.acquire()
                        self.serial.flushInput()
                        self.serial.write("$A0\n".encode('ascii'))
                        time.sleep(0.3)
                        # b = self.serial.readline()
                        b = self.serial.read(self.serial.in_waiting or 300)
                        self.mutex.release()
                        slot = b.splitlines()

                        for i in (1, 2, 3, 4, 5, 6):
                            #print(slot[i-1])
                            self.pp.tab1_frame[i].SlotShowToBuffer(slot[i-1])

                        if self.serial_open_flag:
                            self.serial_open_flag = 0
                            self.pp.updateInit()

                        self.sin.emit()
                    time.sleep(0.2)

                    #if self.pp.tab4_frame[0].checkBox_PowerWave.isChecked() and self.pp.tabWidget.currentIndex() == 3:
                    if self.pp.tab4_frame[0].checkBox_PowerWave.isChecked():
                        if self.volt_now != 4500:
                            self.volt_now = 4500
                            self.mutex.acquire()
                            self.serial.flushInput()
                            self.serial.write(("$v0-" + str(self.volt_now) + "\n").encode('ascii'))
                            time.sleep(0.2)
                            self.serial.flushInput()
                            self.mutex.release()
                        else:
                            self.volt_now = 5500
                            self.mutex.acquire()
                            self.serial.flushInput()
                            self.serial.write(("$v0-" + str(self.volt_now) + "\n").encode('ascii'))
                            time.sleep(0.2)
                            self.serial.flushInput()
                            self.mutex.release()
                    else:
                        if self.volt_now != 5100:
                            self.volt_now = 5100
                            self.mutex.acquire()
                            self.serial.flushInput()
                            self.serial.write(("$v0-" + str(self.volt_now) + "\n").encode('ascii'))
                            time.sleep(0.2)
                            self.serial.flushInput()
                            self.mutex.release()
                        else:
                            time.sleep(0.2)
                        '''
                        else:
                            self.kKcount = self.kKcount + 1
                            if self.kKcount > 10:
                                self.kKcount = 0
                                time.sleep(0.1)
                                os.system("ssdtestboard -n 26 -k 123")
                                time.sleep(0.1)
                                os.system("ssdtestboard -n 26 -K 456")
                            else:
                                time.sleep(0.2)
                        '''

                    # Heating control
                    if self.pp.tab3_frame[0].checkBox_Heating.isChecked() or self.pp.tab5_frame[0].checkBox_Heating.isChecked():
                        if self.pp.tab3_SlotTestingCount != 0 or self.pp.tab5_SlotTestingCount != 0:
                            if self.heating_flag == 0:
                                self.heating_flag = 1
                                if self.pp.tab3_SlotTestingCount != 0:
                                    self.pp.STB_Heating(self.pp.tab3_frame[0].horizontalSlider_heatPercent.value())
                                else:
                                    self.pp.STB_Heating(self.pp.tab5_frame[0].horizontalSlider_heatPercent.value())

                                self.pp.tab3_frame[0].checkBox_Heating.setStyleSheet("color:red;")
                                self.pp.tab5_frame[0].checkBox_Heating.setStyleSheet("color:red;")
                                self.heating_clore = "red"
                        else:
                            if self.heating_flag == 1:
                                self.heating_flag = 0
                                self.pp.STB_Heating(0)

                            if self.heating_clore != "blue":
                                self.heating_clore = "blue"
                                self.pp.tab3_frame[0].checkBox_Heating.setStyleSheet("color:blue;")
                                self.pp.tab5_frame[0].checkBox_Heating.setStyleSheet("color:blue;")
                    else:
                        if self.heating_flag == 1:
                            self.heating_flag = 0
                            self.pp.STB_Heating(0)

                        if self.heating_clore != "black":
                            self.heating_clore = "black"
                            self.pp.tab3_frame[0].checkBox_Heating.setStyleSheet("color:black;")
                            self.pp.tab5_frame[0].checkBox_Heating.setStyleSheet("color:black;")

                except:
                    pass

# tab_3 ################################################################################################################

'''
tab "测试硬盘"
'''
TEST_PASS                   = 0
ERROR_RE_READ_DATA          = 1
ERROR_CE_COMPARE_DATA       = 2
ERROR_WE_WIRTE_DATA         = 3
ERROR_AE_ABORT              = 4
ERROR_TO_TIMEOUT            = 5
ERROR_NE_NOMEM              = 6
ERROR_RO_DISK               = 7
ERROR_DL_NONE_DISK          = 8
ERROR_US_UNSORTED           = 10
ERROR_UA_UNAUTHORIZATION    = 11
ERROR_OV_RUN_TIME_COUNT_OVERFLOW = 12

class DiskTest_Header(object):
    def __init__(self, parent, widget, position):

        self.parent = parent

        self.frame = QtWidgets.QFrame(widget)
        self.frame.setGeometry(position)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("HeadControl")

        '''
        self.pushButton_initTest = QtWidgets.QPushButton(self.frame)
        self.pushButton_initTest.setGeometry(QtCore.QRect(718, 3, 80, 23))
        self.pushButton_initTest.setObjectName("pushButton_initTest")
        self.pushButton_initTest.setText("初始化显示")
        '''

        self.pushButton_deleteDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_deleteDisk.setGeometry(QtCore.QRect(802, 3, 77, 23))
        self.pushButton_deleteDisk.setObjectName("pushButton_deleteDisk")
        self.pushButton_deleteDisk.setText("删除硬盘")

        self.pushButton_manualUpdate = QtWidgets.QPushButton(self.frame)
        self.pushButton_manualUpdate.setGeometry(QtCore.QRect(881, 3, 77, 23))
        self.pushButton_manualUpdate.setObjectName("pushButton_manualUpdate")
        self.pushButton_manualUpdate.setText("手动刷新")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)

        self.pushButton_testTH0 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testTH0.setFont(font)
        self.pushButton_testTH0.setGeometry(QtCore.QRect(3, 3, 75, 23))
        self.pushButton_testTH0.setObjectName("pushButton_testTH0")
        self.pushButton_testTH0.setText("TH0测试")

        self.pushButton_testTH02 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testTH02.setFont(font)
        self.pushButton_testTH02.setGeometry(QtCore.QRect(83, 3, 75, 23))
        self.pushButton_testTH02.setObjectName("pushButton_testTH02")
        self.pushButton_testTH02.setText("TH0.2测试")

        self.pushButton_testTH1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testTH1.setFont(font)
        self.pushButton_testTH1.setGeometry(QtCore.QRect(163, 3, 75, 23))
        self.pushButton_testTH1.setObjectName("pushButton_testTH1")
        self.pushButton_testTH1.setText("TH1测试")

        self.pushButton_testTH3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testTH3.setFont(font)
        self.pushButton_testTH3.setGeometry(QtCore.QRect(243, 3, 75, 23))
        self.pushButton_testTH3.setObjectName("pushButton_testTH3")
        self.pushButton_testTH3.setText("TH3测试")

        self.pushButton_testTH5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testTH5.setFont(font)
        self.pushButton_testTH5.setGeometry(QtCore.QRect(323, 3, 75, 23))
        self.pushButton_testTH5.setObjectName("pushButton_testTH5")
        self.pushButton_testTH5.setText("TH5测试")

        self.pushButton_testTH10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testTH10.setFont(font)
        self.pushButton_testTH10.setGeometry(QtCore.QRect(403, 3, 75, 23))
        self.pushButton_testTH10.setObjectName("pushButton_testTH10")
        self.pushButton_testTH10.setText("TH10测试")

        self.pushButton_testRO1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testRO1.setFont(font)
        self.pushButton_testRO1.setGeometry(QtCore.QRect(483, 3, 75, 23))
        self.pushButton_testRO1.setObjectName("pushButton_testRO1")
        self.pushButton_testRO1.setText("RO1测试")

        self.pushButton_testVY1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testVY1.setFont(font)
        self.pushButton_testVY1.setGeometry(QtCore.QRect(563, 3, 75, 23))
        self.pushButton_testVY1.setObjectName("pushButton_testVY1")
        self.pushButton_testVY1.setText("VY1测试")

        self.checkBox_Heating = QtWidgets.QCheckBox(self.frame)
        self.checkBox_Heating.setGeometry(QtCore.QRect(650, 3, 80, 23))
        self.checkBox_Heating.setObjectName("checkBox_Heating")
        self.checkBox_Heating.setText("开启加热")
        self.checkBox_Heating.setStyleSheet("color:black;")

        self.label_heatPercent = QtWidgets.QLabel(self.frame)
        self.label_heatPercent.setGeometry(QtCore.QRect(725, 2, 60, 10))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setFamily("Arial")
        #font.setBold(True)
        self.label_heatPercent.setFont(font)
        self.label_heatPercent.setAutoFillBackground(False)
        #self.label_heatPercent.setStyleSheet("color:blue;")
        self.label_heatPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.label_heatPercent.setObjectName("label_heatPercent")
        self.label_heatPercent.setText("100%")

        self.horizontalSlider_heatPercent = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_heatPercent.setGeometry(QtCore.QRect(725, 11, 60, 15))
        self.horizontalSlider_heatPercent.setMinimum(0)
        self.horizontalSlider_heatPercent.setMaximum(100)
        self.horizontalSlider_heatPercent.setProperty("value", 100)
        self.horizontalSlider_heatPercent.setTickInterval(1)
        self.horizontalSlider_heatPercent.setSingleStep(1)
        self.horizontalSlider_heatPercent.setPageStep(1)
        self.horizontalSlider_heatPercent.setInvertedAppearance(False)
        self.horizontalSlider_heatPercent.setInvertedControls(True)
        self.horizontalSlider_heatPercent.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_heatPercent.setObjectName("horizontalSlider_heatPercent")

        # 创建定时器
        self.timer_autoUpdate = QtCore.QTimer(self.parent)

        self.__attach_events()

    def __attach_events(self):
        self.pushButton_manualUpdate.clicked.connect(self.On_manualUpdate)
        self.pushButton_deleteDisk.clicked.connect(self.On_deleteDisk)
        #self.checkBox_autoUpdate.stateChanged.connect(self.On_autoUpdate)
        #self.checkBox_Heating.stateChanged.connect(self.On_Heating)
        #self.horizontalSlider_heatPercent.valueChanged.connect(self.On_OnHeatingSlider)
        self.timer_autoUpdate.timeout.connect(self.OnAutoUpdateTimer)

        self.pushButton_testTH0.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_TH0))
        self.pushButton_testTH02.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_TH02))
        self.pushButton_testTH1.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_TH1))
        self.pushButton_testTH3.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_TH3))
        self.pushButton_testTH5.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_TH5))
        self.pushButton_testTH10.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_TH10))
        self.pushButton_testRO1.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_RO1))
        self.pushButton_testVY1.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_VY1))

    def On_manualUpdate(self):
        #print("in On_manualUpdate")
        for i in (1, 2, 3, 4, 5, 6):
            self.parent.tab3_frame[i].SlotIDtoScsiID()

    def On_deleteDisk(self):
        #print("in On_deleteDisk")
        for i in (1, 2, 3, 4, 5, 6):
            self.parent.tab3_frame[i].SlotDeleteDisk()
            self.parent.tab3_frame[i].SlotDeleteSmart()

    '''
    def On_autoUpdate(self):
        #print("in On_autoUpdate")
        if self.checkBox_autoUpdate.isChecked():
            self.pushButton_manualUpdate.setDisabled(True)
            self.timer_autoUpdate.start(500)

        else:
            self.pushButton_manualUpdate.setEnabled(True)
            self.timer_autoUpdate.stop()
    '''

    def On_OnHeatingSlider(self):
        if 1:
            self.label_heatPercent.setText("{}%".format(self.horizontalSlider_heatPercent.value()))
            self.On_Heating()
        else:
            #print("in On_OnTimeSlider")
            #print(self.horizontalSlider_OnTime.value())
            pass

    def On_Heating(self):
        # print("in On_Heating")
        if self.checkBox_Heating.isChecked():
            self.parent.STB_Heating(self.horizontalSlider_heatPercent.value())
        else:
            self.parent.STB_Heating(0)

    def OnAutoUpdateTimer(self):
        #print("in OnAutoUpdateTimer")
        self.On_manualUpdate()
        self.timer_autoUpdate.start(500)

    def On_testAllTHxx(self, testItem):
        self.parent.STB_RuntimePlus()
        self.parent.STB_GetRuntime()
        for i in (1, 2, 3, 4, 5, 6):
            if testItem == TEST_ITEM_TH0:
                self.parent.tab3_frame[i].On_THxx(self.parent.tab3_frame[i].pushButton_TH0, TEST_ITEM_TH0)
            if testItem == TEST_ITEM_TH02:
                self.parent.tab3_frame[i].On_THxx(self.parent.tab3_frame[i].pushButton_TH02, TEST_ITEM_TH02)
            if testItem == TEST_ITEM_TH1:
                self.parent.tab3_frame[i].On_THxx(self.parent.tab3_frame[i].pushButton_TH1, TEST_ITEM_TH1)
            if testItem == TEST_ITEM_TH3:
                self.parent.tab3_frame[i].On_THxx(self.parent.tab3_frame[i].pushButton_TH3, TEST_ITEM_TH3)
            if testItem == TEST_ITEM_TH5:
                self.parent.tab3_frame[i].On_THxx(self.parent.tab3_frame[i].pushButton_TH5, TEST_ITEM_TH5)
            if testItem == TEST_ITEM_TH10:
                self.parent.tab3_frame[i].On_THxx(self.parent.tab3_frame[i].pushButton_TH10, TEST_ITEM_TH10)
            if testItem == TEST_ITEM_RO1:
                self.parent.tab3_frame[i].On_THxx(self.parent.tab3_frame[i].pushButton_RO1, TEST_ITEM_RO1)
            if testItem == TEST_ITEM_VY1:
                self.parent.tab3_frame[i].On_THxx(self.parent.tab3_frame[i].pushButton_VY1, TEST_ITEM_VY1)


TEST_ITEM_NONE = '0'
TEST_ITEM_TH0  = 'TH0'
TEST_ITEM_TH02 = 'TH0.2'
TEST_ITEM_TH1 = 'TH1'
TEST_ITEM_TH3 = 'TH3'
TEST_ITEM_TH5 = 'TH5'
TEST_ITEM_TH10 = 'TH10'
TEST_ITEM_RO1 = 'RO1'
TEST_ITEM_VY1 = 'VY1'

SLOT_EMPTY  = 0
SLOT_INSERT = 1

SLOT_LED_NO_INIT = 0
SLOT_LED_SHOW_NUM = 1
SLOT_LED_SHOW_LINE = 2
SLOT_LED_SHOW_FLASH = 3

class SlotDiskTest(object):
    def __init__(self, parent, widget, position, slotnum):
        self.slotnum = slotnum
        self.pp = parent
        self.serail = parent.serial
        self.mutex = parent.mutex
        self.scsi_id = "{}:0:0:0".format(slotnum - 1)
        self.sdxx = ""
        self.secSize = 0
        self.sin = widget.sin[slotnum]
        self.disklist = []
        self.writeSpeed = "0.0"
        self.readSpeed = "0.0"

        self.testItem = TEST_ITEM_NONE
        self.slotStatus = "SLOT_EMPTY"
        self.SlotDiskTestThread = SlotDiskTest_Thread(self)

        self.smartDict_now = {'01':'0', '05':'0', 'A3':'0', 'C2':'0', 'C3':'0', 'C4':'0', 'C7':'0'}
        self.smartDict_old = {'01':'0', '05':'0', 'A3':'0', 'C2':'0', 'C3':'0', 'C4':'0', 'C7':'0'}

        self.color = {
            'red':"#ff0000",  # red
            'orange':"#ff8800",  # orange
            'yellow' : "#ffff00",  # yellow
            'yellow_green' : "#ccff00",  # yellow green
            'green' : "#00ff00",  # green
            'green-blue': "#00ff88",  # green-xx
            'blue': "#55ff00",  # blue
        }

        # " text-align: center; }}" \

        self.progressBarStyleSheetTemplate = \
            "QProgressBar {{" \
            " border: 1px solid black;" \
            " border-radius: 1px;" \
            " text-align: right; }}" \
        "QProgressBar::chunk:horizontal {{" \
            " background-color: {0};" \
            " width: 1px;" \
            " margin: 0px;}}"


        #self.setStyleSheet(self.progressBarStyleSheetTemplate.format(self.color[yellow_green]))

        self.frame = QtWidgets.QFrame(widget)
        self.frame.setGeometry(position)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame" + "slotnum")

        self.line_0 = QtWidgets.QFrame(self.frame)
        self.line_0.setGeometry(QtCore.QRect(0, 0, 160, 2))
        self.line_0.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_0.setObjectName("line_0")

        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 2, 700))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(159, 0, 2, 700))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 4, 40, 60))
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setStyleSheet("color:white;background:gray")
        self.lcdNumber.setProperty("value", slotnum)
        self.lcdNumber.setObjectName("lcdNumber")

        self.label_progress = QtWidgets.QLabel(self.frame)
        # self.label_progress.setGeometry(QtCore.QRect(51, 70, 60, 20))
        self.label_progress.setGeometry(QtCore.QRect(3, 66, 155, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_progress.setFont(font)
        self.label_progress.setStyleSheet("color:red;")
        self.label_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.label_progress.setFont(font)
        self.label_progress.setObjectName("label_progress")
        self.progressValue = 0
        #self.label_progress.setText("TH10: 10:0000 Dumping")
        self.label_progress.setText("")

        self.label_scsi_id = QtWidgets.QLabel(self.frame)
        self.label_scsi_id.setGeometry(QtCore.QRect(40, 78, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_scsi_id.setFont(font)
        self.label_scsi_id.setAutoFillBackground(False)
        self.label_scsi_id.setStyleSheet("color:#00C78C;")
        self.label_scsi_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_scsi_id.setObjectName("label_scsi_id")
        #self.label_scsi_id.setText("0:0:0:0")
        self.label_scsi_id.setText("-:-:-:-")

        self.label_sdx = QtWidgets.QLabel(self.frame)
        self.label_sdx.setGeometry(QtCore.QRect(40, 95, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_sdx.setFont(font)
        self.label_sdx.setAutoFillBackground(False)
        self.label_sdx.setStyleSheet("color:blue;")
        self.label_sdx.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sdx.setObjectName("label_sdx")
        self.label_sdx.setText("")

        self.label_disknameValue = QtWidgets.QLabel(self.frame)
        self.label_disknameValue.setGeometry(QtCore.QRect(1, 120, 158, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        # font.setFamily("Arial")
        font.setBold(True)
        self.label_disknameValue.setFont(font)
        self.label_disknameValue.setStyleSheet("color:blue;")
        self.label_disknameValue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disknameValue.setFont(font)
        self.label_disknameValue.setObjectName("label_disknameValue")
        #self.label_disknameValue.setText("Faspeed K6-120G12345")
        self.label_disknameValue.setText("")

        self.label_fwVersionValue = QtWidgets.QLabel(self.frame)
        self.label_fwVersionValue.setGeometry(QtCore.QRect(5, 138, 73, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        # font.setFamily("Arial")
        font.setBold(True)
        self.label_fwVersionValue.setFont(font)
        self.label_fwVersionValue.setStyleSheet("color:green;")
        self.label_fwVersionValue.setAlignment(QtCore.Qt.AlignRight)
        self.label_fwVersionValue.setFont(font)
        self.label_fwVersionValue.setObjectName("label_fwVersionValue")
        #self.label_fwVersionValue.setText("{}".format("Q0525A"))
        self.label_fwVersionValue.setText("")

        self.label_sizeValue = QtWidgets.QLabel(self.frame)
        self.label_sizeValue.setGeometry(QtCore.QRect(82, 138, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        font.setBold(True)
        self.label_sizeValue.setFont(font)
        self.label_sizeValue.setStyleSheet("color:blue;")
        self.label_sizeValue.setAlignment(QtCore.Qt.AlignLeft)
        self.label_sizeValue.setFont(font)
        self.label_sizeValue.setObjectName("label_sizeValue")
        #self.label_sizeValue.setText("{}GB".format("120"))
        self.label_sizeValue.setText("")

        self.label_snValue = QtWidgets.QLabel(self.frame)
        self.label_snValue.setGeometry(QtCore.QRect(2, 150, 156, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_snValue.setFont(font)
        self.label_snValue.setStyleSheet("color:blue;")
        self.label_snValue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_snValue.setFont(font)
        self.label_snValue.setObjectName("label_snValue")
        #self.label_snValue.setText("12345678900987654321")
        self.label_snValue.setText("")

        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 170, 160, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_TH0 = QtWidgets.QPushButton(self.frame)
        self.pushButton_TH0.setFont(font)
        self.pushButton_TH0.setGeometry(QtCore.QRect(4, 173, 35, 25))
        self.pushButton_TH0.setObjectName("pushButton_TH0")
        self.pushButton_TH0.setText("TH0")

        self.pushButton_TH02 = QtWidgets.QPushButton(self.frame)
        self.pushButton_TH02.setFont(font)
        self.pushButton_TH02.setGeometry(QtCore.QRect(42, 173, 36, 25))
        self.pushButton_TH02.setObjectName("pushButton_TH02")
        self.pushButton_TH02.setText("TH.2")

        self.pushButton_TH1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_TH1.setFont(font)
        self.pushButton_TH1.setGeometry(QtCore.QRect(81, 173, 36, 25))
        self.pushButton_TH1.setObjectName("pushButton_TH1")
        self.pushButton_TH1.setText("TH1")

        self.pushButton_TH3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_TH3.setFont(font)
        self.pushButton_TH3.setGeometry(QtCore.QRect(120, 173, 36, 25))
        self.pushButton_TH3.setObjectName("pushButton_TH3")
        self.pushButton_TH3.setText("TH3")

        self.pushButton_TH5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_TH5.setFont(font)
        self.pushButton_TH5.setGeometry(QtCore.QRect(4, 200, 35, 25))
        self.pushButton_TH5.setObjectName("pushButton_TH5")
        self.pushButton_TH5.setText("TH5")

        self.pushButton_TH10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_TH10.setFont(font)
        self.pushButton_TH10.setGeometry(QtCore.QRect(42, 200, 36, 25))
        self.pushButton_TH10.setObjectName("pushButton_TH10")
        self.pushButton_TH10.setText("TH10")

        self.pushButton_RO1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_RO1.setFont(font)
        self.pushButton_RO1.setGeometry(QtCore.QRect(81, 200, 36, 25))
        self.pushButton_RO1.setObjectName("pushButton_RO1")
        self.pushButton_RO1.setText("RO1")

        self.pushButton_VY1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_VY1.setFont(font)
        self.pushButton_VY1.setGeometry(QtCore.QRect(120, 200, 36, 25))
        self.pushButton_VY1.setObjectName("pushButton_VY1")
        self.pushButton_VY1.setText("VY1")

        self.line_41 = QtWidgets.QFrame(self.frame)
        self.line_41.setGeometry(QtCore.QRect(0, 227, 160, 2))
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")

        self.label_rwspeed = QtWidgets.QLabel(self.frame)
        self.label_rwspeed.setGeometry(QtCore.QRect(3, 229, 155, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Mono")
        font.setFamily("Arial")
        font.setBold(True)
        self.label_rwspeed.setFont(font)
        self.label_rwspeed.setStyleSheet("color:green;")
        self.label_rwspeed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rwspeed.setFont(font)
        self.label_rwspeed.setObjectName("label_progress")
        self.progressValue = 0
        self.label_rwspeed.setText("R/W[{}/{}]MB/s".format(self.writeSpeed, self.readSpeed))

        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(0, 245, 160, 2))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        # font.setBold(True)
        self.pushButton_DeleteDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_DeleteDisk.setFont(font)
        self.pushButton_DeleteDisk.setGeometry(QtCore.QRect(4, 247, 75, 22))
        self.pushButton_DeleteDisk.setObjectName("pushButton_DeleteDisk")
        self.pushButton_DeleteDisk.setText("删除硬盘")

        self.pushButton_ReflashDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_ReflashDisk.setFont(font)
        self.pushButton_ReflashDisk.setGeometry(QtCore.QRect(81, 247, 75, 22))
        self.pushButton_ReflashDisk.setObjectName("pushButton_ReflashDisk")
        self.pushButton_ReflashDisk.setText("手动刷新")

        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(0, 270, 160, 2))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.testFlag = "NOT_TEST"
        self.testCycleNow = 0
        self.testStartTime = 0
        self.progressBar = [0 for x in range(0, 10)]
        self.eachCycleUsedTime = [0 for x in range(0, 10)]
        self.label_TestUsedTime = [0 for x in range(0, 10)]
        self.label_TestResult = [0 for x in range(0, 10)]
        for i in range(0, 10):
            self.progressBar[i] = QtWidgets.QProgressBar(self.frame)
            self.progressBar[i].setGeometry(QtCore.QRect(3, 275 + i*20, 154, 18))
            self.progressBar[i].setProperty("value", 0)
            self.progressBar[i].setTextVisible(True)
            font = QtGui.QFont()
            font.setPointSize(10)
            # font.setFamily("Arial")
            font.setBold(True)
            self.progressBar[i].setFont(font)
            self.progressBar[i].setStyleSheet(self.progressBarStyleSheetTemplate.format(self.color['green']))
            self.progressBar[i].setOrientation(QtCore.Qt.Horizontal)
            self.progressBar[i].setTextDirection(QtWidgets.QProgressBar.TopToBottom)
            self.progressBar[i].setObjectName("progressBar{}".format(i))
            #self.progressBar[i].setValue(100)

            self.eachCycleUsedTime[i] = 0

            self.label_TestUsedTime[i] = QtWidgets.QLabel(self.frame)
            self.label_TestUsedTime[i].setGeometry(QtCore.QRect(10, 277 + i*20, 50, 18))
            font = QtGui.QFont()
            font.setPointSize(10)
            # font.setFamily("Arial")
            font.setFamily("Mono")
            # font.setBold(True)
            self.label_TestUsedTime[i].setFont(font)
            self.label_TestUsedTime[i].setStyleSheet("color:black;")
            self.label_TestUsedTime[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_TestUsedTime[i].setFont(font)
            self.label_TestUsedTime[i].setObjectName("label_TestUsedTime{}".format(i))
            #self.label_TestUsedTime[i].setText("300m25s")
            self.label_TestUsedTime[i].setText("")

            self.label_TestResult[i] = QtWidgets.QLabel(self.frame)
            self.label_TestResult[i].setGeometry(QtCore.QRect(65, 277 + i * 20, 91, 14))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Mono")
            #font.setFamily("Mono")
            #font.setBold(True)
            self.label_TestResult[i].setFont(font)
            self.label_TestResult[i].setStyleSheet("color:black;")
            self.label_TestResult[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_TestResult[i].setFont(font)
            self.label_TestResult[i].setObjectName("label_TestResult{}".format(i))
            #self.label_TestResult[i].setText("PS[05]68")
            self.label_TestResult[i].setText("")

        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(0, 477, 160, 2))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.label_smartName = [0 for x in range(0, 7)]
        self.label_smartValue = [0 for x in range(0, 7)]
        for i in range(0,7):
            self.label_smartName[i] = QtWidgets.QLabel(self.frame)
            self.label_smartName[i].setGeometry(QtCore.QRect(5, 480 + i*20, 80, 16))
            font = QtGui.QFont()
            font.setPointSize(10)
            #font.setFamily("Arial")
            font.setFamily("Mono")
            #font.setBold(True)
            self.label_smartName[i].setFont(font)
            self.label_smartName[i].setStyleSheet("color:black;")
            self.label_smartName[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_smartName[i].setFont(font)
            self.label_smartName[i].setObjectName("label_smartName{}".format(i))
            self.label_smartName[i].setText("")
            #self.label_smartName[i].setText("{:02X}:".format(i))


            self.label_smartValue[i] = QtWidgets.QLabel(self.frame)
            self.label_smartValue[i].setGeometry(QtCore.QRect(88, 481 + i*20, 67, 16))
            font = QtGui.QFont()
            font.setPointSize(10)
            # font.setFamily("Arial")
            font.setFamily("Mono")
            font.setBold(True)
            self.label_smartValue[i].setFont(font)
            self.label_smartValue[i].setStyleSheet("color:blue;")
            self.label_smartValue[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_smartValue[i].setFont(font)
            self.label_smartValue[i].setObjectName("label_smartValue{}".format(i))
            self.label_smartValue[i].setText("")
            #self.label_smartValue[i].setText("{:02X}:".format(i))

        self.testDiskSn = ""
        self.nowDiskSn = ""

        # 创建定时器
        self.timer_testProgress = QtCore.QTimer(self.pp)
        self.__attach_events()

    def __attach_events(self):
        self.sin.connect(self.updateDiskTestResult)
        self.pushButton_TH0.clicked.connect(lambda: self.On_THxx(self.pushButton_TH0, TEST_ITEM_TH0))
        self.pushButton_TH02.clicked.connect(lambda:self.On_THxx(self.pushButton_TH02, TEST_ITEM_TH02))
        self.pushButton_TH1.clicked.connect(lambda: self.On_THxx(self.pushButton_TH1, TEST_ITEM_TH1))
        self.pushButton_TH3.clicked.connect(lambda: self.On_THxx(self.pushButton_TH3, TEST_ITEM_TH3))
        self.pushButton_TH5.clicked.connect(lambda: self.On_THxx(self.pushButton_TH5, TEST_ITEM_TH5))
        self.pushButton_TH10.clicked.connect(lambda: self.On_THxx(self.pushButton_TH10, TEST_ITEM_TH10))
        self.pushButton_RO1.clicked.connect(lambda: self.On_THxx(self.pushButton_RO1, TEST_ITEM_RO1))
        self.pushButton_VY1.clicked.connect(lambda: self.On_THxx(self.pushButton_VY1, TEST_ITEM_VY1))

        self.timer_testProgress.timeout.connect(self.OnTestProgressTimer)

        self.pushButton_DeleteDisk.clicked.connect(self.On_DeleteDisk)
        self.pushButton_ReflashDisk.clicked.connect(self.On_ReflashDisk)

    def On_DeleteDisk(self):
        self.SlotDeleteDisk()

    def On_ReflashDisk(self):
        for i in range(0, 7):
            self.label_smartName[i].setText("")
            self.label_smartValue[i].setText("")
            self.label_smartValue[i].setStyleSheet("color:blue;")
        self.SlotIDtoScsiID()

    def SetAllTestButtonDisable(self):
        self.pushButton_TH0.setEnabled(False)
        self.pushButton_TH02.setEnabled(False)
        self.pushButton_TH1.setEnabled(False)
        self.pushButton_TH3.setEnabled(False)
        self.pushButton_TH5.setEnabled(False)
        self.pushButton_TH10.setEnabled(False)
        self.pushButton_RO1.setEnabled(False)
        self.pushButton_VY1.setEnabled(False)
        self.pushButton_TH0.setStyleSheet("color:white; background:gray")
        self.pushButton_TH02.setStyleSheet("color:white; background:gray")
        self.pushButton_TH1.setStyleSheet("color:white; background:gray")
        self.pushButton_TH3.setStyleSheet("color:white; background:gray")
        self.pushButton_TH5.setStyleSheet("color:white; background:gray")
        self.pushButton_TH10.setStyleSheet("color:white; background:gray")
        self.pushButton_RO1.setStyleSheet("color:white; background:gray")
        self.pushButton_VY1.setStyleSheet("color:white; background:gray")

    def SetAllTestButtonEnable(self):
        self.pushButton_TH0.setEnabled(True)
        self.pushButton_TH02.setEnabled(True)
        self.pushButton_TH1.setEnabled(True)
        self.pushButton_TH3.setEnabled(True)
        self.pushButton_TH5.setEnabled(True)
        self.pushButton_TH10.setEnabled(True)
        self.pushButton_RO1.setEnabled(True)
        self.pushButton_VY1.setEnabled(True)
        self.pushButton_TH0.setStyleSheet("color:black;")
        self.pushButton_TH02.setStyleSheet("color:black;")
        self.pushButton_TH1.setStyleSheet("color:black;")
        self.pushButton_TH3.setStyleSheet("color:black;")
        self.pushButton_TH5.setStyleSheet("color:black;")
        self.pushButton_TH10.setStyleSheet("color:black;")
        self.pushButton_RO1.setStyleSheet("color:black;")
        self.pushButton_VY1.setStyleSheet("color:black;")

    def On_THxx(self, button, testName):
        if self.testItem == TEST_ITEM_NONE:
            self.InitTest()

            if self.sdxx != "":
                self.SetAllTestButtonDisable()
                button.setStyleSheet("color:white;""background:purple")
                self.testItem = testName
                self.testDiskSn = self.nowDiskSn
                self.testCycleNow = 0
                self.testStartTime = 0
                self.writeSpeed = "0"
                self.readSpeed = "0"
                for i in range(0, 10):
                    self.progressBar[i].setValue(0)
                    self.eachCycleUsedTime[i] = 0
                    self.label_TestUsedTime[i].setText("")
                    self.label_TestResult[i].setText("")
                    self.label_TestResult[i].setStyleSheet("")

                self.testFlag = "RUNNING"
                shownum = sid_to_slotnum[self.scsi_id]
                self.pp.STB_LED_PointFlashCtl(shownum, 1)
                self.SlotDiskTestThread.start()
                self.pp.tab3_SlotTestingCount = self.pp.tab3_SlotTestingCount + 1
                self.timer_testProgress.start(1000)

            else:
                for i in range(0, 10):
                    self.progressBar[i].setValue(0)
                    self.eachCycleUsedTime[i] = 0
                    self.label_TestUsedTime[i].setText("")
                    self.label_TestResult[i].setText("")
                    self.label_TestResult[i].setStyleSheet("")
                shownum = sid_to_slotnum[self.scsi_id]
                self.pp.STB_LED_NumFlashCtl(shownum, 0)
                self.pp.STB_LED_PointFlashCtl(shownum, 0)
                self.pp.STB_LED_Show(shownum, 20)

    def OnTestProgressTimer(self):
        #print("in OnTestProgressTimer")
        #print("{} self.testFlag = {}".format(self.sdxx, self.testFlag))
        if self.testFlag == "RUNNING":
            try:
                f = os.popen('rw_show -c {}'.format(diskid[self.sdxx]))
                rw = f.readlines()

                rws = rw[0].replace('\n', '').strip()
                rwlist = rws.split(' ')
                #print("{} rwlist = {}".format(self.sdxx, rwlist))
            except:
                pass

            try:
                self.progressValue = rwlist[2]
                #print("{} self.progressValue = {} - {}".format(self.sdxx, self.progressValue, int(self.progressValue)))
                if rwlist[1] == "Writing":
                    self.label_progress.setText("{} : {:0.4f} Writing".format(self.testItem, self.testCycleNow + float(self.progressValue) / 100))
                    self.label_progress.setStyleSheet("color:red;")
                    self.progressBar[self.testCycleNow].setValue(int(float(self.progressValue)))
                    self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format('#00C957'))
                elif rwlist[1] == "Dumping" or rwlist[1] == "Verifying":
                    self.label_progress.setText("{} : {:0.4f} Dumping".format(self.testItem, self.testCycleNow + float(self.progressValue) / 100))
                    self.label_progress.setStyleSheet("color:green;")
                    self.progressBar[self.testCycleNow].setValue(int(float(self.progressValue)))
                    self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format('#00FF7F'))

                if rwlist[1] == "Writing":
                    self.writeSpeed = rwlist[3].replace('MB/s','')
                elif rwlist[1] == "Dumping" or rwlist[1] == "Verifying":
                    self.readSpeed = rwlist[3].replace('MB/s','')

                self.label_rwspeed.setText("R/W[{}/{}]MB/s".format(self.readSpeed, self.writeSpeed))

                now_time = time.time()
                self.label_TestUsedTime[self.testCycleNow].setText("{}m{}s".format(int((now_time - self.testStartTime)/60), int((now_time - self.testStartTime)%60)))
            except:
                pass

        #print("{} self.testFlag = {}".format(self.sdxx, self.testFlag))
        if self.testFlag == "FINISH":
            self.timer_testProgress.stop()
            self.SlotDiskTestThread.__del__()
            self.SetAllTestButtonEnable()
            self.testItem = TEST_ITEM_NONE
            shownum = sid_to_slotnum[self.scsi_id]
            self.pp.STB_LED_PointFlashCtl(shownum, 0)
            self.pp.tab3_SlotTestingCount = self.pp.tab3_SlotTestingCount - 1
        else:
            self.timer_testProgress.start(500)

    def updateDiskTestResult(self):
        print("in updateDiskTestResult")

        self.progressValue = 100.00
        self.label_progress.setText("{:0.2f}".format(float(self.progressValue) / 100))

        self.progressBar[diskid[self.sdxx]].setValue(int(self.progressValue))

        self.timer_testProgress.stop()

    def GetSmartInfo(self, sdxx):

        ID01_raw_read_error_rate       = 1
        ID05_reallocated_sectors_count = 5
        ID09_power_on_hours            = 9
        ID0C_power_cycle_count         = 12
        IDA3_original_bad_count        = 163
        IDA7_average_erase_count       = 167
        IDC2_temperature               = 194
        IDC3_read_retry                = 195
        IDC4_reallocation_event_count  = 196
        IDC7_ultraDMA_CRC_error_count  = 199
        IDF1_total_host_written        = 241
        IDF2_total_host_read           = 242

        small = []
        sml = []

        try:
            f = os.popen("smartctl -i /dev/{} | grep 'Firmware'".format(sdxx))
            sm = f.readlines()
            ver = sm[0].replace('Firmware Version:', '').replace('\n', '').strip()
            self.label_fwVersionValue.setText(ver)

            f = os.popen("smartctl -i /dev/{} | grep 'Device Model:'".format(sdxx))
            sm = f.readlines()
            name = sm[0].replace('Device Model:', '').replace('\n', '').strip()
            self.label_disknameValue.setText(name)

            f = os.popen("smartctl -s on -A /dev/{} | grep 0x0".format(sdxx))
            sm = f.readlines()
            for i in sm:
                smll = []
                sml = i.replace('\n', '').strip()
                sm_1space = sml.replace('   ', ' ').replace('   ', ' ').replace('  ', ' ').replace('  ', ' ')
                smlist = sm_1space.split(' ')

                smll.append(smlist[0])
                smll.append(smlist[1])
                smll.append(smlist[9])

                small.append(smll)

            # 读到结果为空，说明读取samrt失败，可能原因是 WE，RE，DL等原因，此种情况，不更新smart信息
            if len(sm) != 0:

                n = 0
                for (id, name, value) in small:
                    if int(id) == ID01_raw_read_error_rate:
                        self.label_smartName[n].setText("{:02X}:读错误率".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) != 0:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['01'] = value

                    elif int(id) == ID05_reallocated_sectors_count:
                        self.label_smartName[n].setText("{:02X}:新增坏块".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) != 0:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['05'] = value

                    elif int(id) == IDA3_original_bad_count:
                        self.label_smartName[n].setText("{:02X}:原始坏块".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['A3'] = int(value)

                    elif int(id) == IDC2_temperature:
                        self.label_smartName[n].setText("{:02X}:主控温度".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) > 40:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['C2'] = value

                    elif int(id) == IDC3_read_retry:
                        self.label_smartName[n].setText("{:02X}:重读次数".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) != 0:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['C3'] = value

                    elif int(id) == IDC4_reallocation_event_count:
                        self.label_smartName[n].setText("{:02X}:读取失败".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) != 0:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['C4'] = value

                    elif int(id) == IDC7_ultraDMA_CRC_error_count:
                        self.label_smartName[n].setText("{:02X}:链路重传".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) != 0:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['C7'] = value

                # 清空没有用到的ID内容
                for i in range(n, 7):
                    self.label_smartName[i].setText("")
                    self.label_smartValue[i].setText("")
        except:
            self.smartDict_now['01'] = '*'
            self.smartDict_now['05'] = '*'
            self.smartDict_now['A3'] = '*'
            self.smartDict_now['C2'] = '*'
            self.smartDict_now['C3'] = '*'
            self.smartDict_now['C4'] = '*'
            self.smartDict_now['C7'] = '*'

    def UpdateSmartOld(self):
        self.smartDict_old['01'] = self.smartDict_now['01']
        self.smartDict_old['05'] = self.smartDict_now['05']
        self.smartDict_old['A3'] = self.smartDict_now['A3']
        self.smartDict_old['C2'] = self.smartDict_now['C2']
        self.smartDict_old['C3'] = self.smartDict_now['C3']
        self.smartDict_old['C4'] = self.smartDict_now['C4']
        self.smartDict_old['C7'] = self.smartDict_now['C7']

    def InitTest(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                # print("[{}] {} {} {} {} {}".format(self.slotnum, scsiid, sdxx, size_GB, deviceName, sn))
                if self.scsi_id == scsiid:
                    self.label_scsi_id.setText("{}".format(scsiid))
                    self.label_sdx.setText("{}".format(sdxx))
                    #self.label_disknameValue.setText(deviceName)
                    self.label_snValue.setText(sn)

                    self.label_sizeValue.setText(size_GB)
                    try:
                        os.system("echo 2 > /sys/block/{}/device/eh_timeout".format(sdxx))
                        os.system("echo 2 > /sys/block/{}/device/timeout".format(sdxx))
                        os.system("echo 1 > /sys/block/{}/device/queue_depth".format(sdxx))
                    except:
                        pass

                    self.lcdNumber.setStyleSheet("color:red;background:#888888")

                    self.sdxx = sdxx
                    self.secSize = secSize
                    self.nowDiskSn = sn

                    self.FirstSmartResultCtl(sdxx)
                    self.UpdateSmartOld()

                    break

            if n == (len(self.disklist) - 1):
                self.lcdNumber.setStyleSheet("color:white;background:#DDDDDD")
                self.label_scsi_id.setText("-:-:-:-")
                self.label_sdx.setText("")
                self.label_disknameValue.setText("")
                self.label_snValue.setText("")
                self.label_sizeValue.setText("")
                self.label_fwVersionValue.setText("")
                self.sdxx = ""
                self.secSize = ""
                self.nowDiskSn = ""
                for i in range(0, 7):
                    self.label_smartName[i].setText("")
                    self.label_smartValue[i].setText("")
                    self.label_smartValue[i].setStyleSheet("color:blue;")

        except:
            pass

    def SlotIDtoScsiID(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                # print("[{}] {} {} {} {} {}".format(self.slotnum, scsiid, sdxx, size_GB, deviceName, sn))
                if self.scsi_id == scsiid:
                    self.label_scsi_id.setText("{}".format(scsiid))
                    self.label_sdx.setText("{}".format(sdxx))
                    #self.label_disknameValue.setText(deviceName)
                    self.label_snValue.setText(sn)

                    self.label_sizeValue.setText(size_GB)
                    try:
                        os.system("echo 2 > /sys/block/{}/device/eh_timeout".format(sdxx))
                        os.system("echo 2 > /sys/block/{}/device/timeout".format(sdxx))
                        os.system("echo 1 > /sys/block/{}/device/queue_depth".format(sdxx))
                    except:
                        pass

                    self.lcdNumber.setStyleSheet("color:red;background:#888888")
                    self.GetSmartInfo(sdxx)
                    self.UpdateSmartOld()
                    self.sdxx = sdxx
                    self.secSize = secSize
                    self.nowDiskSn = sn

                    break

            if n == (len(self.disklist) - 1):
                #self.slotStatus = SLOT_EMPTY
                self.lcdNumber.setStyleSheet("color:white;background:#DDDDDD")
                self.label_scsi_id.setText("-:-:-:-")
                self.label_sdx.setText("")
                self.label_disknameValue.setText("")
                self.label_snValue.setText("")
                self.label_sizeValue.setText("")
                self.label_fwVersionValue.setText("")
                for i in range(0, 7):
                    self.label_smartName[i].setText("")
                    self.label_smartValue[i].setText("")
                    self.label_smartValue[i].setStyleSheet("color:blue;")

                '''
                #没有盘，不要做LED控制
                if self.testItem == TEST_ITEM_NONE and self.sdxx == "":
                    shownum = sid_to_slotnum[self.scsi_id]
                    self.pp.STB_LED_NumFlashCtl(shownum, 0)
                    self.pp.STB_LED_PointFlashCtl(shownum, 0)
                    #self.pp.STB_LED_Show(shownum, 20)
                '''
            # 手动刷新，不要对LED灯进行控制，第一次手动刷新，初始化LED状态
            if self.testItem == TEST_ITEM_NONE and self.slotStatus == SLOT_EMPTY:
                self.slotStatus = SLOT_INSERT
                shownum = sid_to_slotnum[self.scsi_id]
                self.pp.STB_LED_NumFlashCtl(shownum, 0)
                self.pp.STB_LED_PointFlashCtl(shownum, 0)
                self.pp.STB_LED_Show(shownum, shownum)

        except:
            print("{} SlotIDtoScsiID except !!!!!!".format(self.sdxx))
            pass

    def SlotDeleteDisk(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                if self.scsi_id == scsiid:
                    os.system("echo 1 > /sys/block/{}/device/delete".format(sdxx))
        except:
            print("{} SlotDeleteDisk except !!!!!!".format(self.sdxx))
            pass

    def SlotDeleteSmart(self):
        for i in range(0,7):
            self.label_smartName[i].setStyleSheet("color:gray;")
            #self.label_smartValue[i].setText("")
            #self.label_smartName[i].setText("")

    def TestReturn(self, ret):
        self.GetSmartInfo(self.sdxx)

        shownum = sid_to_slotnum[self.scsi_id]
        ret = ret/0x100
        if int(ret) == TEST_PASS:
           resultText = "PS"
           barColor = "#00FF7F"
        elif int(ret) == ERROR_RE_READ_DATA:
            resultText = "RE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_CE_COMPARE_DATA:
            resultText = "CE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_WE_WIRTE_DATA:
            resultText = "WE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_AE_ABORT:
            resultText = "AE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_TO_TIMEOUT:
            resultText = "TO"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_NE_NOMEM:
            resultText = "NE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_RO_DISK:
            resultText = "RO"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_DL_NONE_DISK:
            resultText = "DL"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_US_UNSORTED:
            resultText = "US"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_UA_UNAUTHORIZATION:
            resultText = "UA"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_OV_RUN_TIME_COUNT_OVERFLOW:
            resultText = "OV"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        else:
            resultText = "UK"
            barColor = 'red'
            print("{} ret = {}".format(self.sdxx, ret))
            self.pp.STB_LED_NumFlashCtl(shownum, 1)

        if self.smartDict_now['01'] != self.smartDict_old['01']:
            resultText = resultText + "(01){}".format(self.smartDict_now['01'])
            if barColor != 'red':
                barColor = 'red'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['05'] != self.smartDict_old['05']:
            resultText = resultText + "(05){}".format(self.smartDict_now['05'])
            if barColor != 'red':
                barColor = 'red'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C4'] != self.smartDict_now['C4']:
            resultText = resultText + "(C4){}".format(self.smartDict_now['C4'])
            if barColor != 'red':
                barColor = 'red'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C3'] != self.smartDict_old['C3']:
            resultText = resultText + "(C3){}".format(self.smartDict_now['C3'])
            if barColor != 'red':
                barColor = 'yellow'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C7'] != self.smartDict_old['C7']:
            resultText = resultText + "(C7){}".format(self.smartDict_now['C7'])
            if barColor != 'red':
                barColor = 'yellow'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C2'] > "40":
            resultText = resultText + "(C2){}".format(self.smartDict_now['C2'])
            if barColor != 'red':
                barColor = 'yellow'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        else:
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)

        if self.smartDict_now['01'] != "0" or self.smartDict_now['05'] != "0" or self.smartDict_now['C4'] != "0":
            #print("self.smartDict_now['01'] = {}".format(self.smartDict_now['01']))
            #print("self.smartDict_now['05'] = {}".format(self.smartDict_now['05']))
            #print("self.smartDict_now['C4'] = {}".format(self.smartDict_now['C4']))
            self.pp.STB_LED_NumFlashCtl(shownum, 1)

        self.UpdateSmartOld()

    def FirstSmartResultCtl(self, sdxx):
        # 恢复 LED 显示状态
        shownum = sid_to_slotnum[self.scsi_id]
        self.pp.STB_LED_NumFlashCtl(shownum, 0)
        self.pp.STB_LED_Show(shownum, shownum)
        #self.pp.STB_k()
        #self.pp.STB_K()
        #self.pp.STB_GetRuntime()

        # 初始化新测试硬盘状态
        self.smartDict_now['01'] = "0"
        self.smartDict_now['05'] = "0"
        self.smartDict_now['A3'] = "0"
        self.smartDict_now['C2'] = "0"
        self.smartDict_now['C3'] = "0"
        self.smartDict_now['C4'] = "0"
        self.smartDict_now['C7'] = "0"
        self.UpdateSmartOld()
        self.GetSmartInfo(sdxx)

        if self.smartDict_now['01'] != "0" or self.smartDict_now['05'] != "0" or self.smartDict_now['C4'] != "0":
            #print("self.smartDict_now['01'] = {}".format(self.smartDict_now['01']))
            #print("self.smartDict_now['05'] = {}".format(self.smartDict_now['05']))
            #print("self.smartDict_now['C4'] = {}".format(self.smartDict_now['C4']))
            self.pp.STB_LED_NumFlashCtl(shownum, 1)


LBA_START = 0
LBA_END_05G = (1048576 - 1)

class SlotDiskTest_Thread(QtCore.QThread):

    def __init__(self, parent):
        self.sin = parent.sin
        self.mutex = parent.mutex
        super(SlotDiskTest_Thread, self).__init__()
        self.working = True
        self.pp = parent

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        try:
            self.working = True
        except:
            pass

        while self.working == True:
            #if self.serial.isOpen():
            if True:
                try:
                    if self.pp.testItem == TEST_ITEM_TH0:
                        self.TH0()

                    if self.pp.testItem == TEST_ITEM_TH02:
                        self.TH02()

                    if self.pp.testItem == TEST_ITEM_TH1:
                        self.TH1()

                    if self.pp.testItem == TEST_ITEM_TH3:
                        self.TH3()

                    if self.pp.testItem == TEST_ITEM_TH5:
                        self.TH5()

                    if self.pp.testItem == TEST_ITEM_TH10:
                        self.TH10()

                    if self.pp.testItem == TEST_ITEM_RO1:
                        self.RO1()

                    if self.pp.testItem == TEST_ITEM_VY1:
                        self.VY1()

                    time.sleep(3)
                    self.working = False
                except:
                    print("{}-{} running thread except ！！！！！！！！！！！".format(self.pp.sdxx, self.pp.testItem))
                    break
                    #pass

    def TH0(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        # first test 0.5G
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            #print("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
            #    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, LBA_END_05G, LBA_START))
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 100 -t 0x0000 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, LBA_END_05G, LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[0] = finishTime - startTime
        time.sleep(5)

        self.pp.TestReturn(ret)

        self.pp.testFlag = "FINISH"

    def TH02(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            #print("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 1 -t 0x0000 -I {} /dev/{} {} {}".format(
            #    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, int(self.pp.secSize / 5), LBA_START))
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (int(self.pp.secSize / 5) - 1), LBA_START))

        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[0] = finishTime - startTime
        time.sleep(5)

        self.pp.TestReturn(ret)

        self.pp.testFlag = "FINISH"

    def TH1(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        # cycle 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[0] = finishTime - startTime
        time.sleep(5)

        self.pp.TestReturn(ret)

        self.pp.testFlag = "FINISH"

    def TH3(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        # cycle 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x1234 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[0] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 2
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x4321 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[1] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 3
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[2] = finishTime - startTime
        time.sleep(5)

        self.pp.TestReturn(ret)

        self.pp.testFlag = "FINISH"

    def TH5(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        # cycle 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x1234 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[0] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 2
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x4321 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[1] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 3
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x55AA -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[2] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 4
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xAA55 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        #print("{} ret = = = {}".format(self.pp.sdxx, ret))
        finishTime = time.time()
        self.pp.eachCycleUsedTime[3] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 5
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        #print("{} ret = = = {}".format(self.pp.sdxx, ret))
        finishTime = time.time()
        self.pp.eachCycleUsedTime[4] = finishTime - startTime
        time.sleep(5)

        self.pp.TestReturn(ret)

        self.pp.testFlag = "FINISH"

    def TH10(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        # cycle 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x1234 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[0] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 2
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x4321 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[1] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 3
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x55AA -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[2] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 4
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xAA55 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[3] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 5
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xEA3B -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        #print("{} ret = = = {}".format(self.pp.sdxx, ret))
        finishTime = time.time()
        self.pp.eachCycleUsedTime[4] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 6
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xFF00 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[5] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 7
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x00FF -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[6] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 8
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xCCCC -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[7] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 9
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x3333 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[8] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 10
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[9] = finishTime - startTime
        time.sleep(5)

        self.pp.TestReturn(ret)

        self.pp.testFlag = "FINISH"

    def RO1(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        # cycle 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -r 1 -L {} -w -s -e 10 -t 0xEA3B -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[0] = finishTime - startTime
        time.sleep(5)

        self.pp.TestReturn(ret)

        self.pp.testFlag = "FINISH"

    def VY1(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        # cycle 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "":
            ret = os.system("stb_rw -b 512 -c 2048 -D 1 -R 1 -L {} -w -s -e 10 -t 0x0000 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[0] = finishTime - startTime
        time.sleep(5)

        self.pp.TestReturn(ret)

        self.pp.testFlag = "FINISH"

def itoc(slotnum):
    if slotnum < 10:
        return str(slotnum)
    elif slotnum == 10:
        return 'A'
    elif slotnum == 11:
        return 'b'
    elif slotnum == 12:
        return 'c'
    elif slotnum == 13:
        return 'd'
    elif slotnum == 14:
        return 'E'
    elif slotnum == 15:
        return 'F'
    elif slotnum == 16:
        return 'G'
    elif slotnum == 26:
        return 'z'
    else:
        return 'H'


# tab_4 ################################################################################################################

'''
tab "克隆校验"
'''
CC_TEST_PASS                   = 0
CC_ERROR_RE_READ_DATA          = 1
CC_ERROR_CE_COMPARE_DATA       = 2
CC_ERROR_WE_WIRTE_DATA         = 3
CC_ERROR_SK_SEEK               = 4
CC_ERROR_DS_DATASYNC           = 5
CC_ERROR_DC_DISCARD_CACHE      = 6
CC_ERROR_NM_NMEM               = 7
CC_ERROR_DL_NONE_DISK          = 8
CC_ERROR_US_UNSORTED           = 10
CC_ERROR_UA_UNAUTHORIZATION    = 11
CC_ERROR_CP_CAP_LESS           = 12
CC_ERROR_OV_RUN_TIME_COUNT_OVERFLOW = 13


class CC_DiskTest_Header(object):
    def __init__(self, parent, widget, position):

        self.parent = parent

        self.frame = QtWidgets.QFrame(widget)
        self.frame.setGeometry(position)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("HeadControl")

        '''
        self.pushButton_initTest = QtWidgets.QPushButton(self.frame)
        self.pushButton_initTest.setGeometry(QtCore.QRect(718, 3, 80, 23))
        self.pushButton_initTest.setObjectName("pushButton_initTest")
        self.pushButton_initTest.setText("初始化显示")
        '''

        self.pushButton_deleteDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_deleteDisk.setGeometry(QtCore.QRect(802, 3, 77, 23))
        self.pushButton_deleteDisk.setObjectName("pushButton_deleteDisk")
        self.pushButton_deleteDisk.setText("删除硬盘")

        self.pushButton_manualUpdate = QtWidgets.QPushButton(self.frame)
        self.pushButton_manualUpdate.setGeometry(QtCore.QRect(881, 3, 77, 23))
        self.pushButton_manualUpdate.setObjectName("pushButton_manualUpdate")
        self.pushButton_manualUpdate.setText("手动刷新")

        self.checkBox_PowerWave = QtWidgets.QCheckBox(self.frame)
        self.checkBox_PowerWave.setGeometry(QtCore.QRect(655, 3, 140, 23))
        self.checkBox_PowerWave.setObjectName("checkBox_PowerWave")
        self.checkBox_PowerWave.setText("开启4.5~5.5V测试")
        #self.checkBox_PowerWave.setChecked(True)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)

        self.pushButton_AllCloneOnly = QtWidgets.QPushButton(self.frame)
        self.pushButton_AllCloneOnly.setFont(font)
        self.pushButton_AllCloneOnly.setGeometry(QtCore.QRect(3, 3, 154, 23))
        self.pushButton_AllCloneOnly.setObjectName("pushButton_AllCloneOnly")
        self.pushButton_AllCloneOnly.setText("Clone Only: 仅克隆")

        self.pushButton_AllCompareOnly = QtWidgets.QPushButton(self.frame)
        self.pushButton_AllCompareOnly.setFont(font)
        self.pushButton_AllCompareOnly.setGeometry(QtCore.QRect(163, 3, 154, 23))
        self.pushButton_AllCompareOnly.setObjectName("pushButton_AllCompareOnly")
        self.pushButton_AllCompareOnly.setText("Compare Only: 仅校验")

        self.pushButton_AllCloneAndCompare = QtWidgets.QPushButton(self.frame)
        self.pushButton_AllCloneAndCompare.setFont(font)
        self.pushButton_AllCloneAndCompare.setGeometry(QtCore.QRect(323, 3, 315, 23))
        self.pushButton_AllCloneAndCompare.setObjectName("pushButton_AllCloneAndCompare")
        self.pushButton_AllCloneAndCompare.setText("Clone + Compare: 克隆+校验")

        self.__attach_events()

    def __attach_events(self):
        self.pushButton_manualUpdate.clicked.connect(self.On_manualUpdate)
        self.pushButton_deleteDisk.clicked.connect(self.On_deleteDisk)

        self.pushButton_AllCloneOnly.clicked.connect(lambda: self.On_AllCCtest(CC_TEST_ITEM_CLONE))
        self.pushButton_AllCompareOnly.clicked.connect(lambda: self.On_AllCCtest(CC_TEST_ITEM_COMPARE))
        self.pushButton_AllCloneAndCompare.clicked.connect(lambda: self.On_AllCCtest(CC_TEST_ITEM_CLONECOMPARE))

    def On_manualUpdate(self):
        #print("in On_manualUpdate")
        for i in (1, 2, 3, 4, 5, 6):
            self.parent.tab4_frame[i].SlotIDtoScsiID()

    def On_deleteDisk(self):
        #print("in On_deleteDisk")
        #for i in (1, 2, 3, 4, 5, 6):
        #slot1 is the source drive, do not need to be delete
        for i in (2, 3, 4, 5, 6):
            self.parent.tab4_frame[i].SlotDeleteDisk()
            self.parent.tab4_frame[i].SlotDeleteSmart()

    def On_AllCCtest(self, testItem):
        self.parent.STB_RuntimePlus()
        self.parent.STB_GetRuntime()
        for i in (1, 2, 3, 4, 5, 6):
            if testItem == CC_TEST_ITEM_CLONE:
                self.parent.tab4_frame[i].On_CCtest(self.parent.tab4_frame[i].pushButton_CloneOnly, CC_TEST_ITEM_CLONE)
            if testItem == CC_TEST_ITEM_COMPARE:
                self.parent.tab4_frame[i].On_CCtest(self.parent.tab4_frame[i].pushButton_CompareOnly, CC_TEST_ITEM_COMPARE)
            if testItem == CC_TEST_ITEM_CLONECOMPARE:
                self.parent.tab4_frame[i].On_CCtest(self.parent.tab4_frame[i].pushButton_CloneAndCompare, CC_TEST_ITEM_CLONECOMPARE)

CC_TEST_ITEM_NONE = '0'
CC_TEST_ITEM_CLONE  = 'CLONE'
CC_TEST_ITEM_COMPARE  = 'COMPARE'
CC_TEST_ITEM_CLONECOMPARE  = 'CLONECOMPARE'

class CC_SlotDiskTest(object):
    def __init__(self, parent, widget, position, slotnum):
        self.slotnum = slotnum
        self.pp = parent
        self.serail = parent.serial
        self.mutex = parent.mutex
        self.scsi_id = "{}:0:0:0".format(slotnum - 1)
        self.sdxx = ""
        self.secSize = 0
        self.sin = widget.sin[slotnum]
        self.disklist = []
        self.writeSpeed = "0.0"
        self.readSpeed = "0.0"

        # SLOT1 = "0:0:0:0" is the Source Disk
        self.sdxx_SourceDisk = ""
        self.secSize_SourceDisk = 0

        self.testItem = CC_TEST_ITEM_NONE
        self.slotStatus = "SLOT_EMPTY"
        self.SlotDiskTestThread = CC_SlotDiskTest_Thread(self)

        self.smartDict_now = {'01':'0', '05':'0', 'A3':'0', 'C2':'0', 'C3':'0', 'C4':'0', 'C7':'0'}
        self.smartDict_old = {'01':'0', '05':'0', 'A3':'0', 'C2':'0', 'C3':'0', 'C4':'0', 'C7':'0'}

        self.color = {
            'red':"#ff0000",  # red
            'orange':"#ff8800",  # orange
            'yellow' : "#ffff00",  # yellow
            'yellow_green' : "#ccff00",  # yellow green
            'green' : "#00ff00",  # green
            'green-blue': "#00ff88",  # green-xx
            'blue': "#55ff00",  # blue
        }

        # " text-align: center; }}" \

        self.progressBarStyleSheetTemplate = \
            "QProgressBar {{" \
            " border: 1px solid black;" \
            " border-radius: 1px;" \
            " text-align: right; }}" \
        "QProgressBar::chunk:horizontal {{" \
            " background-color: {0};" \
            " width: 1px;" \
            " margin: 0px;}}"


        #self.setStyleSheet(self.progressBarStyleSheetTemplate.format(self.color[yellow_green]))

        self.frame = QtWidgets.QFrame(widget)
        self.frame.setGeometry(position)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame" + "slotnum")

        self.line_0 = QtWidgets.QFrame(self.frame)
        self.line_0.setGeometry(QtCore.QRect(0, 0, 160, 2))
        self.line_0.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_0.setObjectName("line_0")

        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 2, 700))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(159, 0, 2, 700))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 4, 40, 60))
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setStyleSheet("color:white;background:gray")
        self.lcdNumber.setProperty("value", slotnum)
        self.lcdNumber.setObjectName("lcdNumber")

        self.label_progress = QtWidgets.QLabel(self.frame)
        # self.label_progress.setGeometry(QtCore.QRect(51, 70, 60, 20))
        self.label_progress.setGeometry(QtCore.QRect(3, 66, 155, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_progress.setFont(font)
        self.label_progress.setStyleSheet("color:red;")
        self.label_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.label_progress.setFont(font)
        self.label_progress.setObjectName("label_progress")
        self.progressValue = 0
        #self.label_progress.setText("TH10: 10:0000 Dumping")
        self.label_progress.setText("")

        self.label_scsi_id = QtWidgets.QLabel(self.frame)
        self.label_scsi_id.setGeometry(QtCore.QRect(40, 78, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_scsi_id.setFont(font)
        self.label_scsi_id.setAutoFillBackground(False)
        self.label_scsi_id.setStyleSheet("color:#00C78C;")
        self.label_scsi_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_scsi_id.setObjectName("label_scsi_id")
        #self.label_scsi_id.setText("0:0:0:0")
        self.label_scsi_id.setText("-:-:-:-")

        self.label_sdx = QtWidgets.QLabel(self.frame)
        self.label_sdx.setGeometry(QtCore.QRect(40, 95, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_sdx.setFont(font)
        self.label_sdx.setAutoFillBackground(False)
        self.label_sdx.setStyleSheet("color:blue;")
        self.label_sdx.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sdx.setObjectName("label_sdx")
        self.label_sdx.setText("")

        self.label_disknameValue = QtWidgets.QLabel(self.frame)
        self.label_disknameValue.setGeometry(QtCore.QRect(1, 120, 158, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        # font.setFamily("Arial")
        font.setBold(True)
        self.label_disknameValue.setFont(font)
        self.label_disknameValue.setStyleSheet("color:blue;")
        self.label_disknameValue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disknameValue.setFont(font)
        self.label_disknameValue.setObjectName("label_disknameValue")
        #self.label_disknameValue.setText("Faspeed K6-120G12345")
        self.label_disknameValue.setText("")

        self.label_fwVersionValue = QtWidgets.QLabel(self.frame)
        self.label_fwVersionValue.setGeometry(QtCore.QRect(5, 138, 73, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        # font.setFamily("Arial")
        font.setBold(True)
        self.label_fwVersionValue.setFont(font)
        self.label_fwVersionValue.setStyleSheet("color:green;")
        self.label_fwVersionValue.setAlignment(QtCore.Qt.AlignRight)
        self.label_fwVersionValue.setFont(font)
        self.label_fwVersionValue.setObjectName("label_fwVersionValue")
        #self.label_fwVersionValue.setText("{}".format("Q0525A"))
        self.label_fwVersionValue.setText("")

        self.label_sizeValue = QtWidgets.QLabel(self.frame)
        self.label_sizeValue.setGeometry(QtCore.QRect(82, 138, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        font.setBold(True)
        self.label_sizeValue.setFont(font)
        self.label_sizeValue.setStyleSheet("color:blue;")
        self.label_sizeValue.setAlignment(QtCore.Qt.AlignLeft)
        self.label_sizeValue.setFont(font)
        self.label_sizeValue.setObjectName("label_sizeValue")
        #self.label_sizeValue.setText("{}GB".format("120"))
        self.label_sizeValue.setText("")

        self.label_snValue = QtWidgets.QLabel(self.frame)
        self.label_snValue.setGeometry(QtCore.QRect(2, 150, 156, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_snValue.setFont(font)
        self.label_snValue.setStyleSheet("color:blue;")
        self.label_snValue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_snValue.setFont(font)
        self.label_snValue.setObjectName("label_snValue")
        #self.label_snValue.setText("12345678900987654321")
        self.label_snValue.setText("")

        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 170, 160, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_CloneOnly = QtWidgets.QPushButton(self.frame)
        self.pushButton_CloneOnly.setFont(font)
        self.pushButton_CloneOnly.setGeometry(QtCore.QRect(4, 173, 75, 25))
        self.pushButton_CloneOnly.setObjectName("pushButton_CloneOnly")
        self.pushButton_CloneOnly.setText("Clone")

        self.pushButton_CompareOnly = QtWidgets.QPushButton(self.frame)
        self.pushButton_CompareOnly.setFont(font)
        self.pushButton_CompareOnly.setGeometry(QtCore.QRect(81, 173, 75, 25))
        self.pushButton_CompareOnly.setObjectName("pushButton_CompareOnly")
        self.pushButton_CompareOnly.setText("Compare")

        self.pushButton_CloneAndCompare = QtWidgets.QPushButton(self.frame)
        self.pushButton_CloneAndCompare.setFont(font)
        self.pushButton_CloneAndCompare.setGeometry(QtCore.QRect(4, 200, 152, 25))
        self.pushButton_CloneAndCompare.setObjectName("pushButton_CloneAndCompare")
        self.pushButton_CloneAndCompare.setText("Clone + Compare")

        self.line_41 = QtWidgets.QFrame(self.frame)
        self.line_41.setGeometry(QtCore.QRect(0, 227, 160, 2))
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")

        self.label_rwspeed = QtWidgets.QLabel(self.frame)
        self.label_rwspeed.setGeometry(QtCore.QRect(3, 229, 155, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Mono")
        font.setFamily("Arial")
        font.setBold(True)
        self.label_rwspeed.setFont(font)
        self.label_rwspeed.setStyleSheet("color:green;")
        self.label_rwspeed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rwspeed.setFont(font)
        self.label_rwspeed.setObjectName("label_progress")
        self.progressValue = 0
        self.label_rwspeed.setText("R/W[{}/{}]MB/s".format(self.writeSpeed, self.readSpeed))

        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(0, 245, 160, 2))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        # font.setBold(True)
        self.pushButton_DeleteDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_DeleteDisk.setFont(font)
        self.pushButton_DeleteDisk.setGeometry(QtCore.QRect(4, 247, 75, 22))
        self.pushButton_DeleteDisk.setObjectName("pushButton_DeleteDisk")
        self.pushButton_DeleteDisk.setText("删除硬盘")

        self.pushButton_ReflashDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_ReflashDisk.setFont(font)
        self.pushButton_ReflashDisk.setGeometry(QtCore.QRect(81, 247, 75, 22))
        self.pushButton_ReflashDisk.setObjectName("pushButton_ReflashDisk")
        self.pushButton_ReflashDisk.setText("手动刷新")

        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(0, 270, 160, 2))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.testFlag = "NOT_TEST"
        self.testCycleNow = 0
        self.testStartTime = 0
        self.progressBar = [0 for x in range(0, 2)]
        self.eachCycleUsedTime = [0 for x in range(0, 2)]
        self.label_TestUsedTime = [0 for x in range(0, 2)]
        self.label_TestResult = [0 for x in range(0, 2)]
        for i in range(0, 2):
            self.progressBar[i] = QtWidgets.QProgressBar(self.frame)
            self.progressBar[i].setGeometry(QtCore.QRect(3, 275 + i*100, 154, 97))
            self.progressBar[i].setProperty("value", 0)
            self.progressBar[i].setTextVisible(True)
            font = QtGui.QFont()
            font.setPointSize(10)
            # font.setFamily("Arial")
            font.setBold(True)
            self.progressBar[i].setFont(font)
            self.progressBar[i].setStyleSheet(self.progressBarStyleSheetTemplate.format(self.color['green']))
            self.progressBar[i].setOrientation(QtCore.Qt.Horizontal)
            self.progressBar[i].setTextDirection(QtWidgets.QProgressBar.TopToBottom)
            self.progressBar[i].setObjectName("progressBar{}".format(i))
            #self.progressBar[i].setValue(100)

            self.eachCycleUsedTime[i] = 0

            self.label_TestUsedTime[i] = QtWidgets.QLabel(self.frame)
            self.label_TestUsedTime[i].setGeometry(QtCore.QRect(10, 277 + i*100, 50, 18))
            font = QtGui.QFont()
            font.setPointSize(10)
            # font.setFamily("Arial")
            font.setFamily("Mono")
            # font.setBold(True)
            self.label_TestUsedTime[i].setFont(font)
            self.label_TestUsedTime[i].setStyleSheet("color:black;")
            self.label_TestUsedTime[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_TestUsedTime[i].setFont(font)
            self.label_TestUsedTime[i].setObjectName("label_TestUsedTime{}".format(i))
            #self.label_TestUsedTime[i].setText("300m25s")
            self.label_TestUsedTime[i].setText("")

            self.label_TestResult[i] = QtWidgets.QLabel(self.frame)
            self.label_TestResult[i].setGeometry(QtCore.QRect(65, 277 + i*100, 91, 93))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Mono")
            #font.setFamily("Mono")
            #font.setBold(True)
            self.label_TestResult[i].setFont(font)
            self.label_TestResult[i].setStyleSheet("color:black;")
            self.label_TestResult[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_TestResult[i].setFont(font)
            self.label_TestResult[i].setObjectName("label_TestResult{}".format(i))
            #self.label_TestResult[i].setText("PS[05]68")
            self.label_TestResult[i].setText("")

        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(0, 477, 160, 2))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.label_smartName = [0 for x in range(0, 7)]
        self.label_smartValue = [0 for x in range(0, 7)]
        for i in range(0,7):
            self.label_smartName[i] = QtWidgets.QLabel(self.frame)
            self.label_smartName[i].setGeometry(QtCore.QRect(5, 480 + i*20, 80, 16))
            font = QtGui.QFont()
            font.setPointSize(10)
            #font.setFamily("Arial")
            font.setFamily("Mono")
            #font.setBold(True)
            self.label_smartName[i].setFont(font)
            self.label_smartName[i].setStyleSheet("color:black;")
            self.label_smartName[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_smartName[i].setFont(font)
            self.label_smartName[i].setObjectName("label_smartName{}".format(i))
            self.label_smartName[i].setText("")
            #self.label_smartName[i].setText("{:02X}:".format(i))


            self.label_smartValue[i] = QtWidgets.QLabel(self.frame)
            self.label_smartValue[i].setGeometry(QtCore.QRect(88, 481 + i*20, 67, 16))
            font = QtGui.QFont()
            font.setPointSize(10)
            # font.setFamily("Arial")
            font.setFamily("Mono")
            font.setBold(True)
            self.label_smartValue[i].setFont(font)
            self.label_smartValue[i].setStyleSheet("color:blue;")
            self.label_smartValue[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_smartValue[i].setFont(font)
            self.label_smartValue[i].setObjectName("label_smartValue{}".format(i))
            self.label_smartValue[i].setText("")
            #self.label_smartValue[i].setText("{:02X}:".format(i))

        self.testDiskSn = ""
        self.nowDiskSn = ""

        # 创建定时器
        self.timer_testProgress = QtCore.QTimer(self.pp)
        self.__attach_events()

    def __attach_events(self):
        self.sin.connect(self.updateDiskTestResult)

        self.pushButton_CloneOnly.clicked.connect(lambda: self.On_CCtest(self.pushButton_CloneOnly, CC_TEST_ITEM_CLONE))
        self.pushButton_CompareOnly.clicked.connect(lambda: self.On_CCtest(self.pushButton_CompareOnly, CC_TEST_ITEM_COMPARE))
        self.pushButton_CloneAndCompare.clicked.connect(lambda: self.On_CCtest(self.pushButton_CloneAndCompare, CC_TEST_ITEM_CLONECOMPARE))

        self.timer_testProgress.timeout.connect(self.OnTestProgressTimer)

        self.pushButton_DeleteDisk.clicked.connect(self.On_DeleteDisk)
        self.pushButton_ReflashDisk.clicked.connect(self.On_ReflashDisk)

    def On_DeleteDisk(self):
        self.SlotDeleteDisk()

    def On_ReflashDisk(self):
        self.SlotIDtoScsiID()

    def SetAllTestButtonDisable(self):
        self.pushButton_CloneOnly.setEnabled(False)
        self.pushButton_CompareOnly.setEnabled(False)
        self.pushButton_CloneAndCompare.setEnabled(False)
        self.pushButton_CloneOnly.setStyleSheet("color:white; background:gray")
        self.pushButton_CompareOnly.setStyleSheet("color:white; background:gray")
        self.pushButton_CloneAndCompare.setStyleSheet("color:white; background:gray")

    def SetAllTestButtonEnable(self):
        self.pushButton_CloneOnly.setEnabled(True)
        self.pushButton_CompareOnly.setEnabled(True)
        self.pushButton_CloneAndCompare.setEnabled(True)
        self.pushButton_CloneOnly.setStyleSheet("color:black;")
        self.pushButton_CompareOnly.setStyleSheet("color:black;")
        self.pushButton_CloneAndCompare.setStyleSheet("color:black;")

    def On_CCtest(self, button, testName):
        if self.testItem == CC_TEST_ITEM_NONE:
            self.InitTest()

            if self.sdxx != "":
                self.SetAllTestButtonDisable()
                button.setStyleSheet("color:white;""background:purple")
                self.testItem = testName
                self.testDiskSn = self.nowDiskSn
                self.testCycleNow = 0
                self.testStartTime = 0
                self.writeSpeed = "0"
                self.readSpeed = "0"
                for i in range(0, 2):
                    self.progressBar[i].setValue(0)
                    self.eachCycleUsedTime[i] = 0
                    self.label_TestUsedTime[i].setText("")
                    self.label_TestResult[i].setText("")
                    self.label_TestResult[i].setStyleSheet("")

                self.testFlag = "RUNNING"
                shownum = sid_to_slotnum[self.scsi_id]
                self.pp.STB_LED_PointFlashCtl(shownum, 1)
                self.GetSourceDiskInfo()
                self.SlotDiskTestThread.start()
                self.timer_testProgress.start(1000)

            else:
                for i in range(0, 2):
                    self.progressBar[i].setValue(0)
                    self.eachCycleUsedTime[i] = 0
                    self.label_TestUsedTime[i].setText("")
                    self.label_TestResult[i].setText("")
                    self.label_TestResult[i].setStyleSheet("")
                shownum = sid_to_slotnum[self.scsi_id]
                self.pp.STB_LED_NumFlashCtl(shownum, 0)
                self.pp.STB_LED_PointFlashCtl(shownum, 0)
                self.pp.STB_LED_Show(shownum, 20)

    def OnTestProgressTimer(self):
        #print("in OnTestProgressTimer")
        #print("{} self.testFlag = {}".format(self.sdxx, self.testFlag))
        if self.testFlag == "RUNNING":
            try:
                f = os.popen('cc_show -c {}'.format(diskid[self.sdxx]))
                rw = f.readlines()

                rws = rw[0].replace('\n', '').strip()
                rwlist = rws.split(' ')
                #print("{} rwlist = {}".format(self.sdxx, rwlist))
            except:
                pass

            try:
                self.progressValue = rwlist[2]
                #print("{} self.progressValue = {} - {}".format(self.sdxx, self.progressValue, int(self.progressValue)))
                if rwlist[1] == "Cloning":
                    self.label_progress.setText("Cloning: {:0.4f}".format(float(self.progressValue) / 100))
                    self.label_progress.setStyleSheet("color:red;")
                    self.progressBar[self.testCycleNow].setValue(int(float(self.progressValue)))
                    self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format('#00C957'))
                elif rwlist[1] == "Comparing":
                    self.label_progress.setText("Comparing: {:0.4f}".format(float(self.progressValue) / 100))
                    self.label_progress.setStyleSheet("color:green;")
                    self.progressBar[self.testCycleNow].setValue(int(float(self.progressValue)))
                    self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format('#00FF7F'))

                if rwlist[1] == "Cloning":
                    self.writeSpeed = rwlist[3].replace('MB/s','')
                elif rwlist[1] == "Comparing":
                    self.readSpeed = rwlist[3].replace('MB/s','')

                self.label_rwspeed.setText("R/W[{}/{}]MB/s".format(self.readSpeed, self.writeSpeed))

                now_time = time.time()
                self.label_TestUsedTime[self.testCycleNow].setText("{}m{}s".format(int((now_time - self.testStartTime)/60), int((now_time - self.testStartTime)%60)))
            except:
                pass

        #print("{} self.testFlag = {}".format(self.sdxx, self.testFlag))
        if self.testFlag == "FINISH":
            self.timer_testProgress.stop()
            self.SlotDiskTestThread.__del__()
            self.SetAllTestButtonEnable()
            self.testItem = CC_TEST_ITEM_NONE
            shownum = sid_to_slotnum[self.scsi_id]
            self.pp.STB_LED_PointFlashCtl(shownum, 0)
        else:
            self.timer_testProgress.start(500)

    def updateDiskTestResult(self):
        print("in updateDiskTestResult")

        self.progressValue = 100.00
        self.label_progress.setText("{:0.2f}".format(float(self.progressValue) / 100))

        self.progressBar[diskid[self.sdxx]].setValue(int(self.progressValue))

        self.timer_testProgress.stop()

    def GetSmartInfo(self, sdxx):

        ID01_raw_read_error_rate       = 1
        ID05_reallocated_sectors_count = 5
        ID09_power_on_hours            = 9
        ID0C_power_cycle_count         = 12
        IDA3_original_bad_count        = 163
        IDA7_average_erase_count       = 167
        IDC2_temperature               = 194
        IDC3_read_retry                = 195
        IDC4_reallocation_event_count  = 196
        IDC7_ultraDMA_CRC_error_count  = 199
        IDF1_total_host_written        = 241
        IDF2_total_host_read           = 242

        small = []
        sml = []

        try:
            f = os.popen("smartctl -i /dev/{} | grep 'Firmware'".format(sdxx))
            sm = f.readlines()
            ver = sm[0].replace('Firmware Version:', '').replace('\n', '').strip()
            self.label_fwVersionValue.setText(ver)

            f = os.popen("smartctl -i /dev/{} | grep 'Device Model:'".format(sdxx))
            sm = f.readlines()
            name = sm[0].replace('Device Model:', '').replace('\n', '').strip()
            self.label_disknameValue.setText(name)

            f = os.popen("smartctl -s on -A /dev/{} | grep 0x0".format(sdxx))
            sm = f.readlines()
            for i in sm:
                smll = []
                sml = i.replace('\n', '').strip()
                sm_1space = sml.replace('   ', ' ').replace('   ', ' ').replace('  ', ' ').replace('  ', ' ')
                smlist = sm_1space.split(' ')

                smll.append(smlist[0])
                smll.append(smlist[1])
                smll.append(smlist[9])

                small.append(smll)

            # 读到结果为空，说明读取samrt失败，可能原因是 WE，RE，DL等原因，此种情况，不更新smart信息
            if len(sm) != 0:

                n = 0
                for (id, name, value) in small:
                    if int(id) == ID01_raw_read_error_rate:
                        self.label_smartName[n].setText("{:02X}:读错误率".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) != 0:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['01'] = value

                    elif int(id) == ID05_reallocated_sectors_count:
                        self.label_smartName[n].setText("{:02X}:新增坏块".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) != 0:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['05'] = value

                    elif int(id) == IDA3_original_bad_count:
                        self.label_smartName[n].setText("{:02X}:原始坏块".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['A3'] = int(value)

                    elif int(id) == IDC2_temperature:
                        self.label_smartName[n].setText("{:02X}:主控温度".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) > 40:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['C2'] = value

                    elif int(id) == IDC3_read_retry:
                        self.label_smartName[n].setText("{:02X}:重读次数".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) != 0:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['C3'] = value

                    elif int(id) == IDC4_reallocation_event_count:
                        self.label_smartName[n].setText("{:02X}:读取失败".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) != 0:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['C4'] = value

                    elif int(id) == IDC7_ultraDMA_CRC_error_count:
                        self.label_smartName[n].setText("{:02X}:链路重传".format(int(id)))
                        self.label_smartName[n].setStyleSheet("color:black;")
                        self.label_smartValue[n].setText("{}".format(value))
                        if int(value) != 0:
                            self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                        else:
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                        n = n + 1
                        self.smartDict_now['C7'] = value

                # 清空没有用到的ID内容
                for i in range(n, 7):
                    self.label_smartName[i].setText("")
                    self.label_smartValue[i].setText("")
        except:
            self.smartDict_now['01'] = '*'
            self.smartDict_now['05'] = '*'
            self.smartDict_now['A3'] = '*'
            self.smartDict_now['C2'] = '*'
            self.smartDict_now['C3'] = '*'
            self.smartDict_now['C4'] = '*'
            self.smartDict_now['C7'] = '*'

    def UpdateSmartOld(self):
        self.smartDict_old['01'] = self.smartDict_now['01']
        self.smartDict_old['05'] = self.smartDict_now['05']
        self.smartDict_old['A3'] = self.smartDict_now['A3']
        self.smartDict_old['C2'] = self.smartDict_now['C2']
        self.smartDict_old['C3'] = self.smartDict_now['C3']
        self.smartDict_old['C4'] = self.smartDict_now['C4']
        self.smartDict_old['C7'] = self.smartDict_now['C7']

    def InitTest(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                # print("[{}] {} {} {} {} {}".format(self.slotnum, scsiid, sdxx, size_GB, deviceName, sn))
                if self.scsi_id == scsiid:
                    self.label_scsi_id.setText("{}".format(scsiid))
                    self.label_sdx.setText("{}".format(sdxx))
                    #self.label_disknameValue.setText(deviceName)
                    self.label_snValue.setText(sn)

                    self.label_sizeValue.setText(size_GB)
                    try:
                        os.system("echo 2 > /sys/block/{}/device/eh_timeout".format(sdxx))
                        os.system("echo 2 > /sys/block/{}/device/timeout".format(sdxx))
                        os.system("echo 1 > /sys/block/{}/device/queue_depth".format(sdxx))
                    except:
                        pass

                    self.lcdNumber.setStyleSheet("color:red;background:#888888")

                    self.sdxx = sdxx
                    self.secSize = secSize
                    self.nowDiskSn = sn

                    self.FirstSmartResultCtl(sdxx)
                    self.UpdateSmartOld()

                    break

            if n == (len(self.disklist) - 1):
                self.lcdNumber.setStyleSheet("color:white;background:#DDDDDD")
                self.label_scsi_id.setText("-:-:-:-")
                self.label_sdx.setText("")
                self.label_disknameValue.setText("")
                self.label_snValue.setText("")
                self.label_sizeValue.setText("")
                self.label_fwVersionValue.setText("")
                self.sdxx = ""
                self.secSize = ""
                self.nowDiskSn = ""
                for i in range(0, 7):
                    self.label_smartName[i].setText("")
                    self.label_smartValue[i].setText("")
                    self.label_smartValue[i].setStyleSheet("color:blue;")

        except:
            pass

    def SlotIDtoScsiID(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                # print("[{}] {} {} {} {} {}".format(self.slotnum, scsiid, sdxx, size_GB, deviceName, sn))
                if self.scsi_id == scsiid:
                    self.label_scsi_id.setText("{}".format(scsiid))
                    self.label_sdx.setText("{}".format(sdxx))
                    #self.label_disknameValue.setText(deviceName)
                    self.label_snValue.setText(sn)

                    self.label_sizeValue.setText(size_GB)
                    try:
                        os.system("echo 2 > /sys/block/{}/device/eh_timeout".format(sdxx))
                        os.system("echo 2 > /sys/block/{}/device/timeout".format(sdxx))
                        os.system("echo 1 > /sys/block/{}/device/queue_depth".format(sdxx))
                    except:
                        pass

                    self.lcdNumber.setStyleSheet("color:red;background:#888888")
                    self.GetSmartInfo(sdxx)
                    self.UpdateSmartOld()
                    self.sdxx = sdxx
                    self.secSize = secSize
                    self.nowDiskSn = sn

                    break

            if n == (len(self.disklist) - 1):
                #self.slotStatus = SLOT_EMPTY
                self.lcdNumber.setStyleSheet("color:white;background:#DDDDDD")
                self.label_scsi_id.setText("-:-:-:-")
                self.label_sdx.setText("")
                self.label_disknameValue.setText("")
                self.label_snValue.setText("")
                self.label_sizeValue.setText("")
                self.label_fwVersionValue.setText("")
                for i in range(0, 7):
                    self.label_smartName[i].setText("")
                    self.label_smartValue[i].setText("")
                    self.label_smartValue[i].setStyleSheet("color:blue;")

                '''
                #没有盘，不要做LED控制
                if self.testItem == CC_TEST_ITEM_NONE and self.sdxx == "":
                    shownum = sid_to_slotnum[self.scsi_id]
                    self.pp.STB_LED_NumFlashCtl(shownum, 0)
                    self.pp.STB_LED_PointFlashCtl(shownum, 0)
                    #self.pp.STB_LED_Show(shownum, 20)
                '''
            # 手动刷新，不要对LED灯进行控制，第一次手动刷新，初始化LED状态
            if self.testItem == CC_TEST_ITEM_NONE and self.slotStatus == SLOT_EMPTY:
                self.slotStatus = SLOT_INSERT
                shownum = sid_to_slotnum[self.scsi_id]
                self.pp.STB_LED_NumFlashCtl(shownum, 0)
                self.pp.STB_LED_PointFlashCtl(shownum, 0)
                self.pp.STB_LED_Show(shownum, shownum)

        except:
            print("{} SlotIDtoScsiID except !!!!!!".format(self.sdxx))
            pass

    def GetSourceDiskInfo(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                # print("[{}] {} {} {} {} {}".format(self.slotnum, scsiid, sdxx, size_GB, deviceName, sn))
                if scsiid == "0:0:0:0":
                    self.sdxx_SourceDisk = sdxx
                    self.secSize_SourceDisk = secSize
                    break

            if n == (len(self.disklist) - 1):
                self.sdxx_SourceDisk = ""
                self.secSize_SourceDisk = 0

        except:
            print("{} GetSourceDiskInfo except !!!!!!".format(self.sdxx))
            pass

    def SlotDeleteDisk(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                if self.scsi_id == scsiid:
                    os.system("echo 1 > /sys/block/{}/device/delete".format(sdxx))
        except:
            print("{} SlotDeleteDisk except !!!!!!".format(self.sdxx))
            pass

    def SlotDeleteSmart(self):
        for i in range(0,7):
            self.label_smartName[i].setStyleSheet("color:gray;")
            #self.label_smartValue[i].setText("")
            #self.label_smartName[i].setText("")

    def TestReturn(self, ret):
        self.GetSmartInfo(self.sdxx)

        shownum = sid_to_slotnum[self.scsi_id]
        ret = ret/0x100
        if int(ret) == CC_TEST_PASS:
           resultText = "PS"
           barColor = "#00FF7F"
        elif int(ret) == CC_ERROR_RE_READ_DATA:
            resultText = "RE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == CC_ERROR_CE_COMPARE_DATA:
            resultText = "CE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == CC_ERROR_WE_WIRTE_DATA:
            resultText = "WE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == CC_ERROR_SK_SEEK:
            resultText = "AE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == CC_ERROR_DS_DATASYNC:
            resultText = "DS"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == CC_ERROR_DC_DISCARD_CACHE:
            resultText = "DC"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == CC_ERROR_NM_NMEM:
            resultText = "NM"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == CC_ERROR_DL_NONE_DISK:
            resultText = "DL"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == CC_ERROR_US_UNSORTED:
            resultText = "US"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == CC_ERROR_CP_CAP_LESS:
            resultText = "CP"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == CC_ERROR_UA_UNAUTHORIZATION:
            resultText = "UA"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == CC_ERROR_OV_RUN_TIME_COUNT_OVERFLOW:
            resultText = "OV"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        else:
            resultText = "UK"
            barColor = 'red'
            print("{} ret = {}".format(self.sdxx, ret))
            self.pp.STB_LED_NumFlashCtl(shownum, 1)

        if self.smartDict_now['01'] != self.smartDict_old['01']:
            resultText = resultText + "(01){}".format(self.smartDict_now['01'])
            if barColor != 'red':
                barColor = 'red'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['05'] != self.smartDict_old['05']:
            resultText = resultText + "(05){}".format(self.smartDict_now['05'])
            if barColor != 'red':
                barColor = 'red'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C4'] != self.smartDict_now['C4']:
            resultText = resultText + "(C4){}".format(self.smartDict_now['C4'])
            if barColor != 'red':
                barColor = 'red'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C3'] != self.smartDict_old['C3']:
            resultText = resultText + "(C3){}".format(self.smartDict_now['C3'])
            if barColor != 'red':
                barColor = 'yellow'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C7'] != self.smartDict_old['C7']:
            resultText = resultText + "(C7){}".format(self.smartDict_now['C7'])
            if barColor != 'red':
                barColor = 'yellow'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C2'] > "40":
            resultText = resultText + "(C2){}".format(self.smartDict_now['C2'])
            if barColor != 'red':
                barColor = 'yellow'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        else:
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)

        if self.smartDict_now['01'] != "0" or self.smartDict_now['05'] != "0" or self.smartDict_now['C4'] != "0":
            #print("self.smartDict_now['01'] = {}".format(self.smartDict_now['01']))
            #print("self.smartDict_now['05'] = {}".format(self.smartDict_now['05']))
            #print("self.smartDict_now['C4'] = {}".format(self.smartDict_now['C4']))
            self.pp.STB_LED_NumFlashCtl(shownum, 1)

        self.UpdateSmartOld()

    def FirstSmartResultCtl(self, sdxx):
        # 恢复 LED 显示状态
        shownum = sid_to_slotnum[self.scsi_id]
        self.pp.STB_LED_NumFlashCtl(shownum, 0)
        self.pp.STB_LED_Show(shownum, shownum)
        #self.pp.STB_k()
        #self.pp.STB_K()
        #self.pp.STB_GetRuntime()

        # 初始化新测试硬盘状态
        self.smartDict_now['01'] = "0"
        self.smartDict_now['05'] = "0"
        self.smartDict_now['A3'] = "0"
        self.smartDict_now['C2'] = "0"
        self.smartDict_now['C3'] = "0"
        self.smartDict_now['C4'] = "0"
        self.smartDict_now['C7'] = "0"
        self.UpdateSmartOld()
        self.GetSmartInfo(sdxx)

        if self.smartDict_now['01'] != "0" or self.smartDict_now['05'] != "0" or self.smartDict_now['C4'] != "0":
            #print("self.smartDict_now['01'] = {}".format(self.smartDict_now['01']))
            #print("self.smartDict_now['05'] = {}".format(self.smartDict_now['05']))
            #print("self.smartDict_now['C4'] = {}".format(self.smartDict_now['C4']))
            self.pp.STB_LED_NumFlashCtl(shownum, 1)


class CC_SlotDiskTest_Thread(QtCore.QThread):

    def __init__(self, parent):
        self.sin = parent.sin
        self.mutex = parent.mutex
        super(CC_SlotDiskTest_Thread, self).__init__()
        self.working = True
        self.pp = parent

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        try:
            self.working = True
        except:
            pass

        while self.working == True:
            #if self.serial.isOpen():
            if True:
                try:
                    if self.pp.testItem == CC_TEST_ITEM_CLONE:
                        self.CloneOnly()

                    if self.pp.testItem == CC_TEST_ITEM_COMPARE:
                        self.CompareOnly()

                    if self.pp.testItem == CC_TEST_ITEM_CLONECOMPARE:
                        self.CloneAndCompare()

                    time.sleep(3)
                    self.working = False
                except:
                    print("{}-{} running thread except ！！！！！！！！！！！".format(self.pp.sdxx, self.pp.testItem))
                    break
                    #pass

    def CloneOnly(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        if self.pp.scsi_id != "0:0:0:0":
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                #print("stb_dd if=/dev/{} of=/dev/{} bs=1M count={} oflag=direct devid={}".format(
                #    self.pp.sdxx_SourceDisk, self.pp.sdxx, (int(self.pp.secSize / 2048) + 1), diskid[self.pp.sdxx]))
                ret = os.system("stb_dd if=/dev/{} of=/dev/{} bs=1M count={} oflag=direct devid={}".format(
                    self.pp.sdxx_SourceDisk, self.pp.sdxx, (int(self.pp.secSize / 2048) + 1), diskid[self.pp.sdxx]))
            else:
                ret = CC_ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(5)

            self.pp.TestReturn(ret)

            self.pp.testFlag = "FINISH"
        else:
            ret = CC_TEST_PASS
            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(1)
            self.pp.TestReturn(ret)
            self.pp.testFlag = "FINISH"

    def CompareOnly(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 1

        if self.pp.scsi_id != "0:0:0:0":
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                #print("stb_cmp -s /dev/{} /dev/{}".format(self.pp.sdxx_SourceDisk, self.pp.sdxx))
                ret = os.system("stb_cmp -s /dev/{} /dev/{}".format(self.pp.sdxx_SourceDisk, self.pp.sdxx))
            else:
                ret = CC_ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(5)

            self.pp.TestReturn(ret)

            self.pp.testFlag = "FINISH"
        else:
            ret = CC_TEST_PASS
            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(1)
            self.pp.TestReturn(ret)
            self.pp.testFlag = "FINISH"

    def CloneAndCompare(self):

        # Clone
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        if self.pp.scsi_id != "0:0:0:0":
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                #print("stb_dd if=/dev/{} of=/dev/{} bs=1M count={} oflag=direct devid={}".format(
                #    self.pp.sdxx_SourceDisk, self.pp.sdxx, (int(self.pp.secSize / 2048) + 1), diskid[self.pp.sdxx]))
                ret = os.system("stb_dd if=/dev/{} of=/dev/{} bs=1M count={} oflag=direct devid={}".format(
                    self.pp.sdxx_SourceDisk, self.pp.sdxx, (int(self.pp.secSize / 2048) + 1), diskid[self.pp.sdxx]))
            else:
                ret = CC_ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)

        else:
            ret = CC_TEST_PASS
            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(1)
            self.pp.TestReturn(ret)

        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # Compare
        startTime = time.time()
        self.pp.testStartTime = startTime

        if self.pp.scsi_id != "0:0:0:0":
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                #print("stb_cmp -s /dev/{} /dev/{}".format(self.pp.sdxx_SourceDisk, self.pp.sdxx))
                ret = os.system("stb_cmp -s /dev/{} /dev/{}".format(self.pp.sdxx_SourceDisk, self.pp.sdxx))
            else:
                ret = CC_ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[1] = finishTime - startTime
            time.sleep(5)

            self.pp.TestReturn(ret)

            self.pp.testFlag = "FINISH"
        else:
            ret = CC_TEST_PASS
            finishTime = time.time()
            self.pp.eachCycleUsedTime[1] = finishTime - startTime
            time.sleep(1)
            self.pp.TestReturn(ret)
            self.pp.testFlag = "FINISH"

# tab_5 ################################################################################################################

TEST_ITEM_RO10 = 'RO10'
TEST_ITEM_RO30 = 'RO30'
TEST_ITEM_WO10 = 'WO10'
TEST_ITEM_WO30 = 'WO30'

TEST_ITEM_TH15 = 'TH15'
TEST_ITEM_TH20 = 'TH20'
TEST_ITEM_TH30 = 'TH30'
TEST_ITEM_WO1r = 'WO1r'


class DiskTestPlus_Header(object):
    def __init__(self, parent, widget, position):

        self.parent = parent

        self.frame = QtWidgets.QFrame(widget)
        self.frame.setGeometry(position)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("HeadControl")

        '''
        self.pushButton_initTest = QtWidgets.QPushButton(self.frame)
        self.pushButton_initTest.setGeometry(QtCore.QRect(718, 3, 80, 23))
        self.pushButton_initTest.setObjectName("pushButton_initTest")
        self.pushButton_initTest.setText("初始化显示")
        '''

        self.pushButton_deleteDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_deleteDisk.setGeometry(QtCore.QRect(802, 3, 77, 23))
        self.pushButton_deleteDisk.setObjectName("pushButton_deleteDisk")
        self.pushButton_deleteDisk.setText("删除硬盘")

        self.pushButton_manualUpdate = QtWidgets.QPushButton(self.frame)
        self.pushButton_manualUpdate.setGeometry(QtCore.QRect(881, 3, 77, 23))
        self.pushButton_manualUpdate.setObjectName("pushButton_manualUpdate")
        self.pushButton_manualUpdate.setText("手动刷新")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)

        self.pushButton_testRO10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testRO10.setFont(font)
        self.pushButton_testRO10.setGeometry(QtCore.QRect(3, 3, 75, 23))
        self.pushButton_testRO10.setObjectName("pushButton_testRO10")
        self.pushButton_testRO10.setText("RO10测试")

        self.pushButton_testRO30 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testRO30.setFont(font)
        self.pushButton_testRO30.setGeometry(QtCore.QRect(83, 3, 75, 23))
        self.pushButton_testRO30.setObjectName("pushButton_testRO30")
        self.pushButton_testRO30.setText("RO30测试")

        self.pushButton_testWO10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testWO10.setFont(font)
        self.pushButton_testWO10.setGeometry(QtCore.QRect(163, 3, 75, 23))
        self.pushButton_testWO10.setObjectName("pushButton_testWO10")
        self.pushButton_testWO10.setText("WO10测试")

        self.pushButton_testWO30 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testWO30.setFont(font)
        self.pushButton_testWO30.setGeometry(QtCore.QRect(243, 3, 75, 23))
        self.pushButton_testWO30.setObjectName("pushButton_testWO30")
        self.pushButton_testWO30.setText("WO30测试")

        self.pushButton_testTH15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testTH15.setFont(font)
        self.pushButton_testTH15.setGeometry(QtCore.QRect(323, 3, 75, 23))
        self.pushButton_testTH15.setObjectName("pushButton_testTH15")
        self.pushButton_testTH15.setText("TH15测试")

        self.pushButton_testTH20 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testTH20.setFont(font)
        self.pushButton_testTH20.setGeometry(QtCore.QRect(403, 3, 75, 23))
        self.pushButton_testTH20.setObjectName("pushButton_testTH20")
        self.pushButton_testTH20.setText("TH20测试")

        self.pushButton_testTH30 = QtWidgets.QPushButton(self.frame)
        self.pushButton_testTH30.setFont(font)
        self.pushButton_testTH30.setGeometry(QtCore.QRect(483, 3, 75, 23))
        self.pushButton_testTH30.setObjectName("pushButton_testTH30")
        self.pushButton_testTH30.setText("TH30测试")

        self.pushButton_testWO1r = QtWidgets.QPushButton(self.frame)
        self.pushButton_testWO1r.setFont(font)
        self.pushButton_testWO1r.setGeometry(QtCore.QRect(563, 3, 75, 23))
        self.pushButton_testWO1r.setObjectName("pushButton_testWO1r")
        self.pushButton_testWO1r.setText("WO1r测试")

        self.checkBox_Heating = QtWidgets.QCheckBox(self.frame)
        self.checkBox_Heating.setGeometry(QtCore.QRect(650, 3, 80, 23))
        self.checkBox_Heating.setObjectName("checkBox_Heating")
        self.checkBox_Heating.setText("开启加热")
        self.checkBox_Heating.setStyleSheet("color:black;")

        self.label_heatPercent = QtWidgets.QLabel(self.frame)
        self.label_heatPercent.setGeometry(QtCore.QRect(725, 2, 60, 10))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setFamily("Arial")
        #font.setBold(True)
        self.label_heatPercent.setFont(font)
        self.label_heatPercent.setAutoFillBackground(False)
        #self.label_heatPercent.setStyleSheet("color:blue;")
        self.label_heatPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.label_heatPercent.setObjectName("label_heatPercent")
        self.label_heatPercent.setText("100%")

        self.horizontalSlider_heatPercent = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_heatPercent.setGeometry(QtCore.QRect(725, 11, 60, 15))
        self.horizontalSlider_heatPercent.setMinimum(0)
        self.horizontalSlider_heatPercent.setMaximum(100)
        self.horizontalSlider_heatPercent.setProperty("value", 100)
        self.horizontalSlider_heatPercent.setTickInterval(1)
        self.horizontalSlider_heatPercent.setSingleStep(1)
        self.horizontalSlider_heatPercent.setPageStep(1)
        self.horizontalSlider_heatPercent.setInvertedAppearance(False)
        self.horizontalSlider_heatPercent.setInvertedControls(True)
        self.horizontalSlider_heatPercent.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_heatPercent.setObjectName("horizontalSlider_heatPercent")

        # 创建定时器
        self.timer_autoUpdate = QtCore.QTimer(self.parent)

        self.__attach_events()

    def __attach_events(self):
        self.pushButton_manualUpdate.clicked.connect(self.On_manualUpdate)
        self.pushButton_deleteDisk.clicked.connect(self.On_deleteDisk)
        #self.checkBox_autoUpdate.stateChanged.connect(self.On_autoUpdate)
        #self.checkBox_Heating.stateChanged.connect(self.On_Heating)
        #self.horizontalSlider_heatPercent.valueChanged.connect(self.On_OnHeatingSlider)
        self.timer_autoUpdate.timeout.connect(self.OnAutoUpdateTimer)

        self.pushButton_testRO10.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_RO10))
        self.pushButton_testRO30.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_RO30))
        self.pushButton_testWO10.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_WO10))
        self.pushButton_testWO30.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_WO30))
        self.pushButton_testTH15.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_TH15))
        self.pushButton_testTH20.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_TH20))
        self.pushButton_testTH30.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_TH30))
        self.pushButton_testWO1r.clicked.connect(lambda:self.On_testAllTHxx(TEST_ITEM_WO1r))

    def On_manualUpdate(self):
        #print("in On_manualUpdate")
        for i in (1, 2, 3, 4, 5, 6):
            self.parent.tab5_frame[i].SlotIDtoScsiID()

    def On_deleteDisk(self):
        #print("in On_deleteDisk")
        for i in (1, 2, 3, 4, 5, 6):
            self.parent.tab5_frame[i].SlotDeleteDisk()

    def On_OnHeatingSlider(self):
        if 1:
            self.label_heatPercent.setText("{}%".format(self.horizontalSlider_heatPercent.value()))
            self.On_Heating()
        else:
            #print("in On_OnTimeSlider")
            #print(self.horizontalSlider_OnTime.value())
            pass

    def On_Heating(self):
        # print("in On_Heating")
        if self.checkBox_Heating.isChecked():
            self.parent.STB_Heating(self.horizontalSlider_heatPercent.value())
        else:
            self.parent.STB_Heating(0)

    def OnAutoUpdateTimer(self):
        #print("in OnAutoUpdateTimer")
        self.On_manualUpdate()
        self.timer_autoUpdate.start(500)

    def On_testAllTHxx(self, testItem):
        self.parent.STB_RuntimePlus()
        self.parent.STB_GetRuntime()
        for i in (1, 2, 3, 4, 5, 6):
            if testItem == TEST_ITEM_RO10:
                self.parent.tab5_frame[i].On_THxx(self.parent.tab5_frame[i].pushButton_RO10, TEST_ITEM_RO10)
            if testItem == TEST_ITEM_RO30:
                self.parent.tab5_frame[i].On_THxx(self.parent.tab5_frame[i].pushButton_RO30, TEST_ITEM_RO30)
            if testItem == TEST_ITEM_WO10:
                self.parent.tab5_frame[i].On_THxx(self.parent.tab5_frame[i].pushButton_WO10, TEST_ITEM_WO10)
            if testItem == TEST_ITEM_WO30:
                self.parent.tab5_frame[i].On_THxx(self.parent.tab5_frame[i].pushButton_WO30, TEST_ITEM_WO30)
            if testItem == TEST_ITEM_TH15:
                self.parent.tab5_frame[i].On_THxx(self.parent.tab5_frame[i].pushButton_TH15, TEST_ITEM_TH15)
            if testItem == TEST_ITEM_TH20:
                self.parent.tab5_frame[i].On_THxx(self.parent.tab5_frame[i].pushButton_TH20, TEST_ITEM_TH20)
            if testItem == TEST_ITEM_TH30:
                self.parent.tab5_frame[i].On_THxx(self.parent.tab5_frame[i].pushButton_TH30, TEST_ITEM_TH30)
            if testItem == TEST_ITEM_WO1r:
                self.parent.tab5_frame[i].On_THxx(self.parent.tab5_frame[i].pushButton_WO1r, TEST_ITEM_WO1r)

class SlotDiskTestPlus(object):
    def __init__(self, parent, widget, position, slotnum):
        self.slotnum = slotnum
        self.pp = parent
        self.serail = parent.serial
        self.mutex = parent.mutex
        self.scsi_id = "{}:0:0:0".format(slotnum - 1)
        self.sdxx = ""
        self.secSize = 0
        self.sin = widget.sin[slotnum]
        self.disklist = []
        self.writeSpeed = "0.0"
        self.readSpeed = "0.0"

        self.testItem = TEST_ITEM_NONE
        self.slotStatus = "SLOT_EMPTY"
        self.SlotDiskTestThread = SlotDiskTestPlus_Thread(self)

        self.smartDict_now = {'01':'0', '05':'0', 'A3':'0', 'C2':'0', 'C3':'0', 'C4':'0', 'C7':'0'}
        self.smartDict_old = {'01':'0', '05':'0', 'A3':'0', 'C2':'0', 'C3':'0', 'C4':'0', 'C7':'0'}

        self.color = {
            'red':"#ff0000",  # red
            'orange':"#ff8800",  # orange
            'yellow' : "#ffff00",  # yellow
            'yellow_green' : "#ccff00",  # yellow green
            'green' : "#00ff00",  # green
            'green-blue': "#00ff88",  # green-xx
            'blue': "#55ff00",  # blue
        }

        # " text-align: center; }}" \

        self.progressBarStyleSheetTemplate = \
            "QProgressBar {{" \
            " border: 1px solid black;" \
            " border-radius: 1px;" \
            " text-align: right; }}" \
        "QProgressBar::chunk:horizontal {{" \
            " background-color: {0};" \
            " width: 1px;" \
            " margin: 0px;}}"


        #self.setStyleSheet(self.progressBarStyleSheetTemplate.format(self.color[yellow_green]))

        self.frame = QtWidgets.QFrame(widget)
        self.frame.setGeometry(position)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame" + "slotnum")

        self.line_0 = QtWidgets.QFrame(self.frame)
        self.line_0.setGeometry(QtCore.QRect(0, 0, 160, 2))
        self.line_0.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_0.setObjectName("line_0")

        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 2, 700))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(159, 0, 2, 700))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 4, 40, 60))
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setStyleSheet("color:white;background:gray")
        self.lcdNumber.setProperty("value", slotnum)
        self.lcdNumber.setObjectName("lcdNumber")

        self.label_progress = QtWidgets.QLabel(self.frame)
        # self.label_progress.setGeometry(QtCore.QRect(51, 70, 60, 20))
        self.label_progress.setGeometry(QtCore.QRect(3, 66, 155, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_progress.setFont(font)
        self.label_progress.setStyleSheet("color:red;")
        self.label_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.label_progress.setFont(font)
        self.label_progress.setObjectName("label_progress")
        self.progressValue = 0
        #self.label_progress.setText("TH10: 10:0000 Dumping")
        self.label_progress.setText("")

        self.label_scsi_id = QtWidgets.QLabel(self.frame)
        self.label_scsi_id.setGeometry(QtCore.QRect(40, 78, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_scsi_id.setFont(font)
        self.label_scsi_id.setAutoFillBackground(False)
        self.label_scsi_id.setStyleSheet("color:#00C78C;")
        self.label_scsi_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_scsi_id.setObjectName("label_scsi_id")
        #self.label_scsi_id.setText("0:0:0:0")
        self.label_scsi_id.setText("-:-:-:-")

        self.label_sdx = QtWidgets.QLabel(self.frame)
        self.label_sdx.setGeometry(QtCore.QRect(40, 95, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_sdx.setFont(font)
        self.label_sdx.setAutoFillBackground(False)
        self.label_sdx.setStyleSheet("color:blue;")
        self.label_sdx.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sdx.setObjectName("label_sdx")
        self.label_sdx.setText("")

        self.label_disknameValue = QtWidgets.QLabel(self.frame)
        self.label_disknameValue.setGeometry(QtCore.QRect(1, 120, 158, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        # font.setFamily("Arial")
        font.setBold(True)
        self.label_disknameValue.setFont(font)
        self.label_disknameValue.setStyleSheet("color:blue;")
        self.label_disknameValue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disknameValue.setFont(font)
        self.label_disknameValue.setObjectName("label_disknameValue")
        #self.label_disknameValue.setText("Faspeed K6-120G12345")
        self.label_disknameValue.setText("")

        self.label_fwVersionValue = QtWidgets.QLabel(self.frame)
        self.label_fwVersionValue.setGeometry(QtCore.QRect(5, 138, 73, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        # font.setFamily("Arial")
        font.setBold(True)
        self.label_fwVersionValue.setFont(font)
        self.label_fwVersionValue.setStyleSheet("color:green;")
        self.label_fwVersionValue.setAlignment(QtCore.Qt.AlignRight)
        self.label_fwVersionValue.setFont(font)
        self.label_fwVersionValue.setObjectName("label_fwVersionValue")
        #self.label_fwVersionValue.setText("{}".format("Q0525A"))
        self.label_fwVersionValue.setText("")

        self.label_sizeValue = QtWidgets.QLabel(self.frame)
        self.label_sizeValue.setGeometry(QtCore.QRect(82, 138, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Arial")
        font.setBold(True)
        self.label_sizeValue.setFont(font)
        self.label_sizeValue.setStyleSheet("color:blue;")
        self.label_sizeValue.setAlignment(QtCore.Qt.AlignLeft)
        self.label_sizeValue.setFont(font)
        self.label_sizeValue.setObjectName("label_sizeValue")
        #self.label_sizeValue.setText("{}GB".format("120"))
        self.label_sizeValue.setText("")

        self.label_snValue = QtWidgets.QLabel(self.frame)
        self.label_snValue.setGeometry(QtCore.QRect(2, 150, 156, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.label_snValue.setFont(font)
        self.label_snValue.setStyleSheet("color:blue;")
        self.label_snValue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_snValue.setFont(font)
        self.label_snValue.setObjectName("label_snValue")
        #self.label_snValue.setText("12345678900987654321")
        self.label_snValue.setText("")

        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 170, 160, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        font = QtGui.QFont()
        font.setPointSize(8)
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_RO10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_RO10.setFont(font)
        self.pushButton_RO10.setGeometry(QtCore.QRect(2, 172, 38, 25))
        self.pushButton_RO10.setObjectName("pushButton_RO10")
        self.pushButton_RO10.setText("RO10")

        self.pushButton_RO30 = QtWidgets.QPushButton(self.frame)
        self.pushButton_RO30.setFont(font)
        self.pushButton_RO30.setGeometry(QtCore.QRect(42, 172, 38, 25))
        self.pushButton_RO30.setObjectName("pushButton_RO30")
        self.pushButton_RO30.setText("RO30")

        self.pushButton_WO10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_WO10.setFont(font)
        self.pushButton_WO10.setGeometry(QtCore.QRect(81, 172, 38, 25))
        self.pushButton_WO10.setObjectName("pushButton_WO10")
        self.pushButton_WO10.setText("WO10")

        self.pushButton_WO30 = QtWidgets.QPushButton(self.frame)
        self.pushButton_WO30.setFont(font)
        self.pushButton_WO30.setGeometry(QtCore.QRect(120, 172, 38, 25))
        self.pushButton_WO30.setObjectName("pushButton_WO30")
        self.pushButton_WO30.setText("WO30")

        self.pushButton_TH15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_TH15.setFont(font)
        self.pushButton_TH15.setGeometry(QtCore.QRect(2, 198, 38, 25))
        self.pushButton_TH15.setObjectName("pushButton_TH15")
        self.pushButton_TH15.setText("TH15")

        self.pushButton_TH20 = QtWidgets.QPushButton(self.frame)
        self.pushButton_TH20.setFont(font)
        self.pushButton_TH20.setGeometry(QtCore.QRect(42, 198, 38, 25))
        self.pushButton_TH20.setObjectName("pushButton_TH20")
        self.pushButton_TH20.setText("TH20")

        self.pushButton_TH30 = QtWidgets.QPushButton(self.frame)
        self.pushButton_TH30.setFont(font)
        self.pushButton_TH30.setGeometry(QtCore.QRect(81, 198, 38, 25))
        self.pushButton_TH30.setObjectName("pushButton_TH30")
        self.pushButton_TH30.setText("TH30")

        self.pushButton_WO1r = QtWidgets.QPushButton(self.frame)
        self.pushButton_WO1r.setFont(font)
        self.pushButton_WO1r.setGeometry(QtCore.QRect(120, 198, 38, 25))
        self.pushButton_WO1r.setObjectName("pushButton_WO1r")
        self.pushButton_WO1r.setText("WO1r")

        self.line_41 = QtWidgets.QFrame(self.frame)
        self.line_41.setGeometry(QtCore.QRect(0, 224, 160, 2))
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")

        self.label_rwspeed = QtWidgets.QLabel(self.frame)
        self.label_rwspeed.setGeometry(QtCore.QRect(3, 223, 155, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        #font.setFamily("Mono")
        font.setFamily("Arial")
        font.setBold(True)
        self.label_rwspeed.setFont(font)
        self.label_rwspeed.setStyleSheet("color:green;")
        self.label_rwspeed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rwspeed.setFont(font)
        self.label_rwspeed.setObjectName("label_progress")
        self.progressValue = 0
        self.label_rwspeed.setText("R/W[{}/{}]MB/s".format(self.writeSpeed, self.readSpeed))

        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(0, 239, 160, 2))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        # font.setBold(True)
        self.pushButton_DeleteDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_DeleteDisk.setFont(font)
        self.pushButton_DeleteDisk.setGeometry(QtCore.QRect(4, 240, 75, 20))
        self.pushButton_DeleteDisk.setObjectName("pushButton_DeleteDisk")
        self.pushButton_DeleteDisk.setText("删除硬盘")

        self.pushButton_ReflashDisk = QtWidgets.QPushButton(self.frame)
        self.pushButton_ReflashDisk.setFont(font)
        self.pushButton_ReflashDisk.setGeometry(QtCore.QRect(81, 240, 75, 20))
        self.pushButton_ReflashDisk.setObjectName("pushButton_ReflashDisk")
        self.pushButton_ReflashDisk.setText("手动刷新")

        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(0, 260, 160, 2))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.testFlag = "NOT_TEST"
        self.testCycleNow = 0
        self.testStartTime = 0
        self.progressBar = [0 for x in range(0, 30)]
        self.eachCycleUsedTime = [0 for x in range(0, 30)]
        self.label_TestUsedTime = [0 for x in range(0, 30)]
        self.label_TestResult = [0 for x in range(0, 30)]
        for i in range(0, 30):
            self.progressBar[i] = QtWidgets.QProgressBar(self.frame)
            self.progressBar[i].setGeometry(QtCore.QRect(3, 262 + i*12, 154, 11))
            self.progressBar[i].setProperty("value", 0)
            self.progressBar[i].setTextVisible(True)
            font = QtGui.QFont()
            font.setPointSize(8)
            # font.setFamily("Arial")
            font.setBold(True)
            self.progressBar[i].setFont(font)
            self.progressBar[i].setStyleSheet(self.progressBarStyleSheetTemplate.format(self.color['green']))
            self.progressBar[i].setOrientation(QtCore.Qt.Horizontal)
            self.progressBar[i].setTextDirection(QtWidgets.QProgressBar.TopToBottom)
            self.progressBar[i].setObjectName("progressBar{}".format(i))
            #self.progressBar[i].setValue(100)

            self.eachCycleUsedTime[i] = 0

            self.label_TestUsedTime[i] = QtWidgets.QLabel(self.frame)
            self.label_TestUsedTime[i].setGeometry(QtCore.QRect(10, 263 + i*12, 50, 8))
            font = QtGui.QFont()
            font.setPointSize(7)
            # font.setFamily("Arial")
            font.setFamily("Mono")
            # font.setBold(True)
            self.label_TestUsedTime[i].setFont(font)
            self.label_TestUsedTime[i].setStyleSheet("color:black;")
            self.label_TestUsedTime[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_TestUsedTime[i].setFont(font)
            self.label_TestUsedTime[i].setObjectName("label_TestUsedTime{}".format(i))
            #self.label_TestUsedTime[i].setText("300m25s")
            self.label_TestUsedTime[i].setText("")

            self.label_TestResult[i] = QtWidgets.QLabel(self.frame)
            self.label_TestResult[i].setGeometry(QtCore.QRect(65, 263 + i * 12, 91, 8))
            font = QtGui.QFont()
            font.setPointSize(7)
            font.setFamily("Mono")
            #font.setFamily("Mono")
            #font.setBold(True)
            self.label_TestResult[i].setFont(font)
            self.label_TestResult[i].setStyleSheet("color:black;")
            self.label_TestResult[i].setAlignment(QtCore.Qt.AlignLeft)
            self.label_TestResult[i].setFont(font)
            self.label_TestResult[i].setObjectName("label_TestResult{}".format(i))
            #self.label_TestResult[i].setText("PS[05]68")
            self.label_TestResult[i].setText("")

        self.testDiskSn = ""
        self.nowDiskSn = ""

        # 创建定时器
        self.timer_testProgress = QtCore.QTimer(self.pp)
        self.__attach_events()

    def __attach_events(self):
        self.sin.connect(self.updateDiskTestResult)
        self.pushButton_RO10.clicked.connect(lambda: self.On_THxx(self.pushButton_RO10, TEST_ITEM_RO10))
        self.pushButton_RO30.clicked.connect(lambda: self.On_THxx(self.pushButton_RO30, TEST_ITEM_RO30))
        self.pushButton_WO10.clicked.connect(lambda: self.On_THxx(self.pushButton_WO10, TEST_ITEM_WO10))
        self.pushButton_WO30.clicked.connect(lambda: self.On_THxx(self.pushButton_WO30, TEST_ITEM_WO30))
        self.pushButton_TH15.clicked.connect(lambda: self.On_THxx(self.pushButton_TH15, TEST_ITEM_TH15))
        self.pushButton_TH20.clicked.connect(lambda: self.On_THxx(self.pushButton_TH20, TEST_ITEM_TH20))
        self.pushButton_TH30.clicked.connect(lambda: self.On_THxx(self.pushButton_TH30, TEST_ITEM_TH30))
        self.pushButton_WO1r.clicked.connect(lambda: self.On_THxx(self.pushButton_WO1r, TEST_ITEM_WO1r))

        self.timer_testProgress.timeout.connect(self.OnTestProgressTimer)

        self.pushButton_DeleteDisk.clicked.connect(self.On_DeleteDisk)
        self.pushButton_ReflashDisk.clicked.connect(self.On_ReflashDisk)

    def On_DeleteDisk(self):
        self.SlotDeleteDisk()

    def On_ReflashDisk(self):
        self.SlotIDtoScsiID()

    def SetAllTestButtonDisable(self):
        self.pushButton_RO10.setEnabled(False)
        self.pushButton_RO30.setEnabled(False)
        self.pushButton_WO10.setEnabled(False)
        self.pushButton_WO30.setEnabled(False)
        self.pushButton_TH15.setEnabled(False)
        self.pushButton_TH20.setEnabled(False)
        self.pushButton_TH30.setEnabled(False)
        self.pushButton_WO1r.setEnabled(False)
        self.pushButton_RO10.setStyleSheet("color:white; background:gray")
        self.pushButton_RO30.setStyleSheet("color:white; background:gray")
        self.pushButton_WO10.setStyleSheet("color:white; background:gray")
        self.pushButton_WO30.setStyleSheet("color:white; background:gray")
        self.pushButton_TH15.setStyleSheet("color:white; background:gray")
        self.pushButton_TH20.setStyleSheet("color:white; background:gray")
        self.pushButton_TH30.setStyleSheet("color:white; background:gray")
        self.pushButton_WO1r.setStyleSheet("color:white; background:gray")

    def SetAllTestButtonEnable(self):
        self.pushButton_RO10.setEnabled(True)
        self.pushButton_RO30.setEnabled(True)
        self.pushButton_WO10.setEnabled(True)
        self.pushButton_WO30.setEnabled(True)
        self.pushButton_TH15.setEnabled(True)
        self.pushButton_TH20.setEnabled(True)
        self.pushButton_TH30.setEnabled(True)
        self.pushButton_WO1r.setEnabled(True)
        self.pushButton_RO10.setStyleSheet("color:black;")
        self.pushButton_RO30.setStyleSheet("color:black;")
        self.pushButton_WO10.setStyleSheet("color:black;")
        self.pushButton_WO30.setStyleSheet("color:black;")
        self.pushButton_TH15.setStyleSheet("color:black;")
        self.pushButton_TH20.setStyleSheet("color:black;")
        self.pushButton_TH30.setStyleSheet("color:black;")
        self.pushButton_WO1r.setStyleSheet("color:black;")

    def On_THxx(self, button, testName):
        if self.testItem == TEST_ITEM_NONE:
            self.InitTest()

            if self.sdxx != "":
                self.SetAllTestButtonDisable()
                button.setStyleSheet("color:white;""background:purple")
                self.testItem = testName
                self.testDiskSn = self.nowDiskSn
                self.testCycleNow = 0
                self.testStartTime = 0
                self.writeSpeed = "0"
                self.readSpeed = "0"
                for i in range(0, 30):
                    self.progressBar[i].setValue(0)
                    self.eachCycleUsedTime[i] = 0
                    self.label_TestUsedTime[i].setText("")
                    self.label_TestResult[i].setText("")
                    self.label_TestResult[i].setStyleSheet("")

                self.testFlag = "RUNNING"
                shownum = sid_to_slotnum[self.scsi_id]
                self.pp.STB_LED_PointFlashCtl(shownum, 1)
                self.SlotDiskTestThread.start()
                self.pp.tab5_SlotTestingCount = self.pp.tab5_SlotTestingCount + 1
                self.timer_testProgress.start(1000)

            else:
                for i in range(0, 30):
                    self.progressBar[i].setValue(0)
                    self.eachCycleUsedTime[i] = 0
                    self.label_TestUsedTime[i].setText("")
                    self.label_TestResult[i].setText("")
                    self.label_TestResult[i].setStyleSheet("")
                shownum = sid_to_slotnum[self.scsi_id]
                self.pp.STB_LED_NumFlashCtl(shownum, 0)
                self.pp.STB_LED_PointFlashCtl(shownum, 0)
                self.pp.STB_LED_Show(shownum, 20)

    def OnTestProgressTimer(self):
        #print("in OnTestProgressTimer")
        #print("{} self.testFlag = {}".format(self.sdxx, self.testFlag))
        if self.testFlag == "RUNNING":
            try:
                f = os.popen('rw2_show -c {}'.format(diskid[self.sdxx]))
                rw = f.readlines()

                rws = rw[0].replace('\n', '').strip()
                rwlist = rws.split(' ')
                #print("{} rwlist = {}".format(self.sdxx, rwlist))
            except:
                pass

            try:
                self.progressValue = rwlist[2]
                #print("{} self.progressValue = {} - {}".format(self.sdxx, self.progressValue, int(self.progressValue)))
                if rwlist[1] == "Writing":
                    self.label_progress.setText("{} : {:0.4f} Writing".format(self.testItem, self.testCycleNow + float(self.progressValue) / 100))
                    self.label_progress.setStyleSheet("color:red;")
                    self.progressBar[self.testCycleNow].setValue(int(float(self.progressValue)))
                    self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format('#00C957'))
                elif rwlist[1] == "Dumping" or rwlist[1] == "Verifying":
                    self.label_progress.setText("{} : {:0.4f} Dumping".format(self.testItem, self.testCycleNow + float(self.progressValue) / 100))
                    self.label_progress.setStyleSheet("color:green;")
                    self.progressBar[self.testCycleNow].setValue(int(float(self.progressValue)))
                    self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format('#00FF7F'))

                if rwlist[1] == "Writing":
                    self.writeSpeed = rwlist[3].replace('MB/s','')
                elif rwlist[1] == "Dumping" or rwlist[1] == "Verifying":
                    self.readSpeed = rwlist[3].replace('MB/s','')

                self.label_rwspeed.setText("R/W[{}/{}]MB/s".format(self.readSpeed, self.writeSpeed))

                now_time = time.time()
                self.label_TestUsedTime[self.testCycleNow].setText("{} {}m{}s".format((self.testCycleNow + 1), int((now_time - self.testStartTime)/60), int((now_time - self.testStartTime)%60)))
            except:
                pass

        #print("{} self.testFlag = {}".format(self.sdxx, self.testFlag))
        if self.testFlag == "FINISH":
            self.timer_testProgress.stop()
            self.SlotDiskTestThread.__del__()
            self.SetAllTestButtonEnable()
            self.testItem = TEST_ITEM_NONE
            shownum = sid_to_slotnum[self.scsi_id]
            self.pp.STB_LED_PointFlashCtl(shownum, 0)
            self.pp.tab5_SlotTestingCount = self.pp.tab5_SlotTestingCount - 1
        else:
            self.timer_testProgress.start(500)

    def updateDiskTestResult(self):
        print("in updateDiskTestResult")

        self.progressValue = 100.00
        self.label_progress.setText("{:0.2f}".format(float(self.progressValue) / 100))

        self.progressBar[diskid[self.sdxx]].setValue(int(self.progressValue))

        self.timer_testProgress.stop()

    def GetSmartInfo(self, sdxx):

        ID01_raw_read_error_rate       = 1
        ID05_reallocated_sectors_count = 5
        ID09_power_on_hours            = 9
        ID0C_power_cycle_count         = 12
        IDA3_original_bad_count        = 163
        IDA7_average_erase_count       = 167
        IDC2_temperature               = 194
        IDC3_read_retry                = 195
        IDC4_reallocation_event_count  = 196
        IDC7_ultraDMA_CRC_error_count  = 199
        IDF1_total_host_written        = 241
        IDF2_total_host_read           = 242

        small = []
        sml = []

        try:
            f = os.popen("smartctl -i /dev/{} | grep 'Firmware'".format(sdxx))
            sm = f.readlines()
            ver = sm[0].replace('Firmware Version:', '').replace('\n', '').strip()
            self.label_fwVersionValue.setText(ver)

            f = os.popen("smartctl -i /dev/{} | grep 'Device Model:'".format(sdxx))
            sm = f.readlines()
            name = sm[0].replace('Device Model:', '').replace('\n', '').strip()
            self.label_disknameValue.setText(name)

            f = os.popen("smartctl -s on -A /dev/{} | grep 0x0".format(sdxx))
            sm = f.readlines()
            for i in sm:
                smll = []
                sml = i.replace('\n', '').strip()
                sm_1space = sml.replace('   ', ' ').replace('   ', ' ').replace('  ', ' ').replace('  ', ' ')
                smlist = sm_1space.split(' ')

                smll.append(smlist[0])
                smll.append(smlist[1])
                smll.append(smlist[9])

                small.append(smll)

            # 读到结果为空，说明读取samrt失败，可能原因是 WE，RE，DL等原因，此种情况，不更新smart信息
            if len(sm) != 0:

                for (id, name, value) in small:
                    if int(id) == ID01_raw_read_error_rate:
                        self.smartDict_now['01'] = value

                    elif int(id) == ID05_reallocated_sectors_count:
                        self.smartDict_now['05'] = value

                    elif int(id) == IDA3_original_bad_count:
                        self.smartDict_now['A3'] = int(value)

                    elif int(id) == IDC2_temperature:
                        self.smartDict_now['C2'] = value

                    elif int(id) == IDC3_read_retry:
                        self.smartDict_now['C3'] = value

                    elif int(id) == IDC4_reallocation_event_count:
                        self.smartDict_now['C4'] = value

                    elif int(id) == IDC7_ultraDMA_CRC_error_count:
                        self.smartDict_now['C7'] = value

        except:
            self.smartDict_now['01'] = '*'
            self.smartDict_now['05'] = '*'
            self.smartDict_now['A3'] = '*'
            self.smartDict_now['C2'] = '*'
            self.smartDict_now['C3'] = '*'
            self.smartDict_now['C4'] = '*'
            self.smartDict_now['C7'] = '*'

    def UpdateSmartOld(self):
        self.smartDict_old['01'] = self.smartDict_now['01']
        self.smartDict_old['05'] = self.smartDict_now['05']
        self.smartDict_old['A3'] = self.smartDict_now['A3']
        self.smartDict_old['C2'] = self.smartDict_now['C2']
        self.smartDict_old['C3'] = self.smartDict_now['C3']
        self.smartDict_old['C4'] = self.smartDict_now['C4']
        self.smartDict_old['C7'] = self.smartDict_now['C7']

    def InitTest(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                # print("[{}] {} {} {} {} {}".format(self.slotnum, scsiid, sdxx, size_GB, deviceName, sn))
                if self.scsi_id == scsiid:
                    self.label_scsi_id.setText("{}".format(scsiid))
                    self.label_sdx.setText("{}".format(sdxx))
                    #self.label_disknameValue.setText(deviceName)
                    self.label_snValue.setText(sn)

                    self.label_sizeValue.setText(size_GB)
                    try:
                        os.system("echo 2 > /sys/block/{}/device/eh_timeout".format(sdxx))
                        os.system("echo 2 > /sys/block/{}/device/timeout".format(sdxx))
                        os.system("echo 1 > /sys/block/{}/device/queue_depth".format(sdxx))
                    except:
                        pass

                    self.lcdNumber.setStyleSheet("color:red;background:#888888")

                    self.sdxx = sdxx
                    self.secSize = secSize
                    self.nowDiskSn = sn

                    self.FirstSmartResultCtl(sdxx)
                    self.UpdateSmartOld()

                    break

            if n == (len(self.disklist) - 1):
                self.lcdNumber.setStyleSheet("color:white;background:#DDDDDD")
                self.label_scsi_id.setText("-:-:-:-")
                self.label_sdx.setText("")
                self.label_disknameValue.setText("")
                self.label_snValue.setText("")
                self.label_sizeValue.setText("")
                self.label_fwVersionValue.setText("")
                self.sdxx = ""
                self.secSize = ""
                self.nowDiskSn = ""
        except:
            pass

    def SlotIDtoScsiID(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                # print("[{}] {} {} {} {} {}".format(self.slotnum, scsiid, sdxx, size_GB, deviceName, sn))
                if self.scsi_id == scsiid:
                    self.label_scsi_id.setText("{}".format(scsiid))
                    self.label_sdx.setText("{}".format(sdxx))
                    #self.label_disknameValue.setText(deviceName)
                    self.label_snValue.setText(sn)

                    self.label_sizeValue.setText(size_GB)
                    try:
                        os.system("echo 2 > /sys/block/{}/device/eh_timeout".format(sdxx))
                        os.system("echo 2 > /sys/block/{}/device/timeout".format(sdxx))
                        os.system("echo 1 > /sys/block/{}/device/queue_depth".format(sdxx))
                    except:
                        pass

                    self.lcdNumber.setStyleSheet("color:red;background:#888888")
                    self.GetSmartInfo(sdxx)
                    self.UpdateSmartOld()
                    self.sdxx = sdxx
                    self.secSize = secSize
                    self.nowDiskSn = sn

                    break

            if n == (len(self.disklist) - 1):
                #self.slotStatus = SLOT_EMPTY
                self.lcdNumber.setStyleSheet("color:white;background:#DDDDDD")
                self.label_scsi_id.setText("-:-:-:-")
                self.label_sdx.setText("")
                self.label_disknameValue.setText("")
                self.label_snValue.setText("")
                self.label_sizeValue.setText("")
                self.label_fwVersionValue.setText("")

                '''
                #没有盘，不要做LED控制
                if self.testItem == TEST_ITEM_NONE and self.sdxx == "":
                    shownum = sid_to_slotnum[self.scsi_id]
                    self.pp.STB_LED_NumFlashCtl(shownum, 0)
                    self.pp.STB_LED_PointFlashCtl(shownum, 0)
                    #self.pp.STB_LED_Show(shownum, 20)
                '''
            # 手动刷新，不要对LED灯进行控制，第一次手动刷新，初始化LED状态
            if self.testItem == TEST_ITEM_NONE and self.slotStatus == SLOT_EMPTY:
                self.slotStatus = SLOT_INSERT
                shownum = sid_to_slotnum[self.scsi_id]
                self.pp.STB_LED_NumFlashCtl(shownum, 0)
                self.pp.STB_LED_PointFlashCtl(shownum, 0)
                self.pp.STB_LED_Show(shownum, shownum)

        except:
            print("{} SlotIDtoScsiID except !!!!!!".format(self.sdxx))
            pass

    def SlotDeleteDisk(self):
        try:
            self.disklist = get_disk_info()
            for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                if self.scsi_id == scsiid:
                    os.system("echo 1 > /sys/block/{}/device/delete".format(sdxx))
        except:
            print("{} SlotDeleteDisk except !!!!!!".format(self.sdxx))
            pass

    def TestReturn(self, ret):
        self.GetSmartInfo(self.sdxx)

        shownum = sid_to_slotnum[self.scsi_id]
        ret = ret/0x100
        if int(ret) == TEST_PASS:
           resultText = "PS"
           barColor = "#00FF7F"
        elif int(ret) == ERROR_RE_READ_DATA:
            resultText = "RE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_CE_COMPARE_DATA:
            resultText = "CE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_WE_WIRTE_DATA:
            resultText = "WE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_AE_ABORT:
            resultText = "AE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_TO_TIMEOUT:
            resultText = "TO"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_NE_NOMEM:
            resultText = "NE"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_RO_DISK:
            resultText = "RO"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_DL_NONE_DISK:
            resultText = "DL"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_US_UNSORTED:
            resultText = "US"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_UA_UNAUTHORIZATION:
            resultText = "UA"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        elif int(ret) == ERROR_OV_RUN_TIME_COUNT_OVERFLOW:
            resultText = "OV"
            barColor = 'red'
            self.pp.STB_LED_NumFlashCtl(shownum, 1)
        else:
            resultText = "UK"
            barColor = 'red'
            print("{} ret = {}".format(self.sdxx, ret))
            self.pp.STB_LED_NumFlashCtl(shownum, 1)

        if self.smartDict_now['01'] != self.smartDict_old['01']:
            resultText = resultText + "(01){}".format(self.smartDict_now['01'])
            if barColor != 'red':
                barColor = 'red'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['05'] != self.smartDict_old['05']:
            resultText = resultText + "(05){}".format(self.smartDict_now['05'])
            if barColor != 'red':
                barColor = 'red'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C4'] != self.smartDict_now['C4']:
            resultText = resultText + "(C4){}".format(self.smartDict_now['C4'])
            if barColor != 'red':
                barColor = 'red'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C3'] != self.smartDict_old['C3']:
            resultText = resultText + "(C3){}".format(self.smartDict_now['C3'])
            if barColor != 'red':
                barColor = 'yellow'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C7'] != self.smartDict_old['C7']:
            resultText = resultText + "(C7){}".format(self.smartDict_now['C7'])
            if barColor != 'red':
                barColor = 'yellow'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        elif self.smartDict_now['C2'] > "40":
            resultText = resultText + "(C2){}".format(self.smartDict_now['C2'])
            if barColor != 'red':
                barColor = 'yellow'
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)
        else:
            self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
            self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
            self.label_TestResult[self.testCycleNow].setText(resultText)

        if self.smartDict_now['01'] != "0" or self.smartDict_now['05'] != "0" or self.smartDict_now['C4'] != "0":
            #print("self.smartDict_now['01'] = {}".format(self.smartDict_now['01']))
            #print("self.smartDict_now['05'] = {}".format(self.smartDict_now['05']))
            #print("self.smartDict_now['C4'] = {}".format(self.smartDict_now['C4']))
            self.pp.STB_LED_NumFlashCtl(shownum, 1)

        self.UpdateSmartOld()

    def FirstSmartResultCtl(self, sdxx):
        # 恢复 LED 显示状态
        shownum = sid_to_slotnum[self.scsi_id]
        self.pp.STB_LED_NumFlashCtl(shownum, 0)
        self.pp.STB_LED_Show(shownum, shownum)
        #self.pp.STB_k()
        #self.pp.STB_K()
        #self.pp.STB_GetRuntime()

        # 初始化新测试硬盘状态
        self.smartDict_now['01'] = "0"
        self.smartDict_now['05'] = "0"
        self.smartDict_now['A3'] = "0"
        self.smartDict_now['C2'] = "0"
        self.smartDict_now['C3'] = "0"
        self.smartDict_now['C4'] = "0"
        self.smartDict_now['C7'] = "0"
        self.UpdateSmartOld()
        self.GetSmartInfo(sdxx)

        if self.smartDict_now['01'] != "0" or self.smartDict_now['05'] != "0" or self.smartDict_now['C4'] != "0":
            #print("self.smartDict_now['01'] = {}".format(self.smartDict_now['01']))
            #print("self.smartDict_now['05'] = {}".format(self.smartDict_now['05']))
            #print("self.smartDict_now['C4'] = {}".format(self.smartDict_now['C4']))
            self.pp.STB_LED_NumFlashCtl(shownum, 1)

class SlotDiskTestPlus_Thread(QtCore.QThread):

    def __init__(self, parent):
        self.sin = parent.sin
        self.mutex = parent.mutex
        super(SlotDiskTestPlus_Thread, self).__init__()
        self.working = True
        self.pp = parent

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        try:
            self.working = True
        except:
            pass

        while self.working == True:
            #if self.serial.isOpen():
            if True:
                try:
                    if self.pp.testItem == TEST_ITEM_RO10:
                        self.RO10()

                    if self.pp.testItem == TEST_ITEM_RO30:
                        self.RO30()

                    if self.pp.testItem == TEST_ITEM_WO10:
                        self.WO10()

                    if self.pp.testItem == TEST_ITEM_WO30:
                        self.WO30()

                    if self.pp.testItem == TEST_ITEM_TH15:
                        self.TH15()

                    if self.pp.testItem == TEST_ITEM_TH20:
                        self.TH20()

                    if self.pp.testItem == TEST_ITEM_TH30:
                        self.TH30()

                    if self.pp.testItem == TEST_ITEM_WO1r:
                        self.WO1r()

                    time.sleep(3)
                    self.working = False
                except:
                    print("{}-{} running thread except ！！！！！！！！！！！".format(self.pp.sdxx, self.pp.testItem))
                    break
                    #pass

    def RO10(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        for i in range(0, 10):
            startTime = time.time()
            self.pp.testStartTime = startTime
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 1 -L {} -w -s -e 10 -t 0xEA3B -I {} /dev/{} {} {}".format(
                    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
            else:
                ret = ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[i] = finishTime - startTime
            time.sleep(2)
            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1

        self.pp.testFlag = "FINISH"

    def RO30(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        for i in range(0, 30):
            startTime = time.time()
            self.pp.testStartTime = startTime
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 1 -L {} -w -s -e 10 -t 0xEA3B -I {} /dev/{} {} {}".format(
                    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
            else:
                ret = ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[i] = finishTime - startTime
            time.sleep(2)
            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1

        self.pp.testFlag = "FINISH"

    def WO10(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        for i in range(0, 10):
            startTime = time.time()
            self.pp.testStartTime = startTime
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                ret = os.system("stb_rw2 -b 512 -c 2048 -D 0 -r 0 -L {} -w -s -e 10 -t 0xEA3B -I {} /dev/{} {} {}".format(
                    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
            else:
                ret = ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[i] = finishTime - startTime
            time.sleep(2)
            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1

        self.pp.testFlag = "FINISH"

    def WO30(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        for i in range(0, 30):
            startTime = time.time()
            self.pp.testStartTime = startTime
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                ret = os.system("stb_rw2 -b 512 -c 2048 -D 0 -r 0 -L {} -w -s -e 10 -t 0xEA3B -I {} /dev/{} {} {}".format(
                    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
            else:
                ret = ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[i] = finishTime - startTime
            time.sleep(2)
            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1

        self.pp.testFlag = "FINISH"

    def TH15(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        # add 5cycle random data model
        for i in range(0, 5):
            startTime = time.time()
            self.pp.testStartTime = startTime
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 10 -t 0xEA3B -I {} /dev/{} {} {}".format(
                    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
            else:
                ret = ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[i] = finishTime - startTime
            time.sleep(2)
            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1

        i = 4

        # TH10 model
        # cycle 1
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x1234 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 2
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x4321 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 3
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x55AA -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 4
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xAA55 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 5
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xEA3B -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        #print("{} ret = = = {}".format(self.pp.sdxx, ret))
        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 6
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xFF00 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 7
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x00FF -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 8
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xCCCC -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 9
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x3333 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 10
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(5)

        self.pp.TestReturn(ret)

        self.pp.testFlag = "FINISH"

    def TH20(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        # add 10cycle random data model
        for i in range(0, 10):
            startTime = time.time()
            self.pp.testStartTime = startTime
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 10 -t 0xEA3B -I {} /dev/{} {} {}".format(
                    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
            else:
                ret = ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[i] = finishTime - startTime
            time.sleep(2)
            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1

        i = 9

        # TH10 model
        # cycle 1
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x1234 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 2
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x4321 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 3
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x55AA -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 4
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xAA55 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 5
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xEA3B -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        # print("{} ret = = = {}".format(self.pp.sdxx, ret))
        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 6
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xFF00 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 7
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x00FF -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 8
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xCCCC -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 9
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x3333 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 10
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(5)

        self.pp.TestReturn(ret)

        self.pp.testFlag = "FINISH"

    def TH30(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        # add 5cycle random data model
        for i in range(0, 20):
            startTime = time.time()
            self.pp.testStartTime = startTime
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 10 -t 0xEA3B -I {} /dev/{} {} {}".format(
                    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
            else:
                ret = ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[i] = finishTime - startTime
            time.sleep(2)
            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1

        i = 19

        # TH10 model
        # cycle 1
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x1234 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 2
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x4321 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 3
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x55AA -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 4
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xAA55 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 5
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xEA3B -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        # print("{} ret = = = {}".format(self.pp.sdxx, ret))
        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 6
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xFF00 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 7
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x00FF -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 8
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xCCCC -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 9
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x3333 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(2)

        self.pp.TestReturn(ret)
        self.pp.testCycleNow = self.pp.testCycleNow + 1

        # cycle 10
        i = i + 1
        startTime = time.time()
        self.pp.testStartTime = startTime
        if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
            ret = os.system("stb_rw2 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
        else:
            ret = ERROR_DL_NONE_DISK

        finishTime = time.time()
        self.pp.eachCycleUsedTime[i] = finishTime - startTime
        time.sleep(5)

        self.pp.TestReturn(ret)

        self.pp.testFlag = "FINISH"

    def WO1r(self):
        startTime = time.time()
        self.pp.testStartTime = startTime
        self.pp.testCycleNow = 0

        for i in range(0, 1):
            startTime = time.time()
            self.pp.testStartTime = startTime
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                ret = os.system("stb_rw2 -b 512 -c 2048 -D 0 -r 0 -L {} -w -s -e 10 -t 0xEA3B -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (self.pp.secSize - 1), LBA_START))
            else:
                ret = ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[i] = finishTime - startTime
            time.sleep(2)
            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1

        self.pp.testFlag = "FINISH"


# tab_6 ################################################################################################################

'''
tab "测试硬盘++"
'''

class DiskTest_Header_BIT(object):
        def __init__(self, parent, widget, position):

            self.parent = parent

            self.frame = QtWidgets.QFrame(widget)
            self.frame.setGeometry(position)
            self.frame.setStyleSheet("")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("HeadControl")

            '''
            self.pushButton_initTest = QtWidgets.QPushButton(self.frame)
            self.pushButton_initTest.setGeometry(QtCore.QRect(718, 3, 80, 23))
            self.pushButton_initTest.setObjectName("pushButton_initTest")
            self.pushButton_initTest.setText("初始化显示")
            '''

            self.pushButton_deleteDisk = QtWidgets.QPushButton(self.frame)
            self.pushButton_deleteDisk.setGeometry(QtCore.QRect(802, 3, 77, 23))
            self.pushButton_deleteDisk.setObjectName("pushButton_deleteDisk")
            self.pushButton_deleteDisk.setText("删除硬盘")

            self.pushButton_manualUpdate = QtWidgets.QPushButton(self.frame)
            self.pushButton_manualUpdate.setGeometry(QtCore.QRect(881, 3, 77, 23))
            self.pushButton_manualUpdate.setObjectName("pushButton_manualUpdate")
            self.pushButton_manualUpdate.setText("手动刷新")

            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Arial")
            font.setBold(True)

            self.pushButton_testTH0 = QtWidgets.QPushButton(self.frame)
            self.pushButton_testTH0.setFont(font)
            self.pushButton_testTH0.setGeometry(QtCore.QRect(3, 3, 75, 23))
            self.pushButton_testTH0.setObjectName("pushButton_testTH0")
            self.pushButton_testTH0.setText("TH0测试")

            self.pushButton_testTH02 = QtWidgets.QPushButton(self.frame)
            self.pushButton_testTH02.setFont(font)
            self.pushButton_testTH02.setGeometry(QtCore.QRect(83, 3, 75, 23))
            self.pushButton_testTH02.setObjectName("pushButton_testTH02")
            self.pushButton_testTH02.setText("TH0.2测试")

            self.pushButton_testTH1 = QtWidgets.QPushButton(self.frame)
            self.pushButton_testTH1.setFont(font)
            self.pushButton_testTH1.setGeometry(QtCore.QRect(163, 3, 75, 23))
            self.pushButton_testTH1.setObjectName("pushButton_testTH1")
            self.pushButton_testTH1.setText("TH1测试")

            self.pushButton_testTH3 = QtWidgets.QPushButton(self.frame)
            self.pushButton_testTH3.setFont(font)
            self.pushButton_testTH3.setGeometry(QtCore.QRect(243, 3, 75, 23))
            self.pushButton_testTH3.setObjectName("pushButton_testTH3")
            self.pushButton_testTH3.setText("TH3测试")

            self.pushButton_testTH5 = QtWidgets.QPushButton(self.frame)
            self.pushButton_testTH5.setFont(font)
            self.pushButton_testTH5.setGeometry(QtCore.QRect(323, 3, 75, 23))
            self.pushButton_testTH5.setObjectName("pushButton_testTH5")
            self.pushButton_testTH5.setText("TH5测试")

            self.pushButton_testTH10 = QtWidgets.QPushButton(self.frame)
            self.pushButton_testTH10.setFont(font)
            self.pushButton_testTH10.setGeometry(QtCore.QRect(403, 3, 75, 23))
            self.pushButton_testTH10.setObjectName("pushButton_testTH10")
            self.pushButton_testTH10.setText("TH10测试")

            self.pushButton_testRO1 = QtWidgets.QPushButton(self.frame)
            self.pushButton_testRO1.setFont(font)
            self.pushButton_testRO1.setGeometry(QtCore.QRect(483, 3, 75, 23))
            self.pushButton_testRO1.setObjectName("pushButton_testRO1")
            self.pushButton_testRO1.setText("RO1测试")

            self.pushButton_testVY1 = QtWidgets.QPushButton(self.frame)
            self.pushButton_testVY1.setFont(font)
            self.pushButton_testVY1.setGeometry(QtCore.QRect(563, 3, 75, 23))
            self.pushButton_testVY1.setObjectName("pushButton_testVY1")
            self.pushButton_testVY1.setText("VY1测试")

            self.checkBox_Heating = QtWidgets.QCheckBox(self.frame)
            self.checkBox_Heating.setGeometry(QtCore.QRect(650, 3, 80, 23))
            self.checkBox_Heating.setObjectName("checkBox_Heating")
            self.checkBox_Heating.setText("开启加热")
            self.checkBox_Heating.setStyleSheet("color:black;")

            self.label_heatPercent = QtWidgets.QLabel(self.frame)
            self.label_heatPercent.setGeometry(QtCore.QRect(725, 2, 60, 10))
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setFamily("Arial")
            # font.setBold(True)
            self.label_heatPercent.setFont(font)
            self.label_heatPercent.setAutoFillBackground(False)
            # self.label_heatPercent.setStyleSheet("color:blue;")
            self.label_heatPercent.setAlignment(QtCore.Qt.AlignCenter)
            self.label_heatPercent.setObjectName("label_heatPercent")
            self.label_heatPercent.setText("100%")

            self.horizontalSlider_heatPercent = QtWidgets.QSlider(self.frame)
            self.horizontalSlider_heatPercent.setGeometry(QtCore.QRect(725, 11, 60, 15))
            self.horizontalSlider_heatPercent.setMinimum(0)
            self.horizontalSlider_heatPercent.setMaximum(100)
            self.horizontalSlider_heatPercent.setProperty("value", 100)
            self.horizontalSlider_heatPercent.setTickInterval(1)
            self.horizontalSlider_heatPercent.setSingleStep(1)
            self.horizontalSlider_heatPercent.setPageStep(1)
            self.horizontalSlider_heatPercent.setInvertedAppearance(False)
            self.horizontalSlider_heatPercent.setInvertedControls(True)
            self.horizontalSlider_heatPercent.setOrientation(QtCore.Qt.Horizontal)
            self.horizontalSlider_heatPercent.setObjectName("horizontalSlider_heatPercent")

            # 创建定时器
            self.timer_autoUpdate = QtCore.QTimer(self.parent)

            self.__attach_events()

        def __attach_events(self):
            self.pushButton_manualUpdate.clicked.connect(self.On_manualUpdate)
            self.pushButton_deleteDisk.clicked.connect(self.On_deleteDisk)
            # self.checkBox_autoUpdate.stateChanged.connect(self.On_autoUpdate)
            # self.checkBox_Heating.stateChanged.connect(self.On_Heating)
            # self.horizontalSlider_heatPercent.valueChanged.connect(self.On_OnHeatingSlider)
            self.timer_autoUpdate.timeout.connect(self.OnAutoUpdateTimer)

            self.pushButton_testTH0.clicked.connect(lambda: self.On_testAllTHxx(TEST_ITEM_TH0))
            self.pushButton_testTH02.clicked.connect(lambda: self.On_testAllTHxx(TEST_ITEM_TH02))
            self.pushButton_testTH1.clicked.connect(lambda: self.On_testAllTHxx(TEST_ITEM_TH1))
            self.pushButton_testTH3.clicked.connect(lambda: self.On_testAllTHxx(TEST_ITEM_TH3))
            self.pushButton_testTH5.clicked.connect(lambda: self.On_testAllTHxx(TEST_ITEM_TH5))
            self.pushButton_testTH10.clicked.connect(lambda: self.On_testAllTHxx(TEST_ITEM_TH10))
            self.pushButton_testRO1.clicked.connect(lambda: self.On_testAllTHxx(TEST_ITEM_RO1))
            self.pushButton_testVY1.clicked.connect(lambda: self.On_testAllTHxx(TEST_ITEM_VY1))

        def On_manualUpdate(self):
            # print("in On_manualUpdate")
            for i in (1, 2, 3, 4, 5, 6):
                self.parent.tab6_frame[i].SlotIDtoScsiID()

        def On_deleteDisk(self):
            # print("in On_deleteDisk")
            for i in (1, 2, 3, 4, 5, 6):
                self.parent.tab6_frame[i].SlotDeleteDisk()
                self.parent.tab6_frame[i].SlotDeleteSmart()

        '''
        def On_autoUpdate(self):
            #print("in On_autoUpdate")
            if self.checkBox_autoUpdate.isChecked():
                self.pushButton_manualUpdate.setDisabled(True)
                self.timer_autoUpdate.start(500)

            else:
                self.pushButton_manualUpdate.setEnabled(True)
                self.timer_autoUpdate.stop()
        '''

        def On_OnHeatingSlider(self):
            if 1:
                self.label_heatPercent.setText("{}%".format(self.horizontalSlider_heatPercent.value()))
                self.On_Heating()
            else:
                # print("in On_OnTimeSlider")
                # print(self.horizontalSlider_OnTime.value())
                pass

        def On_Heating(self):
            # print("in On_Heating")
            if self.checkBox_Heating.isChecked():
                self.parent.STB_Heating(self.horizontalSlider_heatPercent.value())
            else:
                self.parent.STB_Heating(0)

        def OnAutoUpdateTimer(self):
            # print("in OnAutoUpdateTimer")
            self.On_manualUpdate()
            self.timer_autoUpdate.start(500)

        def On_testAllTHxx(self, testItem):
            self.parent.STB_RuntimePlus()
            self.parent.STB_GetRuntime()
            for i in (1, 2, 3, 4, 5, 6):
                if testItem == TEST_ITEM_TH0:
                    self.parent.tab6_frame[i].On_THxx(self.parent.tab6_frame[i].pushButton_TH0, TEST_ITEM_TH0)
                if testItem == TEST_ITEM_TH02:
                    self.parent.tab6_frame[i].On_THxx(self.parent.tab6_frame[i].pushButton_TH02, TEST_ITEM_TH02)
                if testItem == TEST_ITEM_TH1:
                    self.parent.tab6_frame[i].On_THxx(self.parent.tab6_frame[i].pushButton_TH1, TEST_ITEM_TH1)
                if testItem == TEST_ITEM_TH3:
                    self.parent.tab6_frame[i].On_THxx(self.parent.tab6_frame[i].pushButton_TH3, TEST_ITEM_TH3)
                if testItem == TEST_ITEM_TH5:
                    self.parent.tab6_frame[i].On_THxx(self.parent.tab6_frame[i].pushButton_TH5, TEST_ITEM_TH5)
                if testItem == TEST_ITEM_TH10:
                    self.parent.tab6_frame[i].On_THxx(self.parent.tab6_frame[i].pushButton_TH10, TEST_ITEM_TH10)
                if testItem == TEST_ITEM_RO1:
                    self.parent.tab6_frame[i].On_THxx(self.parent.tab6_frame[i].pushButton_RO1, TEST_ITEM_RO1)
                if testItem == TEST_ITEM_VY1:
                    self.parent.tab6_frame[i].On_THxx(self.parent.tab6_frame[i].pushButton_VY1, TEST_ITEM_VY1)


class SlotDiskTest_BIT(object):
        def __init__(self, parent, widget, position, slotnum):
            self.slotnum = slotnum
            self.pp = parent
            self.serail = parent.serial
            self.mutex = parent.mutex
            self.scsi_id = "{}:0:0:0".format(slotnum - 1)
            self.sdxx = ""
            self.secSize = 0
            self.sin = widget.sin[slotnum]
            self.disklist = []
            self.writeSpeed = "0.0"
            self.readSpeed = "0.0"

            self.testItem = TEST_ITEM_NONE
            self.slotStatus = "SLOT_EMPTY"
            self.SlotDiskTestThread = SlotDiskTest_Thread_BIT(self)

            self.smartDict_now = {'01': '0', '05': '0', 'A3': '0', 'C2': '0', 'C3': '0', 'C4': '0', 'C7': '0'}
            self.smartDict_old = {'01': '0', '05': '0', 'A3': '0', 'C2': '0', 'C3': '0', 'C4': '0', 'C7': '0'}

            self.lba_start = 0
            self.lba_end = 0
            self.lba_step = 0

            self.color = {
                'red': "#ff0000",  # red
                'orange': "#ff8800",  # orange
                'yellow': "#ffff00",  # yellow
                'yellow_green': "#ccff00",  # yellow green
                'green': "#00ff00",  # green
                'green-blue': "#00ff88",  # green-xx
                'blue': "#55ff00",  # blue
            }

            # " text-align: center; }}" \

            self.progressBarStyleSheetTemplate = \
                "QProgressBar {{" \
                " border: 1px solid black;" \
                " border-radius: 1px;" \
                " text-align: right; }}" \
                "QProgressBar::chunk:horizontal {{" \
                " background-color: {0};" \
                " width: 1px;" \
                " margin: 0px;}}"

            # self.setStyleSheet(self.progressBarStyleSheetTemplate.format(self.color[yellow_green]))

            self.frame = QtWidgets.QFrame(widget)
            self.frame.setGeometry(position)
            self.frame.setStyleSheet("")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame" + "slotnum")

            self.line_0 = QtWidgets.QFrame(self.frame)
            self.line_0.setGeometry(QtCore.QRect(0, 0, 160, 2))
            self.line_0.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_0.setObjectName("line_0")

            self.line_2 = QtWidgets.QFrame(self.frame)
            self.line_2.setGeometry(QtCore.QRect(0, 0, 2, 700))
            self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_2.setObjectName("line_2")

            self.line_3 = QtWidgets.QFrame(self.frame)
            self.line_3.setGeometry(QtCore.QRect(159, 0, 2, 700))
            self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_3.setObjectName("line_3")

            self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
            self.lcdNumber.setGeometry(QtCore.QRect(60, 4, 40, 60))
            self.lcdNumber.setDigitCount(1)
            self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
            self.lcdNumber.setStyleSheet("color:white;background:gray")
            self.lcdNumber.setProperty("value", slotnum)
            self.lcdNumber.setObjectName("lcdNumber")

            self.label_progress = QtWidgets.QLabel(self.frame)
            # self.label_progress.setGeometry(QtCore.QRect(51, 70, 60, 20))
            self.label_progress.setGeometry(QtCore.QRect(3, 66, 155, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Arial")
            font.setBold(True)
            self.label_progress.setFont(font)
            self.label_progress.setStyleSheet("color:red;")
            self.label_progress.setAlignment(QtCore.Qt.AlignCenter)
            self.label_progress.setFont(font)
            self.label_progress.setObjectName("label_progress")
            self.progressValue = 0
            # self.label_progress.setText("TH10: 10:0000 Dumping")
            self.label_progress.setText("")

            self.label_scsi_id = QtWidgets.QLabel(self.frame)
            self.label_scsi_id.setGeometry(QtCore.QRect(40, 78, 80, 30))
            font = QtGui.QFont()
            font.setPointSize(13)
            font.setFamily("Arial")
            font.setBold(True)
            self.label_scsi_id.setFont(font)
            self.label_scsi_id.setAutoFillBackground(False)
            self.label_scsi_id.setStyleSheet("color:#00C78C;")
            self.label_scsi_id.setAlignment(QtCore.Qt.AlignCenter)
            self.label_scsi_id.setObjectName("label_scsi_id")
            # self.label_scsi_id.setText("0:0:0:0")
            self.label_scsi_id.setText("-:-:-:-")

            self.label_sdx = QtWidgets.QLabel(self.frame)
            self.label_sdx.setGeometry(QtCore.QRect(40, 95, 80, 30))
            font = QtGui.QFont()
            font.setPointSize(13)
            font.setFamily("Arial")
            font.setBold(True)
            self.label_sdx.setFont(font)
            self.label_sdx.setAutoFillBackground(False)
            self.label_sdx.setStyleSheet("color:blue;")
            self.label_sdx.setAlignment(QtCore.Qt.AlignCenter)
            self.label_sdx.setObjectName("label_sdx")
            self.label_sdx.setText("")

            self.label_disknameValue = QtWidgets.QLabel(self.frame)
            self.label_disknameValue.setGeometry(QtCore.QRect(1, 120, 158, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            # font.setFamily("Arial")
            font.setBold(True)
            self.label_disknameValue.setFont(font)
            self.label_disknameValue.setStyleSheet("color:blue;")
            self.label_disknameValue.setAlignment(QtCore.Qt.AlignCenter)
            self.label_disknameValue.setFont(font)
            self.label_disknameValue.setObjectName("label_disknameValue")
            # self.label_disknameValue.setText("Faspeed K6-120G12345")
            self.label_disknameValue.setText("")

            self.label_fwVersionValue = QtWidgets.QLabel(self.frame)
            self.label_fwVersionValue.setGeometry(QtCore.QRect(5, 138, 73, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            # font.setFamily("Arial")
            font.setBold(True)
            self.label_fwVersionValue.setFont(font)
            self.label_fwVersionValue.setStyleSheet("color:green;")
            self.label_fwVersionValue.setAlignment(QtCore.Qt.AlignRight)
            self.label_fwVersionValue.setFont(font)
            self.label_fwVersionValue.setObjectName("label_fwVersionValue")
            # self.label_fwVersionValue.setText("{}".format("Q0525A"))
            self.label_fwVersionValue.setText("")

            self.label_sizeValue = QtWidgets.QLabel(self.frame)
            self.label_sizeValue.setGeometry(QtCore.QRect(82, 138, 70, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            # font.setFamily("Arial")
            font.setBold(True)
            self.label_sizeValue.setFont(font)
            self.label_sizeValue.setStyleSheet("color:blue;")
            self.label_sizeValue.setAlignment(QtCore.Qt.AlignLeft)
            self.label_sizeValue.setFont(font)
            self.label_sizeValue.setObjectName("label_sizeValue")
            # self.label_sizeValue.setText("{}GB".format("120"))
            self.label_sizeValue.setText("")

            self.label_snValue = QtWidgets.QLabel(self.frame)
            self.label_snValue.setGeometry(QtCore.QRect(2, 150, 156, 20))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Arial")
            font.setBold(True)
            self.label_snValue.setFont(font)
            self.label_snValue.setStyleSheet("color:blue;")
            self.label_snValue.setAlignment(QtCore.Qt.AlignCenter)
            self.label_snValue.setFont(font)
            self.label_snValue.setObjectName("label_snValue")
            # self.label_snValue.setText("12345678900987654321")
            self.label_snValue.setText("")

            self.line_4 = QtWidgets.QFrame(self.frame)
            self.line_4.setGeometry(QtCore.QRect(0, 170, 160, 2))
            self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_4.setObjectName("line_4")

            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Arial")
            font.setBold(True)
            self.pushButton_TH0 = QtWidgets.QPushButton(self.frame)
            self.pushButton_TH0.setFont(font)
            self.pushButton_TH0.setGeometry(QtCore.QRect(4, 173, 35, 25))
            self.pushButton_TH0.setObjectName("pushButton_TH0")
            self.pushButton_TH0.setText("TH0")

            self.pushButton_TH02 = QtWidgets.QPushButton(self.frame)
            self.pushButton_TH02.setFont(font)
            self.pushButton_TH02.setGeometry(QtCore.QRect(42, 173, 36, 25))
            self.pushButton_TH02.setObjectName("pushButton_TH02")
            self.pushButton_TH02.setText("TH.2")

            self.pushButton_TH1 = QtWidgets.QPushButton(self.frame)
            self.pushButton_TH1.setFont(font)
            self.pushButton_TH1.setGeometry(QtCore.QRect(81, 173, 36, 25))
            self.pushButton_TH1.setObjectName("pushButton_TH1")
            self.pushButton_TH1.setText("TH1")

            self.pushButton_TH3 = QtWidgets.QPushButton(self.frame)
            self.pushButton_TH3.setFont(font)
            self.pushButton_TH3.setGeometry(QtCore.QRect(120, 173, 36, 25))
            self.pushButton_TH3.setObjectName("pushButton_TH3")
            self.pushButton_TH3.setText("TH3")

            self.pushButton_TH5 = QtWidgets.QPushButton(self.frame)
            self.pushButton_TH5.setFont(font)
            self.pushButton_TH5.setGeometry(QtCore.QRect(4, 200, 35, 25))
            self.pushButton_TH5.setObjectName("pushButton_TH5")
            self.pushButton_TH5.setText("TH5")

            self.pushButton_TH10 = QtWidgets.QPushButton(self.frame)
            self.pushButton_TH10.setFont(font)
            self.pushButton_TH10.setGeometry(QtCore.QRect(42, 200, 36, 25))
            self.pushButton_TH10.setObjectName("pushButton_TH10")
            self.pushButton_TH10.setText("TH10")

            self.pushButton_RO1 = QtWidgets.QPushButton(self.frame)
            self.pushButton_RO1.setFont(font)
            self.pushButton_RO1.setGeometry(QtCore.QRect(81, 200, 36, 25))
            self.pushButton_RO1.setObjectName("pushButton_RO1")
            self.pushButton_RO1.setText("RO1")

            self.pushButton_VY1 = QtWidgets.QPushButton(self.frame)
            self.pushButton_VY1.setFont(font)
            self.pushButton_VY1.setGeometry(QtCore.QRect(120, 200, 36, 25))
            self.pushButton_VY1.setObjectName("pushButton_VY1")
            self.pushButton_VY1.setText("VY1")

            self.line_41 = QtWidgets.QFrame(self.frame)
            self.line_41.setGeometry(QtCore.QRect(0, 227, 160, 2))
            self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_41.setObjectName("line_41")

            self.label_rwspeed = QtWidgets.QLabel(self.frame)
            self.label_rwspeed.setGeometry(QtCore.QRect(3, 229, 155, 15))
            font = QtGui.QFont()
            font.setPointSize(10)
            # font.setFamily("Mono")
            font.setFamily("Arial")
            font.setBold(True)
            self.label_rwspeed.setFont(font)
            self.label_rwspeed.setStyleSheet("color:green;")
            self.label_rwspeed.setAlignment(QtCore.Qt.AlignCenter)
            self.label_rwspeed.setFont(font)
            self.label_rwspeed.setObjectName("label_progress")
            self.progressValue = 0
            self.label_rwspeed.setText("R/W[{}/{}]MB/s".format(self.writeSpeed, self.readSpeed))

            self.line_5 = QtWidgets.QFrame(self.frame)
            self.line_5.setGeometry(QtCore.QRect(0, 245, 160, 2))
            self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_5.setObjectName("line_5")

            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Arial")
            # font.setBold(True)
            self.pushButton_DeleteDisk = QtWidgets.QPushButton(self.frame)
            self.pushButton_DeleteDisk.setFont(font)
            self.pushButton_DeleteDisk.setGeometry(QtCore.QRect(4, 247, 75, 22))
            self.pushButton_DeleteDisk.setObjectName("pushButton_DeleteDisk")
            self.pushButton_DeleteDisk.setText("删除硬盘")

            self.pushButton_ReflashDisk = QtWidgets.QPushButton(self.frame)
            self.pushButton_ReflashDisk.setFont(font)
            self.pushButton_ReflashDisk.setGeometry(QtCore.QRect(81, 247, 75, 22))
            self.pushButton_ReflashDisk.setObjectName("pushButton_ReflashDisk")
            self.pushButton_ReflashDisk.setText("手动刷新")

            self.line_6 = QtWidgets.QFrame(self.frame)
            self.line_6.setGeometry(QtCore.QRect(0, 270, 160, 2))
            self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_6.setObjectName("line_6")

            self.testFlag = "NOT_TEST"
            self.testCycleNow = 0
            self.testCyclePercent = 0
            self.testCycle = 0
            self.testStartTime = 0
            self.progressBar = [0 for x in range(0, 10)]
            self.eachCycleUsedTime = [0 for x in range(0, 10)]
            self.label_TestUsedTime = [0 for x in range(0, 10)]
            self.label_TestResult = [0 for x in range(0, 10)]
            self.label_TestResultTemp = [0 for x in range(0, 10)]
            for i in range(0, 10):
                self.progressBar[i] = QtWidgets.QProgressBar(self.frame)
                self.progressBar[i].setGeometry(QtCore.QRect(3, 275 + i * 20, 154, 18))
                self.progressBar[i].setProperty("value", 0)
                self.progressBar[i].setTextVisible(True)
                font = QtGui.QFont()
                font.setPointSize(10)
                # font.setFamily("Arial")
                font.setBold(True)
                self.progressBar[i].setFont(font)
                self.progressBar[i].setStyleSheet(self.progressBarStyleSheetTemplate.format(self.color['green']))
                self.progressBar[i].setOrientation(QtCore.Qt.Horizontal)
                self.progressBar[i].setTextDirection(QtWidgets.QProgressBar.TopToBottom)
                self.progressBar[i].setObjectName("progressBar{}".format(i))
                # self.progressBar[i].setValue(100)

                self.eachCycleUsedTime[i] = 0

                self.label_TestUsedTime[i] = QtWidgets.QLabel(self.frame)
                self.label_TestUsedTime[i].setGeometry(QtCore.QRect(10, 277 + i * 20, 50, 18))
                font = QtGui.QFont()
                font.setPointSize(10)
                # font.setFamily("Arial")
                font.setFamily("Mono")
                # font.setBold(True)
                self.label_TestUsedTime[i].setFont(font)
                self.label_TestUsedTime[i].setStyleSheet("color:black;")
                self.label_TestUsedTime[i].setAlignment(QtCore.Qt.AlignLeft)
                self.label_TestUsedTime[i].setFont(font)
                self.label_TestUsedTime[i].setObjectName("label_TestUsedTime{}".format(i))
                # self.label_TestUsedTime[i].setText("300m25s")
                self.label_TestUsedTime[i].setText("")

                self.label_TestResult[i] = QtWidgets.QLabel(self.frame)
                self.label_TestResult[i].setGeometry(QtCore.QRect(65, 277 + i * 20, 91, 14))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setFamily("Mono")
                # font.setFamily("Mono")
                # font.setBold(True)
                self.label_TestResult[i].setFont(font)
                self.label_TestResult[i].setStyleSheet("color:black;")
                self.label_TestResult[i].setAlignment(QtCore.Qt.AlignLeft)
                self.label_TestResult[i].setFont(font)
                self.label_TestResult[i].setObjectName("label_TestResult{}".format(i))
                # self.label_TestResult[i].setText("PS[05]68")
                self.label_TestResult[i].setText("")

                self.label_TestResultTemp[i] = QtWidgets.QLabel(self.frame)
                self.label_TestResultTemp[i].setGeometry(QtCore.QRect(65, 277 + i * 20, 30, 14))
                self.label_TestResultTemp[i].setFont(font)
                self.label_TestResultTemp[i].setStyleSheet("color:black;")
                self.label_TestResultTemp[i].setAlignment(QtCore.Qt.AlignLeft)
                self.label_TestResultTemp[i].setFont(font)
                self.label_TestResultTemp[i].setObjectName("label_TestResult{}".format(i))
                # self.label_TestResultTemp[i].setText("PS[05]68")
                self.label_TestResultTemp[i].setText("")


            self.line_7 = QtWidgets.QFrame(self.frame)
            self.line_7.setGeometry(QtCore.QRect(0, 477, 160, 2))
            self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_7.setObjectName("line_7")

            self.label_smartName = [0 for x in range(0, 7)]
            self.label_smartValue = [0 for x in range(0, 7)]
            for i in range(0, 7):
                self.label_smartName[i] = QtWidgets.QLabel(self.frame)
                self.label_smartName[i].setGeometry(QtCore.QRect(5, 480 + i * 20, 80, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                # font.setFamily("Arial")
                font.setFamily("Mono")
                # font.setBold(True)
                self.label_smartName[i].setFont(font)
                self.label_smartName[i].setStyleSheet("color:black;")
                self.label_smartName[i].setAlignment(QtCore.Qt.AlignLeft)
                self.label_smartName[i].setFont(font)
                self.label_smartName[i].setObjectName("label_smartName{}".format(i))
                self.label_smartName[i].setText("")
                # self.label_smartName[i].setText("{:02X}:".format(i))


                self.label_smartValue[i] = QtWidgets.QLabel(self.frame)
                self.label_smartValue[i].setGeometry(QtCore.QRect(88, 481 + i * 20, 67, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                # font.setFamily("Arial")
                font.setFamily("Mono")
                font.setBold(True)
                self.label_smartValue[i].setFont(font)
                self.label_smartValue[i].setStyleSheet("color:blue;")
                self.label_smartValue[i].setAlignment(QtCore.Qt.AlignLeft)
                self.label_smartValue[i].setFont(font)
                self.label_smartValue[i].setObjectName("label_smartValue{}".format(i))
                self.label_smartValue[i].setText("")
                # self.label_smartValue[i].setText("{:02X}:".format(i))

            self.testDiskSn = ""
            self.nowDiskSn = ""

            # 创建定时器
            self.timer_testProgress = QtCore.QTimer(self.pp)
            self.__attach_events()

        def __attach_events(self):
            self.sin.connect(self.updateDiskTestResult)
            self.pushButton_TH0.clicked.connect(lambda: self.On_THxx(self.pushButton_TH0, TEST_ITEM_TH0))
            self.pushButton_TH02.clicked.connect(lambda: self.On_THxx(self.pushButton_TH02, TEST_ITEM_TH02))
            self.pushButton_TH1.clicked.connect(lambda: self.On_THxx(self.pushButton_TH1, TEST_ITEM_TH1))
            self.pushButton_TH3.clicked.connect(lambda: self.On_THxx(self.pushButton_TH3, TEST_ITEM_TH3))
            self.pushButton_TH5.clicked.connect(lambda: self.On_THxx(self.pushButton_TH5, TEST_ITEM_TH5))
            self.pushButton_TH10.clicked.connect(lambda: self.On_THxx(self.pushButton_TH10, TEST_ITEM_TH10))
            self.pushButton_RO1.clicked.connect(lambda: self.On_THxx(self.pushButton_RO1, TEST_ITEM_RO1))
            self.pushButton_VY1.clicked.connect(lambda: self.On_THxx(self.pushButton_VY1, TEST_ITEM_VY1))

            self.timer_testProgress.timeout.connect(self.OnTestProgressTimer)

            self.pushButton_DeleteDisk.clicked.connect(self.On_DeleteDisk)
            self.pushButton_ReflashDisk.clicked.connect(self.On_ReflashDisk)

        def On_DeleteDisk(self):
            self.SlotDeleteDisk()

        def On_ReflashDisk(self):
            for i in range(0, 7):
                self.label_smartName[i].setText("")
                self.label_smartValue[i].setText("")
                self.label_smartValue[i].setStyleSheet("color:blue;")
            self.SlotIDtoScsiID()

        def SetAllTestButtonDisable(self):
            self.pushButton_TH0.setEnabled(False)
            self.pushButton_TH02.setEnabled(False)
            self.pushButton_TH1.setEnabled(False)
            self.pushButton_TH3.setEnabled(False)
            self.pushButton_TH5.setEnabled(False)
            self.pushButton_TH10.setEnabled(False)
            self.pushButton_RO1.setEnabled(False)
            self.pushButton_VY1.setEnabled(False)
            self.pushButton_TH0.setStyleSheet("color:white; background:gray")
            self.pushButton_TH02.setStyleSheet("color:white; background:gray")
            self.pushButton_TH1.setStyleSheet("color:white; background:gray")
            self.pushButton_TH3.setStyleSheet("color:white; background:gray")
            self.pushButton_TH5.setStyleSheet("color:white; background:gray")
            self.pushButton_TH10.setStyleSheet("color:white; background:gray")
            self.pushButton_RO1.setStyleSheet("color:white; background:gray")
            self.pushButton_VY1.setStyleSheet("color:white; background:gray")

        def SetAllTestButtonEnable(self):
            self.pushButton_TH0.setEnabled(True)
            self.pushButton_TH02.setEnabled(True)
            self.pushButton_TH1.setEnabled(True)
            self.pushButton_TH3.setEnabled(True)
            self.pushButton_TH5.setEnabled(True)
            self.pushButton_TH10.setEnabled(True)
            self.pushButton_RO1.setEnabled(True)
            self.pushButton_VY1.setEnabled(True)
            self.pushButton_TH0.setStyleSheet("color:black;")
            self.pushButton_TH02.setStyleSheet("color:black;")
            self.pushButton_TH1.setStyleSheet("color:black;")
            self.pushButton_TH3.setStyleSheet("color:black;")
            self.pushButton_TH5.setStyleSheet("color:black;")
            self.pushButton_TH10.setStyleSheet("color:black;")
            self.pushButton_RO1.setStyleSheet("color:black;")
            self.pushButton_VY1.setStyleSheet("color:black;")

        def On_THxx(self, button, testName):
            if self.testItem == TEST_ITEM_NONE:
                self.InitTest()

                if self.sdxx != "":
                    self.SetAllTestButtonDisable()
                    button.setStyleSheet("color:white;""background:purple")
                    self.testItem = testName
                    self.testDiskSn = self.nowDiskSn
                    self.testCycleNow = 0
                    self.testStartTime = 0
                    self.writeSpeed = "0"
                    self.readSpeed = "0"
                    for i in range(0, 10):
                        self.progressBar[i].setValue(0)
                        self.eachCycleUsedTime[i] = 0
                        self.label_TestUsedTime[i].setText("")
                        self.label_TestResult[i].setText("")
                        self.label_TestResult[i].setStyleSheet("")

                    self.testFlag = "RUNNING"
                    shownum = sid_to_slotnum[self.scsi_id]
                    self.pp.STB_LED_PointFlashCtl(shownum, 1)
                    self.SlotDiskTestThread.start()
                    self.pp.tab6_SlotTestingCount = self.pp.tab6_SlotTestingCount + 1
                    self.timer_testProgress.start(1000)

                else:
                    for i in range(0, 10):
                        self.progressBar[i].setValue(0)
                        self.eachCycleUsedTime[i] = 0
                        self.label_TestUsedTime[i].setText("")
                        self.label_TestResult[i].setText("")
                        self.label_TestResult[i].setStyleSheet("")
                    shownum = sid_to_slotnum[self.scsi_id]
                    self.pp.STB_LED_NumFlashCtl(shownum, 0)
                    self.pp.STB_LED_PointFlashCtl(shownum, 0)
                    self.pp.STB_LED_Show(shownum, 20)

        def OnTestProgressTimer(self):
            # print("in OnTestProgressTimer")
            # print("{} self.testFlag = {}".format(self.sdxx, self.testFlag))
            if self.testFlag == "RUNNING":
                try:
                    f = os.popen('rw3_show -c {}'.format(diskid[self.sdxx]))
                    rw = f.readlines()

                    rws = rw[0].replace('\n', '').strip()
                    rwlist = rws.split(' ')
                    # print("{} rwlist = {}".format(self.sdxx, rwlist))
                except:
                    pass

                try:
                    self.progressValue = rwlist[2]
                    # print("{} self.progressValue = {} - {}".format(self.sdxx, self.progressValue, int(self.progressValue)))
                    if rwlist[1] == "Writing":
                        if self.testItem == TEST_ITEM_TH0 or self.testItem ==  TEST_ITEM_TH02:
                            self.label_progress.setText("{} : {:0.4f} Writing".format(self.testItem, self.testCycleNow + float(self.progressValue) / 100))
                        else:
                            self.label_progress.setText("{} : {:0.4f} Writing".format(self.testItem, self.testCycleNow + float(self.testCyclePercent / 100) + float(self.progressValue) / 1000))

                        self.label_progress.setStyleSheet("color:red;")
                        self.progressBar[self.testCycleNow].setValue(int(float(self.progressValue)))
                        self.progressBar[self.testCycleNow].setStyleSheet(
                            self.progressBarStyleSheetTemplate.format('#00C957'))
                    elif rwlist[1] == "Dumping" or rwlist[1] == "Verifying":
                        if self.testItem == TEST_ITEM_TH0 or self.testItem ==  TEST_ITEM_TH02:
                            self.label_progress.setText("{} : {:0.4f} Dumping".format(self.testItem, self.testCycleNow + float(self.progressValue) / 100))
                        else:
                            self.label_progress.setText("{} : {:0.4f} Dumping".format(self.testItem, self.testCycleNow + float(self.testCyclePercent / 100) + float(self.progressValue) / 1000))

                        self.label_progress.setStyleSheet("color:green;")
                        self.progressBar[self.testCycleNow].setValue(int(float(self.progressValue)))
                        self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format('#00FF7F'))

                    if rwlist[1] == "Writing":
                        self.writeSpeed = rwlist[3].replace('MB/s', '')
                    elif rwlist[1] == "Dumping" or rwlist[1] == "Verifying":
                        self.readSpeed = rwlist[3].replace('MB/s', '')

                    self.label_rwspeed.setText("R/W[{}/{}]MB/s".format(self.readSpeed, self.writeSpeed))

                    now_time = time.time()
                    self.label_TestUsedTime[self.testCycleNow].setText(
                        "{}m{}s".format(int((now_time - self.testStartTime) / 60),
                                        int((now_time - self.testStartTime) % 60)))
                except:
                    pass

            # print("{} self.testFlag = {}".format(self.sdxx, self.testFlag))
            if self.testFlag == "FINISH":
                self.timer_testProgress.stop()
                self.SlotDiskTestThread.__del__()
                self.SetAllTestButtonEnable()
                self.testItem = TEST_ITEM_NONE
                shownum = sid_to_slotnum[self.scsi_id]
                self.pp.STB_LED_PointFlashCtl(shownum, 0)
                self.pp.tab3_SlotTestingCount = self.pp.tab6_SlotTestingCount - 1
            else:
                self.timer_testProgress.start(500)

        def updateDiskTestResult(self):
            print("in updateDiskTestResult")

            self.progressValue = 100.00
            self.label_progress.setText("{:0.2f}".format(float(self.progressValue) / 100))

            self.progressBar[diskid[self.sdxx]].setValue(int(self.progressValue))

            self.timer_testProgress.stop()

        def GetSmartInfo(self, sdxx):

            ID01_raw_read_error_rate = 1
            ID05_reallocated_sectors_count = 5
            ID09_power_on_hours = 9
            ID0C_power_cycle_count = 12
            IDA3_original_bad_count = 163
            IDA7_average_erase_count = 167
            IDC2_temperature = 194
            IDC3_read_retry = 195
            IDC4_reallocation_event_count = 196
            IDC7_ultraDMA_CRC_error_count = 199
            IDF1_total_host_written = 241
            IDF2_total_host_read = 242

            small = []
            sml = []

            try:
                f = os.popen("smartctl -i /dev/{} | grep 'Firmware'".format(sdxx))
                sm = f.readlines()
                ver = sm[0].replace('Firmware Version:', '').replace('\n', '').strip()
                self.label_fwVersionValue.setText(ver)

                f = os.popen("smartctl -i /dev/{} | grep 'Device Model:'".format(sdxx))
                sm = f.readlines()
                name = sm[0].replace('Device Model:', '').replace('\n', '').strip()
                self.label_disknameValue.setText(name)

                f = os.popen("smartctl -s on -A /dev/{} | grep 0x0".format(sdxx))
                sm = f.readlines()
                for i in sm:
                    smll = []
                    sml = i.replace('\n', '').strip()
                    sm_1space = sml.replace('   ', ' ').replace('   ', ' ').replace('  ', ' ').replace('  ', ' ')
                    smlist = sm_1space.split(' ')

                    smll.append(smlist[0])
                    smll.append(smlist[1])
                    smll.append(smlist[9])

                    small.append(smll)

                # 读到结果为空，说明读取samrt失败，可能原因是 WE，RE，DL等原因，此种情况，不更新smart信息
                if len(sm) != 0:

                    n = 0
                    for (id, name, value) in small:
                        if int(id) == ID01_raw_read_error_rate:
                            self.label_smartName[n].setText("{:02X}:读错误率".format(int(id)))
                            self.label_smartName[n].setStyleSheet("color:black;")
                            self.label_smartValue[n].setText("{}".format(value))
                            if int(value) != 0:
                                self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                            else:
                                self.label_smartValue[n].setStyleSheet("color:blue;")
                            n = n + 1
                            self.smartDict_now['01'] = value

                        elif int(id) == ID05_reallocated_sectors_count:
                            self.label_smartName[n].setText("{:02X}:新增坏块".format(int(id)))
                            self.label_smartName[n].setStyleSheet("color:black;")
                            self.label_smartValue[n].setText("{}".format(value))
                            if int(value) != 0:
                                self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                            else:
                                self.label_smartValue[n].setStyleSheet("color:blue;")
                            n = n + 1
                            self.smartDict_now['05'] = value

                        elif int(id) == IDA3_original_bad_count:
                            self.label_smartName[n].setText("{:02X}:原始坏块".format(int(id)))
                            self.label_smartName[n].setStyleSheet("color:black;")
                            self.label_smartValue[n].setText("{}".format(value))
                            self.label_smartValue[n].setStyleSheet("color:blue;")
                            n = n + 1
                            self.smartDict_now['A3'] = int(value)

                        elif int(id) == IDC2_temperature:
                            self.label_smartName[n].setText("{:02X}:主控温度".format(int(id)))
                            self.label_smartName[n].setStyleSheet("color:black;")
                            self.label_smartValue[n].setText("{}".format(value))
                            if int(value) > 40:
                                self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                            else:
                                self.label_smartValue[n].setStyleSheet("color:blue;")
                            n = n + 1
                            self.smartDict_now['C2'] = value

                        elif int(id) == IDC3_read_retry:
                            self.label_smartName[n].setText("{:02X}:重读次数".format(int(id)))
                            self.label_smartName[n].setStyleSheet("color:black;")
                            self.label_smartValue[n].setText("{}".format(value))
                            if int(value) != 0:
                                self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                            else:
                                self.label_smartValue[n].setStyleSheet("color:blue;")
                            n = n + 1
                            self.smartDict_now['C3'] = value

                        elif int(id) == IDC4_reallocation_event_count:
                            self.label_smartName[n].setText("{:02X}:读取失败".format(int(id)))
                            self.label_smartName[n].setStyleSheet("color:black;")
                            self.label_smartValue[n].setText("{}".format(value))
                            if int(value) != 0:
                                self.label_smartValue[n].setStyleSheet("color:white;""background:red;")
                            else:
                                self.label_smartValue[n].setStyleSheet("color:blue;")
                            n = n + 1
                            self.smartDict_now['C4'] = value

                        elif int(id) == IDC7_ultraDMA_CRC_error_count:
                            self.label_smartName[n].setText("{:02X}:链路重传".format(int(id)))
                            self.label_smartName[n].setStyleSheet("color:black;")
                            self.label_smartValue[n].setText("{}".format(value))
                            if int(value) != 0:
                                self.label_smartValue[n].setStyleSheet("color:white;""background:orange;")
                            else:
                                self.label_smartValue[n].setStyleSheet("color:blue;")
                            n = n + 1
                            self.smartDict_now['C7'] = value

                    # 清空没有用到的ID内容
                    for i in range(n, 7):
                        self.label_smartName[i].setText("")
                        self.label_smartValue[i].setText("")
            except:
                self.smartDict_now['01'] = '*'
                self.smartDict_now['05'] = '*'
                self.smartDict_now['A3'] = '*'
                self.smartDict_now['C2'] = '*'
                self.smartDict_now['C3'] = '*'
                self.smartDict_now['C4'] = '*'
                self.smartDict_now['C7'] = '*'

        def UpdateSmartOld(self):
            self.smartDict_old['01'] = self.smartDict_now['01']
            self.smartDict_old['05'] = self.smartDict_now['05']
            self.smartDict_old['A3'] = self.smartDict_now['A3']
            self.smartDict_old['C2'] = self.smartDict_now['C2']
            self.smartDict_old['C3'] = self.smartDict_now['C3']
            self.smartDict_old['C4'] = self.smartDict_now['C4']
            self.smartDict_old['C7'] = self.smartDict_now['C7']

        def InitTest(self):
            try:
                self.disklist = get_disk_info()
                for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                    # print("[{}] {} {} {} {} {}".format(self.slotnum, scsiid, sdxx, size_GB, deviceName, sn))
                    if self.scsi_id == scsiid:
                        self.label_scsi_id.setText("{}".format(scsiid))
                        self.label_sdx.setText("{}".format(sdxx))
                        # self.label_disknameValue.setText(deviceName)
                        self.label_snValue.setText(sn)

                        self.label_sizeValue.setText(size_GB)
                        try:
                            os.system("echo 2 > /sys/block/{}/device/eh_timeout".format(sdxx))
                            os.system("echo 2 > /sys/block/{}/device/timeout".format(sdxx))
                            os.system("echo 1 > /sys/block/{}/device/queue_depth".format(sdxx))
                        except:
                            pass

                        self.lcdNumber.setStyleSheet("color:red;background:#888888")

                        self.sdxx = sdxx
                        self.secSize = secSize
                        self.nowDiskSn = sn

                        self.FirstSmartResultCtl(sdxx)
                        self.UpdateSmartOld()

                        break

                if n == (len(self.disklist) - 1):
                    self.lcdNumber.setStyleSheet("color:white;background:#DDDDDD")
                    self.label_scsi_id.setText("-:-:-:-")
                    self.label_sdx.setText("")
                    self.label_disknameValue.setText("")
                    self.label_snValue.setText("")
                    self.label_sizeValue.setText("")
                    self.label_fwVersionValue.setText("")
                    self.sdxx = ""
                    self.secSize = ""
                    self.nowDiskSn = ""
                    for i in range(0, 7):
                        self.label_smartName[i].setText("")
                        self.label_smartValue[i].setText("")
                        self.label_smartValue[i].setStyleSheet("color:blue;")

            except:
                pass

        def SlotIDtoScsiID(self):
            try:
                self.disklist = get_disk_info()
                for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                    # print("[{}] {} {} {} {} {}".format(self.slotnum, scsiid, sdxx, size_GB, deviceName, sn))
                    if self.scsi_id == scsiid:
                        self.label_scsi_id.setText("{}".format(scsiid))
                        self.label_sdx.setText("{}".format(sdxx))
                        # self.label_disknameValue.setText(deviceName)
                        self.label_snValue.setText(sn)

                        self.label_sizeValue.setText(size_GB)
                        try:
                            os.system("echo 2 > /sys/block/{}/device/eh_timeout".format(sdxx))
                            os.system("echo 2 > /sys/block/{}/device/timeout".format(sdxx))
                            os.system("echo 1 > /sys/block/{}/device/queue_depth".format(sdxx))
                        except:
                            pass

                        self.lcdNumber.setStyleSheet("color:red;background:#888888")
                        self.GetSmartInfo(sdxx)
                        self.UpdateSmartOld()
                        self.sdxx = sdxx
                        self.secSize = secSize
                        self.nowDiskSn = sn

                        break

                if n == (len(self.disklist) - 1):
                    # self.slotStatus = SLOT_EMPTY
                    self.lcdNumber.setStyleSheet("color:white;background:#DDDDDD")
                    self.label_scsi_id.setText("-:-:-:-")
                    self.label_sdx.setText("")
                    self.label_disknameValue.setText("")
                    self.label_snValue.setText("")
                    self.label_sizeValue.setText("")
                    self.label_fwVersionValue.setText("")
                    for i in range(0, 7):
                        self.label_smartName[i].setText("")
                        self.label_smartValue[i].setText("")
                        self.label_smartValue[i].setStyleSheet("color:blue;")

                    '''
                    #没有盘，不要做LED控制
                    if self.testItem == TEST_ITEM_NONE and self.sdxx == "":
                        shownum = sid_to_slotnum[self.scsi_id]
                        self.pp.STB_LED_NumFlashCtl(shownum, 0)
                        self.pp.STB_LED_PointFlashCtl(shownum, 0)
                        #self.pp.STB_LED_Show(shownum, 20)
                    '''
                # 手动刷新，不要对LED灯进行控制，第一次手动刷新，初始化LED状态
                if self.testItem == TEST_ITEM_NONE and self.slotStatus == SLOT_EMPTY:
                    self.slotStatus = SLOT_INSERT
                    shownum = sid_to_slotnum[self.scsi_id]
                    self.pp.STB_LED_NumFlashCtl(shownum, 0)
                    self.pp.STB_LED_PointFlashCtl(shownum, 0)
                    self.pp.STB_LED_Show(shownum, shownum)

            except:
                print("{} SlotIDtoScsiID except !!!!!!".format(self.sdxx))
                pass

        def SlotDeleteDisk(self):
            try:
                self.disklist = get_disk_info()
                for n, (sdxx, sn, size_GB, deviceName, scsiid, secSize) in enumerate(self.disklist):
                    if self.scsi_id == scsiid:
                        os.system("echo 1 > /sys/block/{}/device/delete".format(sdxx))
            except:
                print("{} SlotDeleteDisk except !!!!!!".format(self.sdxx))
                pass

        def SlotDeleteSmart(self):
            for i in range(0, 7):
                self.label_smartName[i].setStyleSheet("color:gray;")
                # self.label_smartValue[i].setText("")
                # self.label_smartName[i].setText("")

        def TestReturn(self, ret):
            self.GetSmartInfo(self.sdxx)

            shownum = sid_to_slotnum[self.scsi_id]
            ret = ret / 0x100
            if int(ret) == TEST_PASS:
                resultText = "PS"
                barColor = "#00FF7F"
            elif int(ret) == ERROR_RE_READ_DATA:
                resultText = "RE"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_CE_COMPARE_DATA:
                resultText = "CE"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_WE_WIRTE_DATA:
                resultText = "WE"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_AE_ABORT:
                resultText = "AE"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_TO_TIMEOUT:
                resultText = "TO"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_NE_NOMEM:
                resultText = "NE"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_RO_DISK:
                resultText = "RO"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_DL_NONE_DISK:
                resultText = "DL"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_US_UNSORTED:
                resultText = "US"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_UA_UNAUTHORIZATION:
                resultText = "UA"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_OV_RUN_TIME_COUNT_OVERFLOW:
                resultText = "OV"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            else:
                resultText = "UK"
                barColor = 'red'
                print("{} ret = {}".format(self.sdxx, ret))
                self.pp.STB_LED_NumFlashCtl(shownum, 1)

            if self.smartDict_now['01'] != self.smartDict_old['01']:
                resultText = resultText + "(01){}".format(self.smartDict_now['01'])
                if barColor != 'red':
                    barColor = 'red'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
                self.label_TestResult[self.testCycleNow].setText(resultText)
            elif self.smartDict_now['05'] != self.smartDict_old['05']:
                resultText = resultText + "(05){}".format(self.smartDict_now['05'])
                if barColor != 'red':
                    barColor = 'red'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
                self.label_TestResult[self.testCycleNow].setText(resultText)
            elif self.smartDict_now['C4'] != self.smartDict_now['C4']:
                resultText = resultText + "(C4){}".format(self.smartDict_now['C4'])
                if barColor != 'red':
                    barColor = 'red'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResult[self.testCycleNow].setStyleSheet("color:white;background:{}".format(barColor))
                self.label_TestResult[self.testCycleNow].setText(resultText)
            elif self.smartDict_now['C3'] != self.smartDict_old['C3']:
                resultText = resultText + "(C3){}".format(self.smartDict_now['C3'])
                if barColor != 'red':
                    barColor = 'yellow'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
                self.label_TestResult[self.testCycleNow].setText(resultText)
            elif self.smartDict_now['C7'] != self.smartDict_old['C7']:
                resultText = resultText + "(C7){}".format(self.smartDict_now['C7'])
                if barColor != 'red':
                    barColor = 'yellow'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
                self.label_TestResult[self.testCycleNow].setText(resultText)
            elif self.smartDict_now['C2'] > "40":
                resultText = resultText + "(C2){}".format(self.smartDict_now['C2'])
                if barColor != 'red':
                    barColor = 'yellow'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
                self.label_TestResult[self.testCycleNow].setText(resultText)
            else:
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResult[self.testCycleNow].setStyleSheet("color:black;background:{}".format(barColor))
                self.label_TestResult[self.testCycleNow].setText(resultText)

            if self.smartDict_now['01'] != "0" or self.smartDict_now['05'] != "0" or self.smartDict_now['C4'] != "0":
                # print("self.smartDict_now['01'] = {}".format(self.smartDict_now['01']))
                # print("self.smartDict_now['05'] = {}".format(self.smartDict_now['05']))
                # print("self.smartDict_now['C4'] = {}".format(self.smartDict_now['C4']))
                self.pp.STB_LED_NumFlashCtl(shownum, 1)

            self.UpdateSmartOld()

        def TestReturnTemp(self, ret):
            self.GetSmartInfo(self.sdxx)

            shownum = sid_to_slotnum[self.scsi_id]
            ret = ret / 0x100
            if int(ret) == TEST_PASS:
                #resultText = "PS"
                resultText = ""
                barColor = "#00FF7F"
            elif int(ret) == ERROR_RE_READ_DATA:
                resultText = "RE"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_CE_COMPARE_DATA:
                resultText = "CE"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_WE_WIRTE_DATA:
                resultText = "WE"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_AE_ABORT:
                resultText = "AE"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_TO_TIMEOUT:
                resultText = "TO"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_NE_NOMEM:
                resultText = "NE"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_RO_DISK:
                resultText = "RO"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_DL_NONE_DISK:
                resultText = "DL"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_US_UNSORTED:
                resultText = "US"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_UA_UNAUTHORIZATION:
                resultText = "UA"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            elif int(ret) == ERROR_OV_RUN_TIME_COUNT_OVERFLOW:
                resultText = "OV"
                barColor = 'red'
                self.pp.STB_LED_NumFlashCtl(shownum, 1)
            else:
                resultText = "UK"
                barColor = 'red'
                print("{} ret = {}".format(self.sdxx, ret))
                self.pp.STB_LED_NumFlashCtl(shownum, 1)

            if self.smartDict_now['01'] != self.smartDict_old['01']:
                resultText = resultText + "(01){}".format(self.smartDict_now['01'])
                if barColor != 'red':
                    barColor = 'red'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setStyleSheet("color:{}".format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setText(resultText)
            elif self.smartDict_now['05'] != self.smartDict_old['05']:
                resultText = resultText + "(05){}".format(self.smartDict_now['05'])
                if barColor != 'red':
                    barColor = 'red'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setStyleSheet("color:{}".format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setText(resultText)
            elif self.smartDict_now['C4'] != self.smartDict_now['C4']:
                resultText = resultText + "(C4){}".format(self.smartDict_now['C4'])
                if barColor != 'red':
                    barColor = 'red'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setStyleSheet("color:{}".format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setText(resultText)
            elif self.smartDict_now['C3'] != self.smartDict_old['C3']:
                resultText = resultText + "(C3){}".format(self.smartDict_now['C3'])
                if barColor != 'red':
                    barColor = 'yellow'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setStyleSheet("color:{}".format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setText(resultText)
            elif self.smartDict_now['C7'] != self.smartDict_old['C7']:
                resultText = resultText + "(C7){}".format(self.smartDict_now['C7'])
                if barColor != 'red':
                    barColor = 'yellow'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setStyleSheet("color:{}".format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setText(resultText)
            elif self.smartDict_now['C2'] > "40":
                resultText = resultText + "(C2){}".format(self.smartDict_now['C2'])
                if barColor != 'red':
                    barColor = 'yellow'
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setStyleSheet("color:{}".format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setText(resultText)
            else:
                self.progressBar[self.testCycleNow].setStyleSheet(self.progressBarStyleSheetTemplate.format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setStyleSheet("color:{}".format(barColor))
                self.label_TestResultTemp[self.testCycleNow].setText(resultText)

            if self.smartDict_now['01'] != "0" or self.smartDict_now['05'] != "0" or self.smartDict_now['C4'] != "0":
                # print("self.smartDict_now['01'] = {}".format(self.smartDict_now['01']))
                # print("self.smartDict_now['05'] = {}".format(self.smartDict_now['05']))
                # print("self.smartDict_now['C4'] = {}".format(self.smartDict_now['C4']))
                self.pp.STB_LED_NumFlashCtl(shownum, 1)

            self.UpdateSmartOld()

        def FirstSmartResultCtl(self, sdxx):
            # 恢复 LED 显示状态
            shownum = sid_to_slotnum[self.scsi_id]
            self.pp.STB_LED_NumFlashCtl(shownum, 0)
            self.pp.STB_LED_Show(shownum, shownum)
            # self.pp.STB_k()
            # self.pp.STB_K()
            # self.pp.STB_GetRuntime()

            # 初始化新测试硬盘状态
            self.smartDict_now['01'] = "0"
            self.smartDict_now['05'] = "0"
            self.smartDict_now['A3'] = "0"
            self.smartDict_now['C2'] = "0"
            self.smartDict_now['C3'] = "0"
            self.smartDict_now['C4'] = "0"
            self.smartDict_now['C7'] = "0"
            self.UpdateSmartOld()
            self.GetSmartInfo(sdxx)

            if self.smartDict_now['01'] != "0" or self.smartDict_now['05'] != "0" or self.smartDict_now['C4'] != "0":
                # print("self.smartDict_now['01'] = {}".format(self.smartDict_now['01']))
                # print("self.smartDict_now['05'] = {}".format(self.smartDict_now['05']))
                # print("self.smartDict_now['C4'] = {}".format(self.smartDict_now['C4']))
                self.pp.STB_LED_NumFlashCtl(shownum, 1)

LBA_START = 0
LBA_END_05G = (1048576 - 1)

# 2048 * 512 = 1M
ONCE_BLOCK_COUNT=2048

# one cycle eq xx percent
ONE_CYCLE=10
j_add=100/ONE_CYCLE


class SlotDiskTest_Thread_BIT(QtCore.QThread):

        def __init__(self, parent):
            self.sin = parent.sin
            self.mutex = parent.mutex
            super(SlotDiskTest_Thread_BIT, self).__init__()
            self.working = True
            self.pp = parent

        def __del__(self):
            self.working = False
            self.wait()

        def run(self):
            try:
                self.working = True
            except:
                pass

            while self.working == True:
                # if self.serial.isOpen():
                if True:
                    try:
                        # 1PERCENT start must be 512*2048 multi address
                        LBA_1PERCENT = self.pp.secSize / ONCE_BLOCK_COUNT
                        LBA_1PERCENT = LBA_1PERCENT / ONE_CYCLE
                        LBA_1PERCENT = LBA_1PERCENT * ONCE_BLOCK_COUNT

                        if self.pp.testItem == TEST_ITEM_TH0:
                            self.TH0()

                        if self.pp.testItem == TEST_ITEM_TH02:
                            self.TH02()

                        if self.pp.testItem == TEST_ITEM_TH1:
                            self.TH1()

                        if self.pp.testItem == TEST_ITEM_TH3:
                            self.TH3()

                        if self.pp.testItem == TEST_ITEM_TH5:
                            self.TH5()

                        if self.pp.testItem == TEST_ITEM_TH10:
                            self.TH10()

                        if self.pp.testItem == TEST_ITEM_RO1:
                            self.RO1()

                        if self.pp.testItem == TEST_ITEM_VY1:
                            self.VY1()

                        time.sleep(3)
                        self.working = False
                    except:
                        print("{}-{} running thread except ！！！！！！！！！！！".format(self.pp.sdxx, self.pp.testItem))
                        break
                        # pass

        def TH0(self):
            startTime = time.time()
            self.pp.testStartTime = startTime
            self.pp.testCycleNow = 0

            # first test 0.5G
            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                # print("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                #    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, LBA_END_05G, LBA_START))
                ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 100 -t 0x0000 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, LBA_END_05G, LBA_START))
            else:
                ret = ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(5)

            self.pp.TestReturn(ret)

            self.pp.testFlag = "FINISH"

        def TH02(self):
            startTime = time.time()
            self.pp.testStartTime = startTime
            self.pp.testCycleNow = 0

            if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                # print("stb_rw -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 1 -t 0x0000 -I {} /dev/{} {} {}".format(
                #    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, int(self.pp.secSize / 5), LBA_START))
                ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                    diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, (int(self.pp.secSize / 5) - 1), LBA_START))

            else:
                ret = ERROR_DL_NONE_DISK

            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(5)

            self.pp.TestReturn(ret)

            self.pp.testFlag = "FINISH"

        def TH1(self):
            startTime = time.time()
            self.pp.testStartTime = startTime
            self.pp.testCycleNow = 0
            self.pp.testCyclePercent = 0
            self.pp.lba_step = int(self.pp.secSize / ONCE_BLOCK_COUNT)
            self.pp.lba_step = int(self.pp.lba_step / ONE_CYCLE)
            self.pp.lba_step = int(self.pp.lba_step * ONCE_BLOCK_COUNT)

            # cycle 1
            startTime = time.time()
            self.pp.testStartTime = startTime

            rett = TEST_PASS * 0x100

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(5)

            self.pp.TestReturn(rett)

            self.pp.testFlag = "FINISH"

        def TH3(self):
            startTime = time.time()
            self.pp.testStartTime = startTime
            self.pp.testCycleNow = 0
            self.pp.testCyclePercent = 0
            self.pp.lba_step = int(self.pp.secSize / ONCE_BLOCK_COUNT)
            self.pp.lba_step = int(self.pp.lba_step / ONE_CYCLE)
            self.pp.lba_step = int(self.pp.lba_step * ONCE_BLOCK_COUNT)

            rett = TEST_PASS * 0x100
            # cycle 1
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x1234 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100

            # cycle 2
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x4321 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[1] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 3
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[2] = finishTime - startTime
            time.sleep(5)

            self.pp.TestReturn(ret)

            self.pp.testFlag = "FINISH"

        def TH5(self):
            startTime = time.time()
            self.pp.testStartTime = startTime
            self.pp.testCycleNow = 0
            self.pp.testCyclePercent = 0
            self.pp.lba_step = int(self.pp.secSize / ONCE_BLOCK_COUNT)
            self.pp.lba_step = int(self.pp.lba_step / ONE_CYCLE)
            self.pp.lba_step = int(self.pp.lba_step * ONCE_BLOCK_COUNT)

            rett = TEST_PASS * 0x100
            # cycle 1
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x1234 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 2
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x4321 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[1] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 3
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x55AA -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[2] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 4
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xAA55 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            # print("{} ret = = = {}".format(self.pp.sdxx, ret))
            finishTime = time.time()
            self.pp.eachCycleUsedTime[3] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 5
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            # print("{} ret = = = {}".format(self.pp.sdxx, ret))
            finishTime = time.time()
            self.pp.eachCycleUsedTime[4] = finishTime - startTime
            time.sleep(5)

            self.pp.TestReturn(ret)

            self.pp.testFlag = "FINISH"

        def TH10(self):
            startTime = time.time()
            self.pp.testStartTime = startTime
            self.pp.testCycleNow = 0
            self.pp.testCyclePercent = 0
            self.pp.lba_step = int(self.pp.secSize / ONCE_BLOCK_COUNT)
            self.pp.lba_step = int(self.pp.lba_step / ONE_CYCLE)
            self.pp.lba_step = int(self.pp.lba_step * ONCE_BLOCK_COUNT)

            rett = TEST_PASS * 0x100
            # cycle 1
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x1234 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 2
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x4321 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[1] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 3
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x55AA -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[2] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 4
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xAA55 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[3] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 5
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xEA3B -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            # print("{} ret = = = {}".format(self.pp.sdxx, ret))
            finishTime = time.time()
            self.pp.eachCycleUsedTime[4] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 6
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xFF00 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[5] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 7
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x00FF -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[6] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 8
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0xCCCC -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[7] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 9
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x3333 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[8] = finishTime - startTime
            time.sleep(2)

            self.pp.TestReturn(ret)
            self.pp.testCycleNow = self.pp.testCycleNow + 1
            self.pp.testCyclePercent = 0

            rett = TEST_PASS * 0x100
            # cycle 10
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 0 -L {} -w -s -e 3 -t 0x0000 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[9] = finishTime - startTime
            time.sleep(5)

            self.pp.TestReturn(ret)

            self.pp.testFlag = "FINISH"

        def RO1(self):
            startTime = time.time()
            self.pp.testStartTime = startTime
            self.pp.testCycleNow = 0
            self.pp.testCyclePercent = 0
            self.pp.lba_step = int(self.pp.secSize / ONCE_BLOCK_COUNT)
            self.pp.lba_step = int(self.pp.lba_step / ONE_CYCLE)
            self.pp.lba_step = int(self.pp.lba_step * ONCE_BLOCK_COUNT)

            rett = TEST_PASS * 0x100
            # cycle 1
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -r 1 -L {} -w -s -e 10 -t 0xEA3B -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(5)

            self.pp.TestReturn(ret)

            self.pp.testFlag = "FINISH"

        def VY1(self):
            startTime = time.time()
            self.pp.testStartTime = startTime
            self.pp.testCycleNow = 0
            self.pp.testCyclePercent = 0
            self.pp.lba_step = int(self.pp.secSize / ONCE_BLOCK_COUNT)
            self.pp.lba_step = int(self.pp.lba_step / ONE_CYCLE)
            self.pp.lba_step = int(self.pp.lba_step * ONCE_BLOCK_COUNT)

            rett = TEST_PASS * 0x100
            # cycle 1
            startTime = time.time()
            self.pp.testStartTime = startTime

            for i in range(0, ONE_CYCLE):

                self.pp.lba_start = i * self.pp.lba_step

                if i == (ONE_CYCLE-1):
                    self.pp.lba_end = (self.pp.secSize - 1)
                else:
                    self.pp.lba_end = self.pp.lba_start + self.pp.lba_step

                if self.pp.sdxx != "" and self.pp.testDiskSn == self.pp.nowDiskSn:
                    ret = os.system("stb_rw3 -b 512 -c 2048 -D 1 -R 1 -L {} -w -s -e 10 -t 0x0000 -I {} /dev/{} {} {}".format(
                        diskid[self.pp.sdxx], self.pp.testCycleNow, self.pp.sdxx, self.pp.lba_end, self.pp.lba_start))

                    # rett record the first error
                    if (rett / 0x100) == TEST_PASS:
                        rett = ret

                    self.pp.TestReturnTemp(rett)
                else:
                    rett = ERROR_DL_NONE_DISK

                if i != (ONE_CYCLE-1):
                    self.pp.testCyclePercent = self.pp.testCyclePercent + j_add

            finishTime = time.time()
            self.pp.eachCycleUsedTime[0] = finishTime - startTime
            time.sleep(5)

            self.pp.TestReturn(ret)

            self.pp.testFlag = "FINISH"


# MainWindow ###########################################################################################################

'''
App MainWindow
'''
class Ui_MainWindow(object):
    sinUpdateVIW = QtCore.pyqtSignal()
    mutex = threading.Lock()
    sinUpdateSlotDiskTest_0 = QtCore.pyqtSignal()
    sinUpdateSlotDiskTest_1 = QtCore.pyqtSignal()
    sinUpdateSlotDiskTest_2 = QtCore.pyqtSignal()
    sinUpdateSlotDiskTest_3 = QtCore.pyqtSignal()
    sinUpdateSlotDiskTest_4 = QtCore.pyqtSignal()
    sinUpdateSlotDiskTest_5 = QtCore.pyqtSignal()
    sinUpdateSlotDiskTest_6 = QtCore.pyqtSignal()
    def setupUi(self, MainWindow):
        self.mainwin = MainWindow
        self.serial = serial.Serial()
        self.serialThread = MonitorVIW_Thread(self)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 710)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 964, 680))
        self.tabWidget.setObjectName("tabWidget")

        # tab_1 ##################################################################
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")

        self.tab1_frame = [0, 1, 2, 3, 4, 5, 6]

        position = QtCore.QRect(0, 0, 960, 30)
        self.tab1_frame[0] = UartControl(self, self.tab_1, position)
        self.tab1_frame[0].On_UartPortFlash()
        self.tab1_frame[0].On_UartPortOpen()

        self.sinUpdateVIW.connect(self.updateVIW)

        position = QtCore.QRect(0, 30, 160, 680)
        self.tab1_frame[1] = SlotVIW(self, self.tab_1, position, 1)

        position = QtCore.QRect(160, 30, 160, 680)
        self.tab1_frame[2] = SlotVIW(self, self.tab_1, position, 2)

        position = QtCore.QRect(320, 30, 160, 680)
        self.tab1_frame[3] = SlotVIW(self, self.tab_1, position, 3)

        position = QtCore.QRect(480, 30, 160, 680)
        self.tab1_frame[4] = SlotVIW(self, self.tab_1, position, 4)

        position = QtCore.QRect(640, 30, 160, 680)
        self.tab1_frame[5] = SlotVIW(self, self.tab_1, position, 5)

        position = QtCore.QRect(800, 30, 161, 680)
        self.tab1_frame[6] = SlotVIW(self, self.tab_1, position, 6)

        self.tabWidget.addTab(self.tab_1, "")

        # tab_2 ##################################################################
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.tab2_frame = [0, 1, 2, 3, 4, 5, 6]

        position = QtCore.QRect(0, 0, 960, 30)
        self.tab2_frame[0] = ShowSlotScsiID_Header(self, self.tab_2, position)

        position = QtCore.QRect(0, 30, 160, 680)
        self.tab2_frame[1] = ShowSlotScsiID(self, self.tab_2, position, 1)

        position = QtCore.QRect(160, 30, 160, 680)
        self.tab2_frame[2] = ShowSlotScsiID(self, self.tab_2, position, 2)

        position = QtCore.QRect(320, 30, 160, 680)
        self.tab2_frame[3] = ShowSlotScsiID(self, self.tab_2, position, 3)

        position = QtCore.QRect(480, 30, 160, 680)
        self.tab2_frame[4] = ShowSlotScsiID(self, self.tab_2, position, 4)

        position = QtCore.QRect(640, 30, 160, 680)
        self.tab2_frame[5] = ShowSlotScsiID(self, self.tab_2, position, 5)

        position = QtCore.QRect(800, 30, 161, 680)
        self.tab2_frame[6] = ShowSlotScsiID(self, self.tab_2, position, 6)

        self.tabWidget.addTab(self.tab_2, "")

        # tab_3 ##################################################################
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.tab_3.sin = [ self.sinUpdateSlotDiskTest_0,
                           self.sinUpdateSlotDiskTest_1,
                           self.sinUpdateSlotDiskTest_2,
                           self.sinUpdateSlotDiskTest_3,
                           self.sinUpdateSlotDiskTest_4,
                           self.sinUpdateSlotDiskTest_5,
                           self.sinUpdateSlotDiskTest_6 ]

        self.tab3_frame = [0, 1, 2, 3, 4, 5, 6]

        position = QtCore.QRect(0, 0, 960, 30)
        self.tab3_frame[0] = DiskTest_Header(self, self.tab_3, position)
        self.tab3_SlotTestingCount = 0

        position = QtCore.QRect(0, 30, 160, 680)
        self.tab3_frame[1] = SlotDiskTest(self, self.tab_3, position, 1)

        position = QtCore.QRect(160, 30, 160, 680)
        self.tab3_frame[2] = SlotDiskTest(self, self.tab_3, position, 2)

        position = QtCore.QRect(320, 30, 160, 680)
        self.tab3_frame[3] = SlotDiskTest(self, self.tab_3, position, 3)

        position = QtCore.QRect(480, 30, 160, 680)
        self.tab3_frame[4] = SlotDiskTest(self, self.tab_3, position, 4)

        position = QtCore.QRect(640, 30, 160, 680)
        self.tab3_frame[5] = SlotDiskTest(self, self.tab_3, position, 5)

        position = QtCore.QRect(800, 30, 161, 680)
        self.tab3_frame[6] = SlotDiskTest(self, self.tab_3, position, 6)

        self.tabWidget.addTab(self.tab_3, "")

        # tab_4 ##################################################################
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.tab_4.sin = [self.sinUpdateSlotDiskTest_0,
                          self.sinUpdateSlotDiskTest_1,
                          self.sinUpdateSlotDiskTest_2,
                          self.sinUpdateSlotDiskTest_3,
                          self.sinUpdateSlotDiskTest_4,
                          self.sinUpdateSlotDiskTest_5,
                          self.sinUpdateSlotDiskTest_6]

        self.tab4_frame = [0, 1, 2, 3, 4, 5, 6]

        position = QtCore.QRect(0, 0, 960, 30)
        self.tab4_frame[0] = CC_DiskTest_Header(self, self.tab_4, position)

        position = QtCore.QRect(0, 30, 160, 680)
        self.tab4_frame[1] = CC_SlotDiskTest(self, self.tab_4, position, 1)

        position = QtCore.QRect(160, 30, 160, 680)
        self.tab4_frame[2] = CC_SlotDiskTest(self, self.tab_4, position, 2)

        position = QtCore.QRect(320, 30, 160, 680)
        self.tab4_frame[3] = CC_SlotDiskTest(self, self.tab_4, position, 3)

        position = QtCore.QRect(480, 30, 160, 680)
        self.tab4_frame[4] = CC_SlotDiskTest(self, self.tab_4, position, 4)

        position = QtCore.QRect(640, 30, 160, 680)
        self.tab4_frame[5] = CC_SlotDiskTest(self, self.tab_4, position, 5)

        position = QtCore.QRect(800, 30, 161, 680)
        self.tab4_frame[6] = CC_SlotDiskTest(self, self.tab_4, position, 6)

        self.tabWidget.addTab(self.tab_4, "")

        # tab_5 ##################################################################
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.tab_5.sin = [self.sinUpdateSlotDiskTest_0,
                          self.sinUpdateSlotDiskTest_1,
                          self.sinUpdateSlotDiskTest_2,
                          self.sinUpdateSlotDiskTest_3,
                          self.sinUpdateSlotDiskTest_4,
                          self.sinUpdateSlotDiskTest_5,
                          self.sinUpdateSlotDiskTest_6]

        self.tab5_frame = [0, 1, 2, 3, 4, 5, 6]

        position = QtCore.QRect(0, 0, 960, 30)
        self.tab5_frame[0] = DiskTestPlus_Header(self, self.tab_5, position)
        self.tab5_SlotTestingCount = 0

        position = QtCore.QRect(0, 30, 160, 680)
        self.tab5_frame[1] = SlotDiskTestPlus(self, self.tab_5, position, 1)

        position = QtCore.QRect(160, 30, 160, 680)
        self.tab5_frame[2] = SlotDiskTestPlus(self, self.tab_5, position, 2)

        position = QtCore.QRect(320, 30, 160, 680)
        self.tab5_frame[3] = SlotDiskTestPlus(self, self.tab_5, position, 3)

        position = QtCore.QRect(480, 30, 160, 680)
        self.tab5_frame[4] = SlotDiskTestPlus(self, self.tab_5, position, 4)

        position = QtCore.QRect(640, 30, 160, 680)
        self.tab5_frame[5] = SlotDiskTestPlus(self, self.tab_5, position, 5)

        position = QtCore.QRect(800, 30, 161, 680)
        self.tab5_frame[6] = SlotDiskTestPlus(self, self.tab_5, position, 6)

        self.tabWidget.addTab(self.tab_5, "")

        # tab_6 ##################################################################
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")

        self.tab_6.sin = [self.sinUpdateSlotDiskTest_0,
                          self.sinUpdateSlotDiskTest_1,
                          self.sinUpdateSlotDiskTest_2,
                          self.sinUpdateSlotDiskTest_3,
                          self.sinUpdateSlotDiskTest_4,
                          self.sinUpdateSlotDiskTest_5,
                          self.sinUpdateSlotDiskTest_6]

        self.tab6_frame = [0, 1, 2, 3, 4, 5, 6]

        position = QtCore.QRect(0, 0, 960, 30)
        self.tab6_frame[0] = DiskTest_Header_BIT(self, self.tab_6, position)
        self.tab6_SlotTestingCount = 0

        position = QtCore.QRect(0, 30, 160, 680)
        self.tab6_frame[1] = SlotDiskTest_BIT(self, self.tab_6, position, 1)

        position = QtCore.QRect(160, 30, 160, 680)
        self.tab6_frame[2] = SlotDiskTest_BIT(self, self.tab_6, position, 2)

        position = QtCore.QRect(320, 30, 160, 680)
        self.tab6_frame[3] = SlotDiskTest_BIT(self, self.tab_6, position, 3)

        position = QtCore.QRect(480, 30, 160, 680)
        self.tab6_frame[4] = SlotDiskTest_BIT(self, self.tab_6, position, 4)

        position = QtCore.QRect(640, 30, 160, 680)
        self.tab6_frame[5] = SlotDiskTest_BIT(self, self.tab_6, position, 5)

        position = QtCore.QRect(800, 30, 161, 680)
        self.tab6_frame[6] = SlotDiskTest_BIT(self, self.tab_6, position, 6)

        self.tabWidget.addTab(self.tab_6, "")

        #position = QtCore.QRect(0, 0, 968, 30)
        #self.tab2_frame_0 = UartControl(self, self.tab_2, position)

        '''
        # tab_slot1 ##################################################################
        self.tab_slot1 = QtWidgets.QWidget()
        self.tab_slot1.setObjectName("tab_slot1")
        self.tabWidget.addTab(self.tab_slot1, "")

        # tab_slot2 ##################################################################
        self.tab_slot2 = QtWidgets.QWidget()
        self.tab_slot2.setObjectName("tab_slot2")
        self.tabWidget.addTab(self.tab_slot2, "")

        # tab_slot3 ##################################################################
        self.tab_slot3 = QtWidgets.QWidget()
        self.tab_slot3.setObjectName("tab_slot3")
        self.tabWidget.addTab(self.tab_slot3, "")

        # tab_slot4 ##################################################################
        self.tab_slot4 = QtWidgets.QWidget()
        self.tab_slot4.setObjectName("tab_slot4")
        self.tabWidget.addTab(self.tab_slot4, "")

        # tab_slot5 ##################################################################
        self.tab_slot5 = QtWidgets.QWidget()
        self.tab_slot5.setObjectName("tab_slot5")
        self.tabWidget.addTab(self.tab_slot5, "")

        # tab_slot6 ##################################################################
        self.tab_slot6 = QtWidgets.QWidget()
        self.tab_slot6.setObjectName("tab_slot6")
        self.tabWidget.addTab(self.tab_slot6, "")
        '''

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.DiskTestInit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "STB(SSDTestBoard) V2.91"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "电压监测"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "健康检查"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "硬盘测试"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "克隆校验"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "硬盘测试+"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "硬盘测试++"))

        '''
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_slot1), _translate("MainWindow", "Slot1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_slot2), _translate("MainWindow", "Slot2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_slot3), _translate("MainWindow", "Slot3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_slot4), _translate("MainWindow", "Slot4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_slot5), _translate("MainWindow", "Slot5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_slot6), _translate("MainWindow", "Slot6"))
        '''

    def updateVIW(self):
        #print("in updateVIW")
        for i in (1, 2, 3, 4, 5, 6):
            self.tab1_frame[i].SlotShowOnUpdate()

    def updateInit(self):
        for i in (1, 2, 3, 4, 5, 6):
            self.tab1_frame[i].restoreStatus()

    def DiskTestInit(self):
        os.system("rw_show -k")
        os.system("rw_show -I")
        os.system("cc_show -k")
        os.system("cc_show -I")
        os.system("rw2_show -k")
        os.system("rw2_show -I")
        os.system("rw3_show -k")
        os.system("rw3_show -I")

    def STB_Heating(self, percent):
        #print(("$m0-{}\n".format(percent)).encode('ascii'))
        try:
            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.05)
                self.serial.flushInput()
                self.serial.write(("$m0-{}\n".format(percent)).encode('ascii'))
                time.sleep(0.05)
                self.serial.flushInput()
                self.mutex.release()
        except:
            print("except STB_Heating !!!!!!")
            pass

    def STB_LED_PointFlashCtl(self, slotnum, flag):
        try:
            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.02)
                self.serial.flushInput()
                if flag:
                    self.serial.write(("$F" + "{}".format(itoc(slotnum)) + "\n").encode('ascii'))
                else:
                    self.serial.write(("$f" + "{}".format(itoc(slotnum)) + "\n").encode('ascii'))
                time.sleep(0.01)
                self.serial.flushInput()
                self.mutex.release()
        except:
            print("except STB_LED_PointFlashCtl !!!!!!")
            pass

    def STB_LED_NumFlashCtl(self, slotnum, flag):
        try:
            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.02)
                self.serial.flushInput()
                if flag:
                    self.serial.write(("$E" + "{}".format(itoc(slotnum)) + "\n").encode('ascii'))
                else:
                    self.serial.write(("$e" + "{}".format(itoc(slotnum)) + "\n").encode('ascii'))
                time.sleep(0.01)
                self.serial.flushInput()
                self.mutex.release()
        except:
            print("except STB_LED_NumFlashCtl !!!!!!")
            pass

    def STB_LED_OnOffCtl(self, slotnum, flag):
        try:
            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.02)
                self.serial.flushInput()
                if flag:
                    self.serial.write(("$O" + "{}".format(itoc(slotnum)) + "\n").encode('ascii'))
                else:
                    self.serial.write(("$o" + "{}".format(itoc(slotnum)) + "\n").encode('ascii'))
                time.sleep(0.01)
                self.serial.flushInput()
                self.mutex.release()
        except:
            print("except STB_LED_OnOffCtl !!!!!!")
            pass

    def STB_LED_Show(self, slotnum, num):
        try:
            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.02)
                self.serial.flushInput()
                # 物理编号: 1,2,3,4,5,6
                self.serial.write("$S1\n".encode('ascii'))
                time.sleep(0.02)
                # LED显示
                #print("$d" + "{}".format(itoc(slotnum)) + "{}\n".format(itoc(num)))
                self.serial.write(("$d" + "{}".format(itoc(slotnum)) + "{}\n".format(itoc(num))).encode('ascii'))
                time.sleep(0.01)
                # 清理对应端口VIW
                self.serial.write(("$C" + "{}\n".format(itoc(slotnum))).encode('ascii'))
                time.sleep(0.01)
                self.serial.flushInput()
                self.mutex.release()
        except:
            print("except STB_LED_Show !!!!!!")
            pass

    def STB_k(self):
        try:
            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.01)
                self.serial.flushInput()
                self.serial.write(("$k" + "{}".format(itoc(26)) + "123\n").encode('ascii'))
                time.sleep(0.05)
                self.serial.flushInput()
                self.mutex.release()
        except:
            print("except STB_k !!!!!!")
            pass

    def STB_K(self):
        try:
            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.01)
                self.serial.flushInput()
                self.serial.write(("$K" + "{}".format(itoc(26)) + "456\n").encode('ascii'))
                time.sleep(0.05)
                self.serial.flushInput()
                self.mutex.release()
        except:
            print("except STB_K !!!!!!")
            pass

    def STB_GetRuntime(self):
        try:
            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.1)
                self.serial.flushInput()
                self.serial.write(("$L" + "z\n").encode('ascii'))
                time.sleep(0.1)
                lifecount = self.serial.read(self.serial.in_waiting or 300)
                self.mutex.release()
                print(str(lifecount))
                if len(str(lifecount)) == 0:
                    os.system("ssdtestboard -n 26 -L 65535")
                else:
                    lc = str(lifecount).split("=")
                    os.system("ssdtestboard -n 26 -L {}\n".format(str(lc[1][0:-5])))
        except:
            print("except STB_GetRuntime !!!!!!")
            os.system("ssdtestboard -n 26 -L 65535")
            pass

    def STB_RuntimePlus(self):
        try:
            if self.serial.isOpen():
                self.mutex.acquire()
                time.sleep(0.01)
                self.serial.flushInput()
                self.serial.write(("$d0H\n").encode('ascii'))
                time.sleep(0.1)
                self.serial.flushInput()
                self.mutex.release()
        except:
            print("except STB_RuntimePlus !!!!!!")
            pass

class XDsscomMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(XDsscomMainWindow, self).__init__(parent)

        self.setupUi(self)

    def __attach_events(self):
        pass


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = XDsscomMainWindow()
    myWin.show()
    sys.exit(app.exec_())
