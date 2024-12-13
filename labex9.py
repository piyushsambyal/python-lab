class Database:
    def insert_data(self, id, name, age, salary):
        self.data = []
        self.data.append((id, name, age, salary))

    def display_data(self):
        print("ID | Name | Age | Salary")
        print("-" * 30)
        for i in self.data:
            print(f"{i[0]:<4} {i[1]:<15} {i[2]:<3} {i[3]:<5}")

class Database2(Database):
    def add_data(self, id, name, age, salary):
        self.data.append((id, name, age, salary))

    def remove_row(self, id):
        self.data.pop(id - 1)

d = Database2()
d.insert_data(1, "Piyush Sambyal", 25, 50000)
d.add_data(2, "Aditya kumar", 23, 48000)
d.add_data(3, "Mohit rajpt", 28, 60000)
d.add_data(4, "Rushil amla", 29, 70000)

print("Initial Data")
d.display_data()

d.remove_row(4)
print("\nUpdated Data")
d.display_data()
