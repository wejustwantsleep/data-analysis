from main import *

class SubUIFunctions(MainWindow):
	# 서브메뉴, 주 메뉴 연결
	def connectHomeQuickMenu(self, subUI):
		subUI.homeMoveToSearchButton.clicked.connect(self.Button)
		subUI.homeMoveToAnalysisButton.clicked.connect(self.Button)
		subUI.homeMoveToRecommendButton.clicked.connect(self.Button)

	def connectToggleMenuSelectBtn(self, subUI):
		subUI.recommendBoxButton1.clicked.connect(self.btnToggle)
		subUI.recommendBoxButton2.clicked.connect(self.btnToggle)
		subUI.recommendBoxButton3.clicked.connect(self.btnToggle)
		subUI.recommendBoxButton4.clicked.connect(self.btnToggle)

	def connectSelectMenuButton(self, subUI):
		subUI.recommendSelectMenuButton.clicked.connect(self.btnChangeTab)

	# Search input 박스 내 enter 이벤트 처리
	def connectSearchInputToReturn(self, subUI):
		subUI.searchMenuSearchlineEdit.returnPressed.connect(self.optionNkeywordDetector)

	# 테이블 내부 하이라이트 변경시 우측 메뉴 정보 처리
	def connectHighLightChanged(self, subUI):
		subUI.tableWidget.itemSelectionChanged.connect(self.itemChanged)

	def connectResetButton(self, subUI):
		subUI.searchResetButton.clicked.connect(self.resetTableView)

	# 지역 시값만 추출하여 ComboBox 안에 삽입
	def insertRegionInfo(self, subUI, BasicDF, SearchColName):
		tempRegionList = []
		selectCol = BasicDF.loc[:, [SearchColName]]
		selectRegionList = selectCol.values.tolist()
		# 리스트를 재구성 (시만 추출)
		for val in selectRegionList:
			address = val[0].split(" ")[1]
			if not address in tempRegionList:
				tempRegionList.append(address)
		for region in tempRegionList:
			subUI.searchRegionSelectComboBox.addItem(region)

	# Option/검색어 찾기 함수
	def optionFinder(self, subUI, BasicDF, keyword, region, industry, criteria, check1, check2, nameList):
		tmpDF = BasicDF
		searchQuery = None
		if keyword.replace(" ", "") != "":
			searchQuery = tmpDF[nameList[0]].str.contains(keyword)
			tmpDF = tmpDF[searchQuery]
		if region != "Select Region":
			searchQuery = tmpDF[nameList[1]].str.contains(region)
			tmpDF = tmpDF[searchQuery]
		if industry != "Select Industry":
			searchQuery = tmpDF[nameList[2]].str.contains(industry)
			tmpDF = tmpDF[searchQuery]
		# if criteria != "Select Criteria":
			# searchQuery = tmpDF[nameList[3]].str.contains("Y")
			# tmpDF = tmpDF[searchQuery]
		if check1 != False:
			searchQuery = tmpDF[nameList[4]].str.contains("Y")
			tmpDF = tmpDF[searchQuery]
		if check2 != False:
			searchQuery = tmpDF[nameList[5]].str.contains("Y")
			tmpDF = tmpDF[searchQuery]
		return tmpDF.values.tolist()

	# 옵션/검색 결과값 테이블 안에 삽입
	def insertValueToTable(self, subUI, VLIST, headName):
		subUI.tableWidget.clear()
		subUI.tableWidget.setHorizontalHeaderLabels(headName)
		subUI.tableWidget.setRowCount(len(VLIST))
		for i in range(len(headName)):
			header = subUI.tableWidget.horizontalHeaderItem(int(i))
			header.setFont(QFont(u"Segoe", 14, QFont.Bold))
		for row, SETS in enumerate(VLIST):
			for col, val in enumerate(SETS):
				tempWidgetMethod = None
				# 가게이름
				if col == 1:
					subUI.tableWidget.setItem(row, 0, QTableWidgetItem(val))
				# 업종명
				elif col == 2:
					subUI.tableWidget.setItem(row, 1, QTableWidgetItem(val))
				# 대표메뉴
				elif col == 13:
					subUI.tableWidget.setItem(row, 2, QTableWidgetItem(val))
				# 네이버 인기도
				elif col == 18:
					subUI.tableWidget.setItem(row, 3, QTableWidgetItem(val))
