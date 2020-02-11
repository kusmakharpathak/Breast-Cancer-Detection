import uuid
from dataclasses import field, dataclass
from typing import Dict
from common.utils.utils import Utils
import model.error.errors as UserErrors
from model.model import Models


@dataclass
class Admin(Models):
    collection: str = field(init=False, default="admin")
    f_name: str
    l_name: str
    address: str
    contact_no: str
    email: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @staticmethod
    def find_by_email(email: str):
        try:
            return Admin.find_one('email', email)
        except TypeError:
            print(UserErrors.UserNotFoundError('A user with e-mail was not found.'))

    @classmethod
    def login(cls, email, password):
        user = cls.find_by_email(email)
        if not Utils.check_password(password, user.password):
            return False
        else:
            return True

    @classmethod
    def add_admin(cls, f_name: str, l_name: str, address: str, contact_no: str, email: str, password: str):  # inserting data to database
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError('Email does not have right format.')

        if cls.find_by_email(email):
            raise UserErrors.UserAlreadyRegistredError("Email already register.")
        else:
            cls(f_name, l_name, address, contact_no, email, Utils.hash_password(password)).save_to_mongo()
        return True

    def json(self) -> Dict:
        return {
            "f_name": self.f_name,
            "l_name": self.l_name,
            "address": self.address,
            "contact_no": self.contact_no,
            "email": self.email,
            "password": self.password
        }

    @property
    def id(self):
        return self._id
