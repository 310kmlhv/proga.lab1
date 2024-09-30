from menu import Menu
from xml_handler import load_from_xml, save_to_xml
from json_handler import load_from_json, save_to_json

def main():
    menu = Menu()
    
    while True:
        print("\nГлавное меню:")
        menu.display_menu()
        
        choice = input("Введите номер действия: ")
        
        if choice == "1":
            menu.add_patient()
        elif choice == "2":
            menu.add_doctor()
        elif choice == "3":
            menu.add_nurse()
        elif choice == "4":
            menu.add_medications()
        elif choice == "5":
            menu.add_appointment()
        elif choice == "6":
            menu.display_patients()
        elif choice == "7":
            menu.display_doctors()
        elif choice == "8":
            menu.display_nurses()
        elif choice == "9":
            menu.display_medications()
        elif choice == "10":
            menu.display_appointments()
        elif choice == "11":
            menu.save_data()
        elif choice == "12":
            menu.load_data()
        elif choice == "13":
            break
        else:
            print("Неверный выбор. Пожалуйста, повторите.")
        
        input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
