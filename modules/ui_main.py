# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_maincPCCzi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . files_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 552)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.central_layout = QVBoxLayout(self.centralwidget)
        self.central_layout.setSpacing(0)
        self.central_layout.setObjectName(u"central_layout")
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 50))
        self.top_bar.setAutoFillBackground(False)
        self.top_bar.setStyleSheet(u"\n"
"background-color: rgb(35, 35, 35);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setSpacing(0)
        self.top_bar_layout.setObjectName(u"top_bar_layout")
        self.top_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 50))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(25,25, 25);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.frame_toggle_layout = QVBoxLayout(self.frame_toggle)
        self.frame_toggle_layout.setSpacing(0)
        self.frame_toggle_layout.setObjectName(u"frame_toggle_layout")
        self.frame_toggle_layout.setContentsMargins(0, 0, 0, 0)
        self.button_toggle = QPushButton(self.frame_toggle)
        self.button_toggle.setObjectName(u"button_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_toggle.sizePolicy().hasHeightForWidth())
        self.button_toggle.setSizePolicy(sizePolicy)
        self.button_toggle.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/16x16/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_toggle.setIcon(icon)

        self.frame_toggle_layout.addWidget(self.button_toggle)


        self.top_bar_layout.addWidget(self.frame_toggle)

        self.frame_title = QFrame(self.top_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        self.frame_title.setMaximumSize(QSize(16777215, 50))
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.frame_title_layout = QVBoxLayout(self.frame_title)
        self.frame_title_layout.setSpacing(0)
        self.frame_title_layout.setObjectName(u"frame_title_layout")
        self.frame_title_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_title_top = QFrame(self.frame_title)
        self.frame_title_top.setObjectName(u"frame_title_top")
        self.frame_title_top.setMaximumSize(QSize(16777215, 30))
        self.frame_title_top.setFrameShape(QFrame.NoFrame)
        self.frame_title_top.setFrameShadow(QFrame.Raised)
        self.frame_title_top_layout = QHBoxLayout(self.frame_title_top)
        self.frame_title_top_layout.setSpacing(0)
        self.frame_title_top_layout.setObjectName(u"frame_title_top_layout")
        self.frame_title_top_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_title_text = QFrame(self.frame_title_top)
        self.frame_title_text.setObjectName(u"frame_title_text")
        self.frame_title_text.setFrameShape(QFrame.NoFrame)
        self.frame_title_text.setFrameShadow(QFrame.Raised)
        self.frame_title_text_layout = QHBoxLayout(self.frame_title_text)
        self.frame_title_text_layout.setSpacing(0)
        self.frame_title_text_layout.setObjectName(u"frame_title_text_layout")
        self.frame_title_text_layout.setContentsMargins(0, 0, 0, 0)
        self.icon_title = QPushButton(self.frame_title_text)
        self.icon_title.setObjectName(u"icon_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_title.sizePolicy().hasHeightForWidth())
        self.icon_title.setSizePolicy(sizePolicy1)
        self.icon_title.setMaximumSize(QSize(30, 16777215))
        self.icon_title.setStyleSheet(u"border:0px solid;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/16x16/cil-terminal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_title.setIcon(icon1)

        self.frame_title_text_layout.addWidget(self.icon_title)

        self.label_title = QLabel(self.frame_title_text)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.frame_title_text_layout.addWidget(self.label_title)


        self.frame_title_top_layout.addWidget(self.frame_title_text)

        self.frame_buttons = QFrame(self.frame_title_top)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMaximumSize(QSize(100, 16777215))
        self.frame_buttons.setFrameShape(QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.frame_buttons_layout = QHBoxLayout(self.frame_buttons)
        self.frame_buttons_layout.setSpacing(0)
        self.frame_buttons_layout.setObjectName(u"frame_buttons_layout")
        self.frame_buttons_layout.setContentsMargins(0, 0, 5, 0)
        self.button_minimize = QPushButton(self.frame_buttons)
        self.button_minimize.setObjectName(u"button_minimize")
        sizePolicy1.setHeightForWidth(self.button_minimize.sizePolicy().hasHeightForWidth())
        self.button_minimize.setSizePolicy(sizePolicy1)
        self.button_minimize.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize.setIcon(icon2)

        self.frame_buttons_layout.addWidget(self.button_minimize)

        self.button_close = QPushButton(self.frame_buttons)
        self.button_close.setObjectName(u"button_close")
        sizePolicy1.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy1)
        self.button_close.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon3)

        self.frame_buttons_layout.addWidget(self.button_close)

        self.button_status = QPushButton(self.frame_buttons)
        self.button_status.setObjectName(u"button_status")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_status.sizePolicy().hasHeightForWidth())
        self.button_status.setSizePolicy(sizePolicy2)
        self.button_status.setMinimumSize(QSize(20, 20))
        self.button_status.setMaximumSize(QSize(20, 20))
        self.button_status.setLayoutDirection(Qt.LeftToRight)
        self.button_status.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 61, 63);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"")

        self.frame_buttons_layout.addWidget(self.button_status)


        self.frame_title_top_layout.addWidget(self.frame_buttons)


        self.frame_title_layout.addWidget(self.frame_title_top)

        self.frame_title_bottom = QFrame(self.frame_title)
        self.frame_title_bottom.setObjectName(u"frame_title_bottom")
        self.frame_title_bottom.setMaximumSize(QSize(16777215, 20))
        self.frame_title_bottom.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame_title_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_title_bottom.setFrameShadow(QFrame.Raised)
        self.frame_title_bottom_layout = QVBoxLayout(self.frame_title_bottom)
        self.frame_title_bottom_layout.setSpacing(0)
        self.frame_title_bottom_layout.setObjectName(u"frame_title_bottom_layout")
        self.frame_title_bottom_layout.setContentsMargins(0, 0, 5, 0)
        self.label_page = QLabel(self.frame_title_bottom)
        self.label_page.setObjectName(u"label_page")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(7)
        self.label_page.setFont(font1)
        self.label_page.setStyleSheet(u"color: rgba(255, 255, 255, 155);")
        self.label_page.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.frame_title_bottom_layout.addWidget(self.label_page)


        self.frame_title_layout.addWidget(self.frame_title_bottom)


        self.top_bar_layout.addWidget(self.frame_title)


        self.central_layout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.content_layout = QHBoxLayout(self.content)
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.frame_left_menu_layout = QVBoxLayout(self.frame_left_menu)
        self.frame_left_menu_layout.setSpacing(0)
        self.frame_left_menu_layout.setObjectName(u"frame_left_menu_layout")
        self.frame_left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menu = QFrame(self.frame_left_menu)
        self.frame_top_menu.setObjectName(u"frame_top_menu")
        self.frame_top_menu.setFrameShape(QFrame.NoFrame)
        self.frame_top_menu.setFrameShadow(QFrame.Raised)
        self.frame_top_menu_layout = QVBoxLayout(self.frame_top_menu)
        self.frame_top_menu_layout.setSpacing(0)
        self.frame_top_menu_layout.setObjectName(u"frame_top_menu_layout")
        self.frame_top_menu_layout.setContentsMargins(0, 0, 0, 0)

        self.frame_left_menu_layout.addWidget(self.frame_top_menu, 0, Qt.AlignTop)

        self.frame_bottom_menu = QFrame(self.frame_left_menu)
        self.frame_bottom_menu.setObjectName(u"frame_bottom_menu")
        self.frame_bottom_menu.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_menu.setFrameShadow(QFrame.Raised)
        self.frame_bottom_menu_layout = QVBoxLayout(self.frame_bottom_menu)
        self.frame_bottom_menu_layout.setSpacing(0)
        self.frame_bottom_menu_layout.setObjectName(u"frame_bottom_menu_layout")
        self.frame_bottom_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.button_escom = QPushButton(self.frame_bottom_menu)
        self.button_escom.setObjectName(u"button_escom")
        self.button_escom.setMinimumSize(QSize(40, 40))
        self.button_escom.setMaximumSize(QSize(40, 40))
        self.button_escom.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(25, 25, 25);\n"
"	border-radius:20px\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/16x16/ESCOM.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_escom.setIcon(icon4)
        self.button_escom.setIconSize(QSize(40, 40))

        self.frame_bottom_menu_layout.addWidget(self.button_escom, 0, Qt.AlignHCenter)

        self.button_save = QPushButton(self.frame_bottom_menu)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setMinimumSize(QSize(0, 40))
        self.button_save.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_save.setIcon(icon5)

        self.frame_bottom_menu_layout.addWidget(self.button_save)


        self.frame_left_menu_layout.addWidget(self.frame_bottom_menu, 0, Qt.AlignBottom)


        self.content_layout.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.frame_page_layout = QVBoxLayout(self.frame_pages)
        self.frame_page_layout.setSpacing(0)
        self.frame_page_layout.setObjectName(u"frame_page_layout")
        self.frame_page_layout.setContentsMargins(0, 0, 0, 0)
        self.pages_widget = QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.frame_view = QFrame(self.page_1)
        self.frame_view.setObjectName(u"frame_view")
        self.frame_view.setFrameShape(QFrame.StyledPanel)
        self.frame_view.setFrameShadow(QFrame.Raised)
        self.frame_view_layout = QHBoxLayout(self.frame_view)
        self.frame_view_layout.setSpacing(6)
        self.frame_view_layout.setObjectName(u"frame_view_layout")
        self.frame_view_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_humidity = QFrame(self.frame_view)
        self.frame_humidity.setObjectName(u"frame_humidity")
        self.frame_humidity.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border-radius: 10px \n"
"")
        self.frame_humidity.setFrameShape(QFrame.NoFrame)
        self.frame_humidity.setFrameShadow(QFrame.Raised)
        self.frame_humidity_layout = QVBoxLayout(self.frame_humidity)
        self.frame_humidity_layout.setObjectName(u"frame_humidity_layout")
        self.button_spray = QPushButton(self.frame_humidity)
        self.button_spray.setObjectName(u"button_spray")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_spray.sizePolicy().hasHeightForWidth())
        self.button_spray.setSizePolicy(sizePolicy3)
        self.button_spray.setMinimumSize(QSize(80, 25))
        self.button_spray.setMaximumSize(QSize(80, 25))
        self.button_spray.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/16x16/cil-drop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_spray.setIcon(icon6)

        self.frame_humidity_layout.addWidget(self.button_spray, 0, Qt.AlignHCenter)


        self.frame_view_layout.addWidget(self.frame_humidity)

        self.frame_temperature = QFrame(self.frame_view)
        self.frame_temperature.setObjectName(u"frame_temperature")
        self.frame_temperature.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border-radius: 10px \n"
"")
        self.frame_temperature.setFrameShape(QFrame.NoFrame)
        self.frame_temperature.setFrameShadow(QFrame.Raised)
        self.frame_temperature_layout = QVBoxLayout(self.frame_temperature)
        self.frame_temperature_layout.setObjectName(u"frame_temperature_layout")
        self.button_ventilate = QPushButton(self.frame_temperature)
        self.button_ventilate.setObjectName(u"button_ventilate")
        sizePolicy3.setHeightForWidth(self.button_ventilate.sizePolicy().hasHeightForWidth())
        self.button_ventilate.setSizePolicy(sizePolicy3)
        self.button_ventilate.setMinimumSize(QSize(80, 25))
        self.button_ventilate.setMaximumSize(QSize(80, 25))
        self.button_ventilate.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/16x16/cil-cloudy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_ventilate.setIcon(icon7)

        self.frame_temperature_layout.addWidget(self.button_ventilate, 0, Qt.AlignHCenter)


        self.frame_view_layout.addWidget(self.frame_temperature)


        self.page_1_layout.addWidget(self.frame_view)

        self.frame_table = QFrame(self.page_1)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border-radius: 10px \n"
"")
        self.frame_table.setFrameShape(QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.frame_table_layout = QVBoxLayout(self.frame_table)
        self.frame_table_layout.setObjectName(u"frame_table_layout")
        self.table_sql = QTableWidget(self.frame_table)
        if (self.table_sql.columnCount() < 3):
            self.table_sql.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_sql.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_sql.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_sql.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.table_sql.rowCount() < 20):
            self.table_sql.setRowCount(20)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_sql.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_sql.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_sql.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_sql.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_sql.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_sql.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_sql.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_sql.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_sql.setItem(1, 2, __qtablewidgetitem11)
        self.table_sql.setObjectName(u"table_sql")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.table_sql.sizePolicy().hasHeightForWidth())
        self.table_sql.setSizePolicy(sizePolicy4)
        self.table_sql.setMaximumSize(QSize(16777215, 200))
        self.table_sql.setStyleSheet(u"QTableWidget {	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(43, 43, 43);\n"
"	border-bottom: 1px solid rgb(35, 35, 35);\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(25, 25, 25);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(35, 35, 35);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"   background: rgb(25, 25,25);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(25, 25, 25);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     s"
                        "ubcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: none;\n"
"    background: rgb(25, 25,25);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(35, 35, 35);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(25, 25,25);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(25, 25, 25);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom"
                        "-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(25, 25,25);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }R")
        self.table_sql.setFrameShape(QFrame.NoFrame)
        self.table_sql.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_sql.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_sql.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_sql.setTabKeyNavigation(True)
        self.table_sql.setProperty("showDropIndicator", True)
        self.table_sql.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_sql.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_sql.setTextElideMode(Qt.ElideRight)
        self.table_sql.setShowGrid(True)
        self.table_sql.setGridStyle(Qt.SolidLine)
        self.table_sql.setWordWrap(True)
        self.table_sql.setCornerButtonEnabled(False)
        self.table_sql.setRowCount(20)
        self.table_sql.setColumnCount(3)
        self.table_sql.horizontalHeader().setVisible(False)
        self.table_sql.horizontalHeader().setCascadingSectionResizes(True)
        self.table_sql.horizontalHeader().setStretchLastSection(True)
        self.table_sql.verticalHeader().setVisible(False)
        self.table_sql.verticalHeader().setCascadingSectionResizes(False)
        self.table_sql.verticalHeader().setProperty("showSortIndicator", False)
        self.table_sql.verticalHeader().setStretchLastSection(True)

        self.frame_table_layout.addWidget(self.table_sql)


        self.page_1_layout.addWidget(self.frame_table)

        self.pages_widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout = QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_publish = QFrame(self.page_2)
        self.frame_publish.setObjectName(u"frame_publish")
        self.frame_publish.setMinimumSize(QSize(0, 250))
        self.frame_publish.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border-radius:10px\n"
"")
        self.frame_publish.setFrameShape(QFrame.StyledPanel)
        self.frame_publish.setFrameShadow(QFrame.Raised)
        self.frame_publis_layout = QVBoxLayout(self.frame_publish)
        self.frame_publis_layout.setSpacing(8)
        self.frame_publis_layout.setObjectName(u"frame_publis_layout")
        self.label_publish = QLabel(self.frame_publish)
        self.label_publish.setObjectName(u"label_publish")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_publish.sizePolicy().hasHeightForWidth())
        self.label_publish.setSizePolicy(sizePolicy5)
        self.label_publish.setMaximumSize(QSize(16777215, 15))
        self.label_publish.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.frame_publis_layout.addWidget(self.label_publish)

        self.text_publish = QTextEdit(self.frame_publish)
        self.text_publish.setObjectName(u"text_publish")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.text_publish.sizePolicy().hasHeightForWidth())
        self.text_publish.setSizePolicy(sizePolicy6)
        self.text_publish.setMinimumSize(QSize(0, 20))
        self.text_publish.setMaximumSize(QSize(16777215, 20))
        self.text_publish.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 25);\n"
"border-radius:5px;\n"
"")
        self.text_publish.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_publish.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.frame_publis_layout.addWidget(self.text_publish)

        self.label_topic_publish = QLabel(self.frame_publish)
        self.label_topic_publish.setObjectName(u"label_topic_publish")
        sizePolicy5.setHeightForWidth(self.label_topic_publish.sizePolicy().hasHeightForWidth())
        self.label_topic_publish.setSizePolicy(sizePolicy5)
        self.label_topic_publish.setMaximumSize(QSize(16777215, 15))
        self.label_topic_publish.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.frame_publis_layout.addWidget(self.label_topic_publish)

        self.text_publish_topic = QTextEdit(self.frame_publish)
        self.text_publish_topic.setObjectName(u"text_publish_topic")
        sizePolicy6.setHeightForWidth(self.text_publish_topic.sizePolicy().hasHeightForWidth())
        self.text_publish_topic.setSizePolicy(sizePolicy6)
        self.text_publish_topic.setMinimumSize(QSize(0, 20))
        self.text_publish_topic.setMaximumSize(QSize(16777215, 20))
        self.text_publish_topic.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 25);\n"
"border-radius:5px;\n"
"")
        self.text_publish_topic.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_publish_topic.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.frame_publis_layout.addWidget(self.text_publish_topic)

        self.label_topic_message = QLabel(self.frame_publish)
        self.label_topic_message.setObjectName(u"label_topic_message")
        sizePolicy5.setHeightForWidth(self.label_topic_message.sizePolicy().hasHeightForWidth())
        self.label_topic_message.setSizePolicy(sizePolicy5)
        self.label_topic_message.setMaximumSize(QSize(16777215, 15))
        self.label_topic_message.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.frame_publis_layout.addWidget(self.label_topic_message)

        self.text_publish_message = QTextEdit(self.frame_publish)
        self.text_publish_message.setObjectName(u"text_publish_message")
        sizePolicy6.setHeightForWidth(self.text_publish_message.sizePolicy().hasHeightForWidth())
        self.text_publish_message.setSizePolicy(sizePolicy6)
        self.text_publish_message.setMinimumSize(QSize(0, 25))
        self.text_publish_message.setMaximumSize(QSize(16777215, 25))
        self.text_publish_message.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 25);\n"
"border-radius:5px;\n"
"")
        self.text_publish_message.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_publish_message.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.frame_publis_layout.addWidget(self.text_publish_message)

        self.button_publish = QPushButton(self.frame_publish)
        self.button_publish.setObjectName(u"button_publish")
        self.button_publish.setMinimumSize(QSize(100, 20))
        self.button_publish.setMaximumSize(QSize(100, 20))
        self.button_publish.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.frame_publis_layout.addWidget(self.button_publish, 0, Qt.AlignRight)

        self.button_clear_publish = QPushButton(self.frame_publish)
        self.button_clear_publish.setObjectName(u"button_clear_publish")
        self.button_clear_publish.setMinimumSize(QSize(100, 20))
        self.button_clear_publish.setMaximumSize(QSize(100, 16777215))
        self.button_clear_publish.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.frame_publis_layout.addWidget(self.button_clear_publish, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_publish, 0, Qt.AlignTop)

        self.frame_subscribe = QFrame(self.page_2)
        self.frame_subscribe.setObjectName(u"frame_subscribe")
        sizePolicy5.setHeightForWidth(self.frame_subscribe.sizePolicy().hasHeightForWidth())
        self.frame_subscribe.setSizePolicy(sizePolicy5)
        self.frame_subscribe.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border-radius:10px\n"
"")
        self.frame_subscribe.setFrameShape(QFrame.StyledPanel)
        self.frame_subscribe.setFrameShadow(QFrame.Raised)
        self.frame_subscribe_layout = QVBoxLayout(self.frame_subscribe)
        self.frame_subscribe_layout.setObjectName(u"frame_subscribe_layout")
        self.label_subscribe = QLabel(self.frame_subscribe)
        self.label_subscribe.setObjectName(u"label_subscribe")
        self.label_subscribe.setMaximumSize(QSize(16777215, 15))
        self.label_subscribe.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.frame_subscribe_layout.addWidget(self.label_subscribe)

        self.text_subscribe = QTextEdit(self.frame_subscribe)
        self.text_subscribe.setObjectName(u"text_subscribe")
        sizePolicy6.setHeightForWidth(self.text_subscribe.sizePolicy().hasHeightForWidth())
        self.text_subscribe.setSizePolicy(sizePolicy6)
        self.text_subscribe.setMinimumSize(QSize(0, 20))
        self.text_subscribe.setMaximumSize(QSize(16777215, 20))
        self.text_subscribe.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 25);\n"
"border-radius:5px;\n"
"")
        self.text_subscribe.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.frame_subscribe_layout.addWidget(self.text_subscribe)

        self.label_topic_subscribe = QLabel(self.frame_subscribe)
        self.label_topic_subscribe.setObjectName(u"label_topic_subscribe")
        self.label_topic_subscribe.setMaximumSize(QSize(16777215, 15))
        self.label_topic_subscribe.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.frame_subscribe_layout.addWidget(self.label_topic_subscribe)

        self.text_topic_subscribe = QTextEdit(self.frame_subscribe)
        self.text_topic_subscribe.setObjectName(u"text_topic_subscribe")
        sizePolicy6.setHeightForWidth(self.text_topic_subscribe.sizePolicy().hasHeightForWidth())
        self.text_topic_subscribe.setSizePolicy(sizePolicy6)
        self.text_topic_subscribe.setMinimumSize(QSize(0, 20))
        self.text_topic_subscribe.setMaximumSize(QSize(16777215, 20))
        self.text_topic_subscribe.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 25);\n"
"border-radius:5px;\n"
"")
        self.text_topic_subscribe.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.frame_subscribe_layout.addWidget(self.text_topic_subscribe)

        self.button_subscribe = QPushButton(self.frame_subscribe)
        self.button_subscribe.setObjectName(u"button_subscribe")
        sizePolicy3.setHeightForWidth(self.button_subscribe.sizePolicy().hasHeightForWidth())
        self.button_subscribe.setSizePolicy(sizePolicy3)
        self.button_subscribe.setMinimumSize(QSize(100, 20))
        self.button_subscribe.setMaximumSize(QSize(100, 16777215))
        self.button_subscribe.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.frame_subscribe_layout.addWidget(self.button_subscribe, 0, Qt.AlignRight)

        self.button_unsubscribe = QPushButton(self.frame_subscribe)
        self.button_unsubscribe.setObjectName(u"button_unsubscribe")
        self.button_unsubscribe.setMinimumSize(QSize(100, 20))
        self.button_unsubscribe.setMaximumSize(QSize(100, 16777215))
        self.button_unsubscribe.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.frame_subscribe_layout.addWidget(self.button_unsubscribe, 0, Qt.AlignRight)

        self.button_subscribe_clear = QPushButton(self.frame_subscribe)
        self.button_subscribe_clear.setObjectName(u"button_subscribe_clear")
        self.button_subscribe_clear.setMinimumSize(QSize(100, 20))
        self.button_subscribe_clear.setMaximumSize(QSize(100, 16777215))
        self.button_subscribe_clear.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.frame_subscribe_layout.addWidget(self.button_subscribe_clear, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_subscribe, 0, Qt.AlignTop)

        self.pages_widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.pages_widget.addWidget(self.page_3)

        self.frame_page_layout.addWidget(self.pages_widget, 0, Qt.AlignTop)


        self.content_layout.addWidget(self.frame_pages)


        self.central_layout.addWidget(self.content)

        self.bottom_bar = QFrame(self.centralwidget)
        self.bottom_bar.setObjectName(u"bottom_bar")
        self.bottom_bar.setMinimumSize(QSize(0, 20))
        self.bottom_bar.setMaximumSize(QSize(16777215, 20))
        self.bottom_bar.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.bottom_bar.setFrameShape(QFrame.NoFrame)
        self.bottom_bar.setFrameShadow(QFrame.Raised)
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setSpacing(0)
        self.bottom_bar_layout.setObjectName(u"bottom_bar_layout")
        self.bottom_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.label_version = QLabel(self.bottom_bar)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setFont(font)
        self.label_version.setLayoutDirection(Qt.LeftToRight)
        self.label_version.setStyleSheet(u"color: rgba(255, 255, 255, 155);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.bottom_bar_layout.addWidget(self.label_version)

        self.button_size = QPushButton(self.bottom_bar)
        self.button_size.setObjectName(u"button_size")
        self.button_size.setMaximumSize(QSize(30, 16777215))
        self.button_size.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.button_size.setStyleSheet(u"border:0px solid;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/16x16/cil-size-grip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_size.setIcon(icon8)

        self.bottom_bar_layout.addWidget(self.button_size)


        self.central_layout.addWidget(self.bottom_bar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_toggle.setText("")
        self.icon_title.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"IOT-MQTT", None))
        self.button_minimize.setText("")
        self.button_close.setText("")
        self.button_status.setText("")
        self.label_page.setText(QCoreApplication.translate("MainWindow", u"  PAGE 1", None))
        self.button_escom.setText("")
        self.button_save.setText("")
        self.button_spray.setText(QCoreApplication.translate("MainWindow", u"Spray", None))
        self.button_ventilate.setText(QCoreApplication.translate("MainWindow", u"Ventilate", None))
        ___qtablewidgetitem = self.table_sql.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURE", None));
        ___qtablewidgetitem1 = self.table_sql.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"HUMIDITY", None));
        ___qtablewidgetitem2 = self.table_sql.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"DATE", None));
        ___qtablewidgetitem3 = self.table_sql.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.table_sql.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem5 = self.table_sql.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled = self.table_sql.isSortingEnabled()
        self.table_sql.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.table_sql.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Temperature", None));
        ___qtablewidgetitem7 = self.table_sql.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Humidity", None));
        ___qtablewidgetitem8 = self.table_sql.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.table_sql.setSortingEnabled(__sortingEnabled)

        self.label_publish.setText(QCoreApplication.translate("MainWindow", u"Publish", None))
        self.label_topic_publish.setText(QCoreApplication.translate("MainWindow", u"Topic", None))
        self.label_topic_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.button_publish.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.button_clear_publish.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_subscribe.setText(QCoreApplication.translate("MainWindow", u"Subscribe", None))
        self.label_topic_subscribe.setText(QCoreApplication.translate("MainWindow", u"Topic", None))
        self.button_subscribe.setText(QCoreApplication.translate("MainWindow", u"Subscribe", None))
        self.button_unsubscribe.setText(QCoreApplication.translate("MainWindow", u"Unsubscribe", None))
        self.button_subscribe_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v3.0.0", None))
        self.button_size.setText("")
    # retranslateUi
