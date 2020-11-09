from models.models import Basic_Model, db
from sqlalchemy import Column, Integer, String
import datetime

class Risk(Basic_Model, db.Model):
    __tablename__ = 'risk'

    riskItem = Column(String, nullable=False)
    actions = Column(String, nullable=False)
    impact = Column(String, nullable=False)
    impactDate = Column(db.DateTime, default=datetime.datetime.utcnow,
                         nullable=True)
    status = Column(String, nullable=False)

    def __init__(self, riskItem, actions, impact, 
                 impactDate, status):
        self.riskItem = riskItem
        self.actions = actions
        self.impact = impact
        self.impactDate = impactDate
        self.status = status 

    def format(self):
        return {
            'id': self.id,
            'riskItem': self.riskItem,
            'actions': self.actions,
            'impact': self.impact,
            'impactDate': self.impactDate,
            'status': self.status
        }