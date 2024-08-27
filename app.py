from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import pandas as pd
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql12728040:6teES33BYT@sql12.freesqldatabase.com:3306/sql12728040'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50), unique=True, nullable=False)
    product_name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity_sold = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review_count = db.Column(db.Integer, nullable=False)

@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"msg": "Username already exists"}), 400
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid username or password"}), 401

@app.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    if 'file' not in request.files:
        return jsonify({"msg": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"msg": "No selected file"}), 400
    try:
        df = pd.read_csv(file)
        print("Columns in CSV file:", df.columns)

        required_columns = ['product_id', 'product_name', 'category', 'price', 'quantity_sold', 'rating', 'review_count']
        for col in required_columns:
            if col not in df.columns:
                return jsonify({"msg": f"Missing column: {col}"}), 400

        df['price'].fillna(df['price'].median(), inplace=True)
        df['quantity_sold'].fillna(df['quantity_sold'].median(), inplace=True)
        df['rating'].fillna(df.groupby('category')['rating'].transform('mean'), inplace=True)

        chunk_size = 100
        for start in range(0, len(df), chunk_size):
            end = start + chunk_size
            chunk = df.iloc[start:end]
            with db.session.no_autoflush:
                for _, row in chunk.iterrows():
                    product = Product.query.filter_by(product_id=row['product_id']).first()
                    if product:
                        product.product_name = row['product_name']
                        product.category = row['category']
                        product.price = row['price']
                        product.quantity_sold = row['quantity_sold']
                        product.rating = row['rating']
                        product.review_count = row['review_count']
                    else:
                        product = Product(
                            product_id=row['product_id'],
                            product_name=row['product_name'],
                            category=row['category'],
                            price=row['price'],
                            quantity_sold=row['quantity_sold'],
                            rating=row['rating'],
                            review_count=row['review_count']
                        )
                        db.session.add(product)
                db.session.commit()

        return jsonify({"msg": "Data uploaded successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": str(e)}), 400

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
