import xml.etree.ElementTree as ET

# Функция для добавления отступов (pretty-print)
def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not subelem.tail or not subelem.tail.strip():
            subelem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def save_to_xml(data, filename):
    root = ET.Element('data')

    hospitals = ET.SubElement(root,'hospitals')
    for hospital in data['hospitals']:
        hospital_element = ET.SubElement(hospitals,'hospital')
        for key, value in hospital.items():
            child = ET.SubElement(hospital_element, key)
            child.text = str(value)

    doctors = ET.SubElement(root, 'doctors')
    for doctor in data['doctors']:
        doctor_element = ET.SubElement(doctors,'doctor')
        for key, value in doctor.items():
            child = ET.SubElement(doctor_element, key)
            child.text = str(value)

    patients = ET.SubElement(root, 'patients')
    for patient in data['patients']:
        patient_element = ET.SubElement(patients,'patient')
        for key, value in patient.items():
            child = ET.SubElement(patient_element, key)
            child.text = str(value)

    diagnoses = ET.SubElement(root, 'diagnoses')
    for diagnosis in data['diagnoses']:
        diagnosis_element = ET.SubElement(diagnoses,'diagnosis')
        for key, value in diagnosis.items():
            child = ET.SubElement(diagnosis_element, key)
            child.text = str(value)

    treatments = ET.SubElement(root, 'treatments')
    for treatment in data['treatments']:
        treatment_element = ET.SubElement(treatments,'treatment')
        for key, value in treatment.items():
            child = ET.SubElement(treatment_element, key)
            child.text = str(value)

    medications = ET.SubElement(root, 'medications')
    for medication in data['medications']:
        medication_element = ET.SubElement(medications,'medication')
        for key, value in medication.items():
            child = ET.SubElement(medication_element, key)
            child.text = str(value)

    analyses = ET.SubElement(root, 'analyses')
    for analysis in data['analyses']:
        analysis_element = ET.SubElement(analyses,'analysis')
        for key, value in analysis.items():
            child = ET.SubElement(analysis_element, key)
            child.text = str(value)

    equipment = ET.SubElement(root, 'equipment')
    for equipment_item in data['equipment']:
        equipment_element = ET.SubElement(equipment,'equipment')
        for key, value in equipment_item.items():
            child = ET.SubElement(equipment_element, key)
            child.text = str(value)

    surgeries = ET.SubElement(root, 'surgeries')
    for surgery in data['surgeries']:
        surgery_element = ET.SubElement(surgeries,'surgery')
        for key, value in surgery.items():
            child = ET.SubElement(surgery_element, key)
            child.text = str(value)

    reports = ET.SubElement(root, 'reports')
    for report in data['reports']:
        report_element = ET.SubElement(reports,'report')
        for key, value in report.items():
            child = ET.SubElement(report_element, key)
            child.text