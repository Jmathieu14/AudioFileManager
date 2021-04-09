# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setEnabled(True)
        Frame.resize(500, 300)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        Frame.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(Frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 501, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.settings = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.settings.setFont(font)
        self.settings.setMouseTracking(False)
        self.settings.setAcceptDrops(False)
        self.settings.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.settings.setObjectName("settings")
        self.gridLayout.addWidget(self.settings, 0, 1, 1, 1)
        self.dlSettingsContainer = QtWidgets.QHBoxLayout()
        self.dlSettingsContainer.setObjectName("dlSettingsContainer")
        self.dlLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dlLabel.setFont(font)
        self.dlLabel.setObjectName("dlLabel")
        self.dlSettingsContainer.addWidget(self.dlLabel)
        self.dlDirectPathEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.dlDirectPathEdit.setObjectName("dlDirectPathEdit")
        self.dlSettingsContainer.addWidget(self.dlDirectPathEdit)
        self.dlSearchBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.dlSearchBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dlSearchBtn.setDefault(False)
        self.dlSearchBtn.setFlat(False)
        self.dlSearchBtn.setObjectName("dlSearchBtn")
        self.dlSettingsContainer.addWidget(self.dlSearchBtn)
        self.gridLayout.addLayout(self.dlSettingsContainer, 1, 1, 1, 1)
        self.editsSettingsContainer = QtWidgets.QHBoxLayout()
        self.editsSettingsContainer.setObjectName("editsSettingsContainer")
        self.editsLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editsLabel.setFont(font)
        self.editsLabel.setObjectName("editsLabel")
        self.editsSettingsContainer.addWidget(self.editsLabel)
        self.editsPathEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editsPathEdit.setText("")
        self.editsPathEdit.setObjectName("editsPathEdit")
        self.editsSettingsContainer.addWidget(self.editsPathEdit)
        self.editsSearchBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.editsSearchBtn.setDefault(False)
        self.editsSearchBtn.setFlat(False)
        self.editsSearchBtn.setObjectName("editsSearchBtn")
        self.editsSettingsContainer.addWidget(self.editsSearchBtn)
        self.gridLayout.addLayout(self.editsSettingsContainer, 2, 1, 1, 1)
        self.destinationSettingsContainer = QtWidgets.QHBoxLayout()
        self.destinationSettingsContainer.setObjectName("destinationSettingsContainer")
        self.destLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.destLabel.setFont(font)
        self.destLabel.setObjectName("destLabel")
        self.destinationSettingsContainer.addWidget(self.destLabel)
        self.destPathEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.destPathEdit.setObjectName("destPathEdit")
        self.destinationSettingsContainer.addWidget(self.destPathEdit)
        self.destSearchBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.destSearchBtn.setDefault(False)
        self.destSearchBtn.setFlat(False)
        self.destSearchBtn.setObjectName("destSearchBtn")
        self.destinationSettingsContainer.addWidget(self.destSearchBtn)
        self.gridLayout.addLayout(self.destinationSettingsContainer, 3, 1, 1, 1)
        self.settingsSaveCancel = QtWidgets.QGridLayout()
        self.settingsSaveCancel.setObjectName("settingsSaveCancel")
        self.settingsSaveBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.settingsSaveBtn.setObjectName("settingsSaveBtn")
        self.settingsSaveCancel.addWidget(self.settingsSaveBtn, 0, 1, 1, 1)
        self.settingsCancelBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.settingsCancelBtn.setObjectName("settingsCancelBtn")
        self.settingsSaveCancel.addWidget(self.settingsCancelBtn, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.settingsSaveCancel, 4, 1, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.settings.setText(_translate("Frame", "Settings"))
        self.dlLabel.setText(_translate("Frame", "Downloads:"))
        self.dlSearchBtn.setText(_translate("Frame", "Search"))
        self.editsLabel.setText(_translate("Frame", "Edits:"))
        self.editsSearchBtn.setText(_translate("Frame", "Search"))
        self.destLabel.setText(_translate("Frame", "Destination:"))
        self.destSearchBtn.setText(_translate("Frame", "Search"))
        self.settingsSaveBtn.setText(_translate("Frame", "Save"))
        self.settingsCancelBtn.setText(_translate("Frame", "Cancel"))