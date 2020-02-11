from abc import ABCMeta, abstractmethod
from typing import List, TypeVar, Type, Union, Dict

from common.database.database import Database

T = TypeVar('T', bound='Model')


class Models(metaclass=ABCMeta):
    collection: str
    _id: str

    def __init__(self, *args, **kwargs):
        pass

    def save_to_mongo(self):
        Database.update(self.collection, {"_id": self._id}, self.json())

    def update(self, id):
        Database.update(self.collection, {"_id": id}, self.json())

    @classmethod
    def remove_from_mongo(cls, attribute: str,  value: str):
        Database.remove(cls.collection, {attribute: value})

    @classmethod
    def find_by_id(cls: Type[T], _id: str) -> T:
        return cls.find_one("_id", _id)

    @classmethod
    def find_all(cls: Type[T]) -> List:
        element_from_db = Database.find(cls.collection, {})
        return [cls(**elem) for elem in element_from_db]

    @classmethod
    def find_one(cls: Type[T], attribute: str, value: str) -> T:
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_many(cls: Type[T], attribute: str, value: Union[str, dict]) -> List:
        element_from_mongo = Database.find(cls.collection, {attribute: value})
        return [cls(**elem) for elem in element_from_mongo]

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplemented
