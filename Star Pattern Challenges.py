print("hello")

#challenge one

def challengeone():
    for i in range(3):
        for i in range(3):
            print("*", end=" ")
        
        print("\n")

challengeone()

#challenge two

for row in range(3):
    for col in range(3):
        if row == 1 and col == 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print("\n")

#challenge three

for row in range(3):
    for col in range(3):
        if row == 0 and col == 1 or row == 1 and col == 0 or row == 1 and col == 2 or row == 2 and col == 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print("\n")