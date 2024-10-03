from menu import Menu

def main():
    menu = Menu()
    
    while True:
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

if __name__ == "__main__":
    main()
