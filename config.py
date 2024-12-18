# Configuration file

class Config:
    SECRET_KEY = 'g423s23dk23A!'  # secret key to sign tokens
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://username:password@server_name:port/database_name?'
        'driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # disable tracking modifications
    AppVersion = "1.1.5"  # Agregar la versión de la aplicación