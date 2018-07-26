file = open("elementPeriodicTable.txt", "w+")
file.write("Hydrogen\nHelium\nLithium\nBeryllium\nBoron\nCarbon\nNitrogen\nOxygen\n\
Fluorine\nNeon\nSodium\nMagnesium\nAluminum\nSilicon\nPhosphorus\nSulfur\nChlorine\n\
Argon\nPotassium\nCalcium\n")
file.close()

file = open("elementPeriodicTable.txt", "r+")
file.seek(0)
elementList=[]
newLine = file.readline().strip("\n").lower()
while newLine:
    elementList.append(newLine)
    newLine = file.readline().strip("\n").lower()

print(elementList)



# element =[]
# while len(element)<5:
#     inputForElement= input("Enter your Element: ")
#     if inputForElement in element:
#         print(inputForElement+" was already entered          <--no duplicates allowed ")
#     else:
#         element.append(inputForElement)
# print element
