from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from saleapp import db, app
from enum import Enum as UserEnum
from flask_login import UserMixin


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(1000))
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Dien Thoai')
        # c2 = Category(name='may tinh bang')
        # c3 = Category(name='phu kien')

        # db.session.add_all([c1])
        # db.session.commit()
        # p1 = Product(name='iPhone 13', description='Apple, 128GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg',
        #              category_id=1)
        # p2 = Product(name='iPhone 12', description='Apple, 128GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg',
        #              category_id=1)
        # p3 = Product(name='iPhone 14', description='Apple, 128GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg',
        #              category_id=1)
        # p4 = Product(name='Note 22', description='Samsung, 128GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg',
        #              category_id=1)
        # p5 = Product(name='iPad pro', description='Apple, 128GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg',
        #              category_id=2)
        # db.session.add_all([p1,p2,p3,p4,p5])
        # db.session.commit()

        import hashlib

        password = str(hashlib.md5('123456'.encode('utf-8')).digest())
        u = User(name='Dat', username='admin', password=password, user_role=UserRole.ADMIN,
                 avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg')
        db.session.add(u)
        db.session.commit()
    # db.create_all()
