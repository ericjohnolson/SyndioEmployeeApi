from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.domain import repository, schema
from app.domain.database import engine


app = FastAPI(
    title="Syndio Employee API",
    description="The Employee API is a Syndio Backend App exposing employee diversity and equity indicators.",
    version="0.0.1",
)


@app.get("/")
def api_health_check():
    return {"Message": "API is running."}


@app.get("/employees", response_model=list[schema.Employee])
def get_employees(db: Session = Depends(get_db)):
    employees = repository.get_employees(db)
    return employees
