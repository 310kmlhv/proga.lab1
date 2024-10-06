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

class Disease:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class Treatment:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class Room:
    def __init__(self, id, number, type):
        self.id = id
        self.number = number
        self.type = type


class Bill:
    def __init__(self, id, patient_id, amount):
        self.id = id
        self.patient_id = patient_id
        self.amount = amount


class Payment:
    def __init__(self, id, bill_id, amount, date):
        self.id = id
        self.bill_id = bill_id
        self.amount = amount
        self.date = date