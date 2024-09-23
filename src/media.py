import xml.etree.ElementTree as ET
import json
from datetime import date

class Patient:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.diagnoses = []

    def add_diagnosis(self, diagnosis):
        self.diagnoses.append(diagnosis)

class Doctor:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

class Diagnosis:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Treatment:
    def __init__(self, id, patient, doctor, diagnosis, start_date, end_date=None):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.diagnosis = diagnosis
        self.start_date = start_date
        self.end_date = end_date

class Medication:
    def __init__(self, id, name, dosage_form, dose, frequency, duration):
        self.id = id
        self.name = name
        self.dosage_form = dosage_form
        self.dose = dose
        self.frequency = frequency
        self.duration = duration

class Analysis:
    def __init__(self, id, patient, doctor, analysis_type, result):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.analysis_type = analysis_type
        self.result = result

class Equipment:
    def __init__(self, id, name, equipment_type):
        self.id = id
        self.name = name
        self.equipment_type = equipment_type

class Surgery:
    def __init__(self, id, patient, anesthesiologist, surgeon, operation_date, status):
        self.id = id
        self.patient = patient
        self.anesthesiologist = anesthesiologist
        self.surgeon = surgeon
        self.operation_date = operation_date
        self.status = status

class Report:
    def __init__(self, id, surgery, author, creation_date, summary, observations):
        self.id = id
        self.surgery = surgery
        self.author = author
        self.creation_date = creation_date
        self.summary = summary
        self.observations = observations