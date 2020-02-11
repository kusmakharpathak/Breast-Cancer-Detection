import uuid
from dataclasses import field, dataclass
from typing import Dict
from model.model import Models
# from model.patient.patient import Patient
import model.error.errors as UserErrors


@dataclass
class Diagnosis(Models):
    collection: str = field(init=False, default="diagnosis")
    mean_radius: float
    mean_perimeter: float
    radius_worst: float
    perimeter_worst: float
    mean_area: float
    diagnosis: int
    patient_id: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def add_record(cls, mean_radius: float, mean_perimeter: float, radius_worst: float, perimeter_worst: float, mean_area: float, diagnosis: int, patient_id: str):
        # Diagnosis.find_by_patient_id(patient_id)
        cls(mean_radius, mean_perimeter, radius_worst, perimeter_worst, mean_area, diagnosis, patient_id).save_to_mongo()

    @classmethod
    def update_record(cls, mean_radius: float, mean_perimeter: float, radius_worst: float, perimeter_worst: float, mean_area: float, diagnosis: int, patient_id: str, id: str):
        cls(mean_radius, mean_perimeter, radius_worst, perimeter_worst, mean_area, diagnosis, patient_id).update(id)

    @classmethod
    def find_by_patient_id(cls, patient_id):
        try:
            return cls.find_one("patient_id", patient_id)
        except TypeError:
            print(UserErrors.UserNotFoundError('A user with this ID was not found.'))

    @classmethod
    def remove_pat(cls, pat_id):
        try:
            return cls.remove_from_mongo("patient_id", pat_id)
        except TypeError:
            print(UserErrors.RecordNotFound('No any Data found with this id'))

    def json(self) -> Dict:
        return {
            # mean_radius: float, mean_perimeter: float, radius_worst: float, perimeter_worst: float, mean_area: float,
            # diagnosis: int,
            "mean_radius": self.mean_radius,
            "mean_perimeter": self.mean_perimeter,
            "radius_worst": self.radius_worst,
            "perimeter_worst": self.perimeter_worst,
            "mean_area": self.mean_area,
            "diagnosis": self.diagnosis,
            "patient_id": self.patient_id
        }
