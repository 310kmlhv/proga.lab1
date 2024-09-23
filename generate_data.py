import json
from datetime import date
from media import Hospital, Doctor, Patient, Diagnosis, Treatment, Medication, Analysis, Surgery, Report, Equipment

def generate_hospital(name):
    return Hospital(name)

def generate_doctor(name, specialty, experience):
    return Doctor(name, specialty, experience)

def generate_patient(name, age, diagnosis):
    return Patient(name, name)  # We'll add diagnoses later

def generate_diagnosis(name):
    return Diagnosis(1, name)  # Using a fixed ID for simplicity

def generate_treatment(patient, doctor, diagnosis, start_date):
    return Treatment(1, patient, doctor, diagnosis, start_date)

def generate_medications(name, dosage_form, dose, frequency, duration):
    return Medication(1, name, dosage_form, dose, frequency, duration)

def generate_analysis(patient, doctor, analysis_type, result):
    return Analysis(1, patient, doctor, analysis_type, result)

def generate_equipment(name, equipment_type):
    return Equipment(1, name, equipment_type)

def generate_surgery(patient, anesthesiologist, surgeon, operation_date, status):
    return Surgery(1, patient, anesthesiologist, surgeon, operation_date, status)

def generate_report(surgery, author, creation_date, summary, observations):
    return Report(1, surgery, author, creation_date, summary, observations)

# Generate sample data
hospitals = [
    generate_hospital("Central Hospital"),
    generate_hospital("University Clinic")
]

doctors = [
    generate_doctor("Dr. Smith", "Cardiology", 15),
    generate_doctor("Dr. Johnson", "Neurology", 12),
    generate_doctor("Dr. Brown", "Oncology", 20)
]

patients = [
    generate_patient("Alice Johnson", 35, "Hypertension"),
    generate_patient("Bob Smith", 42, "Diabetes"),
    generate_patient("Charlie Davis", 28, "Asthma")
]

diagnoses = [
    generate_diagnosis("Hypertension"),
    generate_diagnosis("Diabetes"),
    generate_diagnosis("Asthma")
]

treatments = [
    generate_treatment(patients[0], doctors[0], diagnoses[0], date.today())
]

medications = [
    generate_medications("Lisinopril", "Tablets", "10mg", "Once daily", "30 days")
]

analyses = [
    generate_analysis(patients[1], doctors[1], "Blood test", "Normal")
]

equipment = [
    generate_equipment("ECG Machine", "Diagnostic")
]

surgeries = [
    generate_surgery(patients[2], doctors[2], doctors[2], date.today(), "Completed")
]

reports = [
    generate_report(surgeries[0], doctors[2], date.today(), "Successful surgery for appendicitis", "No complications")
]

# Save data to JSON file
data_json = {
    "hospitals": [hospital.to_dict() for hospital in hospitals],
    "doctors": [doctor.to_dict() for doctor in doctors],
    "patients": [patient.to_dict() for patient in patients],
    "diagnoses": [diagnosis.to_dict() for diagnosis in diagnoses],
    "treatments": [treatment.to_dict() for treatment in treatments],
    "medications": [medication.to_dict() for medication in medications],
    "analyses": [analysis.to_dict() for analysis in analyses],
    "equipment": [equipment_item.to_dict() for equipment_item in equipment],
    "surgeries": [surgery.to_dict() for surgery in surgeries],
    "reports": [report.to_dict() for report in reports]
}

with open('data.json', 'w') as f:
    json.dump(data_json, f, indent=4)

# Import xml.etree.ElementTree module
import xml.etree.ElementTree as ET

# Save data to XML file
root = ET.Element('data')

for hospital in hospitals:
    hospital_element = ET.SubElement(root, 'hospital')
    for key, value in hospital.__dict__.items():
        child = ET.SubElement(hospital_element, key)
        child.text = str(value)

for doctor in doctors:
    doctor_element = ET.SubElement(root, 'doctor')
    for key, value in doctor.__dict__.items():
        child = ET.SubElement(doctor_element, key)
        child.text = str(value)

for patient in patients:
    patient_element = ET.SubElement(root, 'patient')
    for key, value in patient.__dict__.items():
        child = ET.SubElement(patient_element, key)
        child.text = str(value)

for diagnosis in diagnoses:
    diagnosis_element = ET.SubElement(root, 'diagnosis')
    for key, value in diagnosis.__dict__.items():
        child = ET.SubElement(diagnosis_element, key)
        child.text = str(value)

for treatment in treatments:
    treatment_element = ET.SubElement(root, 'treatment')
    for key, value in treatment.__dict__.items():
        child = ET.SubElement(treatment_element, key)
        child.text = str(value)

for medication in medications:
    medication_element = ET.SubElement(root, 'medication')
    for key, value in medication.__dict__.items():
        child = ET.SubElement(medication_element, key)
        child.text = str(value)

for analysis in analyses:
    analysis_element = ET.SubElement(root, 'analysis')
    for key, value in analysis.__dict__.items():
        child = ET.SubElement(analysis_element, key)
        child.text = str(value)

for equipment_item in equipment:
    equipment_element = ET.SubElement(root, 'equipment')
    for key, value in equipment_item.__dict__.items():
        child = ET.SubElement(equipment_element, key)
        child.text = str(value)

for surgery in surgeries:
    surgery_element = ET.SubElement(root, 'surgery')
    for key, value in surgery.__dict__.items():
        child = ET.SubElement(surgery_element, key)
        child.text = str(value)

for report in reports:
    report_element = ET.SubElement(root, 'report')
    for key, value in report.__dict__.items():
        child = ET.SubElement(report_element, key)
        child.text = str(value)

# Add indentation to the XML structure
ET.indent(root, space='\t', style={'xml_declaration': True})

# Write the XML tree to a file
ET.ElementTree(root).write('data.xml', encoding='unicode', xml_declaration=True)
