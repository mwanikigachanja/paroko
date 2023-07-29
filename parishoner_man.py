import sqlite3

class ParishionerManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS parishioners (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    address TEXT,
                    contact TEXT,
                    baptism_date TEXT,
                    marriage_date TEXT
                )
            ''')

    def add_parishioner(self, name, address, contact, baptism_date, marriage_date):
        with self.conn:
            self.conn.execute('''
                INSERT INTO parishioners (name, address, contact, baptism_date, marriage_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, address, contact, baptism_date, marriage_date))

    def edit_parishioner(self, id, name, address, contact, baptism_date, marriage_date):
        with self.conn:
            self.conn.execute('''
                UPDATE parishioners
                SET name=?, address=?, contact=?, baptism_date=?, marriage_date=?
                WHERE id=?
            ''', (name, address, contact, baptism_date, marriage_date, id))

    def delete_parishioner(self, id):
        with self.conn:
            self.conn.execute('''
                DELETE FROM parishioners
                WHERE id=?
            ''', (id,))

    def get_parishioner_by_id(self, id):
        with self.conn:
            cursor = self.conn.execute('''
                SELECT * FROM parishioners
                WHERE id=?
            ''', (id,))
            return cursor.fetchone()

    def search_parishioners(self, search_term):
        with self.conn:
            cursor = self.conn.execute('''
                SELECT * FROM parishioners
                WHERE name LIKE ? OR address LIKE ? OR contact LIKE ?
            ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            return cursor.fetchall()

    def get_all_parishioners(self):
        with self.conn:
            cursor = self.conn.execute('''
                SELECT * FROM parishioners
            ''')
            return cursor.fetchall()

    def add_sacrament(self, sacrament_type, date, location=None, presiding_clergy=None):
        with self.conn:
            self.conn.execute('''
                INSERT INTO sacraments (type, date, location, presiding_clergy)
                VALUES (?, ?, ?, ?)
            ''', (sacrament_type, date, location, presiding_clergy))

    def get_sacrament_by_id(self, id):
        with self.conn:
            cursor = self.conn.execute('''
                SELECT * FROM sacraments
                WHERE id=?
            ''', (id,))
            return cursor.fetchone()

    def get_all_sacraments(self):
        with self.conn:
            cursor = self.conn.execute('''
                SELECT * FROM sacraments
            ''')
            return cursor.fetchall()

    def generate_sacrament_report(self):
        with self.conn:
            cursor = self.conn.execute('''
                SELECT * FROM sacraments
            ''')
            return cursor.fetchall()


    def __del__(self):
        self.conn.close()

