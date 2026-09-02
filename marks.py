
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))


total_marks = sub1 + sub2 + sub3
average_marks = total_marks / 3


print("\n--- Student Result Sheet ---")
print(f"Total Marks   : {total_marks}")
print(f"Average Marks : {average_marks:.2f}") 


if average_marks >= 40:
    print("Final Status  : PASS")
else:
    print("Final Status  : FAIL")
