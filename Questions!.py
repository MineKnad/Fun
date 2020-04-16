import random

score = 0
RareNumbers = [1, 2, 10]
#r = int(input("what's the maximum number? "))



while True:


    def question1(range):
        a = random.randint(1,range)
        b = random.randint(1,range)

        if (a in RareNumbers):
            a = random.randint(1, range)

        if (b in RareNumbers):
            b = random.randint(1, range)



        ans = a * b
        print(" What is " + str(a) + " times " + str(b) + " ?")
        return(ans)


    def answer():
        ans = question1(10)
        guess = int(input())

        if guess == ans:
            print("correct!")
            return(score + 1)
        else:
            print("wrong! Right answer was", ans)
            return(score - 1)


    print("score: " + str(score))
    print("")
    score = answer()
