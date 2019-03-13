from common import database

datatypes = {
    'alarm_time': int,       # Minutes from start of day
    'background_theme': str, # Chosen from a list
    'layout_choice': str,    # Chosen from a list
    'calendar_url': str,     # Supplied by user
    'alarm_sound': str,      # Chosen from a list
    'fortune_db': str,       # Chosen from a list
    'forecast_location': int # By zip code
}
possibilities = {
    'background_theme': ['term', 'white'],
    'layout_choice': ['left', 'right'],
    'alarm_sound': ['phone_ringing', 'buzzer'],
    'fortune_db': ['none', 'openbsd']
}

def retrieve():
    # Retrieve config from database.
    cfg = {k: None for k in datatypes.keys()}
    with database.connect() as conn:
        for k in datatypes:
            data = conn.execute('SELECT Value FROM ConfigItems WHERE key = ?', [k]).fetchone()
            if data is not None:
                data = data[0]
                cfg[k] = datatypes[k](data)
    return cfg            


def save(cfg):
    with database.connect() as conn:
        for k in cfg:
            conn.execute('INSERT OR REPLACE INTO ConfigItems (key, value) VALUES (?, ?)', [k, cfg[k]])
        conn.commit()

def setup():
    database.initialize()
    save({
            'alarm_time': 8 * 60,
            'background_theme': 'term',
            'layout_choice': 'left',
            'calendar_url': 'http://www.wright.edu/calendar/term/all/events.ics',
            'alarm_sound': 'phone_ringing',
            'fortune_db': 'none',
            'forecast_location': 45435
    })
