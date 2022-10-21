# Write a program to find out whethera student is pass or fail, if it requires total 40% and atleast 33%, in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter your marks in first subject:\n"))
sub2 = int(input("Enter your marks in second subject:\n"))
sub3 = int(input("Enter your marks in third subject:\n"))

# Assuming total marks are 300 with each total of 100.

# It can also be written as :

if (sub1<33 or sub2<33 or sub3<33):   
    print("You are failed due to total percentage in a subject is less than 33!")
elif (((sub1+sub2+sub3)/3)<40):
    print("You are failed due to total percentage less than 40!")
else:
    print("Congratulations! You passed the exam.")