import random

Ans_list=["APPLE","UMBRELLA","COMPUTER","YELLOW","SCOOTER"]
problem_list=["PLAEP","ELRMABLU","POMRTCEU","WELYOL","TORECSO"]
score=0

for turn in range(4,-1,-1):

    ch=random.randint(0, turn)
    ans=(input("\nArrange the letters to form a valid word: \n{}\n".format(problem_list[ch]))).upper()
    
    if ans == Ans_list[ch]:
        score+=1
        print("\nCorrect\n")
    else:
        score-=1
        print("\nWrong\n")

    del problem_list[ch]
    del Ans_list[ch]

print("\nNet Score is",score)