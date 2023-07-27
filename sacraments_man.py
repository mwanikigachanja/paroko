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
        self.sacraments_table = QTableWidget(self)
        self.sacraments_table.setColumnCount(5)
        self.sacraments_table.setHorizontalHeaderLabels(["ID", "Type", "Date", "Location", "Presiding Clergy"])
        self.sacraments_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.sacraments_table.setSelectionMode(QTableWidget.SingleSelection)
        self.sacraments_table.resize(700, 300)


        add_button = QPushButton("Add Sacrament")
        add_button.clicked.connect(self.add_sacrament)
        # Buttons for editing and deleting sacrament records
        edit_button = QPushButton("Edit Sacrament")
        edit_button.clicked.connect(self.edit_sacrament)
        delete_button = QPushButton("Delete Sacrament")
        delete_button.clicked.connect(self.delete_sacrament)

        # Horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)

        # Vertical layout for the main window
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Sacrament Type:"))
        layout.addWidget(self.sacrament_type_input)
        layout.addWidget(QLabel("Date (YYYY-MM-DD):"))
        layout.addWidget(self.date_input)
        layout.addWidget(QLabel("Location:"))
        layout.addWidget(self.location_input)
        layout.addWidget(QLabel("Presiding Clergy:"))
        layout.addWidget(self.presiding_clergy_input)
        layout.addWidget(add_button)
        layout.addWidget(add_button)
        layout.addWidget(self.sacraments_table)
        layout.addLayout(button_layout)

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

    def load_sacraments_table(self):
        self.sacraments_table.setRowCount(0)
        all_sacraments = manager.get_all_sacraments()

        for row_number, sacrament in enumerate(all_sacraments):
            self.sacraments_table.insertRow(row_number)
            for col_number, item in enumerate(sacrament):
                self.sacraments_table.setItem(row_number, col_number, QTableWidgetItem(str(item)))

    def edit_sacrament(self):
        selected_row = self.sacraments_table.currentRow()
        if selected_row >= 0:
            sacrament_id = int(self.sacraments_table.item(selected_row, 0).text())
            sacrament_type = self.sacrament_type_input.text()
            date = self.date_input.text()
            location = self.location_input.text()
            presiding_clergy = self.presiding_clergy_input.text()

            try:
                manager.edit_sacrament(sacrament_id, sacrament_type, date, location, presiding_clergy)
                self.load_sacraments_table()  # Refresh the table
                QMessageBox.information(self, "Success", "Sacrament edited successfully!")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))

    def delete_sacrament(self):
        selected_row = self.sacraments_table.currentRow()
        if selected_row >= 0:
            sacrament_id = int(self.sacraments_table.item(selected_row, 0).text())

            reply = QMessageBox.question(self, "Confirmation", "Are you sure you want to delete this sacrament?", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    manager.delete_sacrament(sacrament_id)
                    self.load_sacraments_table()  # Refresh the table
                    QMessageBox.information(self, "Success", "Sacrament deleted successfully!")
                except ValueError as e:
                    QMessageBox.warning(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    db_file = "parishioner_management.db"
    manager = ParishionerManager(db_file)

    window = SacramentsManagementGUI()
    window.show()

    window = SacramentsManagementGUI()
    window.show()

    # Load sacrament records into the table
    window.load_sacraments_table()

    sys.exit(app.exec_())

