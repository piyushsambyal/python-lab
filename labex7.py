database = [
    (1, "Rushil",20,"Maths"),
    (2, "Lalu laal Singh",21,"English"),
    (3, "Rohab",22,"Hindi"),
    (4, "Mahem",19,"Science")
]    
database

def display(data):
    print("ID | NAME | AGE | SUBJECT")
    print("---------------------------")

    for i in data:
        print(f"{i[0]:3} | {i[1]:15} | {i[2]:3} | {i[3]}")
display(database)

# Add new data
def add_data(data, id, name, age, subject):
    data.append((id, name, age, subject))

add_data(database, 5, "Sukuna", 23, "Eco")
display(database)

# Remove row
def delete_row(data):
    return data.pop()

delete_row(database)
display(database)