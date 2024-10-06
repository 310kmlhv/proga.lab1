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
            menu.add_disease()
        elif choice == "7":
            menu.add_treatment()
        elif choice == "8":
            menu.add_room()
        elif choice == "9":
            menu.add_bill()
        elif choice == "10":
            menu.add_payment()
        elif choice == "11":
            menu.display_patients()
        elif choice == "12":
            menu.display_doctors()
        elif choice == "13":
            menu.display_nurses()
        elif choice == "14":
            menu.display_medications()
        elif choice == "15":
            menu.display_appointments()
        elif choice == "16":
            menu.display_diseases()
        elif choice == "17":
            menu.display_treatments()
        elif choice == "18":
            menu.display_rooms()
        elif choice == "19":
            menu.display_bills()
        elif choice == "20":
            menu.display_payments()
        elif choice == "21":
            menu.save_data()
        elif choice == "22":
            menu.load_data()
        elif choice == "23":
            break
        else:
            print("Неверный выбор. Пожалуйста, повторите.")

if __name__ == "__main__":
    main()
