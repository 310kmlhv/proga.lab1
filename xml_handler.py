import xml.etree.ElementTree as ET

def load_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    patients = []
    for patient in root.findall(".//patient"):
        patients.append({
            "id": int(patient.get("id")),
            "name": patient.get("name")
        })
    
    return patients

def save_to_xml(data, file_path):
    root = ET.Element("data")
    patients_element = ET.SubElement(root, "patients")
    
    for patient in data:
        patient_element = ET.SubElement(patients_element, "patient")
        patient_element.set("id", str(patient["id"]))
        patient_element.set("name", patient["name"])
    
    tree = ET.ElementTree(root)
    tree.write(file_path)
