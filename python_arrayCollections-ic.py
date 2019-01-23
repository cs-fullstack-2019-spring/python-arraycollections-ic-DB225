def main():
    #problem1()
    #problem2()
    #problem3()
    #problem4()
    problem5()

###############################################################################################
#PROBLEM1
#Create a function that returns an array from 0 to 100.
# Print the array in another function.
def problem1():
    listNumber = []
    for num in range(0,101):
        listNumber.append(num)
        return listNumber
###############################################################################################
#PROBLEM2
#Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def problem2():
    userInput = " "
    while(userInput != "q"):
        userInput = input("Put a string: ")
###############################################################################################
#PROBLEM3
#Create a function with the variable below.
# After you create the variable do the instructions below that.
#listNames = [“John”, “Paul”, “George”, “Pete”]
#a) Print Pete’s name from the list
#b) Change Pete’s name to ‘Ringo’, print the list
#c) Add the name ‘Yoko’ to the list and print
def problem3():
    listNames = ["John", "Paul", "George", "Pete"]
    print(listNames[3])
    listNames[3] = "Ringo"
    print(listNames)
    listNames.append("yoko")
    print(listNames)
###############################################################################################
#PROBLEM4
#Create a function that contains a collection of information for the following. After you create the collection do the instructions below that.
#Vocals/Robert
#Guitar/Jimmy
#Bass/John
#Drums/Bonzo
#a) Print the collection
#b) Print who plays guitar
def problem4():
    musicalGroup = {
         "Vocals":"Robert",
         "Guitar":"Jimmy",
         "Bass":"John",
         "Bonzo": "Drums"
    }
    print(musicalGroup)
    print(musicalGroup["Guitar"])
###############################################################################################
#PROBLEM5
#Create a function that will have a hard coded array of Kenn, Kevin, and Erin several times in the array.
# Print out how many times Kenn, Kevin, or Erin appears in an array.
def problem5():
    listOfNames = ["kenn", "kevin", "Erin","kevin", "Erin","kevin"]
    print(listOfNames.count("kenn"))
    print(listOfNames.count("kevin"))
    print(listOfNames.count("Erin"))

    kevinCount = 0
    kennCount = 0
    ErinCount = 0
    for eachElement in kennCount:
         if(eachElement == "kenn"):
             kennCount +=1
         elif(eachElement == "kevin"):
             kevinCount +=1
         elif(eachElement == "Erin"):
             ErinCount +=1


















if __name__ == '__main__':
    main()