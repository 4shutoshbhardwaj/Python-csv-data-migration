import pandas as pd
from models import Product
from sqlalchemy.orm import sessionmaker

def upload_data(csv_file, engine):
    df = pd.read_csv(csv_file)
    session = sessionmaker(bind=engine)()
    for index, row in df.iterrows():
        product = Product(
            product_id=row['product_id'],
            product_name=row['product_name'],
            category=row['category'],
            price=row['price'],
            quantity_sold=row['quantity_sold'],
            rating=row['rating'],
            review_count=row['review_count']
        )
        session.add(product)
    session.commit()
