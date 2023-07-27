import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class SacramentsManagementGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sacraments Management")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.sacrament_type_input = QLineEdit()
        self.date_input = QLineEdit()
        self.location_input = QLineEdit()
        self.presiding_clergy_input = QLineEdit()

        add_button = QPushButton("Add Sacrament")
        add_button.clicked.connect(self.add_sacrament)

        layout.addWidget(QLabel("Sacrament Type:"))
        layout.addWidget(self.sacrament_type_input)
        layout.addWidget(QLabel("Date (YYYY-MM-DD):"))
        layout.addWidget(self.date_input)
        layout.addWidget(QLabel("Location:"))
        layout.addWidget(self.location_input)
        layout.addWidget(QLabel("Presiding Clergy:"))
        layout.addWidget(self.presiding_clergy_input)
        layout.addWidget(add_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_sacrament(self):
        sacrament_type = self.sacrament_type_input.text()
        date = self.date_input.text()
        location = self.location_input.text()
        presiding_clergy = self.presiding_clergy_input.text()

        try:
            manager.add_sacrament(sacrament_type, date, location, presiding_clergy)
            QMessageBox.information(self, "Success", "Sacrament added successfully!")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    db_file = "parishioner_management.db"
    manager = ParishionerManager(db_file)

    window = SacramentsManagementGUI()
    window.show()

    sys.exit(app.exec_())

