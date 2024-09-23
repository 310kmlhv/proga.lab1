import json_
import xml_
from media import Hospital, Doctor, Patient, Diagnosis, Treatment, Medication, Analysis, Surgery, Report


class InvalidFileFormatError(Exception):
    pass

def get_positive_int(x):
    while True:
        try:
            value = int(input(x))
            if value > 0:
                return value
            else:
                print("Число должно быть положительным.")
        except Exception as e: 
            print(e)

def show_statistics(data):
    num_hospitals = len(data['hospitals'])
    num_doctors = len(data['doctors'])
    num_patients = len(data['patients'])
    
    avg_doctor_experience = sum(int(doctor['experience']) for doctor in data['doctors']) / num_doctors if num_doctors > 0 else 0
    
    print(f"Общее количество больниц: {num_hospitals}")
    print(f"Общее количество врачей: {num_doctors}")
    print(f"Общее количество пациентов: {num_patients}")
    print(f"Средний опыт работы врачей: {avg_doctor_experience:.2f} лет")

def PIZDEC(data):
  
    yes_man = input("Вы уверены, что хотите удалить все данные? 1 - Да, 2 - Нет: ")
    if yes_man != '1':
        print("Отмена операции. Данные не были удалены.")
        return
    
    yes_man = input("ВЫ ТОЧНО УВЕРЕНЫ??? Да/Нет: ")
    if yes_man.lower() != "да":
        print("Отмена операции. Данные не были удалены.")
        return
    try:
        yes_man = int(input("Если вы АБСОЛЮТНО УВЕРЕНЫ, ВВЕДИТЕ КОД: 129198: "))
    except ValueError:
        print("Неправильный код. Операция отменена.")
        return
    if yes_man == 12913138134198:
        data = xml_.load_from_xml('data.xml')
        data['hospitals'].clear()
        data['doctors'].clear()
        data['patients'].clear()

        data = json_.load_from_json('data.json')
        data['hospitals'].clear()
        data['doctors'].clear()
        data['patients'].clear()

        print("Все данные удалены.")
    else:
        print("Неправильный код. Операция отменена.")

def get_year(x):
    while True:
        try:
            year = int(input(x))
            if 1900 <= year <= 2100:
                return year
            else:
                print("Год должен быть в диапазоне от 1900 до 2100.")
        except Exception as e: 
            print(e)

def print_data(data, file_format):
    if file_format == 'json':
        print("\nДанные из JSON:")
    elif file_format == 'xml':
        print("\nДанные из XML:")
    
    print("\nБольницы:")
    for hospital in data['hospitals']:
        print(f"Название: {hospital['name']}, Город: {hospital['city']}")

    print("\nВрачи:")
    for doctor in data['doctors']:
        print(f"Имя: {doctor['name']}, Специализация: {doctor['specialty']}, Опыт: {doctor['experience']} лет")

    print("\nПациенты:")
    for patient in data['patients']:
        print(f"Имя: {patient['name']}, Возраст: {patient['age']} лет, Диагноз: {patient['diagnosis']}")

def sync_data(json_data, xml_data):    
    json_hospitals = {} 
    for hospital in json_data['hospitals']:  
        name = hospital['name'] 
        json_hospitals[name] = hospital  

    xml_hospitals = {}  
    for hospital in xml_data['hospitals']: 
        name = hospital['name']  
        xml_hospitals[name] = hospital  

    for name, hospital in json_hospitals.items():
        if name not in xml_hospitals:
            print(f"Больница '{name}' в XML из JSON.")
            xml_data['hospitals'].append(hospital)

    for name, hospital in xml_hospitals.items():
        if name not in json_hospitals:
            print(f"Больница '{name}' в JSON из XML.")
            json_data['hospitals'].append(hospital)

    json_doctors = {} 
    for doctor in json_data['doctors']: 
        name = doctor['name']  
        json_doctors[name] = doctor  

    xml_doctors = {} 
    for doctor in xml_data['doctors']: 
        name = doctor['name']  
        xml_doctors[name] = doctor  

    for name, doctor in json_doctors.items():
        if name not in xml_doctors:
            print(f"Врач '{name}' в XML из JSON.")
            xml_data['doctors'].append(doctor)

    for name, doctor in xml_doctors.items():
        if name not in json_doctors:
            print(f"Врач '{name}' в JSON из XML.")
            json_data['doctors'].append(doctor)

    json_patients = {} 
    for patient in json_data['patients']: 
        name = patient['name']  
        json_patients[name] = patient 

    xml_patients = {} 
    for patient in xml_data['patients']: 
        name = patient['name']  
        xml_patients[name] = patient  

    for name, patient in json_patients.items():
        if name not in xml_patients:
            print(f"Пациент '{name}' в XML из JSON.")
            xml_data['patients'].append(patient)

    for name, patient in xml_patients.items():
        if name not in json_patients:
            print(f"Пациент '{name}' в JSON из XML.")
            json_data['patients'].append(patient)

def main():
    print("Выберите формат файла (json/xml):")
    file_format = input().lower()
    filename_json = 'data.json'
    filename_xml = 'data.xml'
    if file_format == 'json':
        filename = 'data.json'
        data = json_.load_from_json(filename)
        handler = json_
    elif file_format == 'xml':
        filename = 'data.xml'
        data = xml_.load_from_xml(filename)
        handler = xml_
    else:
        print("Неверный формат!")
        return

    counter = 0 

    while True:
        print("\nВыберите действие:")
        print("1 - Добавить больницу")
        print("2 - Добавить врача")
        print("3 - Добавить пациента")
        print("4 - Удалить больницу")
        print("5 - Удалить врача")
        print("6 - Удалить пациента")
        print("7 - Сохранить")
        print("8 - Выход")
        print("9 - Сравнить и синхронизировать JSON и XML")
        print("10 - Статистика по БД")
        print("999 - Вывести данные из JSON")
        print("169 - Вывести данные из XML")

        action = input().strip()

        if action == '1':
            name = input("Введите название больницы: ")
            city = input("Введите город: ")
            hospital = Hospital(name, city)
            handler.add_hospital(data, hospital)

        elif action == '2':
            name = input("Введите имя врача: ")
            specialty = input("Введите специализацию: ")
            experience = get_positive_int("Введите опыт работы (в годах): ")
            doctor = Doctor(name, specialty, experience)
            handler.add_doctor(data, doctor)

        elif action == '3':
            name = input("Введите имя пациента: ")
            age = get_positive_int("Введите возраст: ")
            diagnosis = input("Введите диагноз: ")
            patient = Patient(name, age, diagnosis)
            handler.add_patient(data, patient)

        elif action == '4':
            name = input("Введите название больницы для удаления: ")
            handler.delete_hospital(data, name)

        elif action == '5':
            name = input("Введите имя врача для удаления: ")
            handler.delete_doctor(data, name)

        elif action == '6':
            name = input("Введите имя пациента для удаления: ")
            handler.delete_patient(data, name)

        elif action == '7':
            json_.save_to_json(data, filename_json)
            xml_.save_to_xml(data, filename_xml)
            print(f"Данные сохранены в {filename_json} и {filename_xml}")

        elif action == '8':
            break

        elif action == '9':
            json_data = json_.load_from_json('data.json')
            xml_data = xml_.load_from_xml('data.xml')
            sync_data(json_data, xml_data)
            json_.save_to_json(json_data, 'data.json')
            xml_.save_to_xml(xml_data, 'data.xml')
            print("Данные успешно синхронизированы и сохранены в оба файла.")

        elif action == '10':
            show_statistics(data)

        elif action == '999':
            try:
                if file_format != 'json':
                    raise InvalidFileFormatError("Неверный формат! Вы выбрали XML, а пытаетесь открыть JSON.")
                else:
                    print_data(data, file_format)
            except InvalidFileFormatError as e:
                print(f"Ошибка: {e}")

        elif action == '169':
            try:
                if file_format != 'xml':
                    counter += 1
                    if counter == 1:
                        raise InvalidFileFormatError("Бывает, промахнулся, ничего страшного.")
                    elif counter == 2:
                        raise InvalidFileFormatError("Чумба, попей колесики.")
                    else:
                        raise InvalidFileFormatError("Ты меня пугаешь...неужели ты не понял что вообще нет смысла в разделении... и ничего мне не мешало немного изменить код? Я просто хотел хоть где то оставить свою лепту, ибо меняя названия переменных я бы потом вообще не понял, а где что....")
                else:
                    print_data(data, file_format)
            except InvalidFileFormatError as e:
                print(f"{e}")

        else:
            print("Неверная команда!")

if __name__ == "__main__":
    main()
