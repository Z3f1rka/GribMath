from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from data import db_session
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, create_refresh_token
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from data.users import User
from data.category import Category
from data.main_category import MainCategory
from data.examples import Example
from data.history import History
from data.achievements_description import Achievement_Description
from data.achievements_users import Achievement_User
from functools import wraps
from datetime import timedelta
import datetime
from sqlalchemy import func
import sqlalchemy


app = Flask(__name__)
app.config.from_object(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'

jwt = JWTManager(app)

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

CORS(app)

# password
def set_password(self, password):
    self.hashed_password = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.hashed_password, password)


# token verification
secret_key = 'super-secret'

def verify_token(token):
  try:
    decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
    return decoded_token
  except jwt.ExpiredSignatureError:
    return 'Signature expired. Please log in again.'
  except jwt.InvalidTokenError:
    return 'Invalid token. Please log in again.'


# for the pages that require authorization
def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', None)
        if not token:
            return jsonify({'error': 'Отсутствует токен JWT'}), 401
        
        try:
            data = jwt.decode(token, 'секретный_ключ')
        except Exception as e:
            return jsonify({'error': 'Неверный токен JWT'}), 401
        
        return f(*args, **kwargs)
    return decorated


# the first page
@app.route('/', methods=['GET'])
def index():
    return jsonify({"msg": "Hello,World"})


# login
@app.route('/login', methods=['POST'])
def login():
    username = request.get_json().get('username')
    password = request.get_json().get('password')

    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.username == username).first()
    if user and check_password_hash(user.hashed_password, password):
        pass
    else:
        return jsonify({'error': 'Неверное имя пользователя или пароль'})
    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    return jsonify({'access_token': access_token, 'refresh_token': refresh_token})




@app.route('/profile/<int:id>', methods=['GET'])
def get_user(id):
  db_sess = db_session.create_session()
  user = db_sess.query(User).filter(User.id == id).first()
  today = datetime.date.today()
  three_months_ago = today - datetime.timedelta(days=31)

  labels = []
  while three_months_ago <= today:
    labels.append(three_months_ago)
    three_months_ago += datetime.timedelta(days=1)
  data = []
  for i in labels:
      history = db_sess.query(History).filter(History.user_id == id).filter(History.date == i).filter(History.is_solved == True)
      data.append(history.count())
  for i in range(len(labels)):
      labels[i] = labels[i].strftime("%d.%m")
  if user:
    return jsonify({'username' : user.username, 'email': user.email, 'registration_date': user.registration_date, 'avatar': user.avatar, 'id':user.id, 'data':data, 'labels':labels })
  else:
    return jsonify({ 'success': False, 'message': 'Данного пользователя не существует' })


# protection
@app.route('/protected', methods=['GET'])
@jwt_required(optional=False)
def protected():
    current_user = get_jwt_identity()
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.username == current_user).first()
    return jsonify({'id': user.id, 'username': user.username, 'avatar': user.avatar})


# registration
@app.route('/register', methods=['POST'])
def register():
    db_sess = db_session.create_session()
    data = request.get_json()
    print(data)
    email = data.get('email')
    password = data.get('password')
    password_again = data.get("password_again")
    username = data.get('username')
    avatar = data.get('avatar')

    if not email or not password or not username:
        return jsonify({'error': 'Необходимо указать email, имя пользователя и пароль'}), 400

    user = db_sess.query(User).filter_by(email=email).first()
    if user:
        return jsonify({'error': 'Пользователь с указанным email уже существует'})
    
    user = db_sess.query(User).filter_by(username=username).first()
    if user:
        return jsonify({'error': 'Пользователь с указанным username уже существует'})
    
    if password != password_again:
       return jsonify({'error': 'Пароли должны совпадать'})
    
    hashed_password = generate_password_hash(password)
    registration_date = datetime.datetime.now()

    if avatar:
       user = User(email=email, hashed_password=hashed_password, username=username, registration_date=registration_date, avatar=avatar)
    else:
       user = User(email=email, hashed_password=hashed_password, username=username, registration_date=registration_date)
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    return jsonify({'access_token': access_token, 'refresh_token': refresh_token})


# add avatar / phone number, edit all info
@app.route('/edit_info/<int:id>', methods=['PUT', 'GET'])
def edit_info(id):
    if request.method == 'PUT':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        phone_number = data.get('phone_number')
        avatar = data.get('avatar')
        
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == id).first()

        if phone_number:
            user.phone_number = phone_number
        else:
            user.phone_number = ''

        if avatar:
            user.avatar = avatar
        else:
            user.avatar = ''

        if not email or not username or not password:
            return jsonify({'error': 'Нельзя не указывать email, username и password, можно только менять!'}), 400

        if user.email != email:
            check_if_user_exists_email = db_sess.query(User).filter(User.email == email).first()
        if check_if_user_exists_email:
            return jsonify({'error': 'Пользователь с указанным email уже существует'}), 409
        else:
            user.email = email

        if user.username != username:
            check_if_user_exists_username = db_sess.query(User).filter(User.username == username).first()
        if check_if_user_exists_username:
            return jsonify({'error': 'Пользователь с указанным username уже существует'}), 409
        else:
            user.username = username

        if user.hashed_password != password:
            user.hashed_password = generate_password_hash(password)

        db_sess.commit()

        return redirect('/')

    elif request.method == 'GET':
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == id).first()

        return jsonify({'username': user.username, 'email': user.email, 'password': user.hashed_password, 'phone_number': user.phone_number, 'avatar': user.avatar})
    

# get all categories
@app.route('/all_categories', methods=['GET'])
def all_categories():
    if request.method == 'GET':
        for_return = []
        db_sess = db_session.create_session()
        all_main_categories = db_sess.query(MainCategory).all()
        for main_category in all_main_categories:
            for_return.append({"title": main_category.title})
            categories = db_sess.query(Category).filter(Category.main_category_id == main_category.main_category_id).all()
        return jsonify(for_return)
    

# leaders
@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    if request.method == 'GET':
        for_return = {}
        db_sess = db_session.create_session()
        history = db_sess.query(History).filter(History.is_solved == True).order_by(History.user_id).all()
        for leader in history:
            if leader in for_return:
                for_return[leader.username] += 1
            else:
                for_return[leader.username] = 1
        return jsonify(for_return)
    

# get examples
@app.route('/examples/<int:category_id>', methods=['GET'])
@jwt_required(optional=False)
def examples(category_id):
    if request.method == 'GET':
        username = get_jwt_identity()
        for_return = []
        num = 1
        db_sess = db_session.create_session()
        current_user = db_sess.query(User).filter(User.username == username).first()
        examples = db_sess.query(Example).filter(Example.category_id == category_id).all()
        for example in examples:
            example_history = db_sess.query(History).filter(History.user_id == current_user.id, History.problem_id == example.problem_id).first()
            if example_history.is_solved == False or not example_history:
                for_return.append({"name": example.problem, "answer": example.answer, "steps": example.steps, "id": example.problem_id})
                num += 1
            if num == 10:
                return jsonify(for_return)
        
        for_return['msg'] = 'Количество примеров меньше 10, так как пользователь решил в этой категории все сгенерированные примеры'
        return jsonify(for_return)
    

def check_achievements(user_id, time):
    db_sess = db_session.create_session()
    # 1
    history = db_sess.query(History).filter(History.user_id == user_id).all()
    if len(history) == 1:
        achievement = Achievement_User(user_id=user_id, achievement_id=1)
        db_sess.add(achievement)
    # 2
    history2 = history[-10:]
    n = 0
    for problem in history2:
        if problem.is_solved == True:
            n += 1
    if n == 10:
        achievement = Achievement_User(user_id=user_id, achievement_id=2)
        db_sess.add(achievement)
    # 3
    if int(time) < 5:
        achievement = Achievement_User(user_id=user_id, achievement_id=3)
        db_sess.add(achievement)
    # 4
    if int(time) < 3:
        achievement = Achievement_User(user_id=user_id, achievement_id=4)
        db_sess.add(achievement)
    # 5
    if len(history) == 50:
        achievement = Achievement_User(user_id=user_id, achievement_id=5)
        db_sess.add(achievement)
    # 6
    if len(history) == 200:
        achievement = Achievement_User(user_id=user_id, achievement_id=6)
        db_sess.add(achievement)
    # 7
    if len(history) == 500:
        achievement = Achievement_User(user_id=user_id, achievement_id=7)
        db_sess.add(achievement)
    # 8
    if len(history) == 1000:
        achievement = Achievement_User(user_id=user_id, achievement_id=8)
        db_sess.add(achievement)
    # 9
    if len(history) == 2000:
        achievement = Achievement_User(user_id=user_id, achievement_id=9)
        db_sess.add(achievement)
    # 10
    history3 = history[-100:]
    n = 0
    for i in history3:
        example = db_sess.query(Example).filter(problem_id=i.problem_id).first()
        main_category = db_sess.query(Category).filter(category_id=example.category_id).first().main_category_id
        if main_category == 1:
            n += 1
    if n == 100:
        achievement = Achievement_User(user_id=user_id, achievement_id=10)
        db_sess.add(achievement)
    # 11
    n = 0
    for i in history3:
        example = db_sess.query(Example).filter(problem_id=i.problem_id).first()
        main_category = db_sess.query(Category).filter(category_id=example.category_id).first().main_category_id
        if main_category == 2:
            n += 1
    if n == 100:
        achievement = Achievement_User(user_id=user_id, achievement_id=11)
        db_sess.add(achievement)
    # 12
    n = 0
    for i in history3:
        example = db_sess.query(Example).filter(problem_id=i.problem_id).first()
        main_category = db_sess.query(Category).filter(category_id=example.category_id).first().main_category_id
        if main_category == 1:
            n += 1
    if n == 100:
        achievement = Achievement_User(user_id=user_id, achievement_id=12)
        db_sess.add(achievement)
    db_sess.commit()
    return


# 10 problems history to db
@app.route('/problem_history', methods=['POST'])
def problem_history():
    db_sess = db_session.create_session()

    data = request.get_json()
    answers = data.get('answers')
    time = data.get('time')

    for answer, result, problem in answers:
        history = History(user_id=current_user.id, is_solved=result, date=datetime.datetime.now(), problem_id=problem)
        db_sess.add(history)
    db_sess.commit()

    # function to check achievements
    check_achievements(current_user.id, time)
    
    

# get achievements
@app.route('/achievements/<int:user_id>', methods=['GET'])
def achievements(user_id):
    if request.method == ['GET']:
        for_return = {}
        db_sess = db_session.create_session()
        achievements = db_sess.query(Achievement_User).filter(Achievement_User.user_id == user_id).all()
        for achievement in achievements:
            res = db_sess.query(Achievement_Description).filter(achievement.achievement_id == Achievement_Description.achievement_id).first()
            for_return[res.title] = [res.picture, res.conditions]
        return jsonify(for_return)
    

@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    refresh_token = create_refresh_token(identity=current_user)
    return jsonify({'access_token': new_token, 'refresh_token': refresh_token})
    

if __name__ == "__main__":
    db_session.global_init("db/users.db")
    app.run(debug=True, port=8080)
