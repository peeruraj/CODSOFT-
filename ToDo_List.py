

class ToDoList:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.works = []
        

    def save_works(self):
        with open(self.filename, "w") as file:
            for work in self.works:
                file.write(work + "\n")

    def add_work(self, work):
        self.works.append(work)
        self.save_works()
        print(f'Work "{work}" added ✔')

    def view_works(self):
        if not self.works:
            print("No works in the list.")
        else:
            for idx, work in enumerate(self.works, start=1):
                print(f"{idx}. {work}")

    def complete_work(self, number):
        if 0 < number <= len(self.works):
            completed_work = self.works.pop(number - 1)
            self.save_works()
            print(f'Work "{completed_work}" marked as complete and removed from the list.')
        else:
            print("Invalid number.")

    def delete_work(self, number):
        if 0 < number <= len(self.works):
            deleted_work = self.works.pop(number - 1)
            self.save_works()
            print(f'Work "{deleted_work}" deleted from the list.')
        else:
            print("Invalid number.")

def display_menu():
    print("\n--------To-Do List Application-------")
    print("1. View all works")
    print("2. Add a work")
    print("3. Complete a work")
    print("4. Delete a work")
    print("5. Exit from app")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter the number from (1-5): ")

        if choice == "1":
            todo_list.view_works()
        elif choice == "2":
            work = input("Enter the Work Name: ")
            todo_list.add_work(work)
        elif choice == "3":
            number = int(input("Enter the work number to mark as complete: "))
            todo_list.complete_work(number)
        elif choice == "4":
            number = int(input("Enter the work number to delete: "))
            todo_list.delete_work(number)
        elif choice == "5":
            print("Exiting the application ↺")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
