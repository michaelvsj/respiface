# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 480)
        Dialog.setMinimumSize(QtCore.QSize(800, 480))
        Dialog.setMaximumSize(QtCore.QSize(800, 480))
        Dialog.setAutoFillBackground(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frm_main = QtWidgets.QFrame(Dialog)
        self.frm_main.setAutoFillBackground(True)
        self.frm_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_main.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frm_main.setLineWidth(0)
        self.frm_main.setObjectName("frm_main")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frm_main)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.frm_main)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frm_op_mode = QtWidgets.QFrame(self.frame_5)
        self.frm_op_mode.setMaximumSize(QtCore.QSize(180, 16777215))
        self.frm_op_mode.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_op_mode.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_op_mode.setObjectName("frm_op_mode")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frm_op_mode)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_title_op_mode = QtWidgets.QLabel(self.frm_op_mode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title_op_mode.sizePolicy().hasHeightForWidth())
        self.lbl_title_op_mode.setSizePolicy(sizePolicy)
        self.lbl_title_op_mode.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_title_op_mode.setFont(font)
        self.lbl_title_op_mode.setObjectName("lbl_title_op_mode")
        self.verticalLayout.addWidget(self.lbl_title_op_mode)
        self.frm_param_op_mode_vcv = QtWidgets.QFrame(self.frm_op_mode)
        self.frm_param_op_mode_vcv.setMinimumSize(QtCore.QSize(0, 70))
        self.frm_param_op_mode_vcv.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_op_mode_vcv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_op_mode_vcv.setLineWidth(2)
        self.frm_param_op_mode_vcv.setObjectName("frm_param_op_mode_vcv")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frm_param_op_mode_vcv)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frm_param_op_mode_vcv)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.frm_param_op_mode_vcv)
        self.frm_param_op_mode_pcv = QtWidgets.QFrame(self.frm_op_mode)
        self.frm_param_op_mode_pcv.setMinimumSize(QtCore.QSize(0, 70))
        self.frm_param_op_mode_pcv.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_op_mode_pcv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_op_mode_pcv.setLineWidth(2)
        self.frm_param_op_mode_pcv.setObjectName("frm_param_op_mode_pcv")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frm_param_op_mode_pcv)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frm_param_op_mode_pcv)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frm_param_op_mode_pcv)
        self.frm_param_op_mode_simv = QtWidgets.QFrame(self.frm_op_mode)
        self.frm_param_op_mode_simv.setMinimumSize(QtCore.QSize(0, 70))
        self.frm_param_op_mode_simv.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_op_mode_simv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_op_mode_simv.setLineWidth(2)
        self.frm_param_op_mode_simv.setObjectName("frm_param_op_mode_simv")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frm_param_op_mode_simv)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frm_param_op_mode_simv)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frm_param_op_mode_simv)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4.addWidget(self.frm_op_mode)
        self.frm_values = QtWidgets.QFrame(self.frame_5)
        self.frm_values.setMinimumSize(QtCore.QSize(400, 0))
        self.frm_values.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_values.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_values.setObjectName("frm_values")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frm_values)
        self.gridLayout_2.setSpacing(8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frm_param_flujoaire = QtWidgets.QFrame(self.frm_values)
        self.frm_param_flujoaire.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_flujoaire.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_flujoaire.setLineWidth(2)
        self.frm_param_flujoaire.setMidLineWidth(0)
        self.frm_param_flujoaire.setObjectName("frm_param_flujoaire")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frm_param_flujoaire)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_basic_5 = QtWidgets.QLabel(self.frm_param_flujoaire)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_basic_5.setFont(font)
        self.lbl_basic_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_basic_5.setObjectName("lbl_basic_5")
        self.horizontalLayout_7.addWidget(self.lbl_basic_5)
        self.lbl_basic_value_5 = QtWidgets.QLabel(self.frm_param_flujoaire)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_basic_value_5.setFont(font)
        self.lbl_basic_value_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_basic_value_5.setObjectName("lbl_basic_value_5")
        self.horizontalLayout_7.addWidget(self.lbl_basic_value_5)
        self.gridLayout_2.addWidget(self.frm_param_flujoaire, 5, 0, 1, 1)
        self.frm_param_sec_2 = QtWidgets.QFrame(self.frm_values)
        self.frm_param_sec_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_sec_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_sec_2.setLineWidth(2)
        self.frm_param_sec_2.setMidLineWidth(0)
        self.frm_param_sec_2.setObjectName("frm_param_sec_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frm_param_sec_2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lbl_sec_2 = QtWidgets.QLabel(self.frm_param_sec_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_sec_2.setFont(font)
        self.lbl_sec_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sec_2.setObjectName("lbl_sec_2")
        self.horizontalLayout_12.addWidget(self.lbl_sec_2)
        self.lbl_sec_value_2 = QtWidgets.QLabel(self.frm_param_sec_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_sec_value_2.setFont(font)
        self.lbl_sec_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sec_value_2.setObjectName("lbl_sec_value_2")
        self.horizontalLayout_12.addWidget(self.lbl_sec_value_2)
        self.gridLayout_2.addWidget(self.frm_param_sec_2, 2, 2, 1, 1)
        self.frm_param_sec_5 = QtWidgets.QFrame(self.frm_values)
        self.frm_param_sec_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_sec_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_sec_5.setLineWidth(2)
        self.frm_param_sec_5.setMidLineWidth(0)
        self.frm_param_sec_5.setObjectName("frm_param_sec_5")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frm_param_sec_5)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lbl_sec_9 = QtWidgets.QLabel(self.frm_param_sec_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_sec_9.setFont(font)
        self.lbl_sec_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sec_9.setObjectName("lbl_sec_9")
        self.horizontalLayout_15.addWidget(self.lbl_sec_9)
        self.lbl_sec_value_5 = QtWidgets.QLabel(self.frm_param_sec_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_sec_value_5.setFont(font)
        self.lbl_sec_value_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sec_value_5.setObjectName("lbl_sec_value_5")
        self.horizontalLayout_15.addWidget(self.lbl_sec_value_5)
        self.gridLayout_2.addWidget(self.frm_param_sec_5, 5, 2, 1, 1)
        self.frm_param_sec_4 = QtWidgets.QFrame(self.frm_values)
        self.frm_param_sec_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_sec_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_sec_4.setLineWidth(2)
        self.frm_param_sec_4.setMidLineWidth(0)
        self.frm_param_sec_4.setObjectName("frm_param_sec_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frm_param_sec_4)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lbl_sec_4 = QtWidgets.QLabel(self.frm_param_sec_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_sec_4.setFont(font)
        self.lbl_sec_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sec_4.setObjectName("lbl_sec_4")
        self.horizontalLayout_14.addWidget(self.lbl_sec_4)
        self.lbl_sec_value_4 = QtWidgets.QLabel(self.frm_param_sec_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_sec_value_4.setFont(font)
        self.lbl_sec_value_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sec_value_4.setObjectName("lbl_sec_value_4")
        self.horizontalLayout_14.addWidget(self.lbl_sec_value_4)
        self.gridLayout_2.addWidget(self.frm_param_sec_4, 4, 2, 1, 1)
        self.frm_param_brpm = QtWidgets.QFrame(self.frm_values)
        self.frm_param_brpm.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_brpm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_brpm.setLineWidth(2)
        self.frm_param_brpm.setMidLineWidth(0)
        self.frm_param_brpm.setObjectName("frm_param_brpm")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frm_param_brpm)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbl_basic_2 = QtWidgets.QLabel(self.frm_param_brpm)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_basic_2.setFont(font)
        self.lbl_basic_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_basic_2.setObjectName("lbl_basic_2")
        self.horizontalLayout_10.addWidget(self.lbl_basic_2)
        self.lbl_basic_value_2 = QtWidgets.QLabel(self.frm_param_brpm)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_basic_value_2.setFont(font)
        self.lbl_basic_value_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_basic_value_2.setObjectName("lbl_basic_value_2")
        self.horizontalLayout_10.addWidget(self.lbl_basic_value_2)
        self.gridLayout_2.addWidget(self.frm_param_brpm, 2, 0, 1, 1)
        self.frm_param_tvm = QtWidgets.QFrame(self.frm_values)
        self.frm_param_tvm.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_tvm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_tvm.setLineWidth(2)
        self.frm_param_tvm.setMidLineWidth(0)
        self.frm_param_tvm.setObjectName("frm_param_tvm")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frm_param_tvm)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_basic_1 = QtWidgets.QLabel(self.frm_param_tvm)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_basic_1.setFont(font)
        self.lbl_basic_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_basic_1.setObjectName("lbl_basic_1")
        self.horizontalLayout_6.addWidget(self.lbl_basic_1)
        self.lbl_basic_value_1 = QtWidgets.QLabel(self.frm_param_tvm)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_basic_value_1.setFont(font)
        self.lbl_basic_value_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_basic_value_1.setObjectName("lbl_basic_value_1")
        self.horizontalLayout_6.addWidget(self.lbl_basic_value_1)
        self.gridLayout_2.addWidget(self.frm_param_tvm, 1, 0, 1, 1)
        self.frm_param_sec_3 = QtWidgets.QFrame(self.frm_values)
        self.frm_param_sec_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_sec_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_sec_3.setLineWidth(2)
        self.frm_param_sec_3.setMidLineWidth(0)
        self.frm_param_sec_3.setObjectName("frm_param_sec_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frm_param_sec_3)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lbl_sec_3 = QtWidgets.QLabel(self.frm_param_sec_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_sec_3.setFont(font)
        self.lbl_sec_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sec_3.setObjectName("lbl_sec_3")
        self.horizontalLayout_13.addWidget(self.lbl_sec_3)
        self.lbl_sec_value_3 = QtWidgets.QLabel(self.frm_param_sec_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_sec_value_3.setFont(font)
        self.lbl_sec_value_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sec_value_3.setObjectName("lbl_sec_value_3")
        self.horizontalLayout_13.addWidget(self.lbl_sec_value_3)
        self.gridLayout_2.addWidget(self.frm_param_sec_3, 3, 2, 1, 1)
        self.frm_param_sec_1 = QtWidgets.QFrame(self.frm_values)
        self.frm_param_sec_1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_sec_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_sec_1.setLineWidth(2)
        self.frm_param_sec_1.setMidLineWidth(0)
        self.frm_param_sec_1.setObjectName("frm_param_sec_1")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frm_param_sec_1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lbl_sec_1 = QtWidgets.QLabel(self.frm_param_sec_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_sec_1.setFont(font)
        self.lbl_sec_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sec_1.setObjectName("lbl_sec_1")
        self.horizontalLayout_11.addWidget(self.lbl_sec_1)
        self.lbl_sec_value_1 = QtWidgets.QLabel(self.frm_param_sec_1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_sec_value_1.setFont(font)
        self.lbl_sec_value_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sec_value_1.setObjectName("lbl_sec_value_1")
        self.horizontalLayout_11.addWidget(self.lbl_sec_value_1)
        self.gridLayout_2.addWidget(self.frm_param_sec_1, 1, 2, 1, 1)
        self.lbl_title_basic_params = QtWidgets.QLabel(self.frm_values)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title_basic_params.sizePolicy().hasHeightForWidth())
        self.lbl_title_basic_params.setSizePolicy(sizePolicy)
        self.lbl_title_basic_params.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_title_basic_params.setFont(font)
        self.lbl_title_basic_params.setObjectName("lbl_title_basic_params")
        self.gridLayout_2.addWidget(self.lbl_title_basic_params, 0, 0, 1, 1)
        self.frm_param_fio2 = QtWidgets.QFrame(self.frm_values)
        self.frm_param_fio2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_fio2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_fio2.setLineWidth(2)
        self.frm_param_fio2.setMidLineWidth(0)
        self.frm_param_fio2.setObjectName("frm_param_fio2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frm_param_fio2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lbl_basic_4 = QtWidgets.QLabel(self.frm_param_fio2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_basic_4.setFont(font)
        self.lbl_basic_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_basic_4.setObjectName("lbl_basic_4")
        self.horizontalLayout_8.addWidget(self.lbl_basic_4)
        self.lbl_basic_value_4 = QtWidgets.QLabel(self.frm_param_fio2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_basic_value_4.setFont(font)
        self.lbl_basic_value_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_basic_value_4.setObjectName("lbl_basic_value_4")
        self.horizontalLayout_8.addWidget(self.lbl_basic_value_4)
        self.gridLayout_2.addWidget(self.frm_param_fio2, 4, 0, 1, 1)
        self.frm_param_peep = QtWidgets.QFrame(self.frm_values)
        self.frm_param_peep.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frm_param_peep.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_param_peep.setLineWidth(2)
        self.frm_param_peep.setMidLineWidth(0)
        self.frm_param_peep.setObjectName("frm_param_peep")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frm_param_peep)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lbl_basic_3 = QtWidgets.QLabel(self.frm_param_peep)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_basic_3.setFont(font)
        self.lbl_basic_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_basic_3.setObjectName("lbl_basic_3")
        self.horizontalLayout_9.addWidget(self.lbl_basic_3)
        self.lbl_basic_value_3 = QtWidgets.QLabel(self.frm_param_peep)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_basic_value_3.setFont(font)
        self.lbl_basic_value_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_basic_value_3.setObjectName("lbl_basic_value_3")
        self.horizontalLayout_9.addWidget(self.lbl_basic_value_3)
        self.gridLayout_2.addWidget(self.frm_param_peep, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        self.lbl_title_more_params = QtWidgets.QLabel(self.frm_values)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title_more_params.sizePolicy().hasHeightForWidth())
        self.lbl_title_more_params.setSizePolicy(sizePolicy)
        self.lbl_title_more_params.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_title_more_params.setFont(font)
        self.lbl_title_more_params.setObjectName("lbl_title_more_params")
        self.gridLayout_2.addWidget(self.lbl_title_more_params, 0, 2, 1, 1)
        self.horizontalLayout_4.addWidget(self.frm_values)
        self.frm_buttons = QtWidgets.QFrame(self.frame_5)
        self.frm_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_buttons.setObjectName("frm_buttons")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frm_buttons)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_title_right = QtWidgets.QLabel(self.frm_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title_right.sizePolicy().hasHeightForWidth())
        self.lbl_title_right.setSizePolicy(sizePolicy)
        self.lbl_title_right.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_title_right.setFont(font)
        self.lbl_title_right.setText("")
        self.lbl_title_right.setObjectName("lbl_title_right")
        self.verticalLayout_5.addWidget(self.lbl_title_right)
        self.frm_params_auto = QtWidgets.QFrame(self.frm_buttons)
        self.frm_params_auto.setMinimumSize(QtCore.QSize(0, 100))
        self.frm_params_auto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_params_auto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_params_auto.setObjectName("frm_params_auto")
        self.gridLayout = QtWidgets.QGridLayout(self.frm_params_auto)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_param_auto_name_3 = QtWidgets.QLabel(self.frm_params_auto)
        self.lbl_param_auto_name_3.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_param_auto_name_3.setFont(font)
        self.lbl_param_auto_name_3.setObjectName("lbl_param_auto_name_3")
        self.gridLayout.addWidget(self.lbl_param_auto_name_3, 2, 0, 1, 1)
        self.lbl_param_auto_val_2 = QtWidgets.QLabel(self.frm_params_auto)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_param_auto_val_2.setFont(font)
        self.lbl_param_auto_val_2.setObjectName("lbl_param_auto_val_2")
        self.gridLayout.addWidget(self.lbl_param_auto_val_2, 1, 1, 1, 1)
        self.lbl_param_auto_name_2 = QtWidgets.QLabel(self.frm_params_auto)
        self.lbl_param_auto_name_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_param_auto_name_2.setFont(font)
        self.lbl_param_auto_name_2.setObjectName("lbl_param_auto_name_2")
        self.gridLayout.addWidget(self.lbl_param_auto_name_2, 1, 0, 1, 1)
        self.lbl_param_auto_val_3 = QtWidgets.QLabel(self.frm_params_auto)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_param_auto_val_3.setFont(font)
        self.lbl_param_auto_val_3.setObjectName("lbl_param_auto_val_3")
        self.gridLayout.addWidget(self.lbl_param_auto_val_3, 2, 1, 1, 1)
        self.lbl_param_auto_name_1 = QtWidgets.QLabel(self.frm_params_auto)
        self.lbl_param_auto_name_1.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_param_auto_name_1.setFont(font)
        self.lbl_param_auto_name_1.setObjectName("lbl_param_auto_name_1")
        self.gridLayout.addWidget(self.lbl_param_auto_name_1, 0, 0, 1, 1)
        self.lbl_param_auto_val_1 = QtWidgets.QLabel(self.frm_params_auto)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_param_auto_val_1.setFont(font)
        self.lbl_param_auto_val_1.setObjectName("lbl_param_auto_val_1")
        self.gridLayout.addWidget(self.lbl_param_auto_val_1, 0, 1, 1, 1)
        self.lbl_param_auto_name_4 = QtWidgets.QLabel(self.frm_params_auto)
        self.lbl_param_auto_name_4.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_param_auto_name_4.setFont(font)
        self.lbl_param_auto_name_4.setObjectName("lbl_param_auto_name_4")
        self.gridLayout.addWidget(self.lbl_param_auto_name_4, 3, 0, 1, 1)
        self.lbl_param_auto_val_4 = QtWidgets.QLabel(self.frm_params_auto)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_param_auto_val_4.setFont(font)
        self.lbl_param_auto_val_4.setObjectName("lbl_param_auto_val_4")
        self.gridLayout.addWidget(self.lbl_param_auto_val_4, 3, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.frm_params_auto)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem2)
        self.frm_aceptar = QtWidgets.QFrame(self.frm_buttons)
        self.frm_aceptar.setMinimumSize(QtCore.QSize(0, 70))
        self.frm_aceptar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_aceptar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_aceptar.setObjectName("frm_aceptar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frm_aceptar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frm_aceptar)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.verticalLayout_5.addWidget(self.frm_aceptar)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.frm_cancelar = QtWidgets.QFrame(self.frm_buttons)
        self.frm_cancelar.setMinimumSize(QtCore.QSize(0, 70))
        self.frm_cancelar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_cancelar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_cancelar.setObjectName("frm_cancelar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frm_cancelar)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.frm_cancelar)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.verticalLayout_5.addWidget(self.frm_cancelar)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.frm_volver = QtWidgets.QFrame(self.frm_buttons)
        self.frm_volver.setMinimumSize(QtCore.QSize(0, 70))
        self.frm_volver.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_volver.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_volver.setObjectName("frm_volver")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frm_volver)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frm_volver)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.verticalLayout_5.addWidget(self.frm_volver)
        self.horizontalLayout_4.addWidget(self.frm_buttons)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.line = QtWidgets.QFrame(self.frm_main)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.frm_adjust = QtWidgets.QFrame(self.frm_main)
        self.frm_adjust.setMinimumSize(QtCore.QSize(0, 50))
        self.frm_adjust.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_adjust.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_adjust.setObjectName("frm_adjust")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frm_adjust)
        self.horizontalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_left_arrow = QtWidgets.QPushButton(self.frm_adjust)
        self.btn_left_arrow.setMinimumSize(QtCore.QSize(60, 40))
        self.btn_left_arrow.setMaximumSize(QtCore.QSize(60, 40))
        self.btn_left_arrow.setObjectName("btn_left_arrow")
        self.horizontalLayout_5.addWidget(self.btn_left_arrow)
        self.horizontalSlider = QtWidgets.QSlider(self.frm_adjust)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_5.addWidget(self.horizontalSlider)
        self.btn_right_arrow = QtWidgets.QPushButton(self.frm_adjust)
        self.btn_right_arrow.setMinimumSize(QtCore.QSize(60, 40))
        self.btn_right_arrow.setMaximumSize(QtCore.QSize(60, 40))
        self.btn_right_arrow.setObjectName("btn_right_arrow")
        self.horizontalLayout_5.addWidget(self.btn_right_arrow)
        self.verticalLayout_6.addWidget(self.frm_adjust)
        self.verticalLayout_2.addWidget(self.frm_main)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_title_op_mode.setText(_translate("Dialog", "Modo de operación"))
        self.label.setText(_translate("Dialog", "VCV"))
        self.label_2.setText(_translate("Dialog", "PCV"))
        self.label_3.setText(_translate("Dialog", "SIMV"))
        self.lbl_basic_5.setText(_translate("Dialog", "Etc."))
        self.lbl_basic_value_5.setText(_translate("Dialog", "0"))
        self.lbl_sec_2.setText(_translate("Dialog", "TextLabel"))
        self.lbl_sec_value_2.setText(_translate("Dialog", "20"))
        self.lbl_sec_9.setText(_translate("Dialog", "TextLabel"))
        self.lbl_sec_value_5.setText(_translate("Dialog", "50"))
        self.lbl_sec_4.setText(_translate("Dialog", "TextLabel"))
        self.lbl_sec_value_4.setText(_translate("Dialog", "40"))
        self.lbl_basic_2.setText(_translate("Dialog", "Frec. Resp. \n"
"[resp/min]"))
        self.lbl_basic_value_2.setText(_translate("Dialog", "0"))
        self.lbl_basic_1.setText(_translate("Dialog", "V. Tidal\n"
"[mL]"))
        self.lbl_basic_value_1.setText(_translate("Dialog", "0"))
        self.lbl_sec_3.setText(_translate("Dialog", "TextLabel"))
        self.lbl_sec_value_3.setText(_translate("Dialog", "30"))
        self.lbl_sec_1.setText(_translate("Dialog", "TextLabel"))
        self.lbl_sec_value_1.setText(_translate("Dialog", "10"))
        self.lbl_title_basic_params.setText(_translate("Dialog", "Valores básicos"))
        self.lbl_basic_4.setText(_translate("Dialog", "Conc.O2\n"
"%"))
        self.lbl_basic_value_4.setText(_translate("Dialog", "0"))
        self.lbl_basic_3.setText(_translate("Dialog", "PEEP \n"
"[cm H2O]"))
        self.lbl_basic_value_3.setText(_translate("Dialog", "0"))
        self.lbl_title_more_params.setText(_translate("Dialog", "Valores adicionales"))
        self.lbl_param_auto_name_3.setText(_translate("Dialog", "V\'"))
        self.lbl_param_auto_val_2.setText(_translate("Dialog", "10,0 L/min"))
        self.lbl_param_auto_name_2.setText(_translate("Dialog", "Vm"))
        self.lbl_param_auto_val_3.setText(_translate("Dialog", "11,0 L/min"))
        self.lbl_param_auto_name_1.setText(_translate("Dialog", "I:E"))
        self.lbl_param_auto_val_1.setText(_translate("Dialog", "1:1,4"))
        self.lbl_param_auto_name_4.setText(_translate("Dialog", "Vr"))
        self.lbl_param_auto_val_4.setText(_translate("Dialog", "300 mL"))
        self.label_5.setText(_translate("Dialog", "Aceptar"))
        self.label_6.setText(_translate("Dialog", "Cancelar"))
        self.label_7.setText(_translate("Dialog", "Volver"))
        self.btn_left_arrow.setText(_translate("Dialog", "<"))
        self.btn_right_arrow.setText(_translate("Dialog", ">"))
