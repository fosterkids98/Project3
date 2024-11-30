from datetime import datetime
from sqlalchemy import (UniqueConstraint, create_engine, String, ForeignKey, BIGINT, DECIMAL, 
                        PrimaryKeyConstraint, select, Column, Table, 
                        ForeignKeyConstraint, Float,DateTime)
from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column, Session, 
                            relationship)
from typing import List
#app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError, fields
import os

# Initialize Flask app
app = Flask(__name__)

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:7374@127.0.0.1/flask_api_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Creating our Base Model
class Base(DeclarativeBase):
    pass

# Initialize extensions
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)
# Create engine for the MySQL database
engine = create_engine('mysql+mysqlconnector://root:7374@127.0.0.1/flask_api_db')


class Base(DeclarativeBase):
    pass
class OrderItem(Base):
    """association table for many to many relationship with items and orders"""
    __tablename__ = 'items_ordered'
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.order_id'),primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('items.item_id'), primary_key=True)
    #using cascade to delete all orders from a deleted user
    order = db.relationship('Order', back_populates='items_ordered', 
                            viewonly=True,cascade='all, delete-orphan')
    #using cascade to delete all products from a deleted order
    product = db.relationship('Item', back_populates='items_ordered', 
                              viewonly=True,cascade='all, delete-orphan')
    #makes user unable to add duplicate items to one order
    __table_args__ = (
        UniqueConstraint('order_id', 'item_id', name='uix_order_item_unique'),
    )

class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    address: Mapped[str] = mapped_column(String(150),nullable=True)
    #creates one to many relationship from user to orders
    orders: Mapped[List['Order']] = relationship('Order', backref='user', lazy=True,cascade='all, delete-orphan')

class Order(Base):
    __tablename__ = 'orders'
    order_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'), nullable=False)
    order_date: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow,nullable=False)
    #many to many relationship with items
    items_ordered = db.relationship('OrderItem', back_populates='order',cascade='all, delete-orphan')
    

class Item(Base):
    __tablename__ = 'items'
    item_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    serial: Mapped[int] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    #many to many relationship with orders
    items_ordered = db.relationship('OrderItem', back_populates='product',cascade='all, delete-orphan')



Base.metadata.create_all(engine)