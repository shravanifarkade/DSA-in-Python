class Node:
    def __init__(self, name, disease, priority, next_node=None):
        self.name = name
        self.disease = disease
        self.priority = priority
        self.next = next_node

class HospitalQueue:
    def __init__(self):
        self.head = None

    def add_patient(self, name, disease, priority):
        new_node = Node(name, disease, priority)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"Added patient: {name}, Disease: {disease}, Priority: {priority}")

    def remove_patient(self):
        if self.head is None:
            print("No patients in the queue.")
            return
        removed_patient = self.head
        self.head = self.head.next
        print(f"Removed patient: {removed_patient.name}, Disease: {removed_patient.disease}")
        return removed_patient

    def move_up_priority(self, name):
        current = self.head
        prev = None
        while current:
            if current.name == name:
                if prev:  # Not the first patient in the queue
                    prev.next = current.next
                    current.next = self.head  # Move to front
                    self.head = current
                    print(f"Moved patient {name} up in priority.")
                return
            prev = current
            current = current.next
        print(f"Patient {name} not found in the queue.")

    def display_queue(self):
        if self.head is None:
            print("No patients in the queue.")
            return
        temp = self.head
        print("Current queue of patients:")
        while temp:
            print(f"Name: {temp.name}, Disease: {temp.disease}, Priority: {temp.priority}")
            temp = temp.next

    def search_patient(self, name):
        current = self.head
        while current:
            if current.name == name:
                print(f"Patient found: Name: {current.name}, Disease: {current.disease}, Priority: {current.priority}")
                return
            current = current.next
        print(f"Patient {name} not found in the queue.")

    def update_patient_info(self, name, new_disease=None, new_priority=None):
        current = self.head
        while current:
            if current.name == name:
                if new_disease:
                    current.disease = new_disease
                if new_priority is not None:
                    current.priority = new_priority
                print(f"Updated patient: {current.name}, New Disease: {current.disease}, New Priority: {current.priority}")
                return
            current = current.next
        print(f"Patient {name} not found in the queue.")

def main():
    hospital_queue = HospitalQueue()
    
    while True:
        print("\nHospital Management System")
        print("1: Add Patient")
        print("2: Remove Patient")
        print("3: Move Patient Up in Priority")
        print("4: Display Queue")
        print("5: Search Patient")
        print("6: Update Patient Info")
        print("7: Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter patient's name: ")
            disease = input("Enter patient's disease: ")
            priority = int(input("Enter priority (1 - High, 2 - Medium, 3 - Low): "))
            hospital_queue.add_patient(name, disease, priority)
        elif choice == 2:
            hospital_queue.remove_patient()
        elif choice == 3:
            name = input("Enter patient's name to move up in priority: ")
            hospital_queue.move_up_priority(name)
        elif choice == 4:
            hospital_queue.display_queue()
        elif choice == 5:
            name = input("Enter patient's name to search: ")
            hospital_queue.search_patient(name)
        elif choice == 6:
            name = input("Enter patient's name to update: ")
            new_disease = input("Enter new disease (or press enter to skip): ")
            new_priority_input = input("Enter new priority (or press enter to skip): ")
            new_priority = int(new_priority_input) if new_priority_input else None
            hospital_queue.update_patient_info(name, new_disease, new_priority)
        elif choice == 7:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
