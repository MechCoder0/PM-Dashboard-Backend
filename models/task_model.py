from models.models import db, Basic_Model
from sqlalchemy import Column, String, Integer

# A capablity class
class Task(Basic_Model, db.Model):
    __tablename__ = 'task'

    description = Column(String, nullable=False)
    category = Column(String, nullable=False)

    def __init__(self, description, category):
        self.description = description
        self.category = category 

    def format(self):
        return {
            'id': self.id,
            'description': self.description,
            'category' : self.category
        }