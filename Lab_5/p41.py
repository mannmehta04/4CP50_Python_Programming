def create_demo_binary_file(filename):
    with open(filename, 'wb') as file:
        file.write(b"1,Mann,24.5\n")
        file.write(b"2,Kalp,30.2\n")
        file.write(b"3,Ayush,22.8\n")
        file.write(b"4,Karma,28.1\n")

def print_all_records(filename):
    with open(filename, 'rb') as file:
        records = file.readlines()
        for record in records:
            id, name, score = record.decode().strip().split(',')
            print(f"ID: {id}, Name: {name}, Score: {score}")

filename = 'data.bin'
create_demo_binary_file(filename)
print_all_records(filename)
