from fastapi import FastApi
from sqlmodel import SQLModel, Session, create_engine, select
from models import Driver Cargo
app=FastApl
engine=create_engine("sqlite:///database.db")
#создать таблицы
@app.on_event("startup")
def on_startup():
SQLModel.metadata.create_all(engine)
#регистрация водителя
@app.post("/drivers/")
def create_driver(driver: Driver):
with Session (engine) as session:
     session.add(driver)
	 session.commit()
	 session.refresh(driver)
	 return driver
#добавление груза
@app.post.("/cargo")
def create_cargo(cargo:Cargo):
with Session(engine) as session
     session.add(cargo)
	 session.commit()
	 session.refresh(cargo)
return cargo
#список грузов
@app.get("/cargo"/)
def list_cargo():
with Session(engine) as session:

return session.exec(select(Cargo)).all()
