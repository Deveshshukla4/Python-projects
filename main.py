print "Hello n welcome to Python Works"

print "Choose from the list given below \n\
      A). Battleship \n\
      B). Exam Stats \n\
      C). Studen_teacher records"

choice= raw_input("Choose from above options")
if choice=="A":
    import battleship
    battleship.main()
elif choice=="B":
    import exam_stats
    exam_stats.main()
elif choice=="C":
    import Student_teacher
    Student_teacher.main()
else:
    print "Wrong choice...Please try again"