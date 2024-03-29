# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/material.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_confMaterial(object):
    def setupUi(self, confMaterial):
        confMaterial.setObjectName("confMaterial")
        confMaterial.resize(1202, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("templates/../icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        confMaterial.setWindowIcon(icon)
        confMaterial.setStyleSheet("background-color: rgba(220, 220, 220, 255)")
        self.centralwidget = QtWidgets.QWidget(confMaterial)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_WBb = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_WBb.sizePolicy().hasHeightForWidth())
        self.comboBox_WBb.setSizePolicy(sizePolicy)
        self.comboBox_WBb.setMinimumSize(QtCore.QSize(150, 25))
        self.comboBox_WBb.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_WBb.setFont(font)
        self.comboBox_WBb.setStyleSheet("QComboBox {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.comboBox_WBb.setObjectName("comboBox_WBb")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.comboBox_WBb.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_WBb, 5, 1, 1, 1)
        self.labelAbertura = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAbertura.sizePolicy().hasHeightForWidth())
        self.labelAbertura.setSizePolicy(sizePolicy)
        self.labelAbertura.setMinimumSize(QtCore.QSize(150, 25))
        self.labelAbertura.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelAbertura.setFont(font)
        self.labelAbertura.setObjectName("labelAbertura")
        self.gridLayout_2.addWidget(self.labelAbertura, 1, 0, 1, 1)
        self.labelCompExposicao = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCompExposicao.sizePolicy().hasHeightForWidth())
        self.labelCompExposicao.setSizePolicy(sizePolicy)
        self.labelCompExposicao.setMinimumSize(QtCore.QSize(150, 25))
        self.labelCompExposicao.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCompExposicao.setFont(font)
        self.labelCompExposicao.setObjectName("labelCompExposicao")
        self.gridLayout_2.addWidget(self.labelCompExposicao, 7, 0, 1, 1)
        self.pushButton_add_linha = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add_linha.sizePolicy().hasHeightForWidth())
        self.pushButton_add_linha.setSizePolicy(sizePolicy)
        self.pushButton_add_linha.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_add_linha.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_add_linha.setFont(font)
        self.pushButton_add_linha.setObjectName("pushButton_add_linha")
        self.gridLayout_2.addWidget(self.pushButton_add_linha, 8, 1, 1, 1)
        self.labelWBb = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelWBb.sizePolicy().hasHeightForWidth())
        self.labelWBb.setSizePolicy(sizePolicy)
        self.labelWBb.setMinimumSize(QtCore.QSize(150, 25))
        self.labelWBb.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelWBb.setFont(font)
        self.labelWBb.setObjectName("labelWBb")
        self.gridLayout_2.addWidget(self.labelWBb, 5, 0, 1, 1)
        self.labelPictureStyle = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPictureStyle.sizePolicy().hasHeightForWidth())
        self.labelPictureStyle.setSizePolicy(sizePolicy)
        self.labelPictureStyle.setMinimumSize(QtCore.QSize(150, 25))
        self.labelPictureStyle.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPictureStyle.setFont(font)
        self.labelPictureStyle.setObjectName("labelPictureStyle")
        self.gridLayout_2.addWidget(self.labelPictureStyle, 6, 0, 1, 1)
        self.labelWBa = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelWBa.sizePolicy().hasHeightForWidth())
        self.labelWBa.setSizePolicy(sizePolicy)
        self.labelWBa.setMinimumSize(QtCore.QSize(150, 25))
        self.labelWBa.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelWBa.setFont(font)
        self.labelWBa.setObjectName("labelWBa")
        self.gridLayout_2.addWidget(self.labelWBa, 4, 0, 1, 1)
        self.pushButton_del_linha = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_del_linha.sizePolicy().hasHeightForWidth())
        self.pushButton_del_linha.setSizePolicy(sizePolicy)
        self.pushButton_del_linha.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_del_linha.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_del_linha.setFont(font)
        self.pushButton_del_linha.setObjectName("pushButton_del_linha")
        self.gridLayout_2.addWidget(self.pushButton_del_linha, 8, 0, 1, 1)
        self.labelISO = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelISO.sizePolicy().hasHeightForWidth())
        self.labelISO.setSizePolicy(sizePolicy)
        self.labelISO.setMinimumSize(QtCore.QSize(150, 25))
        self.labelISO.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelISO.setFont(font)
        self.labelISO.setObjectName("labelISO")
        self.gridLayout_2.addWidget(self.labelISO, 2, 0, 1, 1)
        self.comboBox_ISO = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ISO.sizePolicy().hasHeightForWidth())
        self.comboBox_ISO.setSizePolicy(sizePolicy)
        self.comboBox_ISO.setMinimumSize(QtCore.QSize(150, 25))
        self.comboBox_ISO.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_ISO.setFont(font)
        self.comboBox_ISO.setStyleSheet("QComboBox {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.comboBox_ISO.setObjectName("comboBox_ISO")
        self.comboBox_ISO.addItem("")
        self.comboBox_ISO.addItem("")
        self.comboBox_ISO.addItem("")
        self.comboBox_ISO.addItem("")
        self.comboBox_ISO.addItem("")
        self.comboBox_ISO.addItem("")
        self.comboBox_ISO.addItem("")
        self.comboBox_ISO.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_ISO, 2, 1, 1, 1)
        self.comboBox_CompExposicao = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_CompExposicao.sizePolicy().hasHeightForWidth())
        self.comboBox_CompExposicao.setSizePolicy(sizePolicy)
        self.comboBox_CompExposicao.setMinimumSize(QtCore.QSize(150, 25))
        self.comboBox_CompExposicao.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_CompExposicao.setFont(font)
        self.comboBox_CompExposicao.setStyleSheet("QComboBox {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.comboBox_CompExposicao.setObjectName("comboBox_CompExposicao")
        self.comboBox_CompExposicao.addItem("")
        self.comboBox_CompExposicao.addItem("")
        self.comboBox_CompExposicao.addItem("")
        self.comboBox_CompExposicao.addItem("")
        self.comboBox_CompExposicao.addItem("")
        self.comboBox_CompExposicao.addItem("")
        self.comboBox_CompExposicao.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_CompExposicao, 7, 1, 1, 1)
        self.lineEdit_nomeMaterial = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_nomeMaterial.sizePolicy().hasHeightForWidth())
        self.lineEdit_nomeMaterial.setSizePolicy(sizePolicy)
        self.lineEdit_nomeMaterial.setMinimumSize(QtCore.QSize(305, 30))
        self.lineEdit_nomeMaterial.setMaximumSize(QtCore.QSize(305, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_nomeMaterial.setFont(font)
        self.lineEdit_nomeMaterial.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5%;\n"
"padding: 5px;\n"
"}\n"
"")
        self.lineEdit_nomeMaterial.setReadOnly(False)
        self.lineEdit_nomeMaterial.setObjectName("lineEdit_nomeMaterial")
        self.gridLayout_2.addWidget(self.lineEdit_nomeMaterial, 0, 0, 1, 2)
        self.comboBox_Abertura = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Abertura.sizePolicy().hasHeightForWidth())
        self.comboBox_Abertura.setSizePolicy(sizePolicy)
        self.comboBox_Abertura.setMinimumSize(QtCore.QSize(150, 25))
        self.comboBox_Abertura.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_Abertura.setFont(font)
        self.comboBox_Abertura.setStyleSheet("QComboBox {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.comboBox_Abertura.setObjectName("comboBox_Abertura")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.setItemText(0, "")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.comboBox_Abertura.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Abertura, 1, 1, 1, 1)
        self.comboBox_PictureStyle = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_PictureStyle.sizePolicy().hasHeightForWidth())
        self.comboBox_PictureStyle.setSizePolicy(sizePolicy)
        self.comboBox_PictureStyle.setMinimumSize(QtCore.QSize(150, 25))
        self.comboBox_PictureStyle.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_PictureStyle.setFont(font)
        self.comboBox_PictureStyle.setStyleSheet("QComboBox {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.comboBox_PictureStyle.setObjectName("comboBox_PictureStyle")
        self.comboBox_PictureStyle.addItem("")
        self.comboBox_PictureStyle.addItem("")
        self.comboBox_PictureStyle.addItem("")
        self.comboBox_PictureStyle.addItem("")
        self.comboBox_PictureStyle.addItem("")
        self.comboBox_PictureStyle.addItem("")
        self.comboBox_PictureStyle.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_PictureStyle, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 10, 0, 1, 1)
        self.comboBox_VelDisparo = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_VelDisparo.sizePolicy().hasHeightForWidth())
        self.comboBox_VelDisparo.setSizePolicy(sizePolicy)
        self.comboBox_VelDisparo.setMinimumSize(QtCore.QSize(150, 25))
        self.comboBox_VelDisparo.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_VelDisparo.setFont(font)
        self.comboBox_VelDisparo.setStyleSheet("QComboBox {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.comboBox_VelDisparo.setObjectName("comboBox_VelDisparo")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.setItemText(0, "")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.comboBox_VelDisparo.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_VelDisparo, 3, 1, 1, 1)
        self.labelVelDisparo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVelDisparo.sizePolicy().hasHeightForWidth())
        self.labelVelDisparo.setSizePolicy(sizePolicy)
        self.labelVelDisparo.setMinimumSize(QtCore.QSize(150, 25))
        self.labelVelDisparo.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelVelDisparo.setFont(font)
        self.labelVelDisparo.setObjectName("labelVelDisparo")
        self.gridLayout_2.addWidget(self.labelVelDisparo, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(305, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(305, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 9, 0, 1, 2)
        self.comboBox_WBa = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_WBa.sizePolicy().hasHeightForWidth())
        self.comboBox_WBa.setSizePolicy(sizePolicy)
        self.comboBox_WBa.setMinimumSize(QtCore.QSize(150, 25))
        self.comboBox_WBa.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_WBa.setFont(font)
        self.comboBox_WBa.setStyleSheet("QComboBox {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.comboBox_WBa.setObjectName("comboBox_WBa")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.comboBox_WBa.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_WBa, 4, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.tableWidget_material = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_material.sizePolicy().hasHeightForWidth())
        self.tableWidget_material.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_material.setFont(font)
        self.tableWidget_material.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_material.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed)
        self.tableWidget_material.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_material.setObjectName("tableWidget_material")
        self.tableWidget_material.setColumnCount(8)
        self.tableWidget_material.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        self.tableWidget_material.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_material.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_material.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_material.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_material.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_material.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_material.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_material.setHorizontalHeaderItem(7, item)
        self.tableWidget_material.horizontalHeader().setDefaultSectionSize(110)
        self.horizontalLayout.addWidget(self.tableWidget_material)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        confMaterial.setCentralWidget(self.centralwidget)

        self.retranslateUi(confMaterial)
        QtCore.QMetaObject.connectSlotsByName(confMaterial)

    def retranslateUi(self, confMaterial):
        _translate = QtCore.QCoreApplication.translate
        confMaterial.setWindowTitle(_translate("confMaterial", "Stone Photo Studio"))
        self.comboBox_WBb.setItemText(0, _translate("confMaterial", "0"))
        self.comboBox_WBb.setItemText(1, _translate("confMaterial", "-9"))
        self.comboBox_WBb.setItemText(2, _translate("confMaterial", "-8"))
        self.comboBox_WBb.setItemText(3, _translate("confMaterial", "-7"))
        self.comboBox_WBb.setItemText(4, _translate("confMaterial", "-6"))
        self.comboBox_WBb.setItemText(5, _translate("confMaterial", "-5"))
        self.comboBox_WBb.setItemText(6, _translate("confMaterial", "-4"))
        self.comboBox_WBb.setItemText(7, _translate("confMaterial", "-3"))
        self.comboBox_WBb.setItemText(8, _translate("confMaterial", "-2"))
        self.comboBox_WBb.setItemText(9, _translate("confMaterial", "-1"))
        self.comboBox_WBb.setItemText(10, _translate("confMaterial", "1"))
        self.comboBox_WBb.setItemText(11, _translate("confMaterial", "2"))
        self.comboBox_WBb.setItemText(12, _translate("confMaterial", "3"))
        self.comboBox_WBb.setItemText(13, _translate("confMaterial", "4"))
        self.comboBox_WBb.setItemText(14, _translate("confMaterial", "5"))
        self.comboBox_WBb.setItemText(15, _translate("confMaterial", "6"))
        self.comboBox_WBb.setItemText(16, _translate("confMaterial", "7"))
        self.comboBox_WBb.setItemText(17, _translate("confMaterial", "8"))
        self.comboBox_WBb.setItemText(18, _translate("confMaterial", "9"))
        self.labelAbertura.setText(_translate("confMaterial", "Abertura:"))
        self.labelCompExposicao.setText(_translate("confMaterial", "Comp Exposição:"))
        self.pushButton_add_linha.setText(_translate("confMaterial", "Adicionar"))
        self.labelWBb.setText(_translate("confMaterial", "WB Ajuste B:"))
        self.labelPictureStyle.setText(_translate("confMaterial", "Picture Style:"))
        self.labelWBa.setText(_translate("confMaterial", "WB Ajuste A:"))
        self.pushButton_del_linha.setText(_translate("confMaterial", "Excluir"))
        self.labelISO.setText(_translate("confMaterial", "ISO:"))
        self.comboBox_ISO.setItemText(0, _translate("confMaterial", "Auto"))
        self.comboBox_ISO.setItemText(1, _translate("confMaterial", "100"))
        self.comboBox_ISO.setItemText(2, _translate("confMaterial", "200"))
        self.comboBox_ISO.setItemText(3, _translate("confMaterial", "400"))
        self.comboBox_ISO.setItemText(4, _translate("confMaterial", "800"))
        self.comboBox_ISO.setItemText(5, _translate("confMaterial", "1600"))
        self.comboBox_ISO.setItemText(6, _translate("confMaterial", "3200"))
        self.comboBox_ISO.setItemText(7, _translate("confMaterial", "6400"))
        self.comboBox_CompExposicao.setItemText(0, _translate("confMaterial", "off"))
        self.comboBox_CompExposicao.setItemText(1, _translate("confMaterial", "+/- 1/3"))
        self.comboBox_CompExposicao.setItemText(2, _translate("confMaterial", "+/- 2/3"))
        self.comboBox_CompExposicao.setItemText(3, _translate("confMaterial", "+/- 1"))
        self.comboBox_CompExposicao.setItemText(4, _translate("confMaterial", "+/- 1 1/3"))
        self.comboBox_CompExposicao.setItemText(5, _translate("confMaterial", "+/- 1 2/3"))
        self.comboBox_CompExposicao.setItemText(6, _translate("confMaterial", "+/- 2"))
        self.lineEdit_nomeMaterial.setPlaceholderText(_translate("confMaterial", "Nome do material"))
        self.comboBox_Abertura.setItemText(1, _translate("confMaterial", "2.8"))
        self.comboBox_Abertura.setItemText(2, _translate("confMaterial", "3.2"))
        self.comboBox_Abertura.setItemText(3, _translate("confMaterial", "3.5"))
        self.comboBox_Abertura.setItemText(4, _translate("confMaterial", "4"))
        self.comboBox_Abertura.setItemText(5, _translate("confMaterial", "4.5"))
        self.comboBox_Abertura.setItemText(6, _translate("confMaterial", "5"))
        self.comboBox_Abertura.setItemText(7, _translate("confMaterial", "5.6"))
        self.comboBox_Abertura.setItemText(8, _translate("confMaterial", "6.3"))
        self.comboBox_Abertura.setItemText(9, _translate("confMaterial", "7.1"))
        self.comboBox_Abertura.setItemText(10, _translate("confMaterial", "8"))
        self.comboBox_Abertura.setItemText(11, _translate("confMaterial", "9"))
        self.comboBox_Abertura.setItemText(12, _translate("confMaterial", "10"))
        self.comboBox_Abertura.setItemText(13, _translate("confMaterial", "11"))
        self.comboBox_Abertura.setItemText(14, _translate("confMaterial", "13"))
        self.comboBox_Abertura.setItemText(15, _translate("confMaterial", "14"))
        self.comboBox_Abertura.setItemText(16, _translate("confMaterial", "16"))
        self.comboBox_Abertura.setItemText(17, _translate("confMaterial", "18"))
        self.comboBox_Abertura.setItemText(18, _translate("confMaterial", "20"))
        self.comboBox_Abertura.setItemText(19, _translate("confMaterial", "22"))
        self.comboBox_PictureStyle.setItemText(0, _translate("confMaterial", "Auto"))
        self.comboBox_PictureStyle.setItemText(1, _translate("confMaterial", "Standard"))
        self.comboBox_PictureStyle.setItemText(2, _translate("confMaterial", "Portrait"))
        self.comboBox_PictureStyle.setItemText(3, _translate("confMaterial", "Landscape"))
        self.comboBox_PictureStyle.setItemText(4, _translate("confMaterial", "Neutral"))
        self.comboBox_PictureStyle.setItemText(5, _translate("confMaterial", "Faithful"))
        self.comboBox_PictureStyle.setItemText(6, _translate("confMaterial", "Monochrome"))
        self.comboBox_VelDisparo.setItemText(1, _translate("confMaterial", "buld"))
        self.comboBox_VelDisparo.setItemText(2, _translate("confMaterial", "30"))
        self.comboBox_VelDisparo.setItemText(3, _translate("confMaterial", "25"))
        self.comboBox_VelDisparo.setItemText(4, _translate("confMaterial", "20"))
        self.comboBox_VelDisparo.setItemText(5, _translate("confMaterial", "15"))
        self.comboBox_VelDisparo.setItemText(6, _translate("confMaterial", "13"))
        self.comboBox_VelDisparo.setItemText(7, _translate("confMaterial", "10.3"))
        self.comboBox_VelDisparo.setItemText(8, _translate("confMaterial", "8"))
        self.comboBox_VelDisparo.setItemText(9, _translate("confMaterial", "6.3"))
        self.comboBox_VelDisparo.setItemText(10, _translate("confMaterial", "5"))
        self.comboBox_VelDisparo.setItemText(11, _translate("confMaterial", "4"))
        self.comboBox_VelDisparo.setItemText(12, _translate("confMaterial", "3.2"))
        self.comboBox_VelDisparo.setItemText(13, _translate("confMaterial", "2.5"))
        self.comboBox_VelDisparo.setItemText(14, _translate("confMaterial", "2"))
        self.comboBox_VelDisparo.setItemText(15, _translate("confMaterial", "1.6"))
        self.comboBox_VelDisparo.setItemText(16, _translate("confMaterial", "1.3"))
        self.comboBox_VelDisparo.setItemText(17, _translate("confMaterial", "1"))
        self.comboBox_VelDisparo.setItemText(18, _translate("confMaterial", "0.8"))
        self.comboBox_VelDisparo.setItemText(19, _translate("confMaterial", "0.6"))
        self.comboBox_VelDisparo.setItemText(20, _translate("confMaterial", "0.5"))
        self.comboBox_VelDisparo.setItemText(21, _translate("confMaterial", "0.4"))
        self.comboBox_VelDisparo.setItemText(22, _translate("confMaterial", "0.3"))
        self.comboBox_VelDisparo.setItemText(23, _translate("confMaterial", "1/4"))
        self.comboBox_VelDisparo.setItemText(24, _translate("confMaterial", "1/5"))
        self.comboBox_VelDisparo.setItemText(25, _translate("confMaterial", "1/6"))
        self.comboBox_VelDisparo.setItemText(26, _translate("confMaterial", "1/8"))
        self.comboBox_VelDisparo.setItemText(27, _translate("confMaterial", "1/10"))
        self.comboBox_VelDisparo.setItemText(28, _translate("confMaterial", "1/13"))
        self.comboBox_VelDisparo.setItemText(29, _translate("confMaterial", "1/15"))
        self.comboBox_VelDisparo.setItemText(30, _translate("confMaterial", "1/20"))
        self.comboBox_VelDisparo.setItemText(31, _translate("confMaterial", "1/25"))
        self.comboBox_VelDisparo.setItemText(32, _translate("confMaterial", "1/30"))
        self.comboBox_VelDisparo.setItemText(33, _translate("confMaterial", "1/40"))
        self.comboBox_VelDisparo.setItemText(34, _translate("confMaterial", "1/50"))
        self.comboBox_VelDisparo.setItemText(35, _translate("confMaterial", "1/60"))
        self.comboBox_VelDisparo.setItemText(36, _translate("confMaterial", "1/80"))
        self.comboBox_VelDisparo.setItemText(37, _translate("confMaterial", "1/100"))
        self.comboBox_VelDisparo.setItemText(38, _translate("confMaterial", "1/125"))
        self.comboBox_VelDisparo.setItemText(39, _translate("confMaterial", "1/160"))
        self.comboBox_VelDisparo.setItemText(40, _translate("confMaterial", "1/200"))
        self.comboBox_VelDisparo.setItemText(41, _translate("confMaterial", "1/250"))
        self.comboBox_VelDisparo.setItemText(42, _translate("confMaterial", "1/320"))
        self.comboBox_VelDisparo.setItemText(43, _translate("confMaterial", "1/400"))
        self.comboBox_VelDisparo.setItemText(44, _translate("confMaterial", "1/500"))
        self.comboBox_VelDisparo.setItemText(45, _translate("confMaterial", "1/640"))
        self.comboBox_VelDisparo.setItemText(46, _translate("confMaterial", "1/800"))
        self.comboBox_VelDisparo.setItemText(47, _translate("confMaterial", "1/1000"))
        self.comboBox_VelDisparo.setItemText(48, _translate("confMaterial", "1/1250"))
        self.comboBox_VelDisparo.setItemText(49, _translate("confMaterial", "1/1600"))
        self.comboBox_VelDisparo.setItemText(50, _translate("confMaterial", "1/2000"))
        self.comboBox_VelDisparo.setItemText(51, _translate("confMaterial", "1/2500"))
        self.comboBox_VelDisparo.setItemText(52, _translate("confMaterial", "1/3200"))
        self.comboBox_VelDisparo.setItemText(53, _translate("confMaterial", "1/4000"))
        self.labelVelDisparo.setText(_translate("confMaterial", "Vel. Disparo:"))
        self.pushButton.setText(_translate("confMaterial", "Preview"))
        self.comboBox_WBa.setItemText(0, _translate("confMaterial", "0"))
        self.comboBox_WBa.setItemText(1, _translate("confMaterial", "-9"))
        self.comboBox_WBa.setItemText(2, _translate("confMaterial", "-8"))
        self.comboBox_WBa.setItemText(3, _translate("confMaterial", "-7"))
        self.comboBox_WBa.setItemText(4, _translate("confMaterial", "-6"))
        self.comboBox_WBa.setItemText(5, _translate("confMaterial", "-5"))
        self.comboBox_WBa.setItemText(6, _translate("confMaterial", "-4"))
        self.comboBox_WBa.setItemText(7, _translate("confMaterial", "-3"))
        self.comboBox_WBa.setItemText(8, _translate("confMaterial", "-2"))
        self.comboBox_WBa.setItemText(9, _translate("confMaterial", "-1"))
        self.comboBox_WBa.setItemText(10, _translate("confMaterial", "1"))
        self.comboBox_WBa.setItemText(11, _translate("confMaterial", "2"))
        self.comboBox_WBa.setItemText(12, _translate("confMaterial", "3"))
        self.comboBox_WBa.setItemText(13, _translate("confMaterial", "4"))
        self.comboBox_WBa.setItemText(14, _translate("confMaterial", "5"))
        self.comboBox_WBa.setItemText(15, _translate("confMaterial", "6"))
        self.comboBox_WBa.setItemText(16, _translate("confMaterial", "7"))
        self.comboBox_WBa.setItemText(17, _translate("confMaterial", "8"))
        self.comboBox_WBa.setItemText(18, _translate("confMaterial", "9"))
        item = self.tableWidget_material.horizontalHeaderItem(0)
        item.setText(_translate("confMaterial", "Nome do Material"))
        item = self.tableWidget_material.horizontalHeaderItem(1)
        item.setText(_translate("confMaterial", "Abertura"))
        item = self.tableWidget_material.horizontalHeaderItem(2)
        item.setText(_translate("confMaterial", "ISO"))
        item = self.tableWidget_material.horizontalHeaderItem(3)
        item.setText(_translate("confMaterial", "Vel. Disparo"))
        item = self.tableWidget_material.horizontalHeaderItem(4)
        item.setText(_translate("confMaterial", "WB Ajuste A"))
        item = self.tableWidget_material.horizontalHeaderItem(5)
        item.setText(_translate("confMaterial", "WB Ajuste B"))
        item = self.tableWidget_material.horizontalHeaderItem(6)
        item.setText(_translate("confMaterial", "Picture Style"))
        item = self.tableWidget_material.horizontalHeaderItem(7)
        item.setText(_translate("confMaterial", "Comp. Exposição"))
