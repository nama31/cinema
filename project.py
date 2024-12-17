from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QLineEdit
import requests
from functools import partial
from PyQt5.QtCore import pyqtSignal



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
        self.lineEdit.setPlaceholderText("User ID")
        self.lineEdit.setObjectName("lineEdit")

        # Поле для ввода пароля
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 200, 300, 40))
        self.lineEdit_2.setStyleSheet("""
            border: 2px solid lightgray;
            border-radius: 15px;
            padding: 10px;
        """)
        self.lineEdit_2.setPlaceholderText("Password")
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
        self.Sign_In.clicked.connect(self.sign_in_clicked)
        # self.Sign_In.clicked.connect(self.Show_Main_window)

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
        self.close()

    def Show_main_window(self):
        self.Ui_MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.username)
        self.ui.setupUi(self.Ui_MainWindow)
        self.Ui_MainWindow.show()
        self.close()


    def sign_in_clicked(self):
        name = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()

        if not self.checkBox.isChecked():
            QMessageBox.warning(self, "Validation Error", "Please confirm that you are not a robot!")
            return
        
        if name and password:
            try:
                response = requests.get(
                    "https://nama.pythonanywhere.com/sign_in",
                    params={'username': name, 'password': password}
                )
                
                if response.status_code == 200:
                    
                    self.username = name 
                    self.Show_main_window()  # Переход к главному окну
                else:
                    QMessageBox.warning(self, "Login Failed", "Invalid username or password!")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Error", f"Failed to connect to server:\n{e}")
        else:
            QMessageBox.warning(self, "Error", "User ID and password must be filled!")


       


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
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)   
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 240, 300, 40))
        self.lineEdit_3.setStyleSheet("""
            border: 2px solid lightgray;
            border-radius: 10px;
            padding: 10px;
        """)
        self.lineEdit_3.setPlaceholderText("password")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_2")

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
        self.pushButton_2.clicked.connect(self.sign_up_clicked)

        # Установка центрального виджета
        MainWindow.setCentralWidget(self.centralwidget)

    
        
    def sign_up_clicked(self):
        name = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()
        password_2 = self.lineEdit_3.text().strip()


        if name and password and password == password_2:
            try:
                response = requests.get(
                    "https://nama.pythonanywhere.com/sign_up",
                    params={'username': name, 'password': password}
                )
                if response.status_code == 200:
                    QMessageBox.information(self, "Success", "Account created successfully!")
                    self.Show_Sign_In_Window()
                else:
                    QMessageBox.warning(self, "Sign Up Failed", "Unable to create account. Try again.")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Error", f"Failed to connect to server:\n{e}")
        else:
            QMessageBox.warning(self, "Error", "User ID and password must be filled!")

    def Show_Sign_In_Window(self):
        self.sign_up_window = QtWidgets.QMainWindow()
        self.ui = Sign_In()
        self.ui.setupUi(self.sign_up_window)
        self.sign_up_window.show()
        MainWindow.close()

class ClickableLineEdit(QLineEdit):
    doubleClicked = pyqtSignal(str, int)  # Сигнал для текста и индекса

    def __init__(self, parent=None, index=None):
        super().__init__(parent)
        self.index = index  # Сохраняем индекс строки

    def mouseDoubleClickEvent(self, event):
        text = self.text().strip()
        if text:
            self.doubleClicked.emit(text, self.index)  # Передаем текст и индекс
        else:
            QMessageBox.warning(self, "Error", "Session line is empty!")
        super().mouseDoubleClickEvent(event)

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self,username=None):
        super().__init__()
        self.selected_session = None  # Хранение выбранного сеанса
        self.movie_name = None  # Хранение выбранного фильма
        self.username = username
        self.viwers = None
        self.history = None

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
        bg_colors = ["rgb(217, 217, 217)", "rgb(0, 0, 0)", "rgb(217, 217, 217)", 
                    "rgb(0, 0, 0)", "rgb(217, 217, 217)", "rgb(0, 0, 0)", 
                    "rgb(217, 217, 217)", "rgb(0, 0, 0)", "rgb(217, 217, 217)"]

        for i in range(9):
            line_edit = ClickableLineEdit(self.centralwidget, index=i)  # Передаем индекс
            line_edit.setGeometry(QtCore.QRect(0, i * 70, 1920, 70))
            line_edit.setFont(self.bold_font)

            if bg_colors[i]:
                if i % 2 == 1:
                    line_edit.setStyleSheet(f"background-color: {bg_colors[i]}; color: white;")
                else:
                    line_edit.setStyleSheet(f"background-color: {bg_colors[i]}; color: black;")

            line_edit.setObjectName(f"lineEdit_{i + 1}")
            self.line_edits.append(line_edit)

            # Подключаем сигнал к обработчику
            line_edit.doubleClicked.connect(self.on_session_button_click)


        # Кнопки
        self.pushButton = self.create_button(self.centralwidget, 800, 900, 250, 80, "Seats", self.red_button_style)
        self.pushButton_2 = self.create_button(self.centralwidget, 500, 910, 140, 50, "Movie info", self.white_text_button_style)
        self.pushButton_3 = self.create_button(self.centralwidget, 1200, 910, 140, 50, "User History", self.white_text_button_style)
        self.pushButton_4 = self.create_button(self.centralwidget, 0, 700, 100, 40, "ADD Movie", self.red_button_style)
        self.pushButton_5 = self.create_button(self.centralwidget, 0, 650, 100, 40, "Remove Movie", self.red_button_style)
        self.pushButton_2.clicked.connect(self.Show_Movie_infoWindow)
        self.pushButton_3.clicked.connect(self.Show_HistoryWindow)
        self.pushButton.clicked.connect(self.Show_BuyWindow)
        self.pushButton_4.clicked.connect(self.Show_ADDWindow)
        self.pushButton_5.clicked.connect(self.Show_RemoveWindow)
        self.pushButton_refresh = self.create_button(self.centralwidget, 1810, 700, 100, 40, "Refresh", self.red_button_style)
        self.pushButton_refresh.clicked.connect(self.load_movies_into_line_edits)


    
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

    

    def on_session_button_click(self, movie_name, session_time):
        """Обрабатывает выбор сеанса при клике на кнопку."""
        self.movie_name = movie_name
        self.selected_session = session_time

        response = requests.get("https://nama.pythonanywhere.com/movie_info",
                                params={"movie_name":movie_name ,"session_time":session_time})

        print(f"Selected movie: {self.movie_name}, Selected session: {self.selected_session}")
        if response.status_code == 200:
            self.viwers = response.json().get("viewers", [])
            print(self.viwers)
        # else:
            # print("Error:", response.json())

        # Включаем кнопку "Seats" только после выбора сеанса
        self.pushButton.setEnabled(True)



        
        



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
        # self.line_edits[0].setText(_translate("MainWindow"))


    def load_movies_into_line_edits(self):
        try:
            # Отправляем запрос к серверу
            response = requests.get("https://nama.pythonanywhere.com/movies")

            if response.status_code == 200:
                # Получаем словарь фильмов
                movies = response.json().get("movies", {})

                # Удаляем старые кнопки (если есть)
                for child in self.centralwidget.findChildren(QtWidgets.QPushButton):
                    if child.text() not in ["Seats", "Movie info", "User History", "ADD Movie", "Remove Movie", "Refresh"]:
                        child.deleteLater()

                # Заполняем QLineEdit для каждого фильма
                for i, (movie_name, times) in enumerate(movies.items()):
                    line_edit = self.line_edits[i]  # Получаем соответствующий QLineEdit

                    # Формируем строку для отображения фильма с сеансами
                    session_str = f"{movie_name}"   
                    # : " + "  ".join(times.split(','))

                    # Устанавливаем текст в QLineEdit
                    line_edit.setText(session_str)
                    line_edit.setReadOnly(True)  # Делаем поле только для чтения

                    # Вертикальный отступ между строками фильмов
                    row_height = 70

                    # Добавляем кнопки для каждого сеанса
                    for j, session in enumerate(times.split(',')):

                        # Определяем позицию для текущей строки
                        movie_label_y = i * row_height + 25  # Базовая высота для текущего фильма
                        button_x = 200 + j * 120              # Начальная позиция кнопок
                        button_y = movie_label_y             # Совпадает с высотой названия фильма




                        session_button = QtWidgets.QPushButton(f"{session.strip()}", self.centralwidget)
                        session_button.setGeometry(button_x, button_y, 60, 30)  # Позиция и размер кнопки  
                        session_button.setCheckable(True)  # Делаем кнопку переключаемой
                        # Подключаем обработчик, передаем название фильма и сеанс
                        session_button.clicked.connect(partial(self.on_session_button_click, movie_name, session.strip()))
                        session_button.show()

                # Очистим лишние QLineEdit, если фильмов меньше, чем `line_edits`
                for j in range(len(movies), len(self.line_edits)):
                    self.line_edits[j].clear()

            else:
                QMessageBox.warning(
                    self, 
                    "Error", 
                    f"Failed to load movies. Status code: {response.status_code}"
                )

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(
                self, 
                "Error", 
                f"Failed to connect to the server:\n{e}"
            )








    def Show_BuyWindow(self):
        """Открывает окно покупки билетов для выбранного фильма и сеанса."""
        # Если выбраны фильм и сеанс
        if self.movie_name and self.selected_session:
            # Отправляем запрос на сервер для получения данных о доступных местах
            response = requests.get(
                "https://nama.pythonanywhere.com/choosen",
                params={"movie_name": self.movie_name, "session_time": self.selected_session}
            )
            # give = requests.get(
            #     "https://nama.pythonanywhere.com/update_seat",
            #     params={"movie_name": self.movie_name, "session_time": self.selected_session}
            # )
            if response.status_code == 200:
                # Получаем данные о доступных местах
                attend = response.json().get("attend", [])
                self.buy_Window = QtWidgets.QMainWindow()
                

               # Создаем окно покупки билетов
                self.buy_Window = QtWidgets.QMainWindow()
                self.ui = Buy_Window(self.username,self.buy_Window)
                self.ui.setupUi(self.buy_Window, self.movie_name, self.selected_session, attend)
                self.buy_Window.show()
                MainWindow.close()
            else:
                QMessageBox.warning(self, "Error", "Failed to load available seats.")
        else:
            QMessageBox.warning(self, "Error", "Please select a movie session.")





    def Show_Movie_infoWindow(self):
        self.Movie_info_Window = QtWidgets.QMainWindow()
        self.ui = Movie_info(self.viwers)
        self.ui.setupUi(self.Movie_info_Window)
        self.Movie_info_Window.show()
        MainWindow.close()

    def Show_HistoryWindow(self):
        responce = requests.get("https://nama.pythonanywhere.com/user_history")
        self.history = responce.json().get("user_history",[])
        print(f"Before removal: {self.history}")

        self.HistoryWindow = QtWidgets.QMainWindow()
        self.ui = History(self.history)
        self.ui.setupUi(self.HistoryWindow)
        self.HistoryWindow.show()
        MainWindow.close()

    def Show_ADDWindow(self):
        self.ADDWindow = QtWidgets.QMainWindow()
        self.ui = ADDWindow()
        self.ui.setupUi(self.ADDWindow)
        self.ADDWindow.show()
        MainWindow.close()

    def Show_RemoveWindow(self):
        self.RemoveWindow = QtWidgets.QMainWindow()
        self.ui = RemoveWindow()
        self.ui.setupUi(self.RemoveWindow)
        self.RemoveWindow.show()
        MainWindow.close()

    

class Buy_Window(QtWidgets.QWidget):
    def __init__(self,username,parante):
        super().__init__()
         # Получаем информацию о текущем пользователе (например, из сессии или с помощью API)
        self.username = username
        self.parante = parante

    def setupUi(self, MainWindow, movie_name, session_time, attend):
        # Настройка интерфейса для окна покупки
        self.movie_name = movie_name
        self.session_time = session_time
        self.attend = attend

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
        self.pushButton.clicked.connect(self.close_window)

        self.selected_seat = []

        # Подключение кнопки "Buy" к обработчику

        
        

        





        # Создание кнопок через цикл
        self.buttons = []
        button_positions = [
            (650, 410), (810, 410), (970, 410), (1130, 410),
            (650, 550), (810, 550), (970, 550), (1130, 550),
            (650, 690), (810, 690), (970, 690), (1130, 690),
            (650, 840), (810, 840), (970, 840), (1130, 840)
        ]

        # Создаем кнопки для каждого места
        for i, (x, y) in enumerate(button_positions):
            button = QtWidgets.QPushButton(self.centralwidget)
            button.setGeometry(QtCore.QRect(x, y, 70, 70))

            # Проверяем статус места из self.attend
            if self.attend[i][1] == None:  # Место доступно
                button.setStyleSheet("background-color: rgb(255, 255, 255); border: 2px solid black;")
                # button.setEnabled(True)
            elif self.attend[i][1] == self.username:
                button.setStyleSheet("background-color: rgb(153, 255, 153); border: 2px solid black;")

            else:  # Место занято
                button.setStyleSheet("background-color: rgb(128, 128, 128); color: white;")
                # button.setEnabled(False)

            # button.setText(f"Seat {i+1}")
            button.setObjectName(f"seat_button_{i+1}")
            # button.clicked.connect(partial(self.book_seat, i, button))
            button.clicked.connect(partial(self.toggle_seat_reservation, i, button))
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
        MainWindow.setCentralWidget(self.centralwidget)


   

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                                                                                    Screen"))
        self.pushButton.setText(_translate("MainWindow", "Back"))

    def book_seat(self, seat_index, button):
        """Обрабатывает бронирование места."""

        response = requests.get(
            "https://nama.pythonanywhere.com/update_seat",
            params={
                "movie_name": self.movie_name,
                "session_time": self.session_time,
                "seat_index": seat_index,
                "username":self.username
            }
        )
        print(f"Response status: {response.status_code}, Response content: {response.text}")
        print(f"Movie name: {self.movie_name}, Session time: {self.session_time}, Seat index: {seat_index}, Username: {self.username}")


        if response.status_code == 200:
            # Если место успешно забронировано, обновляем состояние кнопки
            button.setStyleSheet("background-color: rgb(153, 255, 153); color: greean;")
            button.setEnabled(False)
            self.attend[seat_index] = (seat_index, self.username)  # Сохраняем пользователя, который забронировал место
            # QMessageBox.information(self, "Success", f"Seat {seat_index+1} successfully booked!")
        elif response.status_code == 409:
            QMessageBox.warning(self, "Error", f"Seat {seat_index+1} is already booked!")
        else:
            QMessageBox.critical(self, "Error", "Failed to book seat. Please try again.")


    def toggle_seat_reservation(self, seat_index, button):
        """Обрабатывает резервирование или отмену места."""
        # Проверяем текущий статус места
        is_reserved = self.attend[seat_index][1]  # Место уже забронировано?
        
        

        # Если место забронировано и пользователь пытается отменить бронирование
        if is_reserved != None and self.attend[seat_index][1] == self.username:
            # Отправляем запрос на отмену бронирования
            response = requests.get(
                "https://nama.pythonanywhere.com/cancel_seat",
                params={
                    "movie_name": self.movie_name,
                    "session_time": self.session_time,
                    "seat_index": seat_index,
                    "username":self.username
                }
            )
            print(f"movie name:{self.movie_name}, session time:{self.session_time}, seat index:{seat_index}")
            print(f"responce code:{response.status_code}")
            if response.status_code == 200:
                # Успешная отмена резерва
                self.attend[seat_index] = (seat_index, None)  # Снимаем резерв с места
                button.setStyleSheet("background-color: rgb(255, 255, 255); border: 2px solid black;")
                button.setEnabled(True)  # Делаем кнопку снова доступной
                QMessageBox.information(self, "Success", f"Reservation for Seat {seat_index+1} cancelled!")
            else:
                QMessageBox.critical(self, "Error", "Failed to cancel reservation.")
        elif is_reserved == None:
            # Если место свободно, бронируем его
            self.book_seat(seat_index, button)
        else:
            # Если место забронировано другим пользователем
            QMessageBox.warning(self, "Error", "You can only cancel your own reservation.")

    def close_window(self):
        self.parante.close()


class Movie_info(QtWidgets.QWidget):
    def __init__(self,viewers):
        super().__init__()
        self.all = viewers
        self.viewers = set(viewers)  # Создаём множество зрителей
        self.str_viewers = ", ".join(self.viewers)  # Преобразуем в строку, разделённую запятыми
        
        self.setupUi(MainWindow)



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
        

        

        # People Label
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 210, 101, 16))
        self.label_4.setFont(self.get_font(size=10))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        # Quantity Input
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 160, 61, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(0, 0, 0);color: white;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(str(len(self.all)))

       

        # People Input
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 210, 150, 80))
        self.lineEdit_3.setStyleSheet("background-color: rgb(0, 0, 0);color: white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(self.str_viewers)

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
        self.label_4.setText(_translate("MainWindow", "  People:"))

    @staticmethod
    def get_font(size=10, bold=False):
        """Utility method to create and return a QFont object."""
        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(bold)
        return font

class History(QtWidgets.QWidget):
    def __init__(self,history):
        super().__init__()
        self.history = set(history)
        self.str_history = ", ".join(self.history)
        



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
            "background-color: rgb(0, 0, 0); border-color: rgb(0, 0, 0);color: white;"
        )
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText((self.str_history))

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
        self.lineEdit_movie_name.setGeometry(QtCore.QRect(200, 130, 150, 22))
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
        self.lineEdit_movie_duration.setGeometry(QtCore.QRect(200, 200, 150, 22))
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
        self.pushButton_submit.clicked.connect(self.submit)

    def submit(self):
        movie_name = self.lineEdit_movie_name.text().strip()  # Название фильма
        times_str =  [str(self.lineEdit_movie_duration.text().strip())]  # Время показа

        if movie_name and times_str:
            try:


                # Отправляем GET-запрос для добавления фильма
                response = requests.get(
                    "https://nama.pythonanywhere.com/new_movies",  # URL API для добавления фильма
                    params={"movie_name": movie_name, "time": times_str}  # Передаем данные как параметры
                )

                # Выводим статус ответа и тело ответа
                print(f"Response Status Code: {response.status_code}")
                print(f"Response Body: {response.text}")

                # Проверяем статус ответа
                if response.status_code == 200:
                    QMessageBox.information(self, "Success", "Movie added successfully!")
                elif response.status_code == 409:  # Фильм уже существует
                    QMessageBox.warning(self, "Add Movie Failed", "Movie already exists!")
                else:  # Другие ошибки
                    QMessageBox.warning(
                        self, 
                        "Add Movie Failed", 
                        f"Error: {response.json().get('message', 'Unknown error')}"
                    )
            except requests.exceptions.RequestException as e:
                # Обрабатываем ошибки соединения
                QMessageBox.critical(self, "Error", f"Failed to connect to server:\n{e}")
        else:
            # Если поля пустые
            QMessageBox.warning(self, "Error", "Movie name and time must be filled!")


   
    @staticmethod
    def get_font(size=10, bold=False):
        """Utility method to create and return a QFont object."""
        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(bold)
        return font

class RemoveWindow(QtWidgets.QWidget):
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
        self.lineEdit_movie_name.setGeometry(QtCore.QRect(200, 130, 150, 22))
        self.lineEdit_movie_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_movie_name.setObjectName("lineEdit_movie_name")

        # Title Label
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(340, 20, 150, 41))
        self.label_title.setFont(self.get_font(size=12))
        self.label_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_title.setObjectName("label_title")

        # Movie Name Label
        self.label_movie_name = QtWidgets.QLabel(self.centralwidget)
        self.label_movie_name.setGeometry(QtCore.QRect(90, 130, 91, 20))
        self.label_movie_name.setFont(self.get_font(size=10))
        self.label_movie_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_movie_name.setObjectName("label_movie_name")

       
        
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
        self.label_title.setText(_translate("MainWindow", "Remove Movie"))
        self.label_movie_name.setText(_translate("MainWindow", "Movie name:"))
        self.pushButton_submit.setText(_translate("MainWindow", "Submit"))
        self.pushButton_submit.clicked.connect(self.submit)

    def submit(self):
        movie_name = self.lineEdit_movie_name.text().strip()  # Название фильма

        if movie_name:
            try:


                # Отправляем GET-запрос для добавления фильма
                response = requests.get(
                    "https://nama.pythonanywhere.com/remove_movies",  # URL API для добавления фильма
                    params={"movie_name": movie_name}  # Передаем данные как параметры
                )

                # Выводим статус ответа и тело ответа
                print(f"Response Status Code: {response.status_code}")
                print(f"Response Body: {response.text}")

                # Проверяем статус ответа
                if response.status_code == 200:
                    QMessageBox.information(self, "Success", "Movie removed successfully!")
                elif response.status_code == 409:  # Фильм уже существует
                    QMessageBox.warning(self, "Add Movie Failed", "Movie already exists!")
                else:  # Другие ошибки
                    QMessageBox.warning(
                        self, 
                        "Add Movie Failed", 
                        f"Error: {response.json().get('message', 'Unknown error')}"
                    )
            except requests.exceptions.RequestException as e:
                # Обрабатываем ошибки соединения
                QMessageBox.critical(self, "Error", f"Failed to connect to server:\n{e}")
        else:
            # Если поля пустые
            QMessageBox.warning(self, "Error", "Movie name and time must be filled!")


   
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
