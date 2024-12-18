from flask import Flask, render_template, request, jsonify, send_file, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from datetime import *
import jwt
from config import Config  # Importa la configuración


app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)

AppVersion = app.config['AppVersion']

class Usuarios(db.Model):
    wID = db.Column(db.Integer, primary_key=True)
    strUserName = db.Column(db.String(100), unique=True, nullable=False)
    strPassword = db.Column(db.String(100), nullable=False)
    strEmail = db.Column(db.String(100), unique=True, nullable=False)
    fechaRegistro = db.Column(db.DateTime, default=datetime.utcnow)
    IsLogged = db.Column(db.SmallInteger, nullable=False)

class Claves(db.Model):
    wID = db.Column(db.Integer, primary_key=True)
    wUserID = db.Column(db.Integer, nullable=False)
    dwKey = db.Column(db.String(100), nullable=False)
    dTimeExpire = db.Column(db.DateTime, nullable=False)

def usuario_existente(username, email):
    query = text("SELECT COUNT(*) FROM Usuarios WHERE strUserName = :username OR strEmail = :email")
    result = db.session.execute(query, {'username': username, 'email': email})
    count = result.fetchone()[0]
    return count > 0

def insertar_usuario(username, email, password):
    query = text("INSERT INTO Usuarios (strUserName, strPassword, strEmail, fechaRegistro) VALUES (:username, :password, :email, GETDATE())")
    db.session.execute(query, {'username': username, 'password': password, 'email': email})
    db.session.commit()

def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(days=30)  # 30 min
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    if token:
        return token.encode('utf-8')
    else:
        return None  # Handle the case where the token is not generated correctly


@app.route('/validar_version', methods=['POST'])
def validar_version():
    data = request.get_json()
    client_version = data.get('version')

    if AppVersion == client_version:
        return jsonify({"CorrectVersion": True}), 200
    else:
        return jsonify({"CorrectVersion": False}), 200

@app.route('/logout', methods=['POST'])
def logout():
    data = request.form  

    username = data.get('username')  
    
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token faltante'}), 401  
    
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256']) # we could use the config.py file
        username = payload['username']
        user = Usuarios.query.filter_by(strUserName=username).first()
        if user:
            user.IsLogged = 0  
            db.session.commit()
            return jsonify({'message': 'Logout exitoso'})
        else:
            return 'Usuario no encontrado', 404  
        
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token expirado'}), 401  
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Token inválido'}), 401  
    
            
    
# verify connection login
@app.route('/verificar_sesion', methods=['GET', 'POST'])
def verificar_sesion():
    data = request.form 
    username = data.get('username')  
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'message': 'Token faltante'}), 401  
    
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256']) # we could use the config.py file
        username = payload['username']
        user = Usuarios.query.filter_by(strUserName=username).first()
        if user.IsLogged == 1:
            return jsonify({'message': 'Logout exitoso'})
        else:
            return 'Usuario Desconectado', 404  

    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token expirado'}), 
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Token inválido'}), 
          
        


@app.route('/validar_login', methods=['POST'])
def validar_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    version = data.get(('version'))

    if AppVersion != version: ## check if version is not equal
        return jsonify({"valid": False, "permisos": False, "SameVersion": False})


    user = Usuarios.query.filter_by(strUserName=username, strPassword=password).first()

    if user:
        if user.IsLogged == 1:
            return jsonify({"valid": False, "permisos": False, "SameVersion": True, "AlreadyLogged": True})

        user.IsLogged = 1  # mark user as connected
        db.session.commit()

        key = Claves.query.filter_by(wUserID=user.wID).first()

        if key:
            now = datetime.now()
            expiry = key.dTimeExpire # change name of attribute
            if now > expiry:
                Claves.query.filter_by(wID=key.wID).delete() # delete object key
                db.session.commit()
                token = generate_token(username)
                return jsonify({"valid": True, "permisos": False, "SameVersion": True, "AlreadyLogged": False, 'token': token.decode('utf-8')})
            else:
                token = generate_token(username)
                dTimeExpire = key.dTimeExpire.strftime('%Y-%m-%d %H:%M:%S')
                return jsonify({"valid": True, "permisos": True, "SameVersion": True, "AlreadyLogged": False, 'token': token.decode('utf-8'), 'dTimeExpire': dTimeExpire})
        else:
            token = generate_token(username)
            return jsonify({"valid": True, "permisos": False, "SameVersion": True, "AlreadyLogged": False, 'token': token.decode('utf-8')})
    else:
        return jsonify({"valid": False, "permisos": False, "SameVersion": True, "AlreadyLogged": False, 'token': ""})

@app.route('/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        #data = request.get_json()
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not (username and email and password):
            return 'Por favor, complete todos los campos.', 400
        
        if '@' not in email:
            return 'Ingrese un correo electrónico válido.', 400
        
        if Usuarios.query.filter_by(strUserName=username).first() or Usuarios.query.filter_by(strEmail=email).first():
            return 'El usuario o email ya están registrados.', 400
    
        nuevo_usuario = Usuarios(strUserName=username, strEmail=email, strPassword=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        return 'Registro exitoso'

    return render_template('Registro.html')


### patcher

# check actual version
@app.route('/check_update')
def check_update():
    client_version = request.args.get('client_version')  # get version from client
    if client_version != AppVersion:
        # we will just send the files to the client
        files_to_send = ['PokemonMMO_bot.exe', 'settings.json']

        return jsonify(files=files_to_send, update = "True")
    else:
        return jsonify(update = "False")

update_directory = 'C:\\Users\\admin\\Desktop\\PokeServer\\Patches'

@app.route('/download_update/<filename>')
def download_update(filename):
    # check if the file is allowed
    allowed_files = ['PokemonMMO_bot.exe', 'settings.json']
    
    if filename in allowed_files:
        return send_from_directory(update_directory, filename, as_attachment=True)
    else:
        return "Archivo no permitido", 403  



if __name__ == "__main__":
    app.run(debug= True,host='0.0.0.0', port=1345)  

 