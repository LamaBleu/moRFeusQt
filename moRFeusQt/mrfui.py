# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\moRFeusQt\morfeus_pyqt5.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mRFsMain(object):
    def setupUi(self, mRFsMain):
        mRFsMain.setObjectName("mRFsMain")
        mRFsMain.resize(400, 300)
        mRFsMain.setMinimumSize(QtCore.QSize(400, 290))
        mRFsMain.setMaximumSize(QtCore.QSize(400, 290))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mRFsMain.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mRFsMain)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 290))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 290))
        self.centralwidget.setObjectName("centralwidget")
        self.powerInput = QtWidgets.QSpinBox(self.centralwidget)
        self.powerInput.setGeometry(QtCore.QRect(130, 110, 161, 22))
        self.powerInput.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.powerInput.setMaximum(7)
        self.powerInput.setProperty("value", 1)
        self.powerInput.setObjectName("powerInput")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.label_6.setObjectName("label_6")
        self.biasOn = QtWidgets.QPushButton(self.centralwidget)
        self.biasOn.setGeometry(QtCore.QRect(310, 140, 75, 23))
        self.biasOn.setMaximumSize(QtCore.QSize(80, 25))
        self.biasOn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.biasOn.setObjectName("biasOn")
        self.morseInput = QtWidgets.QLineEdit(self.centralwidget)
        self.morseInput.setGeometry(QtCore.QRect(130, 200, 161, 22))
        self.morseInput.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.SouthAfrica))
        self.morseInput.setObjectName("morseInput")
        self.startFreq = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.startFreq.setGeometry(QtCore.QRect(130, 20, 161, 22))
        font = QtGui.QFont()
        font.setKerning(True)
        self.startFreq.setFont(font)
        self.startFreq.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.startFreq.setDecimals(6)
        self.startFreq.setMinimum(85.0)
        self.startFreq.setMaximum(5400.0)
        self.startFreq.setSingleStep(0.1)
        self.startFreq.setProperty("value", 85.0)
        self.startFreq.setObjectName("startFreq")
        self.endFreq = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.endFreq.setGeometry(QtCore.QRect(130, 50, 161, 22))
        self.endFreq.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.endFreq.setDecimals(6)
        self.endFreq.setMinimum(85.0)
        self.endFreq.setMaximum(5400.0)
        self.endFreq.setProperty("value", 88.0)
        self.endFreq.setObjectName("endFreq")
        self.mixButton = QtWidgets.QPushButton(self.centralwidget)
        self.mixButton.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.mixButton.setMaximumSize(QtCore.QSize(80, 25))
        self.mixButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mixButton.setObjectName("mixButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.label_4.setObjectName("label_4")
        self.delay = QtWidgets.QSpinBox(self.centralwidget)
        self.delay.setGeometry(QtCore.QRect(130, 170, 161, 22))
        self.delay.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.delay.setMaximum(10000)
        self.delay.setProperty("value", 1000)
        self.delay.setObjectName("delay")
        self.genButton = QtWidgets.QPushButton(self.centralwidget)
        self.genButton.setGeometry(QtCore.QRect(310, 50, 75, 23))
        self.genButton.setMaximumSize(QtCore.QSize(80, 25))
        self.genButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.genButton.setObjectName("genButton")
        self.startLabel = QtWidgets.QLabel(self.centralwidget)
        self.startLabel.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.startLabel.setObjectName("startLabel")
        self.noiseButton = QtWidgets.QPushButton(self.centralwidget)
        self.noiseButton.setGeometry(QtCore.QRect(310, 80, 75, 23))
        self.noiseButton.setMaximumSize(QtCore.QSize(80, 25))
        self.noiseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.noiseButton.setObjectName("noiseButton")
        self.sweepButton = QtWidgets.QPushButton(self.centralwidget)
        self.sweepButton.setGeometry(QtCore.QRect(310, 110, 75, 23))
        self.sweepButton.setMaximumSize(QtCore.QSize(80, 25))
        self.sweepButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sweepButton.setObjectName("sweepButton")
        self.morseButton = QtWidgets.QPushButton(self.centralwidget)
        self.morseButton.setGeometry(QtCore.QRect(310, 200, 75, 23))
        self.morseButton.setMaximumSize(QtCore.QSize(80, 25))
        self.morseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.morseButton.setObjectName("morseButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 170, 91, 16))
        self.label_7.setObjectName("label_7")
        self.steps = QtWidgets.QSpinBox(self.centralwidget)
        self.steps.setGeometry(QtCore.QRect(130, 140, 161, 22))
        self.steps.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.steps.setMaximum(1000)
        self.steps.setProperty("value", 5)
        self.steps.setObjectName("steps")
        self.biasOff = QtWidgets.QPushButton(self.centralwidget)
        self.biasOff.setGeometry(QtCore.QRect(310, 170, 75, 23))
        self.biasOff.setMaximumSize(QtCore.QSize(80, 25))
        self.biasOff.setFocusPolicy(QtCore.Qt.NoFocus)
        self.biasOff.setObjectName("biasOff")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 91, 16))
        self.label_5.setObjectName("label_5")
        self.stepSize = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.stepSize.setGeometry(QtCore.QRect(130, 80, 161, 22))
        self.stepSize.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.stepSize.setDecimals(4)
        self.stepSize.setMinimum(0.001)
        self.stepSize.setMaximum(50000.0)
        self.stepSize.setProperty("value", 100.0)
        self.stepSize.setObjectName("stepSize")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.label_3.setObjectName("label_3")
        self.readRegButton = QtWidgets.QPushButton(self.centralwidget)
        self.readRegButton.setGeometry(QtCore.QRect(310, 230, 75, 23))
        self.readRegButton.setMaximumSize(QtCore.QSize(80, 25))
        self.readRegButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.readRegButton.setObjectName("readRegButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 81, 16))
        self.label.setObjectName("label")
        self.readReg = QtWidgets.QLineEdit(self.centralwidget)
        self.readReg.setGeometry(QtCore.QRect(130, 230, 161, 22))
        self.readReg.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.readReg.setReadOnly(True)
        self.readReg.setObjectName("readReg")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 230, 81, 16))
        self.label_2.setObjectName("label_2")
        mRFsMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mRFsMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        mRFsMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mRFsMain)
        self.statusbar.setObjectName("statusbar")
        mRFsMain.setStatusBar(self.statusbar)
        self.label_6.setBuddy(self.steps)
        self.label_4.setBuddy(self.stepSize)
        self.startLabel.setBuddy(self.startFreq)
        self.label_7.setBuddy(self.delay)
        self.label_5.setBuddy(self.powerInput)
        self.label_3.setBuddy(self.endFreq)

        self.retranslateUi(mRFsMain)
        QtCore.QMetaObject.connectSlotsByName(mRFsMain)
        mRFsMain.setTabOrder(self.startFreq, self.endFreq)
        mRFsMain.setTabOrder(self.endFreq, self.stepSize)
        mRFsMain.setTabOrder(self.stepSize, self.powerInput)
        mRFsMain.setTabOrder(self.powerInput, self.steps)
        mRFsMain.setTabOrder(self.steps, self.delay)
        mRFsMain.setTabOrder(self.delay, self.morseInput)
        mRFsMain.setTabOrder(self.morseInput, self.readReg)

    def retranslateUi(self, mRFsMain):
        _translate = QtCore.QCoreApplication.translate
        mRFsMain.setWindowTitle(_translate("mRFsMain", "moRFeus Qt v3.123"))
        self.powerInput.setToolTip(_translate("mRFsMain", "Set Device Current"))
        self.label_6.setText(_translate("mRFsMain", "Steps"))
        self.biasOn.setToolTip(_translate("mRFsMain", "Set BiasTee On"))
        self.biasOn.setText(_translate("mRFsMain", "Bias On"))
        self.morseInput.setToolTip(_translate("mRFsMain", "Please enter message"))
        self.startFreq.setToolTip(_translate("mRFsMain", "Set the device freq"))
        self.endFreq.setToolTip(_translate("mRFsMain", "Sweep End Freq"))
        self.mixButton.setToolTip(_translate("mRFsMain", "Set Mixer Mode"))
        self.mixButton.setText(_translate("mRFsMain", "Mixer"))
        self.label_4.setText(_translate("mRFsMain", "Step KHz"))
        self.delay.setToolTip(_translate("mRFsMain", "Do you like time?"))
        self.genButton.setToolTip(_translate("mRFsMain", "Set Generator Mode"))
        self.genButton.setText(_translate("mRFsMain", "Gen"))
        self.startLabel.setText(_translate("mRFsMain", "Device Freq"))
        self.noiseButton.setToolTip(_translate("mRFsMain", "Set Noise Mode"))
        self.noiseButton.setText(_translate("mRFsMain", "Noise"))
        self.sweepButton.setToolTip(_translate("mRFsMain", "Start Freq Sweep"))
        self.sweepButton.setText(_translate("mRFsMain", "Sweep"))
        self.morseButton.setToolTip(_translate("mRFsMain", "Message at Freq"))
        self.morseButton.setText(_translate("mRFsMain", "Send"))
        self.label_7.setText(_translate("mRFsMain", "Delay ms"))
        self.steps.setToolTip(_translate("mRFsMain", "How many ?"))
        self.biasOff.setToolTip(_translate("mRFsMain", "Set BiasTee Off"))
        self.biasOff.setText(_translate("mRFsMain", "Bias Off"))
        self.label_5.setText(_translate("mRFsMain", "Power"))
        self.stepSize.setToolTip(_translate("mRFsMain", "Step Size"))
        self.label_3.setText(_translate("mRFsMain", "Sweep End"))
        self.readRegButton.setToolTip(_translate("mRFsMain", "Read Device Register"))
        self.readRegButton.setText(_translate("mRFsMain", "Read"))
        self.label.setText(_translate("mRFsMain", "Morse Code"))
        self.readReg.setToolTip(_translate("mRFsMain", "Shall I read the device?"))
        self.label_2.setText(_translate("mRFsMain", "Register"))
