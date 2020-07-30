import random
def result(score):
    if score < 0 or score >100:
        print("Invalid score")
    else:
        if score >= 90:
            return 'Excellent'
        elif score >= 50:
            return 'Passable'
        else:
            return 'Bad'
def main():
    score=int(input('Enter the scores:'))
    score2=random.randint(0,100)
    sentence1=str(score)+' is '+str(result(score))
    sentence2=str(score2)+' is '+str(result(score2))
    print(sentence1,'\n',sentence2)
main()