while True:

    try:
        RESPONSE = int(input("When were you born: "))
        if RESPONSE >= 2000 and RESPONSE <= 2022:
            print("You were born in 21st century")
        elif RESPONSE >= 1900 and RESPONSE <= 1999:
            print("You were born in 20th century")
        elif RESPONSE == 1899 or RESPONSE <= 1898:
            print("You should not be running this.")
        else:
            print("Please give me a number")
        break
    except:
        print("Error:did you provide digit e.g 1")   


# [ ]
# COMMAND + ] move to the rith
# COMMAND + [ move to left
# test

ANSWER = "no"
while ANSWER != "yes":
    ANSWER = input("Are you crazy? ")
    if ANSWER == "yes":
        print("I knew that")