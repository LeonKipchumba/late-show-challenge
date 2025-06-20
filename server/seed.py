from server.app import app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.user import User

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed Guests
    guest1 = Guest(name='John Doe', occupation='Comedian')
    guest2 = Guest(name='Jane Smith', occupation='Actor')
    db.session.add_all([guest1, guest2])

    # Seed Episodes
    episode1 = Episode(date='2025-06-01', number=1)
    episode2 = Episode(date='2025-06-02', number=2)
    db.session.add_all([episode1, episode2])

    # Seed Appearances
    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode2)
    db.session.add_all([appearance1, appearance2])

    db.session.commit()
    print('Database seeded!')
