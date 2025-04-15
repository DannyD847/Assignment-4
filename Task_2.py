new_text = input('Enter text to write to the file: ')
file = open('output.txt','r+')
writing_file = file.write(new_text + '\n')
file.close()
print('Data successfully written to output.txt.')

appended_text = input('\nEnter additional text to append: ')
file = open('output.txt','a')
appending_file = file.write(appended_text + '\n')
file.close()
print('Data successfully appended.')

print('\nFinal content of output.txt:')
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
