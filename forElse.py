succesfuld = True

for number in range(3):
    print("attempt")
    if succesfuld:
        print("succesful")
        break
else:
    print("attempted 3 times and failed")