import uuid
from dataclasses import field, dataclass
from typing import Dict
from model.model import Models
import model.error.errors as UserErrors


@dataclass
class Patient(Models):
    collection: str = field(init=False, default="patients")
    f_name: str
    l_name: str
    contact_no: str
    dob: str
    gender: str
    address: str
    email: str
    doctor_id: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def add_patient(cls, f_name, l_name, contact_no, dob, gender, address, doctor_id, email=''):
        if cls.find_by_contact_no(contact_no):
            raise UserErrors.UserAlreadyRegistredError("contact no already register.")
        else:
            cls(f_name, l_name, contact_no, dob, gender, address, email, doctor_id).save_to_mongo()
        return True

    @classmethod
    def find_by_contact_no(cls, contact_no):
        try:
            return cls.find_one("contact_no", contact_no)
        except TypeError:
            print(UserErrors.UserNotFoundError('A user with contact no was not found.'))

    @classmethod
    def find_all_by_doc_id(cls, doctor_id):
        try:
            return cls.find_many("doctor_id", doctor_id)
        except TypeError:
            raise UserErrors.RecordNotFound('No any Data found with this id')

    @classmethod
    def remove_pat(cls, pat_id):
        try:
            return cls.remove_from_mongo("_id", pat_id)
        except TypeError:
            print(UserErrors.RecordNotFound('No any Data found with this id'))

    def json(self) -> Dict:
        return {
            "f_name": self.f_name,
            "l_name": self.l_name,
            "contact_no": self.contact_no,
            "dob": self.dob,
            "gender": self.gender,
            "address": self.address,
            "email": self.email,
            "doctor_id": self.doctor_id
        }
