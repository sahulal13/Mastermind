import random
num = random.randrange(1000,10000)

n = int(input("Guess the 4 digit number:"))

if n == num:
    print("Congrats!!! You have guessed the correct number in the first try. You are a mastermind.")
else:
    tries=0

    while (n!=num):
        tries += 1
        count = 0

        n = str(n)
        num = str(num)

        correct = ['X']*4
        
        for x in range(0,4):
            if (n[x] == num[x]):
                count+=1

                correct[x] = n[x]
            else:
                continue
        if (count < 4 ) and (count !=0):   
          print("Alas!! It's the wrong number. But you did get ",count,"digits correct") 

        print(("These numbers were correct in your guess"))
        for k in correct:
            print(k, end = " ")   
        print('\n') 
        print('\n')
        n = int(input("Enter your next guess:"))

        if(count == 0):
          print("None of your numbers match.")
          n = int(input("Enter your next guess:"))
          if n == num:
              tries+=1
              print("You have guessed the correct number. You have become a mastermind!!")
              print("It took you only",tries,"tries.")

          
