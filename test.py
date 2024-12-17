from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import requests

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
        self.ui = Ui_MainWindow()
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
                    self.Show_main_window()  # Переход к главному окну
                else:
                    QMessageBox.warning(self, "Login Failed", "Invalid username or password!")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Error", f"Failed to connect to server:\n{e}")
        else:
            QMessageBox.warning(self, "Error", "User ID and password must be filled!")


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        # Настройки основного окна
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1200)
        MainWindow.setStyleSheet("background-color: rgb(200, 200, 200);")

        # Центральный виджет
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Кнопка "Добавить фильм"
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(50, 50, 200, 50))
        self.pushButton_add.setText("Add Movie")
        self.pushButton_add.setStyleSheet("background-color: green; color: white; border-radius: 10px;")
        self.pushButton_add.clicked.connect(self.add_movie)

        # Кнопка "Удалить фильм"
        self.pushButton_remove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_remove.setGeometry(QtCore.QRect(50, 120, 200, 50))
        self.pushButton_remove.setText("Remove Movie")
        self.pushButton_remove.setStyleSheet("background-color: red; color: white; border-radius: 10px;")
        self.pushButton_remove.clicked.connect(self.remove_movie)

        # Поле для вывода списка фильмов
        self.textEdit_movies = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_movies.setGeometry(QtCore.QRect(300, 50, 600, 400))
        self.textEdit_movies.setReadOnly(True)
        self.textEdit_movies.setStyleSheet("background-color: white; border: 1px solid gray;")

        # Установка центрального виджета
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Manager"))

    def add_movie(self):
        movie_name, ok = QtWidgets.QInputDialog.getText(None, "Add Movie", "Enter movie name:")
        if ok and movie_name:
            try:
                response = requests.post(
                    "https://nama.pythonanywhere.com/add_movie",
                    json={"movie_name": movie_name}
                )
                if response.status_code == 200:
                    QMessageBox.information(None, "Success", "Movie added successfully!")
                    self.refresh_movie_list()
                else:
                    QMessageBox.warning(None, "Error", "Failed to add movie.")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(None, "Error", f"Failed to connect to server:\n{e}")

    def remove_movie(self):
        movie_name, ok = QtWidgets.QInputDialog.getText(None, "Remove Movie", "Enter movie name to remove:")
        if ok and movie_name:
            try:
                response = requests.post(
                    "https://nama.pythonanywhere.com/remove_movie",
                    json={"movie_name": movie_name}
                )
                if response.status_code == 200:
                    QMessageBox.information(None, "Success", "Movie removed successfully!")
                    self.refresh_movie_list()
                else:
                    QMessageBox.warning(None, "Error", "Failed to remove movie.")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(None, "Error", f"Failed to connect to server:\n{e}")

    def refresh_movie_list(self):
        try:
            response = requests.get("https://nama.pythonanywhere.com/list_movies")
            if response.status_code == 200:
                movies = response.json().get("movies", [])
                self.textEdit_movies.setText("\n".join(movies))
            else:
                QMessageBox.warning(None, "Error", "Failed to load movie list.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(None, "Error", f"Failed to connect to server:\n{e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Sign_In()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())