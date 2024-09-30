import json
import xmltodict
import xml.etree.ElementTree as ET

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
        self.patients.append({"id": len(self.patients) + 1, "name": name})
        
        print(f"Пациент '{name}' добавлен успешно.")

    def add_doctor(self):
        name = input("Введите имя врача: ")
        self.doctors.append({"id": len(self.doctors) + 1, "name": name})
        
        print(f"Врач '{name}' добавлен успешно.")

    def add_nurse(self):
        name = input("Введите имя медсестры: ")
        self.nurses.append({"id": len(self.nurses) + 1, "name": name})
        
        print(f"Медсестра '{name}' добавлена успешно.")

    def add_medications(self):
        medication_name = input("Введите название лекарства: ")
        dosage = input("Введите дозировку: ")
        self.medications.append({
            "id": len(self.medications) + 1,
            "name": medication_name,
            "dosage": dosage
        })
        
        print(f"Лекарство '{medication_name}' добавлено успешно.")

    def add_appointment(self):
        patient_id = int(input("Введите ID пациента: "))
        doctor_id = int(input("Введите ID врача: "))
        nurse_id = int(input("Введите ID медсестры: "))
        medication_id = int(input("Введите ID лекарства: "))
        
        appointment = {
            "id": len(self.appointments) + 1,
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "nurse_id": nurse_id,
            "medication_id": medication_id
        }
        self.appointments.append(appointment)
        
        print("Назначение добавлено успешно.")

    def display_patients(self):
        if not self.patients:
            print("Список пациентов пуст.")
        else:
            print("\nСписок пациентов:")
            for patient in self.patients:
                print(f"{patient['id']}: {patient['name']}")

    def display_doctors(self):
        if not self.doctors:
            print("Список врачей пуст.")
        else:
            print("\nСписок врачей:")
            for doctor in self.doctors:
                print(f"{doctor['id']}: {doctor['name']}")

    def display_nurses(self):
        if not self.nurses:
            print("Список медсестер пуст.")
        else:
            print("\nСписок медсестер:")
            for nurse in self.nurses:
                print(f"{nurse['id']}: {nurse['name']}")

    def display_medications(self):
        if not self.medications:
            print("Список лекарств пуст.")
        else:
            print("\nСписок лекарств:")
            for medication in self.medications:
                print(f"{medication['id']}: {medication['name']} (Дозировка: {medication['dosage']})")

    def display_appointments(self):
        if not self.appointments:
            print("Список назначений пуст.")
        else:
            print("\nСписок назначений:")
            for appointment in self.appointments:
                print(f"{appointment['id']}: Пациент {appointment['patient_id']}, Врач {appointment['doctor_id']}, Медсестра {appointment['nurse_id']}, Лекарство {appointment['medication_id']}")
#####

    def save_data(self):
        root = ET.Element("data")
        patients_element = ET.SubElement(root, "patients")
        doctors_element = ET.SubElement(root, "doctors")
        nurses_element = ET.SubElement(root, "nurses")
        medications_element = ET.SubElement(root, "medications")
        appointments_element = ET.SubElement(root, "appointments")
        
        for patient in self.patients:
            patient_element = ET.SubElement(patients_element, "patient")
            patient_element.text = patient["name"].encode('utf-8').decode('utf-8')
        
        for doctor in self.doctors:
            doctor_element = ET.SubElement(doctors_element, "doctor")
            doctor_element.text = doctor["name"].encode('utf-8').decode('utf-8')
        
        for nurse in self.nurses:
            nurse_element = ET.SubElement(nurses_element, "nurse")
            nurse_element.text = nurse["name"].encode('utf-8').decode('utf-8')
        
        for medication in self.medications:
            medication_element = ET.SubElement(medications_element, "medication")
            medication_element.set("dosage", medication["dosage"])
            medication_element.text = medication["name"].encode('utf-8').decode('utf-8')
        
        for appointment in self.appointments:
            appointment_element = ET.SubElement(appointments_element, "appointment")
            appointment_element.set("patient_id", str(appointment["patient_id"]))
            appointment_element.set("doctor_id", str(appointment["doctor_id"]))
            appointment_element.set("nurse_id", str(appointment["nurse_id"]))
            appointment_element.set("medication_id", str(appointment["medication_id"]))

        tree = ET.ElementTree(root)
        tree.write("/Users/kseniamalahova/Desktop/proga.lab1/f.xml", encoding='utf-8', xml_declaration=True)
        
        json_content = {
            "patients": [{"name": p["name"]} for p in self.patients],
            "doctors": [{"name": d["name"]} for d in self.doctors],
            "nurses": [{"name": n["name"]} for n in self.nurses],
            "medications": [{"name": m["name"], "dosage": m["dosage"]} for m in self.medications],
            "appointments": [{"patient_id": a["patient_id"], "doctor_id": a["doctor_id"], "nurse_id": a["nurse_id"], "medication_id": a["medication_id"]} for a in self.appointments]
        }
        with open("/Users/kseniamalahova/Desktop/proga.lab1/f.json", "w", encoding='utf-8') as f:
            json.dump(json_content, f, indent=2, ensure_ascii=False)

    
    def load_data(self):
        try:
            tree = ET.parse("/Users/kseniamalahova/Desktop/proga.lab1/f.xml")
            root = tree.getroot()
            
            self.patients = []
            for patient in root.findall(".//patient"):
                self.patients.append({
                    "name": patient.text.encode('utf-8').decode('utf-8')
                })

            self.doctors = []
            for doctor in root.findall(".//doctor"):
                self.doctors.append({
                    "name": doctor.text.encode('utf-8').decode('utf-8')
                })

            self.nurses = []
            for nurse in root.findall(".//nurse"):
                self.nurses.append({
                    "name": nurse.text.encode('utf-8').decode('utf-8')
                })

            self.medications = []
            for medication in root.findall(".//medication"):
                self.medications.append({
                    "name": medication.text.encode('utf-8').decode('utf-8'),
                    "dosage": medication.get("dosage")
                })

            self.appointments = []
            for appointment in root.findall(".//appointment"):
                self.appointments.append({
                    "patient_id": int(appointment.get("patient_id")),
                    "doctor_id": int(appointment.get("doctor_id")),
                    "nurse_id": int(appointment.get("nurse_id")),
                    "medication_id": int(appointment.get("medication_id"))
                })

            print(f"Загружено {len(self.patients)} пациентов, {len(self.doctors)} врачей, {len(self.nurses)} медсестер, {len(self.medications)} лекарств и {len(self.appointments)} назначений.")
        except FileNotFoundError:
            print("Файл f.xml не найден. Попытка загрузки из f.json...")
            try:
                with open("/Users/kseniamalahova/Desktop/proga.lab1/f.json", "r") as f:
                    json_content = json.load(f)
                
                self.patients = json_content["patients"]
                self.doctors = json_content["doctors"]
                self.nurses = json_content["nurses"]
                self.medications = json_content["medications"]
                self.appointments = json_content["appointments"]
                
                print(f"Загружено {len(self.patients)} пациентов, {len(self.doctors)} врачей, {len(self.nurses)} медсестер, {len(self.medications)} лекарств и {len(self.appointments)} назначений.")
            except FileNotFoundError:
                print("Файлы f.xml и f.json не найдены.")

    # ... (остальной код остается без изменений)
    # ... (остальной код остается без изменений)
    # def save_data(self):
    #     xml_content = "<data><patients>" + "".join([f"<patient id='{p['id']}' name='{p['name']}'/>" for p in self.patients]) + "</patients></data>"
    #     json_content = {"patients": [{"id": p["id"], "name": p["name"]} for p in self.patients]}
        
    #     with open("/Users/kseniamalahova/Desktop/proga.lab1/f.xml", "w") as f:
    #         f.write(xml_content)
        
    #     with open("/Users/kseniamalahova/Desktop/proga.lab1/f.json", "w") as f:
    #         json.dump(json_content, f, indent=2)

    # def load_data(self):
    #     with open("/Users/kseniamalahova/Desktop/proga.lab1/f.xml", "r") as f:
    #         xml_content = f.read()

    #     with open("/Users/kseniamalahova/Desktop/proga.lab1/f.json", "r") as f:
    #         json_content = json.load(f)

    #     self.patients = []
    #     for patient in xmltodict.parse(xml_content)["data"]["patients"]:
    #         self.patients.append({"id": int(patient["id"]), "name": patient["name"]})

    #     print(f"Загружено {len(self.patients)} пациента(ов).")