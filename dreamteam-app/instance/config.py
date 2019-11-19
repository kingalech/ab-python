import os
DB_HOST = os.environ.get('FLASK_DB_HOST')
SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'mysql://admin:Admin@12345@'+str(DB_HOST)+'/dreamteam_db'
