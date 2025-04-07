from PyQt5 import QtCore, QtGui, QtWidgets
import re

class FormValidationApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Form Validation - Tri Shandy Ananta Axell Saputra | F1D022099")
        self.resize(335, 400)
        self.centralwidget = QtWidgets.QWidget(self)

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 20, 280, 250))
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)

        self.nameField = QtWidgets.QLineEdit()
        self.formLayout.addRow("Name:", self.nameField)

        self.emailField = QtWidgets.QLineEdit()
        self.formLayout.addRow("Email:", self.emailField)

        self.ageField = QtWidgets.QLineEdit()
        self.formLayout.addRow("Age:", self.ageField)

        self.phoneField = QtWidgets.QLineEdit()
        self.phoneField.setInputMask("+62 000 0000 0000")
        self.formLayout.addRow("Phone Number:", self.phoneField)

        self.addressField = QtWidgets.QTextEdit()
        self.formLayout.addRow("Address:", self.addressField)

        self.genderBox = QtWidgets.QComboBox()
        self.genderBox.addItems(["", "Male", "Female"])
        self.formLayout.addRow("Gender:", self.genderBox)

        self.educationBox = QtWidgets.QComboBox()
        self.educationBox.addItems([
            "", "Elementary School", "Junior High School", "Senior High School",
            "Diploma", "Bachelor's Degree", "Master's Degree", "Doctoral's Degree"])
        self.formLayout.addRow("Education:", self.educationBox)

        self.saveButton = QtWidgets.QPushButton("Save")
        self.saveButton.setGeometry(QtCore.QRect(120,300, 75, 23))
        self.saveButton.setParent(self.centralwidget)
        self.saveButton.clicked.connect(self.validateForm)

        self.clearButton = QtWidgets.QPushButton("Clear")
        self.clearButton.setGeometry(QtCore.QRect(230, 300, 75, 23))
        self.clearButton.setParent(self.centralwidget)
        self.clearButton.clicked.connect(self.clearFields)

        self.setCentralWidget(self.centralwidget)

        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, activated=self.close)

    def validateForm(self):
        name = self.nameField.text().strip()
        email = self.emailField.text().strip()
        age = self.ageField.text().strip()
        phone = self.phoneField.text().replace(" ", "")
        address = self.addressField.toPlainText().strip()
        gender = self.genderBox.currentText()
        education = self.educationBox.currentText()

        if not name:
            self.showError("Name is required.")
            return

        if not re.match(r"^[\w\.-]+@gmail\.com$", email):
            self.showError("Email must be a valid @gmail.com address.")
            return

        if not age.isdigit():
            self.showError("Age must be a numeric value.")
            return

        if len(re.sub(r"\D", "", phone)) != 13:
            self.showError("Phone number must contain exactly 13 digits.")
            return

        if not address:
            self.showError("Address is required.")
            return

        if gender == "":
            self.showError("Please select a gender.")
            return

        if education == "":
            self.showError("Please select your education level.")
            return

        QtWidgets.QMessageBox.information(self, "Success", "Form submitted successfully!")
        self.clearFields()

    def clearFields(self):
        self.nameField.clear()
        self.emailField.clear()
        self.ageField.clear()
        self.phoneField.clear()
        self.addressField.clear()
        self.genderBox.setCurrentIndex(0)
        self.educationBox.setCurrentIndex(0)

    def showError(self, message):
        QtWidgets.QMessageBox.warning(self, "Validation Error", message)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = FormValidationApp()
    window.show()
    sys.exit(app.exec_())
