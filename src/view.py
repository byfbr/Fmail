# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Fmail(object):
    def setupUi(self, Fmail):
        Fmail.setObjectName("Fmail")
        Fmail.resize(651, 333)
        self.centralWidget = QtWidgets.QWidget(Fmail)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_mailbox = QtWidgets.QWidget()
        self.tab_mailbox.setObjectName("tab_mailbox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_mailbox)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_check_now = QtWidgets.QPushButton(self.tab_mailbox)
        self.btn_check_now.setObjectName("btn_check_now")
        self.gridLayout_2.addWidget(self.btn_check_now, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_mailbox, "")
        self.tab_accounts = QtWidgets.QWidget()
        self.tab_accounts.setObjectName("tab_accounts")
        self.tabWidget.addTab(self.tab_accounts, "")
        self.tab_accountss = QtWidgets.QWidget()
        self.tab_accountss.setObjectName("tab_accountss")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_accountss)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_account = QtWidgets.QGroupBox(self.tab_accountss)
        self.groupBox_account.setObjectName("groupBox_account")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_account)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_account)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_account)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.lne_username = QtWidgets.QLineEdit(self.groupBox_account)
        self.lne_username.setObjectName("lne_username")
        self.gridLayout_4.addWidget(self.lne_username, 0, 1, 1, 1)
        self.lne_password = QtWidgets.QLineEdit(self.groupBox_account)
        self.lne_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lne_password.setObjectName("lne_password")
        self.gridLayout_4.addWidget(self.lne_password, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_account, 0, 0, 1, 1)
        self.groupBox_imap = QtWidgets.QGroupBox(self.tab_accountss)
        self.groupBox_imap.setObjectName("groupBox_imap")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_imap)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_imap)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_imap)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.lne_imap_server = QtWidgets.QLineEdit(self.groupBox_imap)
        self.lne_imap_server.setObjectName("lne_imap_server")
        self.gridLayout_5.addWidget(self.lne_imap_server, 0, 1, 1, 1)
        self.lne_imap_port = QtWidgets.QLineEdit(self.groupBox_imap)
        self.lne_imap_port.setObjectName("lne_imap_port")
        self.gridLayout_5.addWidget(self.lne_imap_port, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_imap, 0, 1, 1, 1)
        self.groupBox_settings = QtWidgets.QGroupBox(self.tab_accountss)
        self.groupBox_settings.setObjectName("groupBox_settings")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_settings)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.chb_automail = QtWidgets.QCheckBox(self.groupBox_settings)
        self.chb_automail.setObjectName("chb_automail")
        self.gridLayout_7.addWidget(self.chb_automail, 0, 0, 1, 1)
        self.chb_startup = QtWidgets.QCheckBox(self.groupBox_settings)
        self.chb_startup.setObjectName("chb_startup")
        self.gridLayout_7.addWidget(self.chb_startup, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_settings, 1, 0, 1, 1)
        self.groupBox_smtp = QtWidgets.QGroupBox(self.tab_accountss)
        self.groupBox_smtp.setObjectName("groupBox_smtp")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_smtp)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_smtp)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_smtp)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)
        self.lne_smtp_server = QtWidgets.QLineEdit(self.groupBox_smtp)
        self.lne_smtp_server.setObjectName("lne_smtp_server")
        self.gridLayout_6.addWidget(self.lne_smtp_server, 0, 1, 1, 1)
        self.lne_smtp_port = QtWidgets.QLineEdit(self.groupBox_smtp)
        self.lne_smtp_port.setObjectName("lne_smtp_port")
        self.gridLayout_6.addWidget(self.lne_smtp_port, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_smtp, 1, 1, 1, 1)
        self.btn_save_account = QtWidgets.QPushButton(self.tab_accountss)
        self.btn_save_account.setObjectName("btn_save_account")
        self.gridLayout_3.addWidget(self.btn_save_account, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_accountss, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        Fmail.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(Fmail)
        self.statusBar.setObjectName("statusBar")
        Fmail.setStatusBar(self.statusBar)

        self.retranslateUi(Fmail)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Fmail)

    def retranslateUi(self, Fmail):
        _translate = QtCore.QCoreApplication.translate
        Fmail.setWindowTitle(_translate("Fmail", "Fmail"))
        self.btn_check_now.setText(_translate("Fmail", "Check Now"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mailbox), _translate("Fmail", "MailBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_accounts), _translate("Fmail", "Accounts"))
        self.groupBox_account.setTitle(_translate("Fmail", "Account"))
        self.label.setText(_translate("Fmail", "Username"))
        self.label_2.setText(_translate("Fmail", "Password"))
        self.groupBox_imap.setTitle(_translate("Fmail", "Incoming Settings (IMAP)"))
        self.label_3.setText(_translate("Fmail", "IMAP Server"))
        self.label_4.setText(_translate("Fmail", "IMAP Port"))
        self.lne_imap_port.setText(_translate("Fmail", "993"))
        self.groupBox_settings.setTitle(_translate("Fmail", "Settings"))
        self.chb_automail.setText(_translate("Fmail", "Automail Check"))
        self.chb_startup.setText(_translate("Fmail", "Startup Fmail"))
        self.groupBox_smtp.setTitle(_translate("Fmail", "Outgoing Settings (SMTP)"))
        self.label_6.setText(_translate("Fmail", "SMTP Port"))
        self.label_5.setText(_translate("Fmail", "SMTP Server"))
        self.lne_smtp_port.setText(_translate("Fmail", "587"))
        self.btn_save_account.setText(_translate("Fmail", "Save Account"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_accountss), _translate("Fmail", "Settings"))

