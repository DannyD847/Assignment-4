try:
    file = open("sample.txt", "r")
    count = 1
    print('Reading file content: ')
    for line in file:
        print(f"Line {count}: {line.strip()}")
        count += 1
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
