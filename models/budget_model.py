from models.models import db, Basic_Model
from sqlalchemy import Column, String, Integer

# A capablity class
class Budget(Basic_Model, db.Model):
    __tablename__ = 'budget'

    number = Column(Integer, nullable=False)
    task_area = Column(String, nullable=False)
    ceiling_value = Column(Integer, nullable=False)
    funded_value = Column(Integer, nullable=False)
    eac_revenue = Column(Integer, nullable=False)
    eac_profit = Column(Integer, nullable=False)
    eac_profit_percent = Column(Integer, nullable=False)

    def __init__(self, number, task, ceiling, funded, revenue, profit,
                 percent):
        self.number = number
        self.task_area = task
        self.ceiling_value = ceiling
        self.funded_value = funded
        self.eac_revenue = revenue
        self.eac_profit = profit
        self.eac_profit_percent = percent

    def format(self):
        return {
            'id': self.id,
            'number': self.number,
            'task_area' : self.task_area,
            'ceiling_value': self.ceiling_value,
            'funded_value': self.funded_value,
            'eac_revenue': self.eac_revenue,
            'eac_profit' : self.eac_profit,
            'eac_profit_percent' : self.eac_profit_percent
        }