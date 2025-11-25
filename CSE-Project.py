# This list stores all appointments. Each appointment is a list inside this main list.
appointments = []

# Updated header design using multiple asterisks
print("**************************************************")
print("******* 🐾 Welcome to Pet Care Manager! 🐾 *******")
print("**************************************************")

# --- Main Application Loop ---
# The 'while True' loop keeps the program running until the user chooses to exit (option 5).
while True:
    # Updated menu separator design
    print("\n******** MENU ********")
    print("1. Create New Appointment")
    print("2. View All Appointments")
    print("3. Update an Appointment")
    print("4. Delete an Appointment")
    print("5. Exit")
    print("**********************")
    
    choice = input("Enter your choice (1-5): ")

    # --- 1. CREATE (Add a new appointment) ---
    if choice == '1':
        print("\n--- New Appointment ---")
        pet_name = input("Enter pet's name: ")
        owner_name = input("Enter owner's name: ")
        appointment_time = input("Enter appointment time: ")
        
        new_appointment = [pet_name, owner_name, appointment_time]
        
        # Add the new appointment to the list
        appointments.append(new_appointment)
        print(f"\n✅ Appointment for {pet_name} created successfully!")

    # --- 2. READ (Display all appointments) ---
    elif choice == '2':
        print("\n--- All Appointments ---")
        if not appointments:
            print("No appointments scheduled yet.")
        else:
            i = 0
            # Loop through all appointments to display them
            for appointment in appointments:
                display_number = i + 1 
                
                print(f"[{display_number}] Pet: {appointment[0]}, Owner: {appointment[1]}, Time: {appointment[2]}")
                
                i = i + 1

    # --- 3. UPDATE (Modify an existing appointment) ---
    elif choice == '3':
        if not appointments:
            print("\nNo appointments to update.")
            continue 
            
        print("\n--- Appointments to Update ---")
        i = 0
        for appointment in appointments:
            print(f"[{i + 1}] Pet: {appointment[0]}, Owner: {appointment[1]}, Time: {appointment[2]}")
            i = i + 1

        try:
            update_index = int(input("Enter the number of the appointment to update: "))
            
            # Check if the input number is valid
            if 1 <= update_index <= len(appointments):
                list_index = update_index - 1
                
                print(f"\nUpdating appointment {update_index}: Pet {appointments[list_index][0]}")
                
                new_pet_name = input("Enter NEW pet's name (or press Enter to keep current): ")
                new_time = input("Enter NEW time (or press Enter to keep current): ")
                
                # Conditional logic to update fields only if new input is provided
                if new_pet_name:
                    appointments[list_index][0] = new_pet_name
                
                if new_time:
                    appointments[list_index][2] = new_time
                    
                print("\n✅ Appointment updated!")
                
            else:
                print("\n❌ Invalid number. Please enter a number from the list.")
                
        except ValueError:
            print("\n❌ Invalid input. Please enter a number.")

    # --- 4. DELETE (Remove an appointment) ---
    elif choice == '4':
        if not appointments:
            print("\nNo appointments to delete.")
            continue
            
        print("\n--- Appointments to Delete ---")
        i = 0
        for appointment in appointments:
            print(f"[{i + 1}] Pet: {appointment[0]}, Owner: {appointment[1]}, Time: {appointment[2]}")
            i = i + 1

        try:
            delete_index = int(input("Enter the number of the appointment to DELETE: "))
            
            # Check if the input number is valid
            if 1 <= delete_index <= len(appointments):
                list_index = delete_index - 1
                
                # Use .pop() to remove the item at the specified index
                deleted_appointment = appointments.pop(list_index)
                
                print(f"\n🗑️ Appointment for {deleted_appointment[0]} has been cancelled and deleted.")
                
            else:
                print("\n❌ Invalid number. Please enter a number from the list.")
                
        except ValueError:
            print("\n❌ Invalid input. Please enter a number.")

    # --- 5. EXIT (Stop the program) ---
    elif choice == '5':
        print("\nThank you for using the Pet Care Appointment Manager! Goodbye! 👋")
        # 'break' exits the 'while True' loop
        break 
        
    # Handle an invalid menu choice
    else:
        print("\n⚠️ Invalid choice. Please enter a number between 1 and 5.")






