#grading program
score = float(input("Enter your score : "))
if score > 100 or score < 0 :
	print("score must be 0-100")
elif score < 100 and score >= 80 :
	print("your grade is A ")
elif score < 80 and score >= 70 :
	print("your grade is B ")
elif score < 70 and score >= 60 :
	print("your grade is C ")
elif score < 60 and score >= 50 :
	print("your grade is D ")
else :
	print("your grade is F ")