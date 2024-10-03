import json
import xml.etree.ElementTree as ET
from models import Patient, Doctor, Nurse, Medication, Appointment
from xml_handler import XmlHandler
from json_handler import JsonHandler


class Menu:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.nurses = []
        self.medications = []
        self.appointments = []

    def display_menu(self):
        print("1. Добавить пациента")
        print("2. Добавить врача")
        print("3. Добавить медсестру")
        print("4. Добавить лекарство")
        print("5. Добавить назначение")
        print("6. Просмотреть список пациентов")
        print("7. Просмотреть список врачей")
        print("8. Просмотреть список медсестер")
        print("9. Просмотреть список лекарств")
        print("10. Просмотреть список назначений")
        print("11. Сохранить данные")
        print("12. Загрузить данные")
        print("13. Выход из программы")

    def add_patient(self):
        name = input("Введите имя пациента: ")
        self.patients.append(Patient(len(self.patients) + 1, name))
        
        print(f"Пациент '{name}' добавлен успешно.")

    def add_doctor(self):
        name = input("Введите имя врача: ")
        self.doctors.append(Doctor(len(self.doctors) + 1, name))
        
        print(f"Врач '{name}' добавлен успешно.")

    def add_nurse(self):
        name = input("Введите имя медсестры: ")
        self.nurses.append(Nurse(len(self.nurses) + 1, name))
        
        print(f"Медсестра '{name}' добавлена успешно.")

    def add_medications(self):
        medication_name = input("Введите название лекарства: ")
        dosage = input("Введите дозировку: ")
        self.medications.append(Medication(len(self.medications) + 1, medication_name, dosage))
        
        print(f"Лекарство '{medication_name}' добавлено успешно.")

    def add_appointment(self):
        patient_id = int(input("Введите ID пациента: "))
        doctor_id = int(input("Введите ID врача: "))
        nurse_id = int(input("Введите ID медсестры: "))
        medication_id = int(input("Введите ID лекарства: "))
        
        appointment = Appointment(len(self.appointments) + 1, patient_id, doctor_id, nurse_id, medication_id)
        self.appointments.append(appointment)
        
        print("Назначение добавлено успешно.")

    def display_patients(self):
        if not self.patients:
            print("Список пациентов пуст.")
        else:
            print("\nСписок пациентов:")
            for patient in self.patients:
                print(f"{patient.id}: {patient.name}")

    def display_doctors(self):
        if not self.doctors:
            print("Список врачей пуст.")
        else:
            print("\nСписок врачей:")
            for doctor in self.doctors:
                print(f"{doctor.id}: {doctor.name}")

    def display_nurses(self):
        if not self.nurses:
            print("Список медсестер пуст.")
        else:
            print("\nСписок медсестер:")
            for nurse in self.nurses:
                print(f"{nurse.id}: {nurse.name}")

    def display_medications(self):
        if not self.medications:
            print("Список лекарств пуст.")
        else:
            print("\nСписок лекарств:")
            for medication in self.medications:
                print(f"{medication.id}: {medication.name} (Дозировка: {medication.dosage})")

    def display_appointments(self):
        if not self.appointments:
            print("Список назначений пуст.")
        else:
            print("\nСписок назначений:")
            for appointment in self.appointments:
                print(f"{appointment.id}: Пациент {appointment.patient_id}, Врач {appointment.doctor_id}, Медсестра {appointment.nurse_id}, Лекарство {appointment.medication_id}")

    def save_data(self):
        patients = [{"id": p.id, "name": p.name} for p in self.patients]
        doctors = [{"id": d.id, "name": d.name} for d in self.doctors]
        nurses = [{"id": n.id, "name": n.name} for n in self.nurses]
        medications = [
            {"id": m.id, "name": m.name, "dosage": m.dosage}
            for m in self.medications
        ]
        appointments = [
            {
                "id": a.id,
                "patient_id": a.patient_id,
                "doctor_id": a.doctor_id,
                "nurse_id": a.nurse_id,
                "medication_id": a.medication_id
            }
            for a in self.appointments
        ]

        XmlHandler.save_to_xml(patients, doctors, nurses, medications, appointments, "/Users/kseniamalahova/Desktop/proga.lab1/f.xml")
        
        JsonHandler.save_to_json(patients, doctors, nurses, medications, appointments, "/Users/kseniamalahova/Desktop/proga.lab1/f.json")
        
        print("Данные успешно сохранены в файле f.xml и f.json.")

    def load_data(self):
        try:
            patients, doctors, nurses, medications, appointments = XmlHandler.load_from_xml("/Users/kseniamalahova/Desktop/proga.lab1/f.xml")
            self.patients = patients
            self.doctors = doctors
            self.nurses = nurses
            self.medications = medications
            self.appointments = appointments
            
            print(f"Загружено {len(self.patients)} пациентов, {len(self.doctors)} врачей, {len(self.nurses)} медсестер, {len(self.medications)} лекарств и {len(self.appointments)} назначений.")
        except FileNotFoundError:
            print("Файл f.xml не найден. Попытка загрузки из f.json...")
            try:
                patients, doctors, nurses, medications, appointments = JsonHandler.load_from_json("/Users/kseniamalahova/Desktop/proga.lab1/f.json")
                self.patients = patients
                self.doctors = doctors
                self.nurses = nurses
                self.medications = medications
                self.appointments = appointments
                
                print(f"Загружено {len(self.patients)} пациентов, {len(self.doctors)} врачей, {len(self.nurses)} медсестер, {len(self.medications)} лекарств и {len(self.appointments)} назначений.")
            except FileNotFoundError:
                print("Файлы f.xml и f.json не найдены.")


