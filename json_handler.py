import json
from models import Patient, Doctor, Nurse, Medication, Appointment, Disease, Treatment, Room, Bill, Payment

class JsonHandler:
    @staticmethod
    def save_to_json(patients, doctors, nurses, medications, appointments, diseases, treatments, rooms, bills, payments, filename):
        data = {
            "patients": patients,
            "doctors": doctors,
            "nurses": nurses,
            "medications": medications,
            "appointments": appointments,
            "diseases": diseases,
            "treatments": treatments,
            "rooms": rooms,
            "bills": bills,
            "payments": payments
        }

        # Сохраняем данные в JSON формате с отступами для удобства
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)

        print(f"Данные успешно сохранены в файле {filename}")

    @staticmethod
    def load_from_json(filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            
            # Возвращаем все сущности из загруженного JSON
            return (
                data["patients"],
                data["doctors"],
                data["nurses"],
                data["medications"],
                data["appointments"],
                data["diseases"],
                data["treatments"],
                data["rooms"],
                data["bills"],
                data["payments"]
            )
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
            return None, None, None, None, None, None, None, None, None, None
