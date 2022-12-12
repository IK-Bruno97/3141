
questions = { "1": "What is the full meaning of HTML?",
              "2": "What is the full meaning of CSS?",
              "3": "What is the full meaning of JS?",
              "4": "What year was python released?",
              "5": "What is the value of 10 x 10?",
}

answers = ["Hypertext Markup Language", "Cascading stylessheet", "Javascript", 1994, 100]
ans = []


for i in questions.items():
    print(f'{i[0]}: {i[1]}')
    user_input = input("The answer is: ")
    ans.append(user_input)


def correct_answers():
    global correct
    correct = 0

    if ans[0] == answers[0]:
        correct += 1
    if ans[1] == answers[1]:
        correct += 1
    if ans[2] == answers[2]:
        correct += 1
    if int(ans[3]) == answers[3]:
        correct += 1
    if int(ans[4]) == answers[4]:
        correct += 1

    if correct > 3:
        print(f"Bravo, your score is {correct}/{len(questions)} ")
    else:
        print(f"Try again, you scored {correct}/{len(questions)} ")
    
 

correct_answers()