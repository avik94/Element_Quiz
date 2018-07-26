element =[]
while len(element)<5:
    inputForElement= input("Enter your Element: ")
    if inputForElement in element:
        print(inputForElement+" was already entered          <--no duplicates allowed ")
    else:
        element.append(inputForElement)
print element

file = open("elementPeriodicTable.txt", "w+")
file.write("Hydrogen\n Helium\n Lithium\n Beryllium\n Boron\n Carbon\n Nitrogen\n Oxygen\n\
Fluorine\n Neon\n Sodium\n Magnesium\n Aluminum\n Silicon\n Phosphorus\n Sulfur\n Chlorine\n\
Argon\n Potassium\n Calcium\n") 
