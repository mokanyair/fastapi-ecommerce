from typing import Generic, TypeVar, Type
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session):
        return db.query(self.model).all()

    def create(self, db: Session, obj_in):
        print(" CRUD: create")
        obj = self.model(**obj_in.model_dump())
        print("Before commit:", obj)
        db.add(obj)
        db.commit()
        print("After commit:", obj)
        db.refresh(obj)
        return obj

    def update(self, db: Session, db_obj, obj_in):
        data = obj_in.model_dump(exclude_unset=True)
        for field, value in data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id: int):
        obj = self.get(db, id)
        if obj:
            db.delete(obj)
            db.commit()
        return obj