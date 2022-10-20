# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_confServidor(object):
    def setupUi(self, confServidor):
        confServidor.setObjectName("confServidor")
        confServidor.setEnabled(True)
        confServidor.resize(410, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(confServidor.sizePolicy().hasHeightForWidth())
        confServidor.setSizePolicy(sizePolicy)
        confServidor.setMinimumSize(QtCore.QSize(410, 300))
        confServidor.setMaximumSize(QtCore.QSize(410, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("templates\\../imagens/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        confServidor.setWindowIcon(icon)
        confServidor.setStyleSheet("background-color: rgba(220, 220, 220, 255)")
        self.centralwidget = QtWidgets.QWidget(confServidor)
        self.centralwidget.setObjectName("centralwidget")
        self.labelStatusServidor = QtWidgets.QLabel(self.centralwidget)
        self.labelStatusServidor.setGeometry(QtCore.QRect(30, 210, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelStatusServidor.setFont(font)
        self.labelStatusServidor.setStyleSheet("background-color:transparent;\n"
"color: rgb(255, 0, 0);")
        self.labelStatusServidor.setText("")
        self.labelStatusServidor.setObjectName("labelStatusServidor")
        self.inputServidor = QtWidgets.QLineEdit(self.centralwidget)
        self.inputServidor.setGeometry(QtCore.QRect(60, 80, 300, 30))
        self.inputServidor.setMinimumSize(QtCore.QSize(300, 30))
        self.inputServidor.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.inputServidor.setFont(font)
        self.inputServidor.setAutoFillBackground(False)
        self.inputServidor.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5%;\n"
"padding: 5px;\n"
"}\n"
"")
        self.inputServidor.setText("")
        self.inputServidor.setFrame(True)
        self.inputServidor.setCursorPosition(0)
        self.inputServidor.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputServidor.setObjectName("inputServidor")
        self.inputUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUsuario.setGeometry(QtCore.QRect(60, 120, 300, 30))
        self.inputUsuario.setMinimumSize(QtCore.QSize(300, 30))
        self.inputUsuario.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.inputUsuario.setFont(font)
        self.inputUsuario.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5%;\n"
"padding: 5px;\n"
"}")
        self.inputUsuario.setObjectName("inputUsuario")
        self.inputSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.inputSenha.setGeometry(QtCore.QRect(60, 160, 300, 30))
        self.inputSenha.setMinimumSize(QtCore.QSize(300, 30))
        self.inputSenha.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.inputSenha.setFont(font)
        self.inputSenha.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5%;\n"
"padding: 5px;\n"
"}")
        self.inputSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputSenha.setObjectName("inputSenha")
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setGeometry(QtCore.QRect(60, 235, 145, 40))
        self.btnSalvar.setMinimumSize(QtCore.QSize(145, 40))
        self.btnSalvar.setMaximumSize(QtCore.QSize(145, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(162, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btnSalvar.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnSalvar.setFont(font)
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSalvar.setStyleSheet("QPushButton {\n"
"    box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#a2a2a2;\n"
"    border-radius:5px;\n"
"    border-bottom:1px solid #545454;\n"
"    border-right:1px solid #545454;\n"
"    display:inline-block;\n"
"}\n"
"QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#8d8d8d;\n"
"    border-top:1px solid #545454;\n"
"    border-left:1px solid #545454;\n"
"    border-bottom:1px solid #818181;\n"
"    border-right:1px solid #818181;\n"
"}")
        self.btnSalvar.setAutoRepeat(False)
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(215, 235, 145, 40))
        self.btnCancelar.setMinimumSize(QtCore.QSize(145, 40))
        self.btnCancelar.setMaximumSize(QtCore.QSize(145, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelar.setStyleSheet("QPushButton {\n"
"    box-shadow:inset 0px 1px 0px 0px #ffffff;\n"
"    background:linear-gradient(to bottom, #ededed 5%, #dfdfdf 100%);\n"
"    background-color:#ededed;\n"
"    border-radius:6px;\n"
"    border-bottom:1px solid #566963;\n"
"    border-right:1px solid #566963;\n"
"    display:inline-block;\n"
"    padding:6px 24px;\n"
"}\n"
"QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #dfdfdf 5%, #ededed 100%);\n"
"    background-color:#e3e3e3;\n"
"    border-top:1px solid #566963;\n"
"    border-left:1px solid #566963;\n"
"    border-bottom:1px solid #bdbdbd;\n"
"    border-right:1px solid #bdbdbd;\n"
"}")
        self.btnCancelar.setObjectName("btnCancelar")
        self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo.setGeometry(QtCore.QRect(30, 20, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setStyleSheet("background-color:transparent;")
        self.labelTitulo.setObjectName("labelTitulo")
        confServidor.setCentralWidget(self.centralwidget)

        self.retranslateUi(confServidor)
        self.btnCancelar.clicked.connect(confServidor.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(confServidor)

    def retranslateUi(self, confServidor):
        _translate = QtCore.QCoreApplication.translate
        confServidor.setWindowTitle(_translate("confServidor", "Configurção de Amazenamento"))
        self.inputServidor.setPlaceholderText(_translate("confServidor", "IP do servidor - Ex.: 10.0.0.1\\pasta"))
        self.inputUsuario.setPlaceholderText(_translate("confServidor", "Nome de usuário"))
        self.inputSenha.setPlaceholderText(_translate("confServidor", "Senha"))
        self.btnSalvar.setText(_translate("confServidor", "Salvar"))
        self.btnCancelar.setText(_translate("confServidor", "Fechar"))
        self.btnCancelar.setShortcut(_translate("confServidor", "Esc"))
        self.labelTitulo.setText(_translate("confServidor", "Digite as credenciais de rede"))