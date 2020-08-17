def main():
	#write your code here
	print("Welcome to the special recruitment program, please answer the following questions:")

	name = input("What is you name? ")
	age = input("How old are you? ")
	experience = input("How many years of experience do you have? ")

	skills_list = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]

	cv = {}
	cv['name'] = name
	cv['age'] = int(age)
	cv['experience'] = int(experience)
	cv['skills'] = ""

	print("\nSkills:")
	for skill in skills_list:
		print("%d. %s" % ((skills_list.index(skill)+1), skill))

	skill_num1 = input("\nChoose a skill from above by entering its number: ")
	skill_num2 = input("Choose another skill from above by entering its number: ")

	cv['skills'] = (skills_list[int(skill_num1)-1], skills_list[int(skill_num2)-1])
	

	if (int(age) > 25 and int(age) < 40) and int(experience) > 5 and (int(skill_num1) == 6 or  int(skill_num2) == 6):
		print("You have been accepted, %s" % (name.title()))
	else:
		print("You have been rejected, %s" % (name.title()))

	print (cv)


if __name__ == '__main__':
	main()