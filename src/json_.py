import json

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"hospitals": [], "doctors": [], "patients": [], "diagnoses": [], "treatments": [], "medications": [], "analyses": [], "equipment": [], "surgeries": [], "reports": []}

def add_hospital(data, hospital):
    data['hospitals'].append(hospital.to_dict())

def add_doctor(data, doctor):
    data['doctors'].append(doctor.to_dict())

def add_patient(data, patient):
    data['patients'].append(patient.to_dict())

def add_diagnosis(data, diagnosis):
    data['diagnoses'].append(diagnosis.to_dict())

def add_treatment(data, treatment):
    data['treatments'].append(treatment.to_dict())

def add_medications(data, medication):
    data['medications'].append(medication.to_dict())

def add_analysis(data, analysis):
    data['analyses'].append(analysis.to_dict())

def add_equipment(data, equipment):
    data['equipment'].append(equipment.to_dict())

def add_surgery(data, surgery):
    data['surgeries'].append(surgery.to_dict())

def add_report(data, report):
    data['reports'].append(report.to_dict())

def delete_hospital(data, name):
    upd = [hosp for hosp in data['hospitals'] if hosp['name'] != name]
    data['hospitals'] = upd

def delete_doctor(data, name):
    upd = [doc for doc in data['doctors'] if doc['name'] != name]
    data['doctors'] = upd

def delete_patient(data, name):
    upd = [pat for pat in data['patients'] if pat['name'] != name]
    data['patients'] = upd

def delete_diagnosis(data, name):
    upd = [diag for diag in data['diagnoses'] if diag['name'] != name]
    data['diagnoses'] = upd

def delete_treatment(data, id):
    upd = [treat for treat in data['treatments'] if treat['id'] != id]
    data['treatments'] = upd

def delete_medications(data, name):
    upd = [med for med in data['medications'] if med['name'] != name]
    data['medications'] = upd

def delete_analysis(data, id):
    upd = [ana for ana in data['analyses'] if ana['id'] != id]
    data['analyses'] = upd

def delete_equipment(data, name):
    upd = [eq for eq in data['equipment'] if eq['name'] != name]
    data['equipment'] = upd

def delete_surgery(data, id):
    upd = [surg for surg in data['surgeries'] if surg['id'] != id]
    data['surgeries'] = upd

def delete_report(data, id):
    upd = [rep for rep in data['reports'] if rep['id'] != id]
    data['reports'] = upd
