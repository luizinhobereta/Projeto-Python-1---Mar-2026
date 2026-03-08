from sistema import database, app
from sistema.models import Usuario, Foto

with app.app_context():
    database.create_all()