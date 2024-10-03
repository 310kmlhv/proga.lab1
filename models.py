# models.py
class Patient:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Doctor:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Nurse:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Medication:
    def __init__(self, id, name, dosage):
        self.id = id
        self.name = name
        self.dosage = dosage

class Appointment:
    def __init__(self, id, patient_id, doctor_id, nurse_id, medication_id):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.nurse_id = nurse_id
        self.medication_id = medication_id
