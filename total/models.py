# coding: utf-8
from sqlalchemy import Column, Integer, Table, Text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Table1(db.Model):
    __tablename__ = 'table1'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)


class Table2(db.Model):
    __tablename__ = 'table2'

    id = db.Column(db.Integer, primary_key=True)
    table1_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
