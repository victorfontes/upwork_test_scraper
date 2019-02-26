import records
from settings import DATABASE_URI


db = records.Database(DATABASE_URI)


def get_event_id(name, date):
    rows = db.query('SELECT id FROM events WHERE name=:name and date=:date', name=name, date=date) 
    return rows[0]['id']


def create_event(name, date):
    """Create or Select an event and returns the id."""
    rows = db.query('''
                    INSERT INTO 
                        events (id, name, date) 
                    VALUES 
                        (DEFAULT, :name, :date)
                    ON CONFLICT DO NOTHING
                    RETURNING id''', name=name, date=date)
    if not rows:
        return get_event_id(name, date)
    return rows[0]['id']
    


def get_fighter_id(name):
    rows = db.query('SELECT id FROM fighters WHERE name=:name', name=name)
    return rows[0]['id']


def create_fighter(name):
    """Create or Select a fighter and returns the id."""
    rows = db.query('''
            INSERT INTO
                fighters (id, name)
            VALUES
                (DEFAULT, :name)
            ON CONFLICT
                DO NOTHING
            RETURNING 
                id''', name=name)
    
    if not rows:
        return get_fighter_id(name)
    
    return rows[0]['id']