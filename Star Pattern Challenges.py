print("hello")

#challenge one

print("Challenge 1:\n")

def challengeone():
    for i in range(3):
        for i in range(3):
            print("*", end=" ")
        
        print("\n")

challengeone()

#challenge two

print("Challenge 2:\n")

for row in range(3):
    for col in range(3):
        if row == 1 and col == 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print("\n")

#challenge three

print("Challenge 3:\n")

for row in range(3):
    for col in range(3):
        if row == 0 and col == 1 or row == 1 and col == 0 or row == 1 and col == 2 or row == 2 and col == 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print("\n")