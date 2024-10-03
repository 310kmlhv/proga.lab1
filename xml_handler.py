import xml.etree.ElementTree as ET
from models import Patient, Doctor, Nurse, Medication, Appointment

class XmlHandler:
    @staticmethod
    def save_to_xml(patients, doctors, nurses, medications, appointments, filename):
        root = ET.Element("hospital_data")
        
        patient_element = ET.SubElement(root, "patients")
        for patient in patients:
            patient_subelement = ET.SubElement(patient_element, "patient")
            ET.SubElement(patient_subelement, "id").text = str(patient["id"])
            ET.SubElement(patient_subelement, "name").text = patient["name"]
        
        doctor_element = ET.SubElement(root, "doctors")
        for doctor in doctors:
            doctor_subelement = ET.SubElement(doctor_element, "doctor")
            ET.SubElement(doctor_subelement, "id").text = str(doctor["id"])
            ET.SubElement(doctor_subelement, "name").text = doctor["name"]
        
        nurse_element = ET.SubElement(root, "nurses")
        for nurse in nurses:
            nurse_subelement = ET.SubElement(nurse_element, "nurse")
            ET.SubElement(nurse_subelement, "id").text = str(nurse["id"])
            ET.SubElement(nurse_subelement, "name").text = nurse["name"]
        
        medication_element = ET.SubElement(root, "medications")
        for medication in medications:
            medication_subelement = ET.SubElement(medication_element, "medication")
            ET.SubElement(medication_subelement, "id").text = str(medication["id"])
            ET.SubElement(medication_subelement, "name").text = medication["name"]
            ET.SubElement(medication_subelement, "dosage").text = str(medication["dosage"])
        
        appointment_element = ET.SubElement(root, "appointments")
        for appointment in appointments:
            appointment_subelement = ET.SubElement(appointment_element, "appointment")
            ET.SubElement(appointment_subelement, "id").text = str(appointment["id"])
            ET.SubElement(appointment_subelement, "patient_id").text = str(appointment["patient_id"])
            ET.SubElement(appointment_subelement, "doctor_id").text = str(appointment["doctor_id"])
            ET.SubElement(appointment_subelement, "nurse_id").text = str(appointment["nurse_id"])
            ET.SubElement(appointment_subelement, "medication_id").text = str(appointment["medication_id"])
        
        tree = ET.ElementTree(root)
        tree.write(filename)
        
        print("Данные успешно сохранены в файле:", filename)

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

            return patients, doctors, nurses, medications, appointments
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
            return None, None, None, None, None