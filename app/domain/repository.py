from sqlalchemy.orm import Session

from app.domain import model


def get_employees(db: Session):
    return db.query(model.Employee).all()