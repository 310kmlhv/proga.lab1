import json
import xml.etree.ElementTree as ET
from models import Patient, Doctor, Nurse, Medication, Appointment, Disease, Treatment, Room, Bill, Payment
from xml_handler import XmlHandler
from xml_handler import XmlHandler
from json_handler import JsonHandler


class Menu:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.nurses = []
        self.medications = []
        self.appointments = []
        self.diseases = []
        self.treatments = []
        self.rooms = []
        self.bills = []
        self.payments = []

    def display_menu(self):
        print("1. Добавить пациента")
        print("2. Добавить врача")
        print("3. Добавить медсестру")
        print("4. Добавить лекарство")
        print("5. Добавить назначение")
        print("6. Добавить болезнь")
        print("7. Добавить лечение")
        print("8. Добавить палату")
        print("9. Добавить счет")
        print("10. Добавить оплату")
        print("11. Просмотреть список пациентов")
        print("12. Просмотреть список врачей")
        print("13. Просмотреть список медсестер")
        print("14. Просмотреть список лекарств")
        print("15. Просмотреть список назначений")
        print("16. Просмотреть список болезней")
        print("17. Просмотреть список лечений")
        print("18. Просмотреть список палат")
        print("19. Просмотреть список счетов")
        print("20. Просмотреть список оплат")
        print("21. Сохранить данные в xml")
        print("22. Сохранить данные в json")
        print("23. Загрузить данные из xml")
        print("24. Загрузить данные из json")
        print("25. Выход из программы")


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

    # Метод добавления болезни
    def add_disease(self):
        name = input("Введите название болезни: ")
        description = input("Введите описание болезни: ")
        self.diseases.append(Disease(len(self.diseases) + 1, name, description))
        print(f"Болезнь '{name}' добавлена успешно.")

    # Метод добавления лечения
    def add_treatment(self):
        name = input("Введите название лечения: ")
        description = input("Введите описание лечения: ")
        self.treatments.append(Treatment(len(self.treatments) + 1, name, description))
        print(f"Лечение '{name}' добавлено успешно.")

    # Метод добавления палаты
    def add_room(self):
        number = input("Введите номер палаты: ")
        type = input("Введите тип палаты: ")
        self.rooms.append(Room(len(self.rooms) + 1, number, type))
        print(f"Палата '{number}' добавлена успешно.")

    # Метод добавления счета
    def add_bill(self):
        patient_id = int(input("Введите ID пациента: "))
        amount = float(input("Введите сумму счета: "))
        self.bills.append(Bill(len(self.bills) + 1, patient_id, amount))
        print(f"Счет для пациента с ID {patient_id} на сумму {amount} добавлен.")

    # Метод добавления оплаты
    def add_payment(self):
        bill_id = int(input("Введите ID счета: "))
        amount = float(input("Введите сумму оплаты: "))
        date = input("Введите дату оплаты: ")
        self.payments.append(Payment(len(self.payments) + 1, bill_id, amount, date))
        print(f"Оплата по счету ID {bill_id} на сумму {amount} добавлена.")



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

    # Отображение болезней
    def display_diseases(self):
        if not self.diseases:
            print("Список болезней пуст.")
        else:
            print("\nСписок болезней:")
            for disease in self.diseases:
                print(f"{disease.id}: {disease.name} - {disease.description}")

    # Отображение лечений
    def display_treatments(self):
        if not self.treatments:
            print("Список лечений пуст.")
        else:
            print("\nСписок лечений:")
            for treatment in self.treatments:
                print(f"{treatment.id}: {treatment.name} - {treatment.description}")

    # Отображение палат
    def display_rooms(self):
        if not self.rooms:
            print("Список палат пуст.")
        else:
            print("\nСписок палат:")
            for room in self.rooms:
                print(f"{room.id}: {room.number} - {room.type}")

    # Отображение счетов
    def display_bills(self):
        if not self.bills:
            print("Список счетов пуст.")
        else:
            print("\nСписок счетов:")
            for bill in self.bills:
                print(f"{bill.id}: Пациент {bill.patient_id} - Сумма {bill.amount}")

    # Отображение оплат
    def display_payments(self):
        if not self.payments:
            print("Список оплат пуст.")
        else:
            print("\nСписок оплат:")
            for payment in self.payments:
                print(f"{payment.id}: Счет {payment.bill_id} - Сумма {payment.amount} - Дата {payment.date}")


    def save_data_xml(self):
        patients = [{"id": p.id, "name": p.name} for p in self.patients]
        doctors = [{"id": d.id, "name": d.name} for d in self.doctors]
        nurses = [{"id": n.id, "name": n.name} for n in self.nurses]
        medications = [{"id": m.id, "name": m.name, "dosage": m.dosage} for m in self.medications]
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
        diseases = [{"id": d.id, "name": d.name, "description": d.description} for d in self.diseases]
        treatments = [{"id": t.id, "name": t.name, "description": t.description} for t in self.treatments]
        rooms = [{"id": r.id, "number": r.number, "type": r.type} for r in self.rooms]
        bills = [{"id": b.id, "patient_id": b.patient_id, "amount": b.amount} for b in self.bills]
        payments = [{"id": p.id, "bill_id": p.bill_id, "amount": p.amount, "date": p.date} for p in self.payments]

        # Сохраняем все данные в файлы XML
        XmlHandler.save_to_xml(patients, doctors, nurses, medications, appointments, diseases, treatments, rooms, bills, payments, "/Users/kseniamalahova/Desktop/proga.lab1/f.xml")
        
        
        print("Данные успешно сохранены в файлах f.xml")

    def save_data_json(self):
        patients = [{"id": p.id, "name": p.name} for p in self.patients]
        doctors = [{"id": d.id, "name": d.name} for d in self.doctors]
        nurses = [{"id": n.id, "name": n.name} for n in self.nurses]
        medications = [{"id": m.id, "name": m.name, "dosage": m.dosage} for m in self.medications]
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
        diseases = [{"id": d.id, "name": d.name, "description": d.description} for d in self.diseases]
        treatments = [{"id": t.id, "name": t.name, "description": t.description} for t in self.treatments]
        rooms = [{"id": r.id, "number": r.number, "type": r.type} for r in self.rooms]
        bills = [{"id": b.id, "patient_id": b.patient_id, "amount": b.amount} for b in self.bills]
        payments = [{"id": p.id, "bill_id": p.bill_id, "amount": p.amount, "date": p.date} for p in self.payments]

        # Сохраняем все данные в файлы JSON
        
        JsonHandler.save_to_json(patients, doctors, nurses, medications, appointments, diseases, treatments, rooms, bills, payments, "/Users/kseniamalahova/Desktop/proga.lab1/f.json")
        
        print("Данные успешно сохранены в файлах f.json.")

    def load_data_xml(self):
        try:
            patients, doctors, nurses, medications, appointments, diseases, treatments, rooms, bills, payments = XmlHandler.load_from_xml("/Users/kseniamalahova/Desktop/proga.lab1/f.xml")
            self.patients = patients
            self.doctors = doctors
            self.nurses = nurses
            self.medications = medications
            self.appointments = appointments
            self.diseases = diseases
            self.treatments = treatments
            self.rooms = rooms
            self.bills = bills
            self.payments = payments
            
            print(f"Загружено {len(self.patients)} пациентов, {len(self.doctors)} врачей, {len(self.nurses)} медсестер, {len(self.medications)} лекарств, {len(self.appointments)} назначений, {len(self.diseases)} болезней, {len(self.treatments)} лечений, {len(self.rooms)} палат, {len(self.bills)} счетов и {len(self.payments)} оплат.")
        except FileNotFoundError:
            print("Файл f.xml не найден.")
    
    def load_data_json(self):
        try:
            patients, doctors, nurses, medications, appointments, diseases, treatments, rooms, bills, payments = JsonHandler.load_from_json("/Users/kseniamalahova/Desktop/proga.lab1/f.json")
            self.patients = patients
            self.doctors = doctors
            self.nurses = nurses
            self.medications = medications
            self.appointments = appointments
            self.diseases = diseases
            self.treatments = treatments
            self.rooms = rooms
            self.bills = bills
            self.payments = payments

            print(f"Загружено {len(self.patients)} пациентов, {len(self.doctors)} врачей, {len(self.nurses)} медсестер, {len(self.medications)} лекарств, {len(self.appointments)} назначений, {len(self.diseases)} болезней, {len(self.treatments)} лечений, {len(self.rooms)} палат, {len(self.bills)} счетов и {len(self.payments)} оплат.")
        except FileNotFoundError:
            print("Файлы f.xml и f.json не найдены.")