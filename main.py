
import sys
import platform
import csv
import pandas as pd
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from app_modules import *

class MainWindow(QMainWindow):
    ## CSV 파일 읽기
    def readCSV(self, FILEPATH):
        dataList = []
        try:
            with open(FILEPATH, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for val in reader:
                    dataList.append(val)
        except:
            dataList = []
            with open(FILEPATH, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for val in reader:
                    dataList.append(val)
        return dataList

    def convertListToDF(self, LISTVAL, headerFlag):
        if headerFlag == 1:
            uList = pd.DataFrame(LISTVAL)
            header = uList.iloc[0]
            uList = uList.iloc[1:]
            uList.rename(columns=header, inplace=True)
        else:
            uList = pd.DataFrame(LISTVAL)
        return uList

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.subui = Ui_SubWindow()
        self.subui.setupUi(self, self.ui)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())
        ########################################################################
        ## CSV 파일 로드 및 데이터 프레임 생성
        ########################################################################
        restrauntList = self.readCSV("data/data.csv")
        self.resList = self.convertListToDF(restrauntList, 1)
        self.resList = self.resList.loc[:, ~self.resList.columns.duplicated()]
        self.resultList = []
        self.headName = ['Industry', 'Name', 'Main Menu', 'Naver Rating']

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Restaurant Analysis Program')
        UIFunctions.labelTitle(self, 'Restaurant Analysis Program')
        UIFunctions.labelDescription(self, 'Set text')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Search", "btn_search", "url(:/16x16/icons/16x16/cil-mood-good.png)", True)
        UIFunctions.addNewMenu(self, "Analysis", "btn_analysis", "url(:/16x16/icons/16x16/cil-zoom-in.png)", True)
        UIFunctions.addNewMenu(self, "Menu\nRecommend", "btn_menu_recommend", "url(:/16x16/icons/16x16/cil-thumb-up.png)", True)
        UIFunctions.addNewMenu(self, "Introduction\nDeveloper", "btn_intro", "url(:/16x16/icons/16x16/cil-user.png)", False)
        ## ==> END ##

		## ==> 홈화면 Quick button 과 menu 버튼 작동과 연결
        SubUIFunctions.connectHomeQuickMenu(self, self.subui)
        ## ==> Search 탭 화면 밑 검색창 Enter 이벤트 연결
        SubUIFunctions.connectSearchInputToReturn(self, self.subui)
        ## ==> Table 관련 기능 이벤트 연결
        SubUIFunctions.connectHighLightChanged(self, self.subui)
        ## ==> Search 탭 Reset 버튼 연결
        SubUIFunctions.connectResetButton(self, self.subui)
        ## ==> Recommend 화면 Box Button 과 그 밑 활성화 버튼 작동 연결
        SubUIFunctions.connectToggleMenuSelectBtn(self, self.subui)
        SubUIFunctions.connectSelectMenuButton(self, self.subui)
        ## ==> Region 정보 삽입 함수 호출
        SubUIFunctions.insertRegionInfo(self, self.subui, self.resList, "지번주소")

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.subui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "DJ M2", "", True)
        ## ==> END ##


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    # Table 에서 값 선택시 우측 메뉴에 표시
    def itemChanged(self):
        try:
            currentIndex = -1
            tempDF = self.convertListToDF(self.resultList, 0)
            for currentTableItem in self.subui.tableWidget.selectedItems():
                currentIndex = currentTableItem.row()
            infoList = tempDF.loc[currentIndex].values.tolist()
            self.subui.namelineEdit.setText(infoList[1])
            self.subui.menulineEdit.setText(infoList[13])
            self.subui.searchPointLabel.setText(infoList[24])
            self.subui.searchAttractInnerTextEdit.setPlainText(infoList[30])
        except:
            print("no value")

    def resetTableView(self):
        self.subui.tableWidget.clear()
        self.subui.tableWidget.setHorizontalHeaderLabels(self.headName)
        self.subui.tableWidget.setRowCount(20)
        for i in range(len(self.headName)):
            header = self.subui.tableWidget.horizontalHeaderItem(int(i))
            header.setFont(QFont(u"Segoe", 14, QFont.Bold))
        self.subui.namelineEdit.setText("")
        self.subui.menulineEdit.setText("")
        self.subui.searchPointLabel.setText("평점")
        self.subui.searchAttractInnerTextEdit.setPlainText("")
        self.subui.searchMenuSearchlineEdit.setText("")
        self.subui.searchRegionSelectComboBox.setCurrentIndex(0)
        self.subui.searchIndustryTypeComboBox.setCurrentIndex(0)
        self.subui.searchListCriteriaComboBox.setCurrentIndex(0)
        self.subui.searchReservationCheckBox.setChecked(False)
        self.subui.searchParkingCheckBox.setChecked(False)

    # Search Input 감지 및 옵션 값 감지 함수
    def optionNkeywordDetector(self):
        colName = []
        # print("Input Text")
        # print(self.subui.searchMenuSearchlineEdit.text())
        keyword = self.subui.searchMenuSearchlineEdit.text()
        colName.append('대표메뉴')
        # print("Region")
        # print(self.subui.searchRegionSelectComboBox.currentText())
        region = self.subui.searchRegionSelectComboBox.currentText()
        colName.append('지번주소')
        # print("Industry Type")
        # print(self.subui.searchIndustryTypeComboBox.currentText())
       	industry = self.subui.searchIndustryTypeComboBox.currentText()
        colName.append('업종(메뉴)정보')
        # print("List Criteria")
        # print(self.subui.searchListCriteriaComboBox.currentText())
        criteria = self.subui.searchListCriteriaComboBox.currentText()
        colName.append('네이버 인기도')
        # print("Reservation Checked")
        # print(self.subui.searchReservationCheckBox.isChecked())
        reservation = self.subui.searchReservationCheckBox.isChecked()
        colName.append('예약가능여부')
        # print("Parking Checked")
        # print(self.subui.searchParkingCheckBox.isChecked())
        parking = self.subui.searchParkingCheckBox.isChecked()
        colName.append('주차가능유무')

        # List 형태로 결과값 반환
        self.resultList = SubUIFunctions.optionFinder(self, self.subui, self.resList, keyword, region, industry, criteria, reservation, parking, colName)
        SubUIFunctions.insertValueToTable(self, self.subui, self.resultList, self.headName)

    # Recommend 탭 결정 트리거 이후, Search 탭 전환 및 검색어 포커싱
    def btnChangeTab(self):
        sendText = ""
        if self.subui.recommendBoxButton1.isChecked() == True:
            sendText = self.subui.recommendBoxButton1.text()
        elif self.subui.recommendBoxButton2.isChecked() == True:
            sendText = self.subui.recommendBoxButton2.text()
        elif self.subui.recommendBoxButton3.isChecked() == True:
            sendText = self.subui.recommendBoxButton3.text()
        elif self.subui.recommendBoxButton4.isChecked() == True:
            sendText = self.subui.recommendBoxButton4.text()
        self.ui.stackedWidget.setCurrentWidget(self.subui.page_search)
        UIFunctions.resetStyle(self, "btn_search")
        UIFunctions.labelPage(self, "Search")
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName == "btn_search":
                w.setStyleSheet \
                    (Stylestyle_bt_standard.replace('ICON_REPLACE', "url(:/16x16/icons/16x16/cil-mood-good.png);") +
                        ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }"))
        self.subui.searchMenuSearchlineEdit.setText(sendText)

    def btnToggle(self, state):
        inputBtnWidget = self.sender()
        btnBasicStyleHeader = '''
        QPushButton {
        '''
        btnBasicStyleTail = '''
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

        selectBtnStyleTrue = '''QPushButton {
            background-color: rgb(74, 128, 150);
            border: 2px solid rgb(52, 59, 72);
            border-radius: 5px;
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

        selectBtnStyleFalse = '''QPushButton {
            background-color: rgb(50, 71, 84);
            border: 2px solid rgb(52, 59, 72);
            border-radius: 5px;
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

        toggledFont = QFont()
        toggledFont.setFamily(u"Segoe UI")
        toggledFont.setPointSize(20)
        toggledFont.setWeight(int("%s" % ({True: "200", False: "13"}[state])))

        basicFont = QFont()
        basicFont.setFamily(u"Segoe UI")
        basicFont.setPointSize(20)
        basicFont.setWeight(13)

        if inputBtnWidget.objectName() == "recommendBoxButton1":
            inputBtnWidget.setStyleSheet(btnBasicStyleHeader+"color: %s;" % (
            {True: "rgb(93, 180, 210)", False: "white"}[state])+btnBasicStyleTail)
            inputBtnWidget.setFont(toggledFont)
            self.subui.recommendBoxButton2.setChecked(False)
            self.subui.recommendBoxButton2.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton2.setFont(basicFont)
            self.subui.recommendBoxButton3.setChecked(False)
            self.subui.recommendBoxButton3.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton3.setFont(basicFont)
            self.subui.recommendBoxButton4.setChecked(False)
            self.subui.recommendBoxButton4.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton4.setFont(basicFont)
        elif inputBtnWidget.objectName() == "recommendBoxButton2":
            inputBtnWidget.setStyleSheet(btnBasicStyleHeader+"color: %s;" % (
            {True: "rgb(93, 180, 210)", False: "white"}[state])+btnBasicStyleTail)
            inputBtnWidget.setFont(toggledFont)
            self.subui.recommendBoxButton1.setChecked(False)
            self.subui.recommendBoxButton1.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton1.setFont(basicFont)
            self.subui.recommendBoxButton3.setChecked(False)
            self.subui.recommendBoxButton3.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton3.setFont(basicFont)
            self.subui.recommendBoxButton4.setChecked(False)
            self.subui.recommendBoxButton4.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton4.setFont(basicFont)
        elif inputBtnWidget.objectName() == "recommendBoxButton3":
            inputBtnWidget.setStyleSheet(btnBasicStyleHeader+"color: %s;" % (
            {True: "rgb(93, 180, 210)", False: "white"}[state])+btnBasicStyleTail)
            inputBtnWidget.setFont(toggledFont)
            self.subui.recommendBoxButton1.setChecked(False)
            self.subui.recommendBoxButton1.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton1.setFont(basicFont)
            self.subui.recommendBoxButton2.setChecked(False)
            self.subui.recommendBoxButton2.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton2.setFont(basicFont)
            self.subui.recommendBoxButton4.setChecked(False)
            self.subui.recommendBoxButton4.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton4.setFont(basicFont)
        elif inputBtnWidget.objectName() == "recommendBoxButton4":
            inputBtnWidget.setStyleSheet(btnBasicStyleHeader+"color: %s;" % (
            {True: "rgb(93, 180, 210)", False: "white"}[state])+btnBasicStyleTail)
            inputBtnWidget.setFont(toggledFont)
            self.subui.recommendBoxButton1.setChecked(False)
            self.subui.recommendBoxButton1.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton1.setFont(basicFont)
            self.subui.recommendBoxButton2.setChecked(False)
            self.subui.recommendBoxButton2.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton2.setFont(basicFont)
            self.subui.recommendBoxButton3.setChecked(False)
            self.subui.recommendBoxButton3.setStyleSheet(btnBasicStyleHeader+"color: white;"+btnBasicStyleTail)
            self.subui.recommendBoxButton3.setFont(basicFont)

        if self.subui.recommendBoxButton1.isChecked() == True or self.subui.recommendBoxButton2.isChecked() == True or self.subui.recommendBoxButton3.isChecked() == True or self.subui.recommendBoxButton4.isChecked() == True:
            self.subui.recommendSelectMenuButton.setEnabled(True)
            self.subui.recommendSelectMenuButton.setStyleSheet(selectBtnStyleTrue)
        else:
            self.subui.recommendSelectMenuButton.setEnabled(False)
            self.subui.recommendSelectMenuButton.setStyleSheet(selectBtnStyleFalse)

    # 응용 홈 Quick menu button 연동
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()
        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.subui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE SEARCH
        if btnWidget.objectName() == "btn_search" or btnWidget.objectName() == "homeMoveToSearchButton":
            self.ui.stackedWidget.setCurrentWidget(self.subui.page_search)
            UIFunctions.resetStyle(self, "btn_search")
            UIFunctions.labelPage(self, "Search")
            if btnWidget.objectName() == "btn_search":
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            else:
                for w in self.ui.frame_left_menu.findChildren(QPushButton):
                    if w.objectName() == "btn_search":
                        w.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE',
                                                                        "url(:/16x16/icons/16x16/cil-mood-good.png);")+(
                                            "QPushButton { border-right: 7px solid rgb(44, 49, 60); }"))

        # PAGE ANALSIS
        if btnWidget.objectName() == "btn_analysis" or btnWidget.objectName() == "homeMoveToAnalysisButton":
            self.ui.stackedWidget.setCurrentWidget(self.subui.page_analysis)
            UIFunctions.resetStyle(self, "btn_analysis")
            UIFunctions.labelPage(self, "Analysis")
            if btnWidget.objectName() == "btn_analysis":
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            else:
                for w in self.ui.frame_left_menu.findChildren(QPushButton):
                    if w.objectName() == "btn_analysis":
                        w.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE',
                                                                        "url(:/16x16/icons/16x16/cil-zoom-in.png);")+(
                                            "QPushButton { border-right: 7px solid rgb(44, 49, 60); }"))

        # PAGE MENU RECOMMEND
        if btnWidget.objectName() == "btn_menu_recommend" or btnWidget.objectName() == "homeMoveToRecommendButton":
            self.ui.stackedWidget.setCurrentWidget(self.subui.page_recommend)
            UIFunctions.resetStyle(self, "btn_menu_recommend")
            UIFunctions.labelPage(self, "Menu Recommend")
            if btnWidget.objectName() == "btn_menu_recommend":
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            else:
                for w in self.ui.frame_left_menu.findChildren(QPushButton):
                    if w.objectName() == "btn_menu_recommend":
                        w.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE',
                                                                        "url(:/16x16/icons/16x16/cil-thumb-up.png);")+(
                                            "QPushButton { border-right: 7px solid rgb(44, 49, 60); }"))

        # PAGE Introduce
        if btnWidget.objectName() == "btn_intro":
            self.ui.stackedWidget.setCurrentWidget(self.subui.page_intro)
            UIFunctions.resetStyle(self, "btn_intro")
            UIFunctions.labelPage(self, "Introduce Developer")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: '+str(event.key())+' | Text Press: '+str(event.text()))

    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: '+str(self.height())+' | Width: '+str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
