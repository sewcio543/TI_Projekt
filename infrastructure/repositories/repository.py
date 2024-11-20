from collections.abc import Iterable

from sqlmodel import Session, SQLModel, select

from domain.contracts.irepository import IRepository


class Repository[T](IRepository[T]):
    model: type[SQLModel]

    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, id: int) -> T:
        return self.session.get(self.model, id)  # type: ignore

    def get_all(self) -> Iterable[T]:
        stmt = select(self.model)
        result = self.session.exec(stmt)
        return list(result.all())  # type: ignore

    def insert(self, entity: T) -> None:
        self.session.add(entity)

    def delete(self, entity: T) -> None:
        self.session.delete(entity)
