from PyQt5 import QtCore, QtGui, QtWidgets

class Sign_In(QtWidgets.QMainWindow):  # Наследуем от QMainWindow
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)

        # Центральный виджет
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Заголовок "Sign In"
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 50, 100, 40))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        self.label.setText("Sign In")
        self.label.setObjectName("label")

        # Подпись "Enter your user ID and password"
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 100, 300, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setFont(QtGui.QFont("Arial", 10))
        self.label_2.setText("Enter your user ID and password")
        self.label_2.setObjectName("label_2")

        # Поле для ввода user ID
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 150, 300, 40))
        self.lineEdit.setStyleSheet("""
            border: 2px solid lightgray;
            border-radius: 15px;
            padding: 10px;
        """)
        self.lineEdit.setPlaceholderText("user ID")
        self.lineEdit.setObjectName("lineEdit")

        # Поле для ввода пароля
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 200, 300, 40))
        self.lineEdit_2.setStyleSheet("""
            border: 2px solid lightgray;
            border-radius: 15px;
            padding: 10px;
        """)
        self.lineEdit_2.setPlaceholderText("password")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        # Чекбокс "Я не робот"
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(250, 250, 300, 30))
        self.checkBox.setFont(QtGui.QFont("Arial", 10))
        self.checkBox.setStyleSheet("color: gray;")
        self.checkBox.setText("I’m not a robot")
        self.checkBox.setObjectName("checkBox")

        # Кнопка "Sign in with user ID"
        self.Sign_In = QtWidgets.QPushButton(self.centralwidget)
        self.Sign_In.setGeometry(QtCore.QRect(250, 300, 300, 40))
        self.Sign_In.setStyleSheet("""
            background-color: black;
            color: white;
            border-radius: 15px;
            font-size: 14px;
        """)
        self.Sign_In.setText("Sign in with user ID")
        self.Sign_In.setObjectName("Sign_In")
        self.Sign_In.clicked.connect(self.Show_MainWindow)

        # Кнопка "Sign up"
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 350, 300, 40))
        self.pushButton_2.setStyleSheet("""
            background-color: gray;
            color: white;
            border-radius: 15px;
            font-size: 14px;
        """)
        self.pushButton_2.setText("Sign up")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.show_Sign_up)

        # Установка центрального виджета
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign In"))

    def show_Sign_up(self):
        self.sign_up_window = QtWidgets.QMainWindow()
        self.ui = Sign_Up()
        self.ui.setupUi(self.sign_up_window)
        self.sign_up_window.show()
        MainWindow.close()

    def Show_MainWindow(self):
        self.Ui_MainWindow = QtWidgets.QMainWindow()
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self.Ui_MainWindow)
        self.Ui_MainWindow.show()
        MainWindow.close()


class Sign_Up(QtWidgets.QWidget):  # Используем QWidget для SignUp
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SignUpWindow")
        MainWindow.setFixedSize(800, 600)

        # Центральный виджет
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

       # Заголовок "Sign In"
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 30, 100, 40))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        self.label.setText("Sign Up")
        self.label.setObjectName("label")

        # Подпись "Enter your user ID and password"
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 80, 300, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setFont(QtGui.QFont("Arial", 10))
        self.label_2.setText("Enter your user ID and password")
        self.label_2.setObjectName("label_2")

        # Поле для ввода user ID
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 140, 300, 40))
        self.lineEdit.setStyleSheet("""
            border: 2px solid lightgray;
            border-radius: 10px;
            padding: 10px;
        """)
        self.lineEdit.setPlaceholderText("user ID")
        self.lineEdit.setObjectName("lineEdit")

        # Поле для ввода пароля
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 190, 300, 40))
        self.lineEdit_2.setStyleSheet("""
            border: 2px solid lightgray;
            border-radius: 10px;
            padding: 10px;
        """)
        self.lineEdit_2.setPlaceholderText("password")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

         # Поле для ввода пароля #2
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)   
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 240, 300, 40))
        self.lineEdit_2.setStyleSheet("""
            border: 2px solid lightgray;
            border-radius: 10px;
            padding: 10px;
        """)
        self.lineEdit_2.setPlaceholderText("password")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        # Чекбокс "Я не робот"
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(250, 290, 300, 30))
        self.checkBox.setFont(QtGui.QFont("Arial", 10))
        self.checkBox.setStyleSheet("color: gray;")
        self.checkBox.setText("I’m not a robot")
        self.checkBox.setObjectName("checkBox")

       

        # Кнопка "Sign up"
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 350, 300, 40))
        self.pushButton_2.setStyleSheet("""
            background-color: gray;
            color: white;
            border-radius: 10px;
            font-size: 14px;
        """)
        self.pushButton_2.setText("Sign up")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Show_Sign_In_Window)

        # Установка центрального виджета
        MainWindow.setCentralWidget(self.centralwidget)

    def Show_Sign_In_Window(self):
        self.sign_up_window = QtWidgets.QMainWindow()
        self.ui = Sign_In()
        self.ui.setupUi(self.sign_up_window)
        self.sign_up_window.show()
        MainWindow.close()

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        # Настройки основного окна
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1200)
        MainWindow.setStyleSheet("background-color: rgb(200, 200, 200);")

        # Центральный виджет
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Создание шрифтов и стилей
        self.bold_font = self.create_font(bold=True)
        self.red_button_style = "background-color: rgb(186, 63, 63); border-radius: 10px;"
        self.white_text_button_style = "color: rgb(255, 255, 255); " + self.red_button_style

        # Поля ввода
        self.line_edits = []
        bg_colors = ["rgb(217, 217, 217)", "rgb(0, 0, 0)", "rgb(217, 217, 217)", "rgb(0, 0, 0)", "rgb(217, 217, 217)","rgb(0, 0, 0)", "rgb(217, 217, 217)","rgb(0, 0, 0)","rgb(217, 217, 217)"]

        for i in range(9):
            line_edit = QtWidgets.QLineEdit(self.centralwidget)
            line_edit.setGeometry(QtCore.QRect(0, i * 70, 1920, 70))
            line_edit.setFont(self.bold_font)
            if bg_colors[i]:
                line_edit.setStyleSheet(f"background-color: {bg_colors[i]};")
            line_edit.setObjectName(f"lineEdit_{i + 1}")
            self.line_edits.append(line_edit)

        # Кнопки
        self.pushButton = self.create_button(self.centralwidget, 800, 900, 250, 80, "Seats", self.red_button_style)
        self.pushButton_2 = self.create_button(self.centralwidget, 500, 910, 140, 50, "Movie info", self.white_text_button_style)
        self.pushButton_3 = self.create_button(self.centralwidget, 1200, 910, 140, 50, "User History", self.white_text_button_style)
        self.pushButton_4 = self.create_button(self.centralwidget, 0, 700, 100, 40, "ADD Movie", self.red_button_style)
        self.pushButton_2.clicked.connect(self.Show_Movie_infoWindow)
        self.pushButton_3.clicked.connect(self.Show_HistoryWindow)
        self.pushButton.clicked.connect(self.Show_BuyWindow)
        self.pushButton_4.clicked.connect(self.Show_ADDWindow)

        # Установка центрального виджета
        MainWindow.setCentralWidget(self.centralwidget)

        # Меню и статусбар
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_font(self, bold=False):
        """Создает и возвращает объект шрифта."""
        font = QtGui.QFont()
        font.setBold(bold)
        font.setWeight(75 if bold else 50)
        return font

    def create_button(self, parent, x, y, width, height, text, style):
        """Создает и возвращает кнопку с заданными параметрами."""
        button = QtWidgets.QPushButton(parent)
        button.setGeometry(QtCore.QRect(x, y, width, height))
        button.setFont(self.bold_font)
        button.setStyleSheet(style)
        button.setText(text)
        return button

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line_edits[0].setText(_translate("MainWindow", "Gladiator"))

    def Show_BuyWindow(self):
        self.buy_Window = QtWidgets.QMainWindow()
        self.ui = Buy_Window()
        self.ui.setupUi(self.buy_Window)
        self.buy_Window.show()
        MainWindow.close()

    def Show_Movie_infoWindow(self):
        self.Movie_info_Window = QtWidgets.QMainWindow()
        self.ui = Movie_info()
        self.ui.setupUi(self.Movie_info_Window)
        self.Movie_info_Window.show()
        MainWindow.close()

    def Show_HistoryWindow(self):
        self.HistoryWindow = QtWidgets.QMainWindow()
        self.ui = History()
        self.ui.setupUi(self.HistoryWindow)
        self.HistoryWindow.show()
        MainWindow.close()

    def Show_ADDWindow(self):
        self.ADDWindow = QtWidgets.QMainWindow()
        self.ui = ADDWindow()
        self.ui.setupUi(self.ADDWindow)
        self.ADDWindow.show()
        MainWindow.close()

class Buy_Window(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        # Настройка основного окна
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1200)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Заголовок
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 210, 1031, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px;")
        self.label.setObjectName("label")

        # Кнопка "Buy"
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 1030, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(186, 63, 63); border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")

        # Создание кнопок через цикл
        self.buttons = []
        button_positions = [
            (650, 410), (810, 410), (970, 410), (1130, 410),
            (650, 550), (810, 550), (970, 550), (1130, 550),
            (650, 690), (810, 690), (970, 690), (1130, 690),
            (650, 840), (810, 840), (970, 840), (1130, 840)
        ]

        for i, (x, y) in enumerate(button_positions):
            button = QtWidgets.QPushButton(self.centralwidget)
            button.setGeometry(QtCore.QRect(x, y, 70, 70))
            button.setStyleSheet("background-color: rgb(255, 255, 255);")
            button.setObjectName(f"button_{i + 1}")
            button.clicked.connect(button.hide)  # Добавляем скрытие кнопки
            self.buttons.append(button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                                                                                    Skrin"))
        self.pushButton.setText(_translate("MainWindow", "Buy"))

class Movie_info(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        # Main Window Setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 60, 101, 31))
        self.label.setFont(self.get_font(size=15))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        # Quantity Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 160, 101, 16))
        self.label_2.setFont(self.get_font(size=10))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        # Seans Label
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 210, 101, 16))
        self.label_3.setFont(self.get_font(size=10))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        # People Label
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 260, 101, 16))
        self.label_4.setFont(self.get_font(size=10))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        # Quantity Input
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 160, 61, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")

        # Seans Input
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 210, 61, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        # People Input
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 260, 61, 22))
        self.lineEdit_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lineEdit_3.setObjectName("lineEdit_3")

        # Setting Central Widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Adding Translations
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  Movie"))
        self.label_2.setText(_translate("MainWindow", "  Quantity:"))
        self.label_3.setText(_translate("MainWindow", "  Seans:"))
        self.label_4.setText(_translate("MainWindow", "  People:"))

    @staticmethod
    def get_font(size=10, bold=False):
        """Utility method to create and return a QFont object."""
        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(bold)
        return font

class History(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        # Main Window Configuration
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 40, 81, 31))
        self.label.setFont(self.get_font(size=15))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        # Movie Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 51, 21))
        self.label_2.setFont(self.get_font(size=10))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        # Movie Input Field
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 120, 351, 31))
        self.lineEdit.setStyleSheet(
            "background-color: rgb(0, 0, 0); border-color: rgb(0, 0, 0);"
        )
        self.lineEdit.setObjectName("lineEdit")

        # Set Central Widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Add Translations
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "History"))
        self.label_2.setText(_translate("MainWindow", "Movie"))

    @staticmethod
    def get_font(size=10, bold=False):
        """Utility method to create and return a QFont object."""
        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(bold)
        return font
    
class ADDWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        # Main Window Configuration
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Movie Name Input
        self.lineEdit_movie_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_movie_name.setGeometry(QtCore.QRect(200, 130, 111, 22))
        self.lineEdit_movie_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_movie_name.setObjectName("lineEdit_movie_name")

        # Title Label
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(340, 20, 101, 41))
        self.label_title.setFont(self.get_font(size=12))
        self.label_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_title.setObjectName("label_title")

        # Movie Name Label
        self.label_movie_name = QtWidgets.QLabel(self.centralwidget)
        self.label_movie_name.setGeometry(QtCore.QRect(90, 130, 91, 20))
        self.label_movie_name.setFont(self.get_font(size=10))
        self.label_movie_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_movie_name.setObjectName("label_movie_name")

        # Movie Duration Input
        self.lineEdit_movie_duration = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_movie_duration.setGeometry(QtCore.QRect(200, 200, 111, 22))
        self.lineEdit_movie_duration.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_movie_duration.setObjectName("lineEdit_movie_duration")

        # Movie Duration Label
        self.label_movie_duration = QtWidgets.QLabel(self.centralwidget)
        self.label_movie_duration.setGeometry(QtCore.QRect(70, 200, 111, 20))
        self.label_movie_duration.setFont(self.get_font(size=10))
        self.label_movie_duration.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_movie_duration.setObjectName("label_movie_duration")

        # Submit Button
        self.pushButton_submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submit.setGeometry(QtCore.QRect(340, 370, 121, 41))
        self.pushButton_submit.setStyleSheet(
            "background-color: rgb(186, 63, 63); border-radius: 10px;"
        )
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.pushButton_submit.clicked.connect(MainWindow.close)

        # Set Central Widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Add Translations
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "ADD Movie"))
        self.label_movie_name.setText(_translate("MainWindow", "Movie name:"))
        self.label_movie_duration.setText(_translate("MainWindow", "Movie duration:"))
        self.pushButton_submit.setText(_translate("MainWindow", "Submit"))

    @staticmethod
    def get_font(size=10, bold=False):
        """Utility method to create and return a QFont object."""
        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(bold)
        return font


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Sign_In()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
