from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QPainterPath)
from PySide2.QtWidgets import *

import files_rc
import newfiles_rc
import aa

class Ui_SubWindow(object):
	def setupUi(self, MainWindow, ui):
		buttonBasic = '''
			QPushButton
			{
				background-position: center;
				border: none;
				border-radius: 15px;
				background-color: rgb(27, 29, 35);
			}
			QPushButton:hover
			{
				background-color: rgb(33, 37, 43);
			}
			QPushButton:pressed
			{
				background-color: rgb(85, 170, 255);
			}
		'''
		frameBasic = '''
			QFrame
			{
				background-color: rgb(40, 44, 53);
				border-radius: 5px;
			}
		'''

		brush6 = QBrush(QColor(210, 210, 210, 255))
		brush6.setStyle(Qt.SolidPattern)

		tableSizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		tableSizePolicy.setHorizontalStretch(0)
		tableSizePolicy.setVerticalStretch(0)

		########### Home 탭 UI
		self.page_home = QWidget()
		self.page_home.setObjectName(u"page_home")

		# 홈화면 위젯 전반 Vertical Layout 옵션 부여 및 메인 프레임 생성
		self.homeVerticalMainLayout = QVBoxLayout(self.page_home)
		self.homeVerticalMainLayout.setObjectName(u"homeVerticalMainLayout")

		self.homeMainFrame = QFrame(self.page_home)
		self.homeMainFrame.setFrameShape(QFrame.StyledPanel)
		self.homeMainFrame.setFrameShadow(QFrame.Raised)
		self.homeMainFrame.setMinimumSize(QSize(0, 450))
		self.homeMainFrame.setObjectName(u"homeMainFrame")

		# 홈화면 상단 프레임 초기화 작업
		self.homeFrameUpper = QFrame(self.homeMainFrame)
		self.homeFrameUpper.setObjectName(u"homeFrameUpper")
		self.homeFrameUpper.setMinimumSize(QSize(0, 370))
		self.homeFrameUpper.setMaximumSize(QSize(16777215, 350))
		self.homeFrameUpper.setFrameShape(QFrame.NoFrame)
		self.homeFrameUpper.setFrameShadow(QFrame.Raised)
		self.homeFrameUpper.setStyleSheet(u"QFrame {\n"
		"	border-radius: 5px;\n"
		"}")

		# 홈화면 하단 프레임 초기화 작업
		self.homeFrameBottom = QFrame(self.homeMainFrame)
		self.homeFrameBottom.setObjectName(u"homeFrameBottom")
		self.homeFrameBottom.setMinimumSize(QSize(0, 180))
		self.homeFrameBottom.setMaximumSize(QSize(16777215, 180))
		self.homeFrameBottom.setFrameShape(QFrame.NoFrame)
		self.homeFrameBottom.setFrameShadow(QFrame.Raised)
		self.homeFrameBottom.setStyleSheet(u"QFrame {\n"
		"	background-color: rgb(40, 44, 53);\n"
		"	border-radius: 5px;\n"
		"}")

		# 홈화면 라벨 홀더 프레임 생성
		self.homeLabelcontentFrame = QFrame(self.homeFrameUpper)
		self.homeLabelcontentFrame.setObjectName(u"homeLabelcontentFrame")
		self.homeLabelcontentFrame.setMinimumSize(QSize(0, 300))
		self.homeLabelcontentFrame.setMaximumSize(QSize(16777215, 300))
		self.homeLabelcontentFrame.setFrameShape(QFrame.NoFrame)
		self.homeLabelcontentFrame.setFrameShadow(QFrame.Raised)

		# 홈화면 라벨 Horizontal Layout 옵션 부여
		self.homeLabelHorizontalLayout = QHBoxLayout(self.homeFrameUpper)
		self.homeLabelHorizontalLayout.setObjectName(u"homeLabelHorizontalLayout")

		# 홈화면 라벨 홀더 프레임 Grid Layout 옵션 부여
		self.homeUpperGridLayout = QGridLayout()
		self.homeUpperGridLayout.setObjectName(u"homeUpperGridLayout")
		self.homeUpperGridLayout.setContentsMargins(-1, -1, -1, 0)

		# 홈화면 라벨 생성
		self.homeLabel = QLabel(self.homeLabelcontentFrame)
		self.homeLabel.setObjectName(u"homeLabel")
		font5 = QFont()
		font5.setFamily(u"Segoe UI")
		font5.setPointSize(45)
		font5.setWeight(QFont.Bold)
		self.homeLabel.setFont(font5)
		self.homeLabel.setMinimumSize(QSize(0, 300))
		self.homeLabel.setStyleSheet('''
		QLabel
		{
			color: white;
			background-image: url(:/newimg/icons/image/background.jpg) 0 0 0 0 stretch stretch;
			background-position: center;
			background-repeat: no-repeat;
		}
		''')
		self.homeLabel.setAlignment(Qt.AlignCenter)

		# 홈 화면 하단 Horizontal Layout 선언
		self.homeBottomHorizontalLayout = QHBoxLayout(self.homeFrameBottom)
		self.homeBottomHorizontalLayout.setObjectName(u"homeBottomHorizontalLayout")

		# 홈 화면 버튼 홀더 프레임을 위한 Horizontal Layout 선언
		self.homeButtonHorizontalLayout = QHBoxLayout()
		self.homeButtonHorizontalLayout.setObjectName(u"homeButtonHorizontalLayout")

		## 홈화면 퀵메뉴 버튼 생성
		# 홈에서 Search 탭으로 버튼
		self.homeMoveToSearchButton = QPushButton()
		self.homeMoveToSearchButton.setStyleSheet(buttonBasic)
		self.homeMoveToSearchButton.setObjectName(u"homeMoveToSearchButton")
		self.homeMoveToSearchButton.setMinimumSize(QSize(180, 100))
		self.homeMoveToSearchButton.setMaximumSize(QSize(16777215, 100))
		self.homeMoveToSearchButton.setFont(QFont(u"Segoe UI", 28, QFont.Bold))
		# 홈에서 Analysis 탭으로 버튼 
		self.homeMoveToAnalysisButton = QPushButton()
		self.homeMoveToAnalysisButton.setStyleSheet(buttonBasic)
		self.homeMoveToAnalysisButton.setObjectName(u"homeMoveToAnalysisButton")
		self.homeMoveToAnalysisButton.setMinimumSize(QSize(180, 100))
		self.homeMoveToAnalysisButton.setMaximumSize(QSize(16777215, 100))
		self.homeMoveToAnalysisButton.setFont(QFont(u"Segoe UI", 28, QFont.Bold))
		# 홈에서 Recommend 탭으로 버튼
		self.homeMoveToRecommendButton = QPushButton()
		self.homeMoveToRecommendButton.setObjectName(u"homeMoveToRecommendButton")
		self.homeMoveToRecommendButton.setStyleSheet(buttonBasic)
		self.homeMoveToRecommendButton.setMinimumSize(QSize(180, 100))
		self.homeMoveToRecommendButton.setMaximumSize(QSize(16777215, 100))
		self.homeMoveToRecommendButton.setFont(QFont(u"Segoe UI", 26, QFont.Bold))

		# 홈 화면 Grid Layout 에 라벨 삽입
		self.homeUpperGridLayout.addWidget(self.homeLabel, 0, 0, 0, 0)

		# 홈 화면 Horizontal Layout 에 Grid Layout
		self.homeLabelHorizontalLayout.addLayout(self.homeUpperGridLayout)

		# 홈 화면 Horizontal Layout 에 버튼 삽입
		self.homeButtonHorizontalLayout.addWidget(self.homeMoveToSearchButton)
		self.homeButtonHorizontalLayout.addWidget(self.homeMoveToAnalysisButton)
		self.homeButtonHorizontalLayout.addWidget(self.homeMoveToRecommendButton)

		# 홈 화면 Horizontal Layout 에 버튼 홀더 프레임 삽입
		self.homeBottomHorizontalLayout.addLayout(self.homeButtonHorizontalLayout)

		# 홈 화면 메인 Layout 에 상단, 하단 프레임 순차 삽입
		self.homeVerticalMainLayout.addWidget(self.homeFrameUpper)
		self.homeVerticalMainLayout.addWidget(self.homeFrameBottom)

		# 위젯 스택에 home 탭 UI 삽입
		ui.stackedWidget.addWidget(self.page_home)

		########### Search Tab
		self.page_search = QWidget()
		self.page_search.setObjectName(u"page_search")

		# Search 탭 전반 Vertical Layout 부여
		self.searchVerticalMainLayout = QVBoxLayout(self.page_search)
		self.searchVerticalMainLayout.setObjectName(u"homeVerticalMainLayout")

		# Search Grid Layout
		self.searchUpperGridLayout = QGridLayout()
		self.searchUpperGridLayout.setObjectName(u"searchUpperGridLayout")
		self.searchUpperGridLayout.setContentsMargins(0, 0, 0, 0)

		# Search 라벨 홀더 프레임(좌측 상단)
		self.searchListLabelFrame = QFrame()
		self.searchListLabelFrame.setObjectName(u"searchListLabelFrame")
		self.searchListLabelFrame.setFrameShape(QFrame.StyledPanel)
		self.searchListLabelFrame.setFrameShadow(QFrame.Raised)
		self.searchListLabelFrame.setMinimumSize(QSize(0, 20))
		self.searchListLabelFrame.setMaximumSize(QSize(16777215, 20))

		# 좌측 상단 라벨
		self.searchLeftLabel = QLabel(self.searchListLabelFrame)
		self.searchLeftLabel.setObjectName(u"searchLeftLabel")
		self.searchLeftLabel.setFont(QFont(u"Segoe UI", 13, QFont.Bold))
		self.searchLeftLabel.setStyleSheet(u"color: white;")

		# Search 라벨 홀더 프레임(우측 상단)
		self.searchInfoLabelFrame = QFrame()
		self.searchInfoLabelFrame.setObjectName(u"searchInfoLabelFrame")
		self.searchInfoLabelFrame.setFrameShape(QFrame.StyledPanel)
		self.searchInfoLabelFrame.setFrameShadow(QFrame.Raised)
		self.searchInfoLabelFrame.setMinimumSize(QSize(250, 20))
		self.searchInfoLabelFrame.setMaximumSize(QSize(250, 20))

		# 우측 상단 라벨
		self.searchRightLabel = QLabel(self.searchInfoLabelFrame)
		self.searchRightLabel.setObjectName(u"searchRightLabel")
		self.searchRightLabel.setFont(QFont(u"Segoe UI", 13, QFont.Bold))
		self.searchRightLabel.setStyleSheet(u"color: white;")

		# Search 테이블 홀더 프레임
		self.searchTablecontainFrame = QFrame()
		self.searchTablecontainFrame.setObjectName(u"searchTableFrame")
		self.searchTablecontainFrame.setFrameShape(QFrame.StyledPanel)
		self.searchTablecontainFrame.setFrameShadow(QFrame.Raised)
		self.searchTablecontainFrame.setMinimumSize(QSize(0, 150))
		self.searchTablecontainFrame.setMaximumSize(QSize(16777215, 16777215))
		# self.searchTablecontainFrame.setStyleSheet(u"background-color: yellow;")

		# Search 테이블 홀더 Layout
		self.searchTableHorizontalLayout = QHBoxLayout(self.searchTablecontainFrame)
		self.searchTableHorizontalLayout.setObjectName(u"searchTableHorizontalLayout")
		self.searchTableHorizontalLayout.setSpacing(0)
		self.searchTableHorizontalLayout.setContentsMargins(0, 0, 0, 0)

		# Search 테이블 프레임 삽입
		self.searchTableFrame = QFrame(self.searchTablecontainFrame)
		self.searchTableFrame.setObjectName(u"searchTableFrame")
		self.searchTableFrame.setFrameShape(QFrame.StyledPanel)
		self.searchTableFrame.setFrameShadow(QFrame.Raised)
		self.searchTableFrame.setMinimumSize(QSize(0, 340))
		# self.searchTableFrame.setMaximumSize(QSize(16777215, 16777215))
		self.searchTableFrame.setStyleSheet(frameBasic)

		self.tableWidget = QTableWidget(self.searchTablecontainFrame)

		if (self.tableWidget.columnCount() < 4):
			self.tableWidget.setColumnCount(4)
		__qtablewidgetitem = QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
		__qtablewidgetitem1 = QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
		__qtablewidgetitem2 = QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
		__qtablewidgetitem3 = QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)

		if (self.tableWidget.rowCount() < 16):
			self.tableWidget.setRowCount(16)

		__qtablewidgetitem4 = QTableWidgetItem()
		# __qtablewidgetitem4.setFont(font2);
		self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
		__qtablewidgetitem5 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
		__qtablewidgetitem6 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
		__qtablewidgetitem7 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
		__qtablewidgetitem8 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
		__qtablewidgetitem9 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
		__qtablewidgetitem10 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
		__qtablewidgetitem11 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
		__qtablewidgetitem12 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
		__qtablewidgetitem13 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
		__qtablewidgetitem14 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
		__qtablewidgetitem15 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
		__qtablewidgetitem16 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
		__qtablewidgetitem17 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
		__qtablewidgetitem18 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
		__qtablewidgetitem19 = QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
		__qtablewidgetitem20 = QTableWidgetItem()

		self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
		__qtablewidgetitem21 = QTableWidgetItem()
		self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
		__qtablewidgetitem22 = QTableWidgetItem()
		self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
		__qtablewidgetitem23 = QTableWidgetItem()
		self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
		self.tableWidget.setObjectName(u"tableWidget")
		tableSizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
		self.tableWidget.setSizePolicy(tableSizePolicy)

		palette1 = QPalette()
		palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
		brush15 = QBrush(QColor(39, 44, 54, 255))
		brush15.setStyle(Qt.SolidPattern)
		palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
		palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
		palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
		palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
		palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
		brush16 = QBrush(QColor(210, 210, 210, 128))
		brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
		palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
		palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
		palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
		palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
		palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
		palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
		brush17 = QBrush(QColor(210, 210, 210, 128))
		brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
		palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
		palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
		palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
		palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
		palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
		palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
		brush18 = QBrush(QColor(210, 210, 210, 128))
		brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
		self.tableWidget.setPalette(palette1)
		self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: rgb(52, 59, 72);\n"
"	height: 14px;\n"
"	margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background: rgb(52, 59, 72);\n"
"	width: 14px;\n"
"	margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
	"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"	border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

		self.tableWidget.setFrameShape(QFrame.NoFrame)
		self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
		self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget.setAlternatingRowColors(False)
		self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
		self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.tableWidget.setShowGrid(True)
		self.tableWidget.setGridStyle(Qt.SolidLine)
		self.tableWidget.setSortingEnabled(False)
		self.tableWidget.horizontalHeader().setVisible(True)
		self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.tableWidget.verticalHeader().setVisible(False)
		self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
		self.tableWidget.verticalHeader().setHighlightSections(False)
		self.tableWidget.verticalHeader().setStretchLastSection(True)

		# Search 우측 메뉴
		self.searchRightFrame = QFrame()
		self.searchRightFrame.setObjectName(u"searchRightFrame")
		self.searchRightFrame.setFrameShape(QFrame.StyledPanel)
		self.searchRightFrame.setFrameShadow(QFrame.Raised)
		self.searchRightFrame.setMinimumSize(QSize(250, 340))
		self.searchRightFrame.setMaximumSize(QSize(250, 16777215))
		self.searchRightFrame.setStyleSheet(frameBasic)

		# Search 우측 내부 전체 Vertical Layout 지정
		self.searchRightMenuLayout = QVBoxLayout(self.searchRightFrame)
		self.searchRightMenuLayout.setObjectName(u"searchRightMenuLayout")
		self.searchRightMenuLayout.setSpacing(0)
		self.searchRightMenuLayout.setContentsMargins(0, 0, 0, 0)

		# 하위 메뉴 라벨 폰트 설정
		searchLabelFont = QFont()
		searchLabelFont.setFamily(u"Segoe UI")
		searchLabelFont.setPointSize(13)
		searchLabelFont.setBold(True)
		searchLabelFont.setWeight(75)

		# Search Name Widget Line Edit 프레임 설정
		self.searchRightNameFrame = QFrame(self.searchRightFrame)
		self.searchRightNameFrame.setObjectName(u"searchRightNameFrame")
		self.searchRightNameFrame.setFrameShape(QFrame.NoFrame)
		self.searchRightNameFrame.setFrameShadow(QFrame.Raised)
		self.searchRightNameFrame.setMaximumSize(QSize(16777215, 70))

		# Search 메뉴 프레임 내부 inner Vertical Layout 지정
		self.searchRightNameLayout = QVBoxLayout(self.searchRightNameFrame)
		self.searchRightNameLayout.setObjectName(u"searchRightNameLayout")
		self.searchRightNameLayout.setSpacing(0)
		self.searchRightNameLayout.setContentsMargins(4, 0, 4, 3)

		# line Edit 라벨 생성
		self.nameEditLabel = QLabel(self.searchRightNameFrame)
		self.nameEditLabel.setObjectName(u"nameEditLabel")
		self.nameEditLabel.setFont(searchLabelFont)
		self.nameEditLabel.setMaximumSize(QSize(16777215, 50))
		self.nameEditLabel.setStyleSheet(u"color: white;")

		# line Edit 생성
		self.namelineEdit = QLineEdit(self.searchRightNameFrame)
		self.namelineEdit.setObjectName(u"namelineEdit")
		self.namelineEdit.setMinimumSize(QSize(0, 30))
		self.namelineEdit.setStyleSheet(u"QLineEdit {\n"
		"	background-color: rgb(27, 29, 35);\n"
		"	border-radius: 5px;\n"
		"	padding-left: 10px;\n"
		"}\n"
		"QLineEdit:hover {\n"
		"	border: 2px solid rgb(64, 71, 88);\n"
		"}\n"
		"QLineEdit:focus {\n"
		"	border: 2px solid rgb(91, 101, 124);\n"
		"}"
		)

		# Search Main menu Widget Line Edit 프레임 설정
		self.searchRightMainMenuFrame = QFrame(self.searchRightFrame)
		self.searchRightMainMenuFrame.setObjectName(u"searchRightMenuFrame")
		self.searchRightMainMenuFrame.setFrameShape(QFrame.NoFrame)
		self.searchRightMainMenuFrame.setFrameShadow(QFrame.Raised)
		self.searchRightMainMenuFrame.setMaximumSize(QSize(16777215, 70))

		# Search 메뉴 프레임 내부 inner Vertical Layout 지정
		self.searchRightMainMenuLayout = QVBoxLayout(self.searchRightMainMenuFrame)
		self.searchRightMainMenuLayout.setObjectName(u"searchRightMenuLayout")
		self.searchRightMainMenuLayout.setSpacing(0)
		self.searchRightMainMenuLayout.setContentsMargins(4, 1, 4, 5)

		# line Edit 라벨 생성
		self.menuEditLabel = QLabel(self.searchRightMainMenuFrame)
		self.menuEditLabel.setObjectName(u"menuEditLabel")
		self.menuEditLabel.setFont(searchLabelFont)
		self.menuEditLabel.setStyleSheet(u"color: white;")

		# line Edit 생성
		self.menulineEdit = QLineEdit(self.searchRightMainMenuFrame)
		self.menulineEdit.setObjectName(u"menulineEdit")
		self.menulineEdit.setMinimumSize(QSize(0, 30))
		self.menulineEdit.setStyleSheet(u"QLineEdit {\n"
		"	background-color: rgb(27, 29, 35);\n"
		"	border-radius: 5px;\n"
		"	padding-left: 10px;\n"
		"}\n"
		"QLineEdit:hover {\n"
		"	border: 2px solid rgb(64, 71, 88);\n"
		"}\n"
		"QLineEdit:focus {\n"
		"	border: 2px solid rgb(91, 101, 124);\n"
		"}"
		)

		# Search Button Font
		searchBtnFont = QFont()
		searchBtnFont.setFamily(u"Segoe UI")
		searchBtnFont.setPointSize(13)
		searchBtnFont.setWeight(15)

		searchBtnIcon = QIcon()
		searchBtnIcon.addFile(u":/16x16/icons/16x16/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)

		# Search Menu 버튼 홀더 프레임
		self.searchBtnHolderFrame = QFrame(self.searchRightFrame)
		self.searchBtnHolderFrame.setObjectName(u"searchBtnHolderFrame")
		self.searchBtnHolderFrame.setMaximumSize(QSize(16777215, 100))

		# Search Menu 버튼 inner Horizontal Layout 지정
		self.searchBtnHolderLayout = QVBoxLayout(self.searchBtnHolderFrame)
		self.searchBtnHolderLayout.setObjectName(u"searchBtnHolderLayout")
		self.searchBtnHolderLayout.setSpacing(0)
		self.searchBtnHolderLayout.setContentsMargins(0, 0, 0, 0)

		# Location 프레임
		self.searchLocationBtnFrame = QFrame(self.searchBtnHolderFrame)
		self.searchLocationBtnFrame.setObjectName(u"searchLocationBtnFrame")
		self.searchLocationBtnFrame.setMaximumSize(QSize(16777215, 140))

		# Location 프레임 레이아웃
		self.searchLocationBtnFrameLayout = QHBoxLayout(self.searchLocationBtnFrame)
		self.searchLocationBtnFrameLayout.setObjectName(u"searchLocationBtnFrameLayout")
		self.searchLocationBtnFrameLayout.setContentsMargins(4, 3, 4, 0)

		# Location Label
		self.searchLocationLabel = QLabel(self.searchLocationBtnFrame)
		self.searchLocationLabel.setObjectName(u"searchLocationLabel")
		self.searchLocationLabel.setFont(searchLabelFont)
		self.searchLocationLabel.setMaximumSize(QSize(70, 16777215))
		self.searchLocationLabel.setStyleSheet(u"color: white;")
		
		# Location 버튼 생성
		self.searchLocationBtn = QPushButton(self.searchLocationBtnFrame)
		self.searchLocationBtn.setObjectName(u"searchLocationBtn")
		self.searchLocationBtn.setMinimumSize(QSize(0, 30))
		self.searchLocationBtn.setFont(searchBtnFont)
		self.searchLocationBtn.setIcon(searchBtnIcon)
		self.searchLocationBtn.setStyleSheet(u"QPushButton {\n"
		"	border: 2px solid rgb(52, 59, 72);\n"
		"	border-radius: 5px;\n"
		"	background-color: rgb(52, 59, 72);\n"
		"}\n"
		"QPushButton:hover {\n"
		"	background-color: rgb(57, 65, 80);\n"
		"	border: 2px solid rgb(61, 70, 86);\n"
		"}\n"
		"QPushButton:pressed {\n"
		"	background-color: rgb(35, 40, 49);\n"
		"	border: 2px solid rgb(43, 50, 61);\n"
		"}")


		# Review 프레임
		self.searchReviewBtnFrame = QFrame(self.searchBtnHolderFrame)
		self.searchReviewBtnFrame.setObjectName(u"searchReviewBtnFrame")
		self.searchReviewBtnFrame.setMaximumSize(QSize(16777215, 140))

		# Review 프레임 레이아웃
		self.searchReviewBtnFrameLayout = QHBoxLayout(self.searchReviewBtnFrame)
		self.searchReviewBtnFrameLayout.setObjectName(u"searchReviewBtnFrameLayout")
		self.searchReviewBtnFrameLayout.setContentsMargins(4, 3, 4, 0)

		# Review Label
		self.searchReviewLabel = QLabel(self.searchReviewBtnFrame)
		self.searchReviewLabel.setObjectName(u"searchReviewLabel")
		self.searchReviewLabel.setFont(searchLabelFont)
		self.searchReviewLabel.setMaximumSize(QSize(70, 16777215))
		self.searchReviewLabel.setStyleSheet(u"color: white;")

		# Review 버튼
		self.searchReviewBtn = QPushButton(self.searchReviewBtnFrame)
		self.searchReviewBtn.setObjectName(u"searchReviewBtn")
		self.searchReviewBtn.setMinimumSize(QSize(0, 30))
		self.searchReviewBtn.setFont(searchBtnFont)
		self.searchReviewBtn.setIcon(searchBtnIcon)
		self.searchReviewBtn.setStyleSheet(u"QPushButton {\n"
		"   border: 2px solid rgb(52, 59, 72);\n"
		"   border-radius: 5px;\n"
		"   background-color: rgb(52, 59, 72);\n"
		"}\n"
		"QPushButton:hover {\n"
		"   background-color: rgb(57, 65, 80);\n"
		"   border: 2px solid rgb(61, 70, 86);\n"
		"}\n"
		"QPushButton:pressed {\n"
		"   background-color: rgb(35, 40, 49);\n"
		"   border: 2px solid rgb(43, 50, 61);\n"
		"}")

		# Logo image holder 프레임
		self.searchImageHolderFrame = QFrame(self.searchRightFrame)
		self.searchImageHolderFrame.setFrameShape(QFrame.StyledPanel)
		self.searchImageHolderFrame.setFrameShadow(QFrame.Raised)
		self.searchImageHolderFrame.setMinimumSize(QSize(0, 50))
		self.searchImageHolderFrame.setMaximumSize(QSize(16777215, 50))

		# Logo image holder 프레임 Layout
		self.searchImageHolderFrameLayout = QHBoxLayout(self.searchImageHolderFrame)
		self.searchImageHolderFrameLayout.setContentsMargins(0, 0, 0, 0)

		# Logo image holder 프레임 내부 logo image Label
		self.searchImageLabel = QLabel(self.searchImageHolderFrame)
		self.searchImageLabel.setObjectName(u"searchImageLabel")
		self.searchImageLabel.setMaximumSize(QSize(50, 50))
		self.searchImageLabel.setPixmap(":/newimg/icons/image/naver.jpg")
		self.searchImageLabel.setScaledContents(True);

		pointFont = QFont()
		pointFont.setFamily(u"Segoe UI")
		pointFont.setPointSize(22)
		pointFont.setWeight(75)

		# Logo image holder 프레임 내부 평점 Label
		self.searchPointLabel = QLabel(self.searchImageHolderFrame)
		self.searchPointLabel.setObjectName(u"searchImageLabel")
		self.searchPointLabel.setFont(pointFont)
		self.searchPointLabel.setMinimumSize(QSize(100, 50))
		self.searchPointLabel.setStyleSheet(u"color: white;")
		
		## Attraction
		self.searchAttractHolderFrame = QFrame(self.searchRightFrame)
		self.searchAttractHolderFrame.setFrameShape(QFrame.StyledPanel)
		self.searchAttractHolderFrame.setFrameShadow(QFrame.Raised)
		# self.searchAttractHolderFrame.setMinimumSize(QSize(110, 110))
		self.searchAttractHolderFrame.setMaximumSize(QSize(245, 16777215))
		# self.searchAttractHolderFrame.setStyleSheet(u"background-color: red;")

		# Search attract Layout 지정
		self.searchAttractHolderFrameLayout = QVBoxLayout(self.searchAttractHolderFrame)
		self.searchAttractHolderFrameLayout.setObjectName(u"searchAttractHolderFrameLayout")
		self.searchAttractHolderFrameLayout.setContentsMargins(4, 5, 4, 5)

		# Search attract label 생성
		self.searchAttractLabel = QLabel(self.searchAttractHolderFrame)
		self.searchAttractLabel.setObjectName(u"searchAttractLabel")
		self.searchAttractLabel.setFont(searchLabelFont)
		self.searchAttractLabel.setStyleSheet(u"color: white;")

		'''
		# Search attract scroll area 생성
		self.searchAttractScrollArea = QScrollArea(self.searchAttractHolderFrame)
		self.searchAttractScrollArea.setObjectName(u"searchAttractScrollArea")
		self.searchAttractScrollArea.setFrameShape(QFrame.NoFrame)
		self.searchAttractScrollArea.setMaximumSize(QSize(245, 16777215))
		self.searchAttractScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.searchAttractScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
		self.searchAttractScrollArea.setWidgetResizable(True)
		self.searchAttractScrollArea.setStyleSheet(u"QScrollArea {\n"
		"	border: none;\n"
		"	border-radius: 0px;\n"
		"}\n"
		"QScrollBar:horizontal {\n"
		"    border: none;\n"
		"    background: rgb(52, 59, 72);\n"
		"    height: 14px;\n"
		"    margin: 0px 21px 0 21px;\n"
		"	border-radius: 0px;\n"
		"}\n"
		" QScrollBar:vertical {\n"
		"	border: none;\n"
		"    background: rgb(52, 59, 72);\n"
		"    width: 14px;\n"
		"    margin: 21px 0 21px 0;\n"
		"	border-radius: 0px;\n"
		" }\n"
		"")

		# Search Attract Scroll Area 내부 Widget 생성
		self.searchAttractInnerWidget = QWidget()
		self.searchAttractInnerWidget.setObjectName(u"scrollAttractInnerWidget")

		# Search Attract Inner Widget Layout 설정
		self.searchAttractInnerWidgetLayout = QHBoxLayout(self.searchAttractInnerWidget)
		self.searchAttractInnerWidgetLayout.setObjectName(u"searchAttractInnerWidgetLayout")
		self.searchAttractInnerWidgetLayout.setContentsMargins(0, 0, 0, 0)
		'''

		# Search Attract Inner Text Edit 생성
		self.searchAttractInnerTextEdit = QPlainTextEdit(self.searchAttractHolderFrame)
		self.searchAttractInnerTextEdit.setObjectName(u"searchAttractInnerTextEdit")
		self.searchAttractInnerTextEdit.setMinimumSize(QSize(0, 0))
		self.searchAttractInnerTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
		"	background-color: rgb(27, 29, 35);\n"
		"	border-radius: 5px;\n"
		"	padding: 10px;\n"
		"}\n"
		"QPlainTextEdit:hover {\n"
		"	border: 2px solid rgb(64, 71, 88);\n"
		"}\n"
		"QPlainTextEdit:focus {\n"
		"	border: 2px solid rgb(91, 101, 124);\n"
		"}")

		# Search 하단 프레임
		self.searchBottomFrame = QFrame()
		self.searchBottomFrame.setObjectName(u"searchBottomFrame")
		self.searchBottomFrame.setFrameShape(QFrame.StyledPanel)
		self.searchBottomFrame.setFrameShadow(QFrame.Raised)
		self.searchBottomFrame.setMinimumSize(QSize(0, 150))
		self.searchBottomFrame.setMaximumSize(QSize(16777215, 150))
		self.searchBottomFrame.setStyleSheet(frameBasic)

		# Search 하단 프레임 전체 Layout 지정
		self.searchBottomFrameLayout = QVBoxLayout(self.searchBottomFrame)
		self.searchBottomFrameLayout.setObjectName(u"searchBottomFrameLayout")

		# Search Reset 버튼 프레임
		self.searchResetButtonFrame = QFrame(self.searchBottomFrame)
		self.searchResetButtonFrame.setObjectName(u"searchResetButtonFrame")
		self.searchResetButtonFrame.setFrameShape(QFrame.NoFrame)
		self.searchResetButtonFrame.setFrameShadow(QFrame.Raised)
		self.searchResetButtonFrame.setMaximumSize(QSize(1677215, 50))

		# Search 하단 Reset 버튼
		self.searchResetButton = QPushButton(self.searchResetButtonFrame)
		self.searchResetButton.setObjectName(u"searchResetButton")
		self.searchResetButton.setMinimumSize(QSize(150, 30))
		self.searchResetButton.setMaximumSize(QSize(150, 30))
		self.searchResetButton.setFont(searchBtnFont)
		self.searchResetButton.setStyleSheet(u"QPushButton {\n"
		"   border: 2px solid rgb(52, 59, 72);\n"
		"   border-radius: 5px;\n"
		"   background-color: rgb(52, 59, 72);\n"
		"}\n"
		"QPushButton:hover {\n"
		"   background-color: rgb(57, 65, 80);\n"
		"   border: 2px solid rgb(61, 70, 86);\n"
		"}\n"
		"QPushButton:pressed {\n"
		"   background-color: rgb(35, 40, 49);\n"
		"   border: 2px solid rgb(43, 50, 61);\n"
		"}")

		# Search 하단 inner 하단 프레임 
		self.searchBottomInnerFrame = QFrame(self.searchBottomFrame)
		self.searchBottomInnerFrame.setObjectName(u"searchBottomInnerFrame")
		self.searchBottomInnerFrame.setFrameShape(QFrame.NoFrame)
		self.searchBottomInnerFrame.setFrameShadow(QFrame.Raised)
		# self.searchBottomInnerFrame.setStyleSheet(u"background-color: yellow;")

		# Search 하단 inner 하단 프레임 Layout 설정
		self.searchBottomInnerFrameLayout = QHBoxLayout(self.searchBottomInnerFrame)
		self.searchBottomInnerFrameLayout.setObjectName(u"self.searchBottomInnerFrameLayout")
		self.searchBottomInnerFrameLayout.setContentsMargins(0, 0, 0, 0)

		# Menu Search 프레임
		self.searchMenuSearchFrame = QFrame(self.searchBottomInnerFrame)
		self.searchMenuSearchFrame.setObjectName(u"searchMenuSearchFrame")
		self.searchMenuSearchFrame.setFrameShape(QFrame.NoFrame)
		self.searchMenuSearchFrame.setFrameShadow(QFrame.Raised)

		# Menu Search 프레임 내부 Layout 설정
		self.searchMenuSearchFrameLayout = QVBoxLayout(self.searchMenuSearchFrame)
		self.searchMenuSearchFrameLayout.setObjectName(u"searchMenuSearchFrameLayout")
		self.searchMenuSearchFrameLayout.setSpacing(0)
		self.searchMenuSearchFrameLayout.setContentsMargins(0, 0, 0, 5)

		# Menu Search 라벨
		self.searchMenuSearchLabel = QLabel(self.searchMenuSearchFrame)
		self.searchMenuSearchLabel.setObjectName(u"searchMenuSearchLabel")
		self.searchMenuSearchLabel.setFont(searchLabelFont)
		self.searchMenuSearchLabel.setMaximumSize(QSize(16777215, 30))
		self.searchMenuSearchLabel.setStyleSheet(u"color: white;")

		# Menu Search line Edit 생성
		self.searchMenuSearchlineEdit = QLineEdit(self.searchMenuSearchFrame)
		self.searchMenuSearchlineEdit.setObjectName(u"searchMenuSearchlineEdit")
		self.searchMenuSearchlineEdit.setMinimumSize(QSize(0, 30))
		self.searchMenuSearchlineEdit.setStyleSheet(u"QLineEdit {\n"
		"   background-color: rgb(27, 29, 35);\n"
		"	background-image: url(:/16x16/icons/16x16/cil-zoom-in.png);\n"
		"	background-repeat: no-repeat;\n"
		"	background-position: right;\n"
		"   border-radius: 5px;\n"
		"   padding-left: 10px;\n"
		"	padding-right: 10px;\n"
		"}\n"
		"QLineEdit:hover {\n"
		"   border: 2px solid rgb(64, 71, 88);\n"
		"}\n"
		"QLineEdit:focus {\n"
		"   border: 2px solid rgb(91, 101, 124);\n"
		"}")

		# Region Select 프레임
		self.searchRegionSelectFrame = QFrame(self.searchBottomInnerFrame)
		self.searchRegionSelectFrame.setObjectName(u"searchRegionSelectFrame")
		self.searchRegionSelectFrame.setFrameShape(QFrame.NoFrame)
		self.searchRegionSelectFrame.setFrameShadow(QFrame.Raised)
		self.searchRegionSelectFrame.setMinimumSize(QSize(150, 0))

		# Region Select 프레임 내부 Layout 설정
		self.searchRegionSelectFrameLayout = QVBoxLayout(self.searchRegionSelectFrame)
		self.searchRegionSelectFrameLayout.setObjectName(u"searchRegionSelectFrameLayout")

		# Region Select 라벨
		self.searchRegionSelectLabel = QLabel(self.searchRegionSelectFrame)
		self.searchRegionSelectLabel.setObjectName(u"searchRegionSelectLabel")
		self.searchRegionSelectLabel.setFont(searchLabelFont)
		self.searchRegionSelectLabel.setStyleSheet(u"color: white;")

		# Search Combo Box Font
		searchComboFont = QFont()
		searchComboFont.setFamily(u"Segoe UI")
		searchComboFont.setPointSize(9)

		# Region Select Combo Box 생성
		self.searchRegionSelectComboBox = QComboBox(self.searchRegionSelectFrame)
		self.searchRegionSelectComboBox.setObjectName(u"searchRegionSelectComboBox")
		self.searchRegionSelectComboBox.addItem("Select Region")
		self.searchRegionSelectComboBox.setFont(searchComboFont)
		self.searchRegionSelectComboBox.setStyleSheet(u"QComboBox {\n"
		"	background-color: rgb(27, 29, 35);\n"
		"	border-radius: 5px;\n"
		"	border: 2px solid rgb(27, 29, 35);\n"
		"	padding: 5px;\n"
		"	padding-left: 10px;\n"
		"}\n"
		"QComboBox:hover{\n"
		"	border: 2px solid rgb(64, 71, 88);\n"
		"}\n"
		"QComboBox QAbstractItemView {\n"
		"	color: rgb(85, 170, 255);	\n"
		"	background-color: rgb(27, 29, 35);\n"
		"	padding: 10px;\n"
		"	selection-background-color: rgb(39, 44, 54);\n"
		"}")

		# Industry Type 프레임
		self.searchIndustryTypeFrame = QFrame(self.searchBottomInnerFrame)
		self.searchIndustryTypeFrame.setObjectName(u"searchIndustryTypeFrame")
		self.searchIndustryTypeFrame.setFrameShape(QFrame.NoFrame)
		self.searchIndustryTypeFrame.setFrameShadow(QFrame.Raised)
		self.searchIndustryTypeFrame.setMinimumSize(QSize(150, 0))

		# Industry Type 프레임 내부 Layout 설정
		self.searchIndustryTypeFrameLayout = QVBoxLayout(self.searchIndustryTypeFrame)
		self.searchIndustryTypeFrameLayout.setObjectName(u"searchIndustryTypeFrameLayout")

		# Industry Type 라벨
		self.searchIndustryTypeLabel = QLabel()
		self.searchIndustryTypeLabel.setObjectName(u"searchIndustryTypeLabel")
		self.searchIndustryTypeLabel.setFont(searchLabelFont)
		self.searchIndustryTypeLabel.setStyleSheet(u"color: white;")

		# Industry Type Combo Box
		self.searchIndustryTypeComboBox = QComboBox(self.searchIndustryTypeFrame)
		self.searchIndustryTypeComboBox.setObjectName(u"searchIndustryTypeComboBox")
		self.searchIndustryTypeComboBox.addItem("Select Industry")
		self.searchIndustryTypeComboBox.setFont(searchComboFont)
		self.searchIndustryTypeComboBox.setStyleSheet(u"QComboBox {\n"
		"	background-color: rgb(27, 29, 35);\n"
		"	border-radius: 5px;\n"
		"	border: 2px solid rgb(27, 29, 35);\n"
		"	padding: 5px;\n"
		"	padding-left: 10px;\n"
		"}\n"
		"QComboBox:hover{\n"
		"	border: 2px solid rgb(64, 71, 88);\n"
		"}\n"
		"QComboBox QAbstractItemView {\n"
		"	color: rgb(85, 170, 255);	\n"
		"	background-color: rgb(27, 29, 35);\n"
		"	padding: 10px;\n"
		"	selection-background-color: rgb(39, 44, 54);\n"
		"}")

		# List Criteria 프레임
		self.searchListCriteriaFrame = QFrame(self.searchBottomInnerFrame)
		self.searchListCriteriaFrame.setObjectName(u"searchListCriteriaFrame")
		self.searchListCriteriaFrame.setFrameShape(QFrame.NoFrame)
		self.searchListCriteriaFrame.setFrameShadow(QFrame.Raised)
		self.searchListCriteriaFrame.setMinimumSize(QSize(150, 0))

		# List Criteria 프레임 내부 Layout 설정
		self.searchListCriteriaFrameLayout = QVBoxLayout(self.searchListCriteriaFrame)
		self.searchListCriteriaFrameLayout.setObjectName(u"searchListCriteriaFrameLayout")

		# List Criteria 라벨
		self.searchListCriteriaLabel = QLabel(self.searchListCriteriaFrame)
		self.searchListCriteriaLabel.setObjectName(u"searchLsitCriteria")
		self.searchListCriteriaLabel.setFont(searchLabelFont)
		self.searchListCriteriaLabel.setStyleSheet(u"color: white;")

		# List Criteria Combo Box
		self.searchListCriteriaComboBox = QComboBox(self.searchListCriteriaFrame)
		self.searchListCriteriaComboBox.setObjectName(u"searchListCriteriaComboBox")
		self.searchListCriteriaComboBox.addItem("Select Criteria")
		self.searchListCriteriaComboBox.addItem("평점 높은 순")
		self.searchListCriteriaComboBox.addItem("평점 낮은 순")
		self.searchListCriteriaComboBox.setFont(searchComboFont)
		self.searchListCriteriaComboBox.setStyleSheet(u"QComboBox {\n"
		"   background-color: rgb(27, 29, 35);\n"
		"   border-radius: 5px;\n"
		"   border: 2px solid rgb(27, 29, 35);\n"
		"   padding: 5px;\n"
		"   padding-left: 10px;\n"
		"}\n"
		"QComboBox:hover{\n"
		"   border: 2px solid rgb(64, 71, 88);\n"
		"}\n"
		"QComboBox QAbstractItemView {\n"
		"   color: rgb(85, 170, 255);   \n"
		"   background-color: rgb(27, 29, 35);\n"
		"   padding: 10px;\n"
		"   selection-background-color: rgb(39, 44, 54);\n"
		"}")

		# Search 하단 메뉴 체크 박스 프레임
		self.searchBottomCheckBoxHolderFrame = QFrame(self.searchBottomInnerFrame)
		self.searchBottomCheckBoxHolderFrame.setObjectName(u"searchBottomCheckBoxHolderFrame")
		self.searchBottomCheckBoxHolderFrame.setFrameShape(QFrame.NoFrame)
		self.searchBottomCheckBoxHolderFrame.setFrameShadow(QFrame.Raised)

		# Search 하단 메뉴 체크 박스 프레임 내부 Layout 지정
		self.searchBottomCheckBoxHolderFrameLayout = QGridLayout(self.searchBottomCheckBoxHolderFrame)
		self.searchBottomCheckBoxHolderFrameLayout.setObjectName(u"searchBottomCheckBoxHolderFrameLayout")

		# Reservation Check Box
		self.searchReservationCheckBox = QCheckBox(self.searchBottomCheckBoxHolderFrame)
		self.searchReservationCheckBox.setObjectName(u"searchReservationCheckBox")
		self.searchReservationCheckBox.setAutoFillBackground(False)
		self.searchReservationCheckBox.setStyleSheet(u"")

		# Parking Check Box
		self.searchParkingCheckBox = QCheckBox(self.searchBottomCheckBoxHolderFrame)
		self.searchParkingCheckBox.setObjectName(u"searchParkingCheckBox")
		self.searchParkingCheckBox.setAutoFillBackground(False)
		self.searchParkingCheckBox.setStyleSheet(u"")

		# 좌측상단 라벨 프레임 삽입
		self.searchUpperGridLayout.addWidget(self.searchListLabelFrame, 0, 0)
		# 우측 상단 라벨 프레임 삽입
		self.searchUpperGridLayout.addWidget(self.searchInfoLabelFrame, 0, 1)
		# 테이블 프레임 삽입(Layout 에 삽입, 위젯 삽입 순서)
		self.searchTableHorizontalLayout.addWidget(self.tableWidget)
		self.searchUpperGridLayout.addWidget(self.searchTablecontainFrame, 1, 0)
		## 우측 메뉴 메뉴 프레임 삽입
		# Name 
		self.searchRightNameLayout.addWidget(self.nameEditLabel)
		self.searchRightNameLayout.addWidget(self.namelineEdit)
		# Main Menu
		self.searchRightMainMenuLayout.addWidget(self.menuEditLabel)
		self.searchRightMainMenuLayout.addWidget(self.menulineEdit)
		self.searchRightMainMenuLayout.addWidget(self.searchBtnHolderFrame)
		# Location
		self.searchLocationBtnFrameLayout.addWidget(self.searchLocationLabel)
		self.searchLocationBtnFrameLayout.addWidget(self.searchLocationBtn)
		self.searchBtnHolderLayout.addWidget(self.searchLocationBtnFrame)
		# Review
		self.searchReviewBtnFrameLayout.addWidget(self.searchReviewLabel)
		self.searchReviewBtnFrameLayout.addWidget(self.searchReviewBtn)
		self.searchBtnHolderLayout.addWidget(self.searchReviewBtnFrame)
		# Logo image/text
		self.searchImageHolderFrameLayout.addWidget(self.searchImageLabel)
		self.searchImageHolderFrameLayout.addWidget(self.searchPointLabel)

		# Attraction
		# self.searchAttractInnerWidgetLayout.addWidget(self.searchAttractInnerTextEdit)
		self.searchAttractHolderFrameLayout.addWidget(self.searchAttractLabel)
		self.searchAttractHolderFrameLayout.addWidget(self.searchAttractInnerTextEdit)
		# self.searchAttractHolderFrameLayout.addWidget(self.searchAttractScrollArea)

		# 오른쪽 메뉴 프레임에 차례로 프레임 삽입
		self.searchRightMenuLayout.addWidget(self.searchRightNameFrame)
		self.searchRightMenuLayout.addWidget(self.searchRightMainMenuFrame)
		self.searchRightMenuLayout.addWidget(self.searchBtnHolderFrame)
		self.searchRightMenuLayout.addWidget(self.searchImageHolderFrame)
		self.searchRightMenuLayout.addWidget(self.searchAttractHolderFrame)
		self.searchUpperGridLayout.addWidget(self.searchRightFrame, 1, 1)

		# Search 페이지에 그리드 레이아웃 삽입
		self.searchVerticalMainLayout.addLayout(self.searchUpperGridLayout)

		# 하단 프레임 설정
		## 버튼 삽입
		self.searchBottomFrameLayout.addWidget(self.searchResetButtonFrame)
		## 하단 내부 프레임에 Menu Search 프레임 삽입
		self.searchMenuSearchFrameLayout.addWidget(self.searchMenuSearchLabel)
		self.searchMenuSearchFrameLayout.addWidget(self.searchMenuSearchlineEdit)
		self.searchBottomInnerFrameLayout.addWidget(self.searchMenuSearchFrame)
		## 하단 내부 프레임에 Region Select 프레임 삽입
		self.searchRegionSelectFrameLayout.addWidget(self.searchRegionSelectLabel)
		self.searchRegionSelectFrameLayout.addWidget(self.searchRegionSelectComboBox)
		self.searchBottomInnerFrameLayout.addWidget(self.searchRegionSelectFrame)
		## 하단 내부 프레임에 Industry Type 프레임 삽입
		self.searchIndustryTypeFrameLayout.addWidget(self.searchIndustryTypeLabel)
		self.searchIndustryTypeFrameLayout.addWidget(self.searchIndustryTypeComboBox)
		self.searchBottomInnerFrameLayout.addWidget(self.searchIndustryTypeFrame)
		## 하단 내부 프레임에 List Criteria 프레임 삽입
		self.searchListCriteriaFrameLayout.addWidget(self.searchListCriteriaLabel)
		self.searchListCriteriaFrameLayout.addWidget(self.searchListCriteriaComboBox)
		self.searchBottomInnerFrameLayout.addWidget(self.searchListCriteriaFrame)
		## 하단 내부 프레임에 Check Box 홀더 프레임 삽입
		self.searchBottomCheckBoxHolderFrameLayout.addWidget(self.searchReservationCheckBox, 0, 0)
		self.searchBottomCheckBoxHolderFrameLayout.addWidget(self.searchParkingCheckBox, 1, 0)
		self.searchBottomInnerFrameLayout.addWidget(self.searchBottomCheckBoxHolderFrame)
		# 하단 내부 프레임 삽입
		self.searchBottomFrameLayout.addWidget(self.searchBottomInnerFrame)

		# 하단 프레임 삽입
		self.searchVerticalMainLayout.addWidget(self.searchBottomFrame)

		# Stacked Widget 에 page_search 탭 삽입
		ui.stackedWidget.addWidget(self.page_search)

		########### Analysis Tab
		self.page_analysis = QWidget()
		self.page_analysis.setObjectName(u"page_analysis")

		# Analysis Tab 전반 레이아웃 부여
		self.analysisVerticalMainLayout = QVBoxLayout(self.page_analysis)
		self.analysisVerticalMainLayout.setObjectName(u"analysisVerticalMainLayout")

		# Analysis 내부 Grid 레이아웃
		self.analysisInnerGridLayout = QGridLayout()
		self.analysisInnerGridLayout.setObjectName(u"analyisInnerGridLayout")

		# Analysis 상단 내부 좌측 라벨 프레임
		self.analysisUpperLeftLabelFrame = QFrame()
		self.analysisUpperLeftLabelFrame.setObjectName(u"analysisUpperLeftLabelFrame")
		self.analysisUpperLeftLabelFrame.setFrameShape(QFrame.StyledPanel)
		self.analysisUpperLeftLabelFrame.setFrameShadow(QFrame.Raised)
		self.analysisUpperLeftLabelFrame.setMinimumSize(QSize(0, 20))
		self.analysisUpperLeftLabelFrame.setMaximumSize(QSize(16777215, 20))

		# Analysis 상단 내부 우측 라벨 프레임
		self.analysisUpperRightLabelFrame = QFrame()
		self.analysisUpperRightLabelFrame.setObjectName(u"analysisUpperRightLabelFrame")
		self.analysisUpperRightLabelFrame.setFrameShape(QFrame.StyledPanel)
		self.analysisUpperRightLabelFrame.setFrameShadow(QFrame.Raised)
		self.analysisUpperRightLabelFrame.setMinimumSize(QSize(0, 20))
		self.analysisUpperRightLabelFrame.setMaximumSize(QSize(16777215, 20))

		# Analysis 상단 내부 좌측 라벨
		self.titleLabel0 = QLabel(self.analysisUpperLeftLabelFrame)
		self.titleLabel0.setObjectName(u"titleLabel0")
		self.titleLabel0.setFont(QFont(u"Segoe UI", 13, QFont.Bold))
		self.titleLabel0.setStyleSheet(u"color: white;")

		# Analysis 상단 내부 우측 라벨
		self.titleLabel1 = QLabel(self.analysisUpperRightLabelFrame)
		self.titleLabel1.setObjectName(u"titleLabel1")
		self.titleLabel1.setFont(QFont(u"Segoe UI", 13, QFont.Bold))
		self.titleLabel1.setStyleSheet(u"color: white;")

		# Analysis 상단 내부 좌측 컨텐츠 프레임
		self.analysisUpperLeftContentFrame = QFrame()
		self.analysisUpperLeftContentFrame.setObjectName(u"analysisUpperLeftContentFrame")
		self.analysisUpperLeftContentFrame.setFrameShape(QFrame.StyledPanel)
		self.analysisUpperLeftContentFrame.setFrameShadow(QFrame.Raised)
		self.analysisUpperLeftContentFrame.setMinimumSize(QSize(0, 240))
		self.analysisUpperLeftContentFrame.setMaximumSize(QSize(16777215, 16777215))
		self.analysisUpperLeftContentFrame.setStyleSheet(frameBasic)

		# Analysis 상단 내부 우측 컨텐츠 프레임
		self.analysisUpperRightContentFrame = QFrame()
		self.analysisUpperRightContentFrame.setObjectName(u"analysisUpperRightContentFrame")
		self.analysisUpperRightContentFrame.setFrameShape(QFrame.StyledPanel)
		self.analysisUpperRightContentFrame.setFrameShadow(QFrame.Raised)
		self.analysisUpperRightContentFrame.setMinimumSize(QSize(0, 240))
		self.analysisUpperRightContentFrame.setMaximumSize(QSize(16777215, 16777215))
		self.analysisUpperRightContentFrame.setStyleSheet(frameBasic)

		# Analysis 상단 내부 좌측 라벨 프레임
		self.analysisBottomLeftLabelFrame = QFrame()
		self.analysisBottomLeftLabelFrame.setObjectName(u"analysisBottomLeftLabelFrame")
		self.analysisBottomLeftLabelFrame.setFrameShape(QFrame.StyledPanel)
		self.analysisBottomLeftLabelFrame.setFrameShadow(QFrame.Raised)
		self.analysisBottomLeftLabelFrame.setMinimumSize(QSize(0, 20))
		self.analysisBottomLeftLabelFrame.setMaximumSize(QSize(16777215, 20))

		# Analysis 하단 라벨 프레임 1
		self.analysisBottomRightLabelFrame = QFrame()
		self.analysisBottomRightLabelFrame.setObjectName(u"analysisBottomRightLabelFrame1")
		self.analysisBottomRightLabelFrame.setFrameShape(QFrame.StyledPanel)
		self.analysisBottomRightLabelFrame.setFrameShadow(QFrame.Raised)
		self.analysisBottomRightLabelFrame.setMinimumSize(QSize(0, 20))
		self.analysisBottomRightLabelFrame.setMaximumSize(QSize(16777215, 20))

		# Analysis 하단 좌측 라벨
		self.titleLabel2 = QLabel(self.analysisBottomLeftLabelFrame)
		self.titleLabel2.setObjectName(u"titleLabel2")
		self.titleLabel2.setFont(QFont(u"Segoe UI", 13, QFont.Bold))
		self.titleLabel2.setStyleSheet(u"color: white;")

		# Analysis 하단 우측 라벨
		self.titleLabel3 = QLabel(self.analysisBottomRightLabelFrame)
		self.titleLabel3.setObjectName(u"titleLabel3")
		self.titleLabel3.setFont(QFont(u"Segoe UI", 13, QFont.Bold))
		self.titleLabel3.setStyleSheet(u"color: white;")
	
		# 하단 컨텐츠 프레임 1
		self.analysisBottomLeftContentFrame = QFrame()
		self.analysisBottomLeftContentFrame.setObjectName(u"analysisBottomLeftContentFrame")
		self.analysisBottomLeftContentFrame.setFrameShape(QFrame.StyledPanel)
		self.analysisBottomLeftContentFrame.setFrameShadow(QFrame.Raised)
		self.analysisBottomLeftContentFrame.setMinimumSize(QSize(300, 220))
		self.analysisBottomLeftContentFrame.setMaximumSize(QSize(16777215, 16777215))
		self.analysisBottomLeftContentFrame.setStyleSheet(frameBasic)

		# 하단 컨텐츠 프레임 2
		self.analysisBottomRightContentFrame = QFrame()
		self.analysisBottomRightContentFrame.setObjectName(u"analysisBottomRightContentFrame")
		self.analysisBottomRightContentFrame.setFrameShape(QFrame.StyledPanel)
		self.analysisBottomRightContentFrame.setFrameShadow(QFrame.Raised)
		self.analysisBottomRightContentFrame.setMinimumSize(QSize(300, 220))
		self.analysisBottomRightContentFrame.setMaximumSize(QSize(16777215, 16777215))
		self.analysisBottomRightContentFrame.setStyleSheet(frameBasic)

		# 하단 컨텐츠 프레임 2 Layout 지정
		self.analysisBottomRightContentFrameLayout = QVBoxLayout(self.analysisBottomRightContentFrame)
		self.analysisBottomRightContentFrameLayout.setObjectName(u"analysisBottomRightContentFrameLayout")

		# 하단 콤보 박스
		self.analysisBottomComboBox = QComboBox(self.analysisBottomRightContentFrame)
		self.analysisBottomComboBox.setObjectName(u"analysisBottomComboBox")
		self.analysisBottomComboBox.addItem("Select Region")
		self.analysisBottomComboBox.addItem("")
		self.analysisBottomComboBox.addItem("")
		self.analysisBottomComboBox.addItem("")
		self.analysisBottomComboBox.setFont(searchComboFont)
		self.analysisBottomComboBox.setMaximumSize(QSize(150, 16777215))
		self.analysisBottomComboBox.setStyleSheet(u"QComboBox {\n"
		"   background-color: rgb(27, 29, 35);\n"
		"   border-radius: 5px;\n"
		"   border: 2px solid rgb(27, 29, 35);\n"
		"   padding: 5px;\n"
		"   padding-left: 10px;\n"
		"}\n"
		"QComboBox:hover{\n"
		"   border: 2px solid rgb(64, 71, 88);\n"
		"}\n"
		"QComboBox QAbstractItemView {\n"
		"   color: rgb(85, 170, 255);   \n"
		"   background-color: rgb(27, 29, 35);\n"
		"   padding: 10px;\n"
		"   selection-background-color: rgb(39, 44, 54);\n"
		"}")

		# 하단 내부 Inner 컨텐츠 프레임
		self.analysisBottomRightInnerContentFrame = QFrame(self.analysisBottomRightContentFrame)
		self.analysisBottomRightInnerContentFrame.setFrameShape(QFrame.StyledPanel)
		self.analysisBottomRightInnerContentFrame.setFrameShadow(QFrame.Raised)
		self.analysisBottomRightInnerContentFrame.setMinimumSize(QSize(0, 300))

		# 하단 컨텐츠 2 지정
		self.analysisBottomRightContentFrameLayout.addWidget(self.analysisBottomComboBox)
		self.analysisBottomRightContentFrameLayout.addWidget(self.analysisBottomRightInnerContentFrame)

		# Analysis Grid 레이아웃 지정
		self.analysisInnerGridLayout.addWidget(self.analysisUpperLeftLabelFrame, 0, 0)
		self.analysisInnerGridLayout.addWidget(self.analysisUpperRightLabelFrame, 0, 1)
		self.analysisInnerGridLayout.addWidget(self.analysisUpperLeftContentFrame, 1, 0)
		self.analysisInnerGridLayout.addWidget(self.analysisUpperRightContentFrame, 1, 1)
		self.analysisInnerGridLayout.addWidget(self.analysisBottomLeftLabelFrame, 2, 0)
		self.analysisInnerGridLayout.addWidget(self.analysisBottomRightLabelFrame, 2, 1)
		self.analysisInnerGridLayout.addWidget(self.analysisBottomLeftContentFrame, 3, 0)
		self.analysisInnerGridLayout.addWidget(self.analysisBottomRightContentFrame, 3, 1)

		# Analysis Main Layout 에 Grid Layout 삽입
		self.analysisVerticalMainLayout.addLayout(self.analysisInnerGridLayout)

		# StackedWidget 에 page_analysis 탭 삽입
		ui.stackedWidget.addWidget(self.page_analysis)

		########### Menu Recommend Tab
		self.page_recommend = QWidget()
		self.page_recommend.setObjectName(u"page_recommend")

		self.recommendMainLayout = QVBoxLayout(self.page_recommend)
		self.recommendMainLayout.setObjectName(u"recommendMainLayout")

		# Recommend 제목 폰트 설정
		recommendTitleFont = QFont()
		recommendTitleFont.setFamily(u"Segoe UI")
		recommendTitleFont.setPointSize(40)
		recommendTitleFont.setWeight(QFont.Bold)

		# Recommend 버튼 폰트 설정
		recommendBtnFont = QFont()
		recommendBtnFont.setFamily(u"Segoe UI")
		recommendBtnFont.setPointSize(14)
		recommendBtnFont.setWeight(QFont.Bold)

		# Recommend 제목 홀더
		self.recommendTitleHolderFrame = QFrame()
		self.recommendTitleHolderFrame.setObjectName(u"recommendTitleHolderFrame")
		self.recommendTitleHolderFrame.setFrameShape(QFrame.StyledPanel)
		self.recommendTitleHolderFrame.setFrameShadow(QFrame.Raised)
		self.recommendTitleHolderFrame.setMaximumSize(QSize(16777215, 70))

		self.recommendTitleHolderLayout = QHBoxLayout(self.recommendTitleHolderFrame)
		self.recommendTitleHolderLayout.setObjectName(u"recommendTitleHolderLayout")

		self.recommendTitleLabel = QLabel(self.recommendTitleHolderFrame)
		self.recommendTitleLabel.setObjectName(u"recommendTitleLabel")
		self.recommendTitleLabel.setFont(recommendTitleFont)
		self.recommendTitleLabel.setStyleSheet(u"color: white;")
		self.recommendTitleLabel.setAlignment(Qt.AlignCenter)

		# Recommend 클릭 버튼 홀더 상단
		self.recommendButtonHolderUpperFrame = QFrame()
		self.recommendButtonHolderUpperFrame.setObjectName(u"recommendButtonHolderUpperFrame")
		self.recommendButtonHolderUpperFrame.setFrameShape(QFrame.StyledPanel)
		self.recommendButtonHolderUpperFrame.setFrameShadow(QFrame.Raised)
		self.recommendButtonHolderUpperFrame.setMinimumSize(QSize(0, 300))
		self.recommendButtonHolderUpperFrame.setStyleSheet(frameBasic)

		# Recommend 클릭 버튼 홀더 상단 Layout 지정
		self.recommendButtonHolderUpperFrameLayout = QVBoxLayout(self.recommendButtonHolderUpperFrame)
		self.recommendButtonHolderUpperFrameLayout.setObjectName(u"recommendButtonHolderUpperFrame")

		# Recommend 클릭 버튼 홀더 상단 Inner 프레임
		self.recommendBtnInnerUpperFrame = QFrame(self.recommendButtonHolderUpperFrame)
		self.recommendBtnInnerUpperFrame.setObjectName(u"recommmendBtnInnerUpperFrame")
		self.recommendBtnInnerUpperFrame.setFrameShape(QFrame.StyledPanel)
		self.recommendBtnInnerUpperFrame.setFrameShadow(QFrame.Raised)

		# Recommend 클릭 버튼 홀더 상단 Inner 프레임 Layout
		self.recommendBtnInnerUpperFrameLayout = QHBoxLayout(self.recommendBtnInnerUpperFrame)
		self.recommendBtnInnerUpperFrameLayout.setObjectName(u"recommendBtnInnerUpperFrameLayout")

		# Box button 스타일 지정
		boxButton = '''
		QPushButton {
			border: 2px solid rgb(27, 29, 34);
			border-radius: 5px;
			background-color: rgb(27, 29, 34);
		}
		QPushButton:hover {
			background-color: rgb(57, 65, 80);
			border: 2px solid rgb(61, 70, 86);
		}
		QPushButton:pressed {
		background-color: rgb(35, 40, 49);
		border: 2px solid rgb(43, 50, 61);
		}
		'''

		# Box button 폰트 지정
		boxFont = QFont()
		boxFont.setFamily(u"Segoe UI")
		boxFont.setPointSize(20)

		# Basic button 폰트 지정
		boxBasicFont = QFont()
		boxBasicFont.setFamily(u"Segoe UI")
		boxBasicFont.setPointSize(12)

		# Box1
		self.recommendBoxButton1 = QPushButton(self.recommendBtnInnerUpperFrame)
		self.recommendBoxButton1.setObjectName(u"recommendBoxButton1")
		self.recommendBoxButton1.setMinimumSize(QSize(0, 150))
		self.recommendBoxButton1.setCheckable(True)
		self.recommendBoxButton1.setFont(boxFont)
		self.recommendBoxButton1.setStyleSheet(boxButton)

		# Box2
		self.recommendBoxButton2 = QPushButton(self.recommendBtnInnerUpperFrame)
		self.recommendBoxButton2.setObjectName(u"recommendBoxButton2")
		self.recommendBoxButton2.setMinimumSize(QSize(0, 150))
		self.recommendBoxButton2.setCheckable(True)
		self.recommendBoxButton2.setFont(boxFont)
		self.recommendBoxButton2.setStyleSheet(boxButton)

		# Box3
		self.recommendBoxButton3 = QPushButton(self.recommendBtnInnerUpperFrame)
		self.recommendBoxButton3.setObjectName(u"recommendBoxButton3")
		self.recommendBoxButton3.setMinimumSize(QSize(0, 150))
		self.recommendBoxButton3.setCheckable(True)
		self.recommendBoxButton3.setFont(boxFont)
		self.recommendBoxButton3.setStyleSheet(boxButton)

		# Box4
		self.recommendBoxButton4 = QPushButton(self.recommendBtnInnerUpperFrame)
		self.recommendBoxButton4.setObjectName(u"recommendBoxButton4")
		self.recommendBoxButton4.setMinimumSize(QSize(0, 150))
		self.recommendBoxButton4.setCheckable(True)
		self.recommendBoxButton4.setFont(boxFont)
		self.recommendBoxButton4.setStyleSheet(boxButton)

		# Recommend 클릭 버튼 홀더 상단 Inner 하단 버튼 프레임
		self.recommendSearchBtnInnerBottomFrame = QFrame(self.recommendButtonHolderUpperFrame)
		self.recommendSearchBtnInnerBottomFrame.setObjectName(u"recommendSearchBtnInnerBottomFrame")
		self.recommendSearchBtnInnerBottomFrame.setFrameShape(QFrame.StyledPanel)
		self.recommendSearchBtnInnerBottomFrame.setFrameShadow(QFrame.Raised)
		self.recommendSearchBtnInnerBottomFrame.setMaximumSize(QSize(16777215, 60))

		# Recommend Select Button Frame 내부 Layout 지정
		self.recommendSearchBtnInnerBottomLayout = QHBoxLayout(self.recommendSearchBtnInnerBottomFrame)
		self.recommendSearchBtnInnerBottomLayout.setObjectName(u"recommendSearchBtnInnerBottomLayout")

		# Recommend Select Button
		self.recommendSelectMenuButton = QPushButton(self.recommendSearchBtnInnerBottomFrame)
		self.recommendSelectMenuButton.setObjectName(u"recommendSelectMenuButton")
		self.recommendSelectMenuButton.setMaximumSize(QSize(340, 60))
		self.recommendSelectMenuButton.setFont(recommendBtnFont)
		self.recommendSelectMenuButton.setEnabled(False)
		self.recommendSelectMenuButton.setStyleSheet(u"QPushButton {\n"
		"	border: 2px solid rgb(52, 59, 72);\n"
		"	border-radius: 5px;\n"
		"	background-color: rgb(50, 71, 84);\n"
		"}\n"
		"QPushButton:hover {\n"
		"	background-color: rgb(57, 65, 80);\n"
		"	border: 2px solid rgb(61, 70, 86);\n"
		"}\n"
		"QPushButton:pressed {\n"
		"	background-color: rgb(35, 40, 49);\n"
		"	border: 2px solid rgb(43, 50, 61);\n"
		"}")

		# Recommend 클릭 버튼 홀더 하단
		self.recommendButtonHolderBottomFrame = QFrame()
		self.recommendButtonHolderBottomFrame.setFrameShape(QFrame.StyledPanel)
		self.recommendButtonHolderBottomFrame.setMaximumSize(QSize(16777215, 300))
		self.recommendButtonHolderBottomFrame.setFrameShadow(QFrame.Raised)

		# Recommend 클릭 버튼 홀더 Layout 설정
		self.recommendButtonHolderBottomFrameLayout = QGridLayout(self.recommendButtonHolderBottomFrame)
		self.recommendButtonHolderBottomFrameLayout.setObjectName(u"recommendButtonHolderBottomFrameLayout")

		# Recommend 하단 blank 프레임 생성
		self.recommendBlankFrame = QFrame(self.recommendButtonHolderBottomFrame)
		self.recommendBlankFrame.setObjectName(u"recommendBlankFrame")
		self.recommendBlankFrame.setMaximumSize(QSize(180, 200))
		self.recommendBlankFrame.setFrameShape(QFrame.NoFrame)
		self.recommendBlankFrame.setFrameShadow(QFrame.Raised)

		# Recommend 하단 프레임 Start 버튼 생성
		self.recommendStartButton = QPushButton(self.recommendButtonHolderBottomFrame)
		self.recommendStartButton.setObjectName(u"recommendStartButton")
		self.recommendStartButton.setMaximumSize(QSize(220, 200))
		self.recommendStartButton.setFont(recommendTitleFont)
		self.recommendStartButton.setStyleSheet(u"QPushButton {\n"
		"   border: 2px solid rgb(40, 44, 53);\n"
		"   border-radius: 5px;\n"
		"   background-color: rgb(40, 44, 53);\n"
		"}\n"
		"QPushButton:hover {\n"
		"   background-color: rgb(57, 65, 80);\n"
		"   border: 2px solid rgb(61, 70, 86);\n"
		"}\n"
		"QPushButton:pressed {\n"
		"   background-color: rgb(35, 40, 49);\n"
		"   border: 2px solid rgb(43, 50, 61);\n"
		"}")

		# Recommend 하단 Next Button Icon 설정
		recommendBtnIcon = QIcon()
		recommendBtnIcon.addFile(u":/newimg/icons/24x24/cil-chevron-circle-right-alt.png", QSize(), QIcon.Normal, QIcon.Off)

		# Recommend 하단 프레임 Next Button 생성
		self.recommendNextButton = QPushButton(self.recommendButtonHolderBottomFrame)
		self.recommendNextButton.setObjectName(u"recommendNextButton")
		self.recommendNextButton.setMaximumSize(QSize(220, 200))
		self.recommendNextButton.setFont(recommendTitleFont)
		self.recommendNextButton.setIcon(recommendBtnIcon)
		self.recommendNextButton.setIconSize(QSize(100, 100))
		self.recommendNextButton.setLayoutDirection(Qt.RightToLeft)
		self.recommendNextButton.setStyleSheet(u"QPushButton {\n"
		"   border: 2px solid rgb(40, 44, 53);\n"
		"   border-radius: 5px;\n"
		"   background-color: rgb(40, 44, 53);\n"
		"}\n"
		"QPushButton:hover {\n"
		"   background-color: rgb(57, 65, 80);\n"
		"   border: 2px solid rgb(61, 70, 86);\n"
		"}\n"
		"QPushButton:pressed {\n"
		"   background-color: rgb(35, 40, 49);\n"
		"   border: 2px solid rgb(43, 50, 61);\n"
		"}")

		# Recommend 제목 홀더 프레임 Layout에 Label 삽입
		self.recommendTitleHolderLayout.addWidget(self.recommendTitleLabel)

		# Recommend Inner 버튼 홀더에 Box 버튼 삽입
		self.recommendBtnInnerUpperFrameLayout.addWidget(self.recommendBoxButton1)
		self.recommendBtnInnerUpperFrameLayout.addWidget(self.recommendBoxButton2)
		self.recommendBtnInnerUpperFrameLayout.addWidget(self.recommendBoxButton3)
		self.recommendBtnInnerUpperFrameLayout.addWidget(self.recommendBoxButton4)

		# Recommend 버튼 홀더 Upper Layout 에 프레임 및 하위요소 삽입
		self.recommendSearchBtnInnerBottomLayout.addWidget(self.recommendSelectMenuButton)
		self.recommendButtonHolderUpperFrameLayout.addWidget(self.recommendBtnInnerUpperFrame)
		self.recommendButtonHolderUpperFrameLayout.addWidget(self.recommendSearchBtnInnerBottomFrame)

		# Recommend 버튼 홀더 Bottom Layout 에 하위 요소 삽입
		self.recommendButtonHolderBottomFrameLayout.addWidget(self.recommendBlankFrame, 0, 0)
		self.recommendButtonHolderBottomFrameLayout.addWidget(self.recommendStartButton, 0, 1)
		self.recommendButtonHolderBottomFrameLayout.addWidget(self.recommendNextButton, 0, 2)

		# Recommend Vertical Layout 에 삽입
		self.recommendMainLayout.addWidget(self.recommendTitleHolderFrame)
		self.recommendMainLayout.addWidget(self.recommendButtonHolderUpperFrame)
		self.recommendMainLayout.addWidget(self.recommendButtonHolderBottomFrame)

		# StackWidget 에 page_recommend 탭 삽입
		ui.stackedWidget.addWidget(self.page_recommend)

		########### Introduction Developer Tab
		self.page_intro = QWidget()
		self.page_intro.setObjectName(u"page_intro")

		# Introduce 프로필 사진 Style 지정
		profilePicStyle =  '''
		QFrame {
		}
		'''

		nameLabelFont = QFont()
		nameLabelFont.setFamily(u"Segoe UI")
		nameLabelFont.setPointSize(20)
		nameLabelFont.setWeight(300)

		roleLabelFont = QFont()
		roleLabelFont.setFamily(u"Segoe UI")
		roleLabelFont.setPointSize(12)
		roleLabelFont.setWeight(QFont.Bold)

		donateTitleFont = QFont()
		donateTitleFont.setFamily(u"Segoe UI")
		donateTitleFont.setPointSize(18)
		donateTitleFont.setWeight(300)

		donateBankFont = QFont()
		donateBankFont.setFamily(u"Segoe UI")
		donateBankFont.setPointSize(20)
		donateBankFont.setWeight(QFont.Bold)

		# Introduce Main 화면 레이아웃 지정
		self.introMainLayout = QVBoxLayout(self.page_intro)
		self.introMainLayout.setObjectName(u"introMainLayout")

		# Introduce 제목 홀더 프레임
		self.introTitleHolderFrame = QFrame()
		self.introTitleHolderFrame.setObjectName(u"introTitleHolderFrame")
		self.introTitleHolderFrame.setFrameShape(QFrame.StyledPanel)
		self.introTitleHolderFrame.setFrameShadow(QFrame.Raised)
		self.introTitleHolderFrame.setMaximumSize(QSize(16777215, 70))

		# Introduce 제목 폰트 설정
		introTitleFont = QFont()
		introTitleFont.setFamily("Segoe UI")
		introTitleFont.setPointSize(40)
		introTitleFont.setWeight(QFont.Bold)

		# Introduce 제목 홀더 프레임 Layout 지정
		self.introTitleHolderFrameLayout = QHBoxLayout(self.introTitleHolderFrame)
		self.introTitleHolderFrameLayout.setObjectName(u"introTitleHolderFrameLayout")

		# Introduce 제목 Label 생성
		self.introTitleLabel = QLabel(self.introTitleHolderFrame)
		self.introTitleLabel.setObjectName(u"introTitleHolder")
		self.introTitleLabel.setFont(introTitleFont)
		self.introTitleLabel.setAlignment(Qt.AlignCenter)
		self.introTitleLabel.setStyleSheet(u"color: white;")

		# Introduce 프로필 홀더 프레임
		self.introProfileHolderFrame = QFrame()
		self.introProfileHolderFrame.setObjectName(u"introProfileHolderFrame")
		self.introProfileHolderFrame.setFrameShape(QFrame.StyledPanel)
		self.introProfileHolderFrame.setFrameShadow(QFrame.Raised)
		self.introProfileHolderFrame.setMaximumSize(QSize(900, 500))

		# Introduce 프로필 홀더 Layout 설정
		self.introProfileHolderFrameLayout = QHBoxLayout(self.introProfileHolderFrame)
		self.introProfileHolderFrameLayout.setObjectName(u"introProfileHolderFrameLayout")

		## 프로필 프레임 1
		# Introduce 프로필 프레임 1
		self.introProfileFrame1 = QFrame(self.introProfileHolderFrame)
		self.introProfileFrame1.setObjectName(u"introProfileFrame1")
		self.introProfileFrame1.setFrameShape(QFrame.StyledPanel)
		self.introProfileFrame1.setFrameShadow(QFrame.Raised)

		# Introduce 프로필 프레임 1 내부 Layout 지정
		self.introProfileFrame1Layout = QVBoxLayout(self.introProfileFrame1)
		self.introProfileFrame1Layout.setObjectName(u"introProfileFrame1Layout")

		# Introduce 프로필 프레임 1 안 사진 라벨
		self.introProfilePicLabel1 = QLabel(self.introProfileFrame1)
		self.introProfilePicLabel1.setObjectName(u"introProfilePicLabel1")
		self.introProfilePicLabel1.setFrameShape(QFrame.StyledPanel)
		self.introProfilePicLabel1.setFrameShadow(QFrame.Raised)
		self.introProfilePicLabel1.setStyleSheet(profilePicStyle)
		self.introProfilePicLabel1.setMinimumSize(160, 160)
		self.introProfilePicLabel1.setMaximumSize(160, 160)

		# Picture
		self.pic1 = QPixmap(self.introProfilePicLabel1.size())
		self.pic1.fill(Qt.transparent)
		p = QPixmap(":/newimg/icons/image/dongchan.jpg").scaled(160, 160, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
		painter = QPainter(self.pic1)
		painter.setRenderHint(QPainter.Antialiasing, True)
		painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
		painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
		path = QPainterPath()
		path.addRoundedRect(0, 0, self.introProfilePicLabel1.width(), self.introProfilePicLabel1.height(), 80, 80)
		painter.setClipPath(path)
		painter.drawPixmap(0, 0, p)
		self.introProfilePicLabel1.setPixmap(self.pic1)

		# Introduce 프로필 프레임 1 설명 프레임
		self.introDescriptFrame1 = QFrame(self.introProfileFrame1)
		self.introDescriptFrame1.setObjectName(u"introDescriptFrame1")
		self.introDescriptFrame1.setFrameShape(QFrame.StyledPanel)
		self.introDescriptFrame1.setFrameShadow(QFrame.Raised)
		self.introDescriptFrame1.setMaximumSize(QSize(1677215, 100))

		# Introduce 프로필 프레임 1 설명 프레임 Layout 지정
		self.introDescriptFrame1Layout = QVBoxLayout(self.introDescriptFrame1)
		self.introDescriptFrame1Layout.setObjectName(u"introDescriptFrame1Layout")

		# Introduce 프로필 프레임 1 설명 프레임 내부 이름 라벨
		self.introDescript1NameLabel = QLabel(self.introDescriptFrame1)
		self.introDescript1NameLabel.setFont(nameLabelFont)
		self.introDescript1NameLabel.setStyleSheet(u"color: white;")
		self.introDescript1NameLabel.setAlignment(Qt.AlignCenter)

		# Introduce 프로필 프레임 1 설명 프레임 내부 이름 라벨
		self.introDescript1RoleLabel = QLabel(self.introDescriptFrame1)
		self.introDescript1RoleLabel.setFont(roleLabelFont)
		self.introDescript1RoleLabel.setStyleSheet(u"color: white;")
		self.introDescript1RoleLabel.setAlignment(Qt.AlignCenter)

		## 프로필 프레임 2
		# Introduce 프로필 프레임 2
		self.introProfileFrame2 = QFrame(self.introProfileHolderFrame)
		self.introProfileFrame2.setObjectName(u"introProfileFrame2")
		self.introProfileFrame2.setFrameShape(QFrame.WinPanel)
		self.introProfileFrame2.setFrameShadow(QFrame.Raised)

		# Introduce 프로필 프레임 2 내부 Layout 지정
		self.introProfileFrame2Layout = QVBoxLayout(self.introProfileFrame2)
		self.introProfileFrame2Layout.setObjectName(u"introProfileFrame2Layout")

		# Introduce 프로필 프레임 2 안 사진 라벨
		self.introProfilePicLabel2 = QLabel(self.introProfileFrame2)
		self.introProfilePicLabel2.setObjectName(u"introProfilePicLabel2")
		self.introProfilePicLabel2.setFrameShape(QFrame.StyledPanel)
		self.introProfilePicLabel2.setFrameShadow(QFrame.Raised)
		self.introProfilePicLabel2.setStyleSheet(profilePicStyle)
		self.introProfilePicLabel2.setMinimumSize(160, 160)
		self.introProfilePicLabel2.setMaximumSize(160, 160)

		# Picture
		self.pic2 = QPixmap(self.introProfilePicLabel2.size())
		self.pic2.fill(Qt.transparent)
		p = QPixmap(":/newimg/icons/image/juhwan.jpg").scaled(160, 160, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
		painter = QPainter(self.pic2)
		painter.setRenderHint(QPainter.Antialiasing, True)
		painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
		painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
		path = QPainterPath()
		path.addRoundedRect(0, 0, self.introProfilePicLabel2.width(), self.introProfilePicLabel2.height(), 80, 80)
		painter.setClipPath(path)
		painter.drawPixmap(0, 0, p)
		self.introProfilePicLabel2.setPixmap(self.pic2)

		# Introduce 프로필 프레임 2 설명 프레임
		self.introDescriptFrame2 = QFrame(self.introProfileFrame2)
		self.introDescriptFrame2.setObjectName(u"introDescriptFrame2")
		self.introDescriptFrame2.setFrameShape(QFrame.StyledPanel)
		self.introDescriptFrame2.setFrameShadow(QFrame.Raised)
		self.introDescriptFrame2.setMaximumSize(QSize(1677215, 100))

		# Introduce 프로필 프레임 2 설명 프레임 Layout 지정
		self.introDescriptFrame2Layout = QVBoxLayout(self.introDescriptFrame2)
		self.introDescriptFrame2Layout.setObjectName(u"introDescriptFrame2Layout")

		# Introduce 프로필 프레임 2 설명 프레임 내부 이름 라벨
		self.introDescript2NameLabel = QLabel(self.introDescriptFrame2)
		self.introDescript2NameLabel.setFont(nameLabelFont)
		self.introDescript2NameLabel.setStyleSheet(u"color: white;")
		self.introDescript2NameLabel.setAlignment(Qt.AlignCenter)

		# Introduce 프로필 프레임 1 설명 프레임 내부 이름 라벨
		self.introDescript2RoleLabel = QLabel(self.introDescriptFrame2)
		self.introDescript2RoleLabel.setFont(roleLabelFont)
		self.introDescript2RoleLabel.setStyleSheet(u"color: white;")
		self.introDescript2RoleLabel.setAlignment(Qt.AlignCenter)

		## 프로필 프레임 3
		# Introduce 프로필 프레임 3
		self.introProfileFrame3 = QFrame(self.introProfileHolderFrame)
		self.introProfileFrame3.setObjectName(u"introProfileFrame3")
		self.introProfileFrame3.setFrameShape(QFrame.StyledPanel)
		self.introProfileFrame3.setFrameShadow(QFrame.Raised)

		# Introduce 프로필 프레임 3 내부 Layout 지정
		self.introProfileFrame3Layout = QVBoxLayout(self.introProfileFrame3)
		self.introProfileFrame3Layout.setObjectName(u"introProfileFrame3Layout")

		# Introduce 프로필 프레임 3 안 사진 라벨
		self.introProfilePicLabel3 = QLabel(self.introProfileFrame3)
		self.introProfilePicLabel3.setObjectName(u"introProfilePicLabel3")
		self.introProfilePicLabel3.setFrameShape(QFrame.StyledPanel)
		self.introProfilePicLabel3.setFrameShadow(QFrame.Raised)
		self.introProfilePicLabel3.setStyleSheet(profilePicStyle)
		self.introProfilePicLabel3.setMinimumSize(160, 160)
		self.introProfilePicLabel3.setMaximumSize(160, 160)

		# Picture
		self.pic3 = QPixmap(self.introProfilePicLabel3.size())
		self.pic3.fill(Qt.transparent)
		p = QPixmap(":/newimg/icons/image/myeongdong.jpg").scaled(160, 160, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
		painter = QPainter(self.pic3)
		painter.setRenderHint(QPainter.Antialiasing, True)
		painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
		painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
		path = QPainterPath()
		path.addRoundedRect(0, 0, self.introProfilePicLabel3.width(), self.introProfilePicLabel3.height(), 80, 80)
		painter.setClipPath(path)
		painter.drawPixmap(0, 0, p)
		self.introProfilePicLabel3.setPixmap(self.pic3)

		# Introduce 프로필 프레임 3 설명 프레임
		self.introDescriptFrame3 = QFrame(self.introProfileFrame3)
		self.introDescriptFrame3.setObjectName(u"introDescriptFrame3")
		self.introDescriptFrame3.setFrameShape(QFrame.StyledPanel)
		self.introDescriptFrame3.setFrameShadow(QFrame.Raised)
		self.introDescriptFrame3.setMaximumSize(QSize(1677215, 100))

		# Introduce 프로필 프레임 3 설명 프레임 Layout 지정
		self.introDescriptFrame3Layout = QVBoxLayout(self.introDescriptFrame3)
		self.introDescriptFrame3Layout.setObjectName(u"introDescriptFrame3Layout")

		# Introduce 프로필 프레임 3 설명 프레임 내부 이름 라벨
		self.introDescript3NameLabel = QLabel(self.introDescriptFrame3)
		self.introDescript3NameLabel.setFont(nameLabelFont)
		self.introDescript3NameLabel.setStyleSheet(u"color: white;")
		self.introDescript3NameLabel.setAlignment(Qt.AlignCenter)

		# Introduce 프로필 프레임 3 설명 프레임 내부 이름 라벨
		self.introDescript3RoleLabel = QLabel(self.introDescriptFrame3)
		self.introDescript3RoleLabel.setFont(roleLabelFont)
		self.introDescript3RoleLabel.setStyleSheet(u"color: white;")
		self.introDescript3RoleLabel.setAlignment(Qt.AlignCenter)

		## 프로필 프레임 4
		# Introduce 프로필 프레임 4
		self.introProfileFrame4 = QFrame(self.introProfileHolderFrame)
		self.introProfileFrame4.setObjectName(u"introProfileFrame4")
		self.introProfileFrame4.setFrameShape(QFrame.StyledPanel)
		self.introProfileFrame4.setFrameShadow(QFrame.Raised)

		# Introduce 프로필 프레임 4 내부 Layout 지정
		self.introProfileFrame4Layout = QVBoxLayout(self.introProfileFrame4)
		self.introProfileFrame4Layout.setObjectName(u"introProfileFrame4Layout")

		# Introduce 프로필 프레임 4 안 사진 라벨
		self.introProfilePicLabel4 = QLabel(self.introProfileFrame4)
		self.introProfilePicLabel4.setObjectName(u"introProfilePicLabel4")
		self.introProfilePicLabel4.setFrameShape(QFrame.StyledPanel)
		self.introProfilePicLabel4.setFrameShadow(QFrame.Raised)
		self.introProfilePicLabel4.setStyleSheet(profilePicStyle)
		self.introProfilePicLabel4.setMinimumSize(160, 160)
		self.introProfilePicLabel4.setMaximumSize(160, 160)

		# Picture
		self.pic4 = QPixmap(self.introProfilePicLabel4.size())
		self.pic4.fill(Qt.transparent)
		p = QPixmap(u":/newimg/icons/image/myeongun.jpg").scaled(160, 160, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
		painter = QPainter(self.pic4)
		painter.setRenderHint(QPainter.Antialiasing, True)
		painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
		painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
		path = QPainterPath()
		path.addRoundedRect(0, 0, self.introProfilePicLabel4.width(), self.introProfilePicLabel4.height(), 80, 80)
		painter.setClipPath(path)
		painter.drawPixmap(0, 0, p)
		self.introProfilePicLabel4.setPixmap(self.pic4)

		# Introduce 프로필 프레임 4 설명 프레임
		self.introDescriptFrame4 = QFrame(self.introProfileFrame4)
		self.introDescriptFrame4.setObjectName(u"introDescriptFrame4")
		self.introDescriptFrame4.setFrameShape(QFrame.StyledPanel)
		self.introDescriptFrame4.setFrameShadow(QFrame.Raised)
		self.introDescriptFrame4.setMaximumSize(QSize(1677215, 100))

		# Introduce 프로필 프레임 4 설명 프레임 Layout 지정
		self.introDescriptFrame4Layout = QVBoxLayout(self.introDescriptFrame4)
		self.introDescriptFrame4Layout.setObjectName(u"introDescriptFrame4Layout")

		# Introduce 프로필 프레임 4 설명 프레임 내부 이름 라벨
		self.introDescript4NameLabel = QLabel(self.introDescriptFrame4)
		self.introDescript4NameLabel.setFont(nameLabelFont)
		self.introDescript4NameLabel.setStyleSheet(u"color: white;")
		self.introDescript4NameLabel.setAlignment(Qt.AlignCenter)

		# Introduce 프로필 프레임 4 설명 프레임 내부 이름 라벨
		self.introDescript4RoleLabel = QLabel(self.introDescriptFrame4)
		self.introDescript4RoleLabel.setFont(roleLabelFont)
		self.introDescript4RoleLabel.setStyleSheet(u"color: white;")
		self.introDescript4RoleLabel.setAlignment(Qt.AlignCenter)

		# Introduce Donate 홀더 프레임
		self.introDonateHolderFrame = QFrame()
		self.introDonateHolderFrame.setObjectName(u"introDonateHolderFrame")
		self.introDonateHolderFrame.setFrameShape(QFrame.StyledPanel)
		self.introDonateHolderFrame.setFrameShadow(QFrame.Raised)
		self.introDonateHolderFrame.setMaximumSize(QSize(16777215, 300))

		# Introduce Donate 홀더 프레임 Layout 지정
		self.introDonateHolderFrameLayout = QVBoxLayout(self.introDonateHolderFrame)
		self.introDonateHolderFrameLayout.setObjectName(u"introDonateHolderFrameLayout")

		# Introduce Donate Title Label
		self.introDonateTitleLabel = QLabel(self.introDonateHolderFrame)
		self.introDonateTitleLabel.setFont(donateTitleFont)
		self.introDonateTitleLabel.setStyleSheet(u"color: white;")
		self.introDonateTitleLabel.setAlignment(Qt.AlignCenter)

		# Introduce Donate Bank Number
		self.introDonateBankLabel = QLabel(self.introDonateHolderFrame)
		self.introDonateBankLabel.setFont(donateBankFont)
		self.introDonateBankLabel.setStyleSheet(u"color: white;")
		self.introDonateBankLabel.setAlignment(Qt.AlignCenter)

		# Introduce 제목 Frame 에 Label 삽입
		self.introTitleHolderFrameLayout.addWidget(self.introTitleLabel)

		# Introduce 설명 프레임에 이름, 역할 라벨 삽입
		self.introDescriptFrame1Layout.addWidget(self.introDescript1NameLabel)
		self.introDescriptFrame1Layout.addWidget(self.introDescript1RoleLabel)
		self.introDescriptFrame2Layout.addWidget(self.introDescript2NameLabel)
		self.introDescriptFrame2Layout.addWidget(self.introDescript2RoleLabel)
		self.introDescriptFrame3Layout.addWidget(self.introDescript3NameLabel)
		self.introDescriptFrame3Layout.addWidget(self.introDescript3RoleLabel)
		self.introDescriptFrame4Layout.addWidget(self.introDescript4NameLabel)
		self.introDescriptFrame4Layout.addWidget(self.introDescript4RoleLabel)

		# Introduce 개별 프레임 하위 요소들 삽입
		# self.introProfileFrame1Layout.addWidget(self.introProfilePicFrame1)
		self.introProfileFrame1Layout.addWidget(self.introProfilePicLabel1)
		self.introProfileFrame1Layout.addWidget(self.introDescriptFrame1)
		self.introProfileFrame2Layout.addWidget(self.introProfilePicLabel2)
		self.introProfileFrame2Layout.addWidget(self.introDescriptFrame2)
		self.introProfileFrame3Layout.addWidget(self.introProfilePicLabel3)
		self.introProfileFrame3Layout.addWidget(self.introDescriptFrame3)
		self.introProfileFrame4Layout.addWidget(self.introProfilePicLabel4)
		self.introProfileFrame4Layout.addWidget(self.introDescriptFrame4)

		# Introduce 프로필 Frame 에 개별 프레임 삽입
		self.introProfileHolderFrameLayout.addWidget(self.introProfileFrame1)
		self.introProfileHolderFrameLayout.addWidget(self.introProfileFrame2)
		self.introProfileHolderFrameLayout.addWidget(self.introProfileFrame3)
		self.introProfileHolderFrameLayout.addWidget(self.introProfileFrame4)

		# Introduce Donate 프레임에 개별 요소 삽입
		self.introDonateHolderFrameLayout.addWidget(self.introDonateTitleLabel)
		self.introDonateHolderFrameLayout.addWidget(self.introDonateBankLabel)

		# Introduce Main Layout 에 프레임 삽입
		self.introMainLayout.addWidget(self.introTitleHolderFrame)
		self.introMainLayout.addWidget(self.introProfileHolderFrame)
		self.introMainLayout.addWidget(self.introDonateHolderFrame)

		# Stacked Widget 에 page_intro 삽입
		ui.stackedWidget.addWidget(self.page_intro)

		# GUI에 초기 텍스트 삽입
		self.retranslateUi(MainWindow)
		ui.stackedWidget.setCurrentIndex(1)

	def retranslateUi(self, MainWindow):
		self.homeLabel.setText(QCoreApplication.translate("MainWindow", u"Restaurant Analysis Program", None))
		self.homeMoveToSearchButton.setText("Search")
		self.homeMoveToAnalysisButton.setText("Analysis")
		self.homeMoveToRecommendButton.setText("Menu\nRecommend")
		self.searchLeftLabel.setText("Restaurant List")
		self.searchRightLabel.setText("Restaurant Information")
		self.titleLabel0.setText("Restaurant Distribution Map")
		self.titleLabel1.setText("Nearby tourist attractions")
		self.titleLabel2.setText("Menu Popularity By Food Industry Graph")
		self.titleLabel3.setText("Distribution Plot of Restaurants by Region")

		___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
		___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Industry", None));
		___qtablewidgetitem.setFont(QFont(u"Segoe", 14, QFont.Bold))
		___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
		___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
		___qtablewidgetitem1.setFont(QFont(u"Segoe", 14, QFont.Bold))
		___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
		___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Main Menu", None));
		___qtablewidgetitem2.setFont(QFont(u"Segoe", 14, QFont.Bold))
		___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
		___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Naver Rating", None));
		___qtablewidgetitem3.setFont(QFont(u"Segoe", 14, QFont.Bold))

		___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
		___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
		___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
		___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
		___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
		___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
		___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
		___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
		___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
		___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
		___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
		___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
		___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
		___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
		___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
		___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
		___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
		___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.tableWidget.setSortingEnabled(False)
		self.tableWidget.setSortingEnabled(__sortingEnabled)

		# Label
		self.nameEditLabel.setText(u"Name")
		self.menuEditLabel.setText(u"Main Menu")
		self.searchLocationLabel.setText(u"Address")
		self.searchLocationBtn.setText(u"View Location")
		self.searchReviewLabel.setText(u"Rating")
		self.searchPointLabel.setText(u"평점")
		self.searchReviewBtn.setText(u"View Reviews")
		self.searchAttractLabel.setText(u"Nearby tourist attractions")
		self.searchResetButton.setText(u"Reset")
		self.searchMenuSearchLabel.setText(u"Menu Search")
		self.searchRegionSelectLabel.setText(u"Region Select")
		self.searchIndustryTypeLabel.setText(u"Industry Type")
		self.searchListCriteriaLabel.setText(u"List Criteria")
		self.searchReservationCheckBox.setText(u"Reservation available")
		self.searchParkingCheckBox.setText(u"Parking available")
		self.recommendTitleLabel.setText(u"Random Menu Recommend")
		self.recommendBoxButton1.setText(u"Test1")
		self.recommendBoxButton2.setText(u"Test2")
		self.recommendBoxButton3.setText(u"Test3")
		self.recommendBoxButton4.setText(u"Test4")
		self.recommendSelectMenuButton.setText(u"Search Selected Menu Restaurant")
		self.recommendStartButton.setText(u"Start")
		self.recommendNextButton.setText(u"Next")
		self.introTitleLabel.setText(u"DJ M2")
		self.introDescript1NameLabel.setText(u"서동찬")
		self.introDescript1RoleLabel.setText(u"Map Manager")
		self.introDescript2NameLabel.setText(u"박주환")
		self.introDescript2RoleLabel.setText(u"Graph Manager")
		self.introDescript3NameLabel.setText(u"김명동")
		self.introDescript3RoleLabel.setText(u"GUI Manager")
		self.introDescript4NameLabel.setText(u"정명언")
		self.introDescript4RoleLabel.setText(u"Data Manager")
		self.introDonateTitleLabel.setText(u"Donate Account")
		self.introDonateBankLabel.setText(u"9003 2230 7289 3 새마을")

		# Insert Value to Search Tab's ComboBox
		self.searchIndustryTypeComboBox.addItem("한식")
		self.searchIndustryTypeComboBox.addItem("일식")
		self.searchIndustryTypeComboBox.addItem("양식")
		self.searchIndustryTypeComboBox.addItem("중식")
		self.searchIndustryTypeComboBox.addItem("카페")
		self.searchIndustryTypeComboBox.addItem("패스트푸드")


