def quiz(s):
    f = 0
    for n in s:
        print(n['text'])
        for i, option in enumerate(n['options'], 1):
            print(f"{i}. {option}")
        a = int(input("Enter the number of your answer: "))
        if a == n['correct_option']:
            print("Correct!\n")
            f += 1
        else:
            t= n['options'][n['correct_option'] - 1]
            print(f"Wrong! The correct answer was {n['correct_option']}: {t}\n")
    print(f"Quiz completed! Your score is {f}/{len(s)}.")
m = [
    {'text': "What is the capital of india?", 'options': ["delhi", "mumbai", "haryana", "assam"], 'correct_option': 1},
    {'text': "who is the most run scorer in indian cricket?", 'options': ["Rohit Sharma", "Virat kohli", "KL Rahul", "Shreyas Iyer"], 'correct_option': 2},
    {'text': "Which country has the highest populatio?", 'options': ["India", "USA", "China", "France"], 'correct_option': 1},
]
quiz(m)