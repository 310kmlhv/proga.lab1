import json
from models import Patient, Doctor, Nurse, Medication, Appointment

class JsonHandler:
    @staticmethod
    def save_to_json(patients, doctors, nurses, medications, appointments, filename):
        data = {
            "patients": patients,
            "doctors": doctors,
            "nurses": nurses,
            "medications": medications,
            "appointments": appointments
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=2)

        print(f"Данные успешно сохранены в файле {filename}")

    @staticmethod
    def load_from_json(filename):
        with open(filename, "r") as file:
            data = json.load(file)
        
        return data["patients"], data["doctors"], data["nurses"], data["medications"], data["appointments"]

    # @staticmethod
    # def load_from_json(filename):
    #     try:
    #         with open(filename, "r") as f:
    #             data = json.load(f)
            
    #         patients = [Patient(p["id"], p["name"]) for p in data["patients"]]
    #         doctors = [Doctor(d["id"], d["name"]) for d in data["doctors"]]
    #         nurses = [Nurse(n["id"], n["name"]) for n in data["nurses"]]
    #         medications = [
    #             Medication(m["id"], m["name"], m["dosage"])
    #             for m in data["medications"]
    #         ]
    #         appointments = [
    #             Appointment(
    #                 a["id"],
    #                 a["patient_id"],
    #                 a["doctor_id"],
    #                 a["nurse_id"],
    #                 a["medication_id"]
    #             )
    #             for a in data["appointments"]
    #         ]
            
    #         return patients, doctors, nurses, medications, appointments
    #     except FileNotFoundError:
    #         print(f"Файл {filename} не найден.")
    #         return None, None, None, None, None