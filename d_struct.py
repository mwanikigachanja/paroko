import datetime
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox


class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.schedule = {}
    def add_person(self):
        name = self.priest_input.text().strip()
        role = self.event_roles.index("priest")  # Assuming we are only adding priests in this example
        preference = self.preference_input.text().strip()  # Added preference field
        person = Person(name, role, preference)  # Updated Person constructor
        self.ministers["priest"].append(person)
        self.priest_input.clear()
        self.preference_input.clear()  # Clear preference input field
        self.update_schedule_table()

    def toggle_preference_field(self):
        # Enable the preference input field when a role other than "priest" is selected
        is_priest = self.role_dropdown.currentText().lower() == "priest"
        self.preference_input.setEnabled(not is_priest)

class Event:
    def __init__(self, event_type, date_time, location):
        self.event_type = event_type
        self.date_time = date_time
        self.location = location
        self.ministers = {}

class MassSchedulerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mass and Liturgy Scheduler")
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

    def init_ui(self):
        # Input fields
        self.event_type_input = QLineEdit()
        self.date_time_input = QLineEdit()
        self.location_input = QLineEdit()
        self.priest_input = QLineEdit()
        self.deacon_input = QLineEdit()
        self.other_input = QLineEdit()
        self.preference_input = QLineEdit()  # Preference input field
        self.role_dropdown = QComboBox()  # Dropdown for selecting minister role
        self.role_dropdown.addItems(["Priest", "Deacon", "Other"])
        self.role_dropdown.currentIndexChanged.connect(self.toggle_preference_field)

        # Buttons
        add_person_button = QPushButton("Add Person")
        add_person_button.clicked.connect(self.add_person)

        schedule_event_button = QPushButton("Schedule Event")
        schedule_event_button.clicked.connect(self.add_event)

        delete_event_button = QPushButton("Delete Event")
        delete_event_button.clicked.connect(self.delete_event)
        delete_event_button = QPushButton("Delete Event")
        delete_event_button.clicked.connect(self.delete_event)


        # Table to display the schedule
        self.schedule_table = QTableWidget(self)
        self.schedule_table.setColumnCount(5)
        self.schedule_table.setHorizontalHeaderLabels(["Event Type", "Date and Time", "Location", "Priest", "Deacon/Other"])
        self.schedule_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Vertical layout for the main window
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Event Type:"))
        layout.addWidget(self.event_type_input)
        layout.addWidget(QLabel("Date and Time (YYYY-MM-DD HH:MM):"))
        layout.addWidget(self.date_time_input)
        layout.addWidget(QLabel("Location:"))
        layout.addWidget(self.location_input)
        layout.addWidget(QLabel("Priest:"))
        layout.addWidget(self.priest_input)
        layout.addWidget(QLabel("Deacon/Other:"))
        layout.addWidget(self.deacon_input)
        layout.addWidget(add_person_button)
        layout.addWidget(schedule_event_button)
        layout.addWidget(self.schedule_table)
        layout.addWidget(delete_event_button)
        layout.addWidget(QLabel("Priest:"))
        layout.addWidget(self.priest_input)
        layout.addWidget(QLabel("Preference:"))  # Label for the preference field
        layout.addWidget(self.preference_input)  # Preference input field
        layout.addWidget(add_person_button)
        layout.addWidget(schedule_event_button)
        layout.addWidget(self.schedule_table)
        layout.addWidget(delete_event_button)


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Sample data
        self.ministers = {
            "priest": [],
            "deacon": [],
            "other": []
        }
        self.event_roles = ["priest", "deacon", "other"]
        self.events = []

    def add_person(self):
        role = self.role_dropdown.currentText().lower()  # Get selected role from the dropdown

        if not name or not role:
            QMessageBox.warning(self, "Error", "Name and Role are required.")
            return

        # Preference field is still optional, but now it's role-specific
        preference = self.preference_input.text().strip() if self.preference_input.isEnabled() else ""

        person = Person(name, role, preference)
        self.ministers[role].append(person)
        self.name_input.clear()
        self.preference_input.clear()
        self.update_schedule_table()

    def add_event(self):
        event_type = self.event_type_input.text().strip()
        date_time = self.date_time_input.text().strip()
        location = self.location_input.text().strip()
        priest_name = self.priest_input.text().strip()
        deacon_name = self.deacon_input.text().strip()
        other_name = self.other_input.text().strip()

        # Find ministers by name
        priest = next((p for p in self.ministers["priest"] if p.name == priest_name), None)
        deacon = next((d for d in self.ministers["deacon"] if d.name == deacon_name), None)
        other = next((o for o in self.ministers["other"] if o.name == other_name), None)

        if not event_type or not date_time or not location or not priest:
            QMessageBox.warning(self, "Error", "Event Type, Date and Time, Location, and Priest are required.")
            return

        date_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        event = Event(event_type, date_time, location)
        event.add_minister(priest, "priest")
        if deacon:
            event.add_minister(deacon, "deacon")
        if other:
            event.add_minister(other, "other")

        self.events.append(event)
        self.update_schedule_table()

        # Clear input fields
        self.event_type_input.clear()
        self.date_time_input.clear()
        self.location_input.clear()
        self.priest_input.clear()
        self.deacon_input.clear()
        self.other_input.clear()
    def toggle_preference_field(self):
        # Enable the preference input field when a role other than "priest" is selected
        is_priest = self.role_dropdown.currentText().lower() == "priest"
        self.preference_input.setEnabled(not is_priest)

    def update_schedule_table(self):
        self.schedule_table.setRowCount(0)
        for event in self.events:
            row_count = self.schedule_table.rowCount()
            self.schedule_table.insertRow(row_count)

            self.schedule_table.setItem(row_count, 0, QTableWidgetItem(event.event_type))
            self.schedule_table.setItem(row_count, 1, QTableWidgetItem(event.date_time.strftime("%Y-%m-%d %H:%M")))
            self.schedule_table.setItem(row_count, 2, QTableWidgetItem(event.location))
            self.schedule_table.setItem(row_count, 3, QTableWidgetItem(event.ministers.get("priest", "").name))
            self.schedule_table.setItem(row_count, 4, QTableWidgetItem(event.ministers.get("deacon", "").name + ", " + event.ministers.get("other", "").name))

    def delete_event(self):
        selected_rows = sorted(set(index.row() for index in self.schedule_table.selectedIndexes()), reverse=True)
        for row in selected_rows:
            event = self.events[row]
            for minister in event.ministers.values():
                if event.date_time in minister.schedule:
                    del minister.schedule[event.date_time]
            self.events.pop(row)

        self.update_schedule_table()

    def add_minister(self, person, role):
        self.ministers[role] = person

    def remove_minister(self, role):
        if role in self.ministers:
            del self.ministers[role]

    def __str__(self):
        return f"{self.event_type} - {self.date_time.strftime('%Y-%m-%d %H:%M')} @ {self.location}"
    
    def schedule_event(event, ministers, roles):
    for role in roles:
        if role in event.ministers:
            continue
        for minister in ministers[role]:
            if minister.schedule.get(event.date_time) is None:
                event.add_minister(minister, role)
                minister.schedule[event.date_time] = event
                break

    def add_person(name, role):
    person = Person(name, role)
    ministers[role].append(person)
    print(f"{role.capitalize()} '{name}' added successfully.")

def add_event(event_type, date_time, location):
    date_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M')
    event = Event(event_type, date_time, location)
    events.append(event)
    schedule_event(event, ministers, event_roles)
    print(f"{event_type} scheduled for {date_time.strftime('%Y-%m-%d %H:%M')} at {location}.")

def view_schedule():
    print("Scheduled Events:")
    for event in events:
        print(f"- {event}")
def delete_event(self):
        selected_rows = sorted(set(index.row() for index in self.schedule_table.selectedIndexes()), reverse=True)
        for row in selected_rows:
            event = self.events[row]
            for minister in event.ministers.values():
                if event.date_time in minister.schedule:
                    del minister.schedule[event.date_time]
            self.events.pop(row)
        self.update_schedule_table()


# Sample data
ministers = {
    "priest": [],
    "deacon": [],
    "other": []
}
event_roles = ["priest", "deacon", "other"]
events = []

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MassSchedulerGUI()
    window.show()

    sys.exit(app.exec_())
