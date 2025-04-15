print("grade calculator")
scores = []

while True:
    score = input("Enter a test score (or done): ")
    if score.lower() == 'done':
        print("goodbye")
        break
    scores.append(float(score))
    average = sum(scores) / len(scores)
    print(f"Average score is {average}")
   
    if average >= 90:
        print("Grade A")
    elif average >= 80:
        print("Grade B")
    elif average >= 70:
        print("Grade B")
    else:
        print("Grade is D or F")

  
