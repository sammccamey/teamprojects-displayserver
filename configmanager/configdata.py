from common import database

class Configuration():
    def __init__(self):
        self.datatypes = {
                'alarm_time': int,       # Minutes from start of day
                'background_theme': str, # Chosen from a list
                'layout_choice': str,    # Chosen from a list
                'calendar_url': str,     # Supplied by user
                'alarm_sound': str,      # Chosen from a list
                'fortune_db': str,       # Chosen from a list
                'forecast_location': int # By zip code
        }
        self.data = {
                'alarm_time': 8 * 60,
                'background_theme': 'term',
                'layout_choice': 'cf',
                'calendar_url': 'http://www.wright.edu/calendar/term/all/events.ics',
                'alarm_sound': 'phone_ringing',
                'fortune_db': 'none',
                'forecast_location': 45435
        }

    def retrieve(self):
        # Retrieve config from database.
        with database.connect() as conn:
            for k in self.datatypes:
                data = conn.execute('SELECT Value FROM ConfigItems WHERE key = ?', [k]).fetchone()
                if data is not None:
                    data = data[0]
                    self.data[k] = self.datatypes[k](data)

    def save(self):
        with database.connect() as conn:
            for k in self.data:
                conn.execute('INSERT OR REPLACE INTO ConfigItems (key, value) VALUES (?, ?)', [k, self.data[k]])
            conn.commit()

    def setup(self):
        database.initialize()
        self.save()
