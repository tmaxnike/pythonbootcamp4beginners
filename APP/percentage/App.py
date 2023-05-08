#write a program that calculate the percentage a student get in a test with 40 questions.
#Each question is worth 2 marks
#Algorithm

numberofQuestion = 40
markperQuestion = 2
totalmarksfortest = numberofQuestion * markperQuestion
numberofcorrectQuestions = 28
totalMarkforstudent = numberofcorrectQuestions * markperQuestion
percentage = (totalMarkforstudent / totalmarksfortest) * 100
print(percentage)
