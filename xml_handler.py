import xml.etree.ElementTree as ET
from models import Patient, Doctor, Nurse, Medication, Appointment, Disease, Treatment, Room, Bill, Payment

class XmlHandler:
    @staticmethod
    def save_to_xml(patients, doctors, nurses, medications, appointments, diseases, treatments, rooms, bills, payments, filename):
        root = ET.Element("hospital_data")

        # Patients
        patient_element = ET.SubElement(root, "patients")
        for patient in patients:
            patient_subelement = ET.SubElement(patient_element, "patient")
            ET.SubElement(patient_subelement, "id").text = str(patient["id"])
            ET.SubElement(patient_subelement, "name").text = patient["name"]

        # Doctors
        doctor_element = ET.SubElement(root, "doctors")
        for doctor in doctors:
            doctor_subelement = ET.SubElement(doctor_element, "doctor")
            ET.SubElement(doctor_subelement, "id").text = str(doctor["id"])
            ET.SubElement(doctor_subelement, "name").text = doctor["name"]

        # Nurses
        nurse_element = ET.SubElement(root, "nurses")
        for nurse in nurses:
            nurse_subelement = ET.SubElement(nurse_element, "nurse")
            ET.SubElement(nurse_subelement, "id").text = str(nurse["id"])
            ET.SubElement(nurse_subelement, "name").text = nurse["name"]

        # Medications
        medication_element = ET.SubElement(root, "medications")
        for medication in medications:
            medication_subelement = ET.SubElement(medication_element, "medication")
            ET.SubElement(medication_subelement, "id").text = str(medication["id"])
            ET.SubElement(medication_subelement, "name").text = medication["name"]
            ET.SubElement(medication_subelement, "dosage").text = str(medication["dosage"])

        # Appointments
        appointment_element = ET.SubElement(root, "appointments")
        for appointment in appointments:
            appointment_subelement = ET.SubElement(appointment_element, "appointment")
            ET.SubElement(appointment_subelement, "id").text = str(appointment["id"])
            ET.SubElement(appointment_subelement, "patient_id").text = str(appointment["patient_id"])
            ET.SubElement(appointment_subelement, "doctor_id").text = str(appointment["doctor_id"])
            ET.SubElement(appointment_subelement, "nurse_id").text = str(appointment["nurse_id"])
            ET.SubElement(appointment_subelement, "medication_id").text = str(appointment["medication_id"])

        # Diseases
        disease_element = ET.SubElement(root, "diseases")
        for disease in diseases:
            disease_subelement = ET.SubElement(disease_element, "disease")
            ET.SubElement(disease_subelement, "id").text = str(disease["id"])
            ET.SubElement(disease_subelement, "name").text = disease["name"]
            ET.SubElement(disease_subelement, "description").text = disease["description"]

        # Treatments
        treatment_element = ET.SubElement(root, "treatments")
        for treatment in treatments:
            treatment_subelement = ET.SubElement(treatment_element, "treatment")
            ET.SubElement(treatment_subelement, "id").text = str(treatment["id"])
            ET.SubElement(treatment_subelement, "name").text = treatment["name"]
            ET.SubElement(treatment_subelement, "description").text = treatment["description"]

        # Rooms
        room_element = ET.SubElement(root, "rooms")
        for room in rooms:
            room_subelement = ET.SubElement(room_element, "room")
            ET.SubElement(room_subelement, "id").text = str(room["id"])
            ET.SubElement(room_subelement, "number").text = room["number"]
            ET.SubElement(room_subelement, "type").text = room["type"]

        # Bills
        bill_element = ET.SubElement(root, "bills")
        for bill in bills:
            bill_subelement = ET.SubElement(bill_element, "bill")
            ET.SubElement(bill_subelement, "id").text = str(bill["id"])
            ET.SubElement(bill_subelement, "patient_id").text = str(bill["patient_id"])
            ET.SubElement(bill_subelement, "amount").text = str(bill["amount"])

        # Payments
        payment_element = ET.SubElement(root, "payments")
        for payment in payments:
            payment_subelement = ET.SubElement(payment_element, "payment")
            ET.SubElement(payment_subelement, "id").text = str(payment["id"])
            ET.SubElement(payment_subelement, "bill_id").text = str(payment["bill_id"])
            ET.SubElement(payment_subelement, "amount").text = str(payment["amount"])
            ET.SubElement(payment_subelement, "date").text = payment["date"]

        # Формируем отступы перед записью
        XmlHandler.indent(root)

        tree = ET.ElementTree(root)
        tree.write(filename)

        print("Данные успешно сохранены в файле:", filename)

    @staticmethod
    def indent(elem, level=0):
        """Функция для добавления отступов (pretty-print)"""
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                XmlHandler.indent(subelem, level + 1)
            if not subelem.tail or not subelem.tail.strip():
                subelem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    @staticmethod
    def load_from_xml(filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()

            patients = []
            doctors = []
            nurses = []
            medications = []
            appointments = []
            diseases = []
            treatments = []
            rooms = []
            bills = []
            payments = []

            for patient in root.findall(".//patient"):
                patients.append(Patient(int(patient.find("id").text), patient.find("name").text))

            for doctor in root.findall(".//doctor"):
                doctors.append(Doctor(int(doctor.find("id").text), doctor.find("name").text))

            for nurse in root.findall(".//nurse"):
                nurses.append(Nurse(int(nurse.find("id").text), nurse.find("name").text))

            for medication in root.findall(".//medication"):
                medications.append(Medication(
                    int(medication.find("id").text),
                    medication.find("name").text,
                    medication.find("dosage").text
                ))

            for appointment in root.findall(".//appointment"):
                appointments.append(Appointment(
                    int(appointment.find("id").text),
                    int(appointment.find("patient_id").text),
                    int(appointment.find("doctor_id").text),
                    int(appointment.find("nurse_id").text),
                    int(appointment.find("medication_id").text)
                ))

            for disease in root.findall(".//disease"):
                diseases.append(Disease(
                    int(disease.find("id").text),
                    disease.find("name").text,
                    disease.find("description").text
                ))

            for treatment in root.findall(".//treatment"):
                treatments.append(Treatment(
                    int(treatment.find("id").text),
                    treatment.find("name").text,
                    treatment.find("description").text
                ))

            for room in root.findall(".//room"):
                rooms.append(Room(
                    int(room.find("id").text),
                    room.find("number").text,
                    room.find("type").text
                ))

            for bill in root.findall(".//bill"):
                bills.append(Bill(
                    int(bill.find("id").text),
                    int(bill.find("patient_id").text),
                    float(bill.find("amount").text)
                ))

            for payment in root.findall(".//payment"):
                payments.append(Payment(
                    int(payment.find("id").text),
                    int(payment.find("bill_id").text),
                    float(payment.find("amount").text),
                    payment.find("date").text
                ))

            return patients, doctors, nurses, medications, appointments, diseases, treatments, rooms, bills, payments
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
            return None, None, None, None, None, None, None, None, None, None
