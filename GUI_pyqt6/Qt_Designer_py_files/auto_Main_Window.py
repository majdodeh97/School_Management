# Form implementation generated from reading ui file 'Qt_Designer_ui_files/Main_Window.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 771)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 771, 571))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(2, 5, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.query_text = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.query_text.sizePolicy().hasHeightForWidth())
        self.query_text.setSizePolicy(sizePolicy)
        self.query_text.setObjectName("query_text")
        self.horizontalLayout.addWidget(self.query_text)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.treeView = QtWidgets.QTreeView(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.select_all_tool_button = QtWidgets.QTabWidget(parent=self.gridLayoutWidget)
        self.select_all_tool_button.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.select_all_tool_button.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.select_all_tool_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.select_all_tool_button.setAutoFillBackground(False)
        self.select_all_tool_button.setStyleSheet(" QTabWidget::pane{border: 1px;border-color:red;background-color: transparent;} \n"
"QTabBar::tab {background-color: transparent;} \n"
"QTabBar::tab:hover{background-color:#ddd; color: white;}     \n"
"QTabBar::tab:selected{background-color: #363535; color: #008BEA;}\n"
"")
        self.select_all_tool_button.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.select_all_tool_button.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.select_all_tool_button.setIconSize(QtCore.QSize(16, 16))
        self.select_all_tool_button.setDocumentMode(True)
        self.select_all_tool_button.setTabBarAutoHide(False)
        self.select_all_tool_button.setObjectName("select_all_tool_button")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 391, 321))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.addRecipient_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addRecipient_button.sizePolicy().hasHeightForWidth())
        self.addRecipient_button.setSizePolicy(sizePolicy)
        self.addRecipient_button.setMinimumSize(QtCore.QSize(0, 60))
        self.addRecipient_button.setStyleSheet("")
        self.addRecipient_button.setAutoDefault(False)
        self.addRecipient_button.setObjectName("addRecipient_button")
        self.gridLayout_2.addWidget(self.addRecipient_button, 0, 0, 1, 1)
        self.email_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_button.sizePolicy().hasHeightForWidth())
        self.email_button.setSizePolicy(sizePolicy)
        self.email_button.setMinimumSize(QtCore.QSize(0, 60))
        self.email_button.setBaseSize(QtCore.QSize(0, 0))
        self.email_button.setObjectName("email_button")
        self.gridLayout_2.addWidget(self.email_button, 2, 0, 1, 1)
        self.removeRecipient_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeRecipient_button.sizePolicy().hasHeightForWidth())
        self.removeRecipient_button.setSizePolicy(sizePolicy)
        self.removeRecipient_button.setMinimumSize(QtCore.QSize(0, 60))
        self.removeRecipient_button.setObjectName("removeRecipient_button")
        self.gridLayout_2.addWidget(self.removeRecipient_button, 1, 0, 1, 1)
        self.recipient_list = QtWidgets.QListWidget(parent=self.gridLayoutWidget_2)
        self.recipient_list.setObjectName("recipient_list")
        self.gridLayout_2.addWidget(self.recipient_list, 0, 1, 3, 1)
        self.select_all_tool_button.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.subject_comboBox = QtWidgets.QComboBox(parent=self.tab_2)
        self.subject_comboBox.setGeometry(QtCore.QRect(100, 40, 111, 22))
        self.subject_comboBox.setObjectName("subject_comboBox")
        self.category_comboBox = QtWidgets.QComboBox(parent=self.tab_2)
        self.category_comboBox.setGeometry(QtCore.QRect(100, 90, 111, 22))
        self.category_comboBox.setObjectName("category_comboBox")
        self.Subject_label = QtWidgets.QLabel(parent=self.tab_2)
        self.Subject_label.setGeometry(QtCore.QRect(20, 40, 58, 16))
        self.Subject_label.setObjectName("Subject_label")
        self.category_label = QtWidgets.QLabel(parent=self.tab_2)
        self.category_label.setGeometry(QtCore.QRect(20, 90, 58, 16))
        self.category_label.setObjectName("category_label")
        self.quarter_label = QtWidgets.QLabel(parent=self.tab_2)
        self.quarter_label.setGeometry(QtCore.QRect(20, 130, 58, 16))
        self.quarter_label.setObjectName("quarter_label")
        self.Q1_checkBox = QtWidgets.QCheckBox(parent=self.tab_2)
        self.Q1_checkBox.setGeometry(QtCore.QRect(90, 130, 84, 21))
        self.Q1_checkBox.setObjectName("Q1_checkBox")
        self.Q2_checkBox = QtWidgets.QCheckBox(parent=self.tab_2)
        self.Q2_checkBox.setGeometry(QtCore.QRect(140, 130, 84, 21))
        self.Q2_checkBox.setObjectName("Q2_checkBox")
        self.Q3_checkBox = QtWidgets.QCheckBox(parent=self.tab_2)
        self.Q3_checkBox.setGeometry(QtCore.QRect(190, 130, 84, 21))
        self.Q3_checkBox.setObjectName("Q3_checkBox")
        self.Q4_checkBox = QtWidgets.QCheckBox(parent=self.tab_2)
        self.Q4_checkBox.setGeometry(QtCore.QRect(240, 130, 84, 21))
        self.Q4_checkBox.setObjectName("Q4_checkBox")
        self.graph_button = QtWidgets.QPushButton(parent=self.tab_2)
        self.graph_button.setGeometry(QtCore.QRect(10, 190, 151, 41))
        self.graph_button.setObjectName("graph_button")
        self.select_all_button = QtWidgets.QPushButton(parent=self.tab_2)
        self.select_all_button.setGeometry(QtCore.QRect(290, 130, 31, 26))
        self.select_all_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Qt_Designer_ui_files/../../../../Downloads/select-all-icon-10.jpg.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.select_all_button.setIcon(icon)
        self.select_all_button.setIconSize(QtCore.QSize(23, 23))
        self.select_all_button.setCheckable(False)
        self.select_all_button.setFlat(True)
        self.select_all_button.setObjectName("select_all_button")
        self.deselect_all_button = QtWidgets.QPushButton(parent=self.tab_2)
        self.deselect_all_button.setGeometry(QtCore.QRect(330, 130, 31, 26))
        self.deselect_all_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Qt_Designer_ui_files/../../../../Downloads/deselect all icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.deselect_all_button.setIcon(icon1)
        self.deselect_all_button.setIconSize(QtCore.QSize(18, 18))
        self.deselect_all_button.setFlat(True)
        self.deselect_all_button.setObjectName("deselect_all_button")
        self.select_all_tool_button.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tab_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 40, 160, 159))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.edit_percentages_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.edit_percentages_button.setObjectName("edit_percentages_button")
        self.verticalLayout.addWidget(self.edit_percentages_button)
        self.grade_calculate_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.grade_calculate_button.setObjectName("grade_calculate_button")
        self.verticalLayout.addWidget(self.grade_calculate_button)
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.verticalLayoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab_4)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 90, 211, 421))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_grade_calculator_left = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_grade_calculator_left.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_grade_calculator_left.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_grade_calculator_left.setObjectName("gridLayout_grade_calculator_left")
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout_grade_calculator_left.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout_grade_calculator_left.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout_grade_calculator_left.addWidget(self.label_4, 0, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.tab_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 201, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.subject_gc_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.subject_gc_label.setObjectName("subject_gc_label")
        self.horizontalLayout_4.addWidget(self.subject_gc_label)
        self.subject_gc_comboBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget)
        self.subject_gc_comboBox.setObjectName("subject_gc_comboBox")
        self.horizontalLayout_4.addWidget(self.subject_gc_comboBox)
        self.gc_quarters_comboBox = QtWidgets.QComboBox(parent=self.tab_4)
        self.gc_quarters_comboBox.setGeometry(QtCore.QRect(280, 230, 61, 31))
        self.gc_quarters_comboBox.setObjectName("gc_quarters_comboBox")
        self.gc_extract_grades_button = QtWidgets.QPushButton(parent=self.tab_4)
        self.gc_extract_grades_button.setGeometry(QtCore.QRect(339, 230, 101, 26))
        self.gc_extract_grades_button.setObjectName("gc_extract_grades_button")
        self.gc_clear_button = QtWidgets.QPushButton(parent=self.tab_4)
        self.gc_clear_button.setGeometry(QtCore.QRect(320, 280, 80, 26))
        self.gc_clear_button.setObjectName("gc_clear_button")
        self.select_all_tool_button.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.select_all_tool_button, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(parent=self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuTools = QtWidgets.QMenu(parent=self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.import_excel_file_menu_action = QtGui.QAction(parent=MainWindow)
        self.import_excel_file_menu_action.setObjectName("import_excel_file_menu_action")
        self.actionHow = QtGui.QAction(parent=MainWindow)
        self.actionHow.setObjectName("actionHow")
        self.actionAre = QtGui.QAction(parent=MainWindow)
        self.actionAre.setObjectName("actionAre")
        self.actionYou = QtGui.QAction(parent=MainWindow)
        self.actionYou.setObjectName("actionYou")
        self.import_from_folder_menu_action = QtGui.QAction(parent=MainWindow)
        self.import_from_folder_menu_action.setObjectName("import_from_folder_menu_action")
        self.print_calculation_menu_action = QtGui.QAction(parent=MainWindow)
        self.print_calculation_menu_action.setObjectName("print_calculation_menu_action")
        self.menuMenu.addAction(self.import_excel_file_menu_action)
        self.menuMenu.addAction(self.import_from_folder_menu_action)
        self.menuTools.addAction(self.print_calculation_menu_action)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.select_all_tool_button.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "School Management"))
        self.label.setText(_translate("MainWindow", "Search:"))
        self.addRecipient_button.setText(_translate("MainWindow", "Add Recipient"))
        self.email_button.setText(_translate("MainWindow", "Email"))
        self.removeRecipient_button.setText(_translate("MainWindow", "Remove Recipient"))
        self.select_all_tool_button.setTabText(self.select_all_tool_button.indexOf(self.tab_3), _translate("MainWindow", "Email"))
        self.Subject_label.setText(_translate("MainWindow", "Subject:"))
        self.category_label.setText(_translate("MainWindow", "Category:"))
        self.quarter_label.setText(_translate("MainWindow", "Quarter:"))
        self.Q1_checkBox.setText(_translate("MainWindow", "Q1"))
        self.Q2_checkBox.setText(_translate("MainWindow", "Q2"))
        self.Q3_checkBox.setText(_translate("MainWindow", "Q3"))
        self.Q4_checkBox.setText(_translate("MainWindow", "Q4"))
        self.graph_button.setText(_translate("MainWindow", "Generate graph"))
        self.select_all_tool_button.setTabText(self.select_all_tool_button.indexOf(self.tab_2), _translate("MainWindow", "Statistics"))
        self.edit_percentages_button.setText(_translate("MainWindow", "Edit Percentages"))
        self.grade_calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.label_3.setText(_translate("MainWindow", "Grade"))
        self.label_2.setText(_translate("MainWindow", "Category"))
        self.label_4.setText(_translate("MainWindow", "Weight"))
        self.subject_gc_label.setText(_translate("MainWindow", "Subject:"))
        self.gc_extract_grades_button.setText(_translate("MainWindow", "Extract Grades"))
        self.gc_clear_button.setText(_translate("MainWindow", "Clear"))
        self.select_all_tool_button.setTabText(self.select_all_tool_button.indexOf(self.tab_4), _translate("MainWindow", "Grade Calculator"))
        self.menuMenu.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.import_excel_file_menu_action.setText(_translate("MainWindow", "Import Excel File"))
        self.actionHow.setText(_translate("MainWindow", "How"))
        self.actionAre.setText(_translate("MainWindow", "Are"))
        self.actionYou.setText(_translate("MainWindow", "You"))
        self.import_from_folder_menu_action.setText(_translate("MainWindow", "Import from folder"))
        self.print_calculation_menu_action.setText(_translate("MainWindow", "Print Calculation"))
