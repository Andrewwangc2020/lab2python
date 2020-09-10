# Author: Andrew Wang aqw5628@psu.edu
# Collaborator: Chris Belt cob5463@psu.edu
# Collaborator: Eric Beardslee eab6024@psu.edu
# Collaborator: Devanshi Mittal dfm5688@psu.edu
# Section: 005R
# Breakout: 7

def getLetterGrade(grade: float):
  if(grade >= 93.0):
    return "A";
  elif (grade >= 90.0):
    return "A-";
  elif (grade >= 87.0):
    return "B+";
  elif (grade >= 83.0):
    return "B";
  elif (grade >= 80.0):
    return "B-";
  elif (grade >= 77.0):
    return "C+";
  elif (grade >= 70.0):
    return "C";
  elif (grade >= 60.0):
    return "D";
  elif (grade < 60):
    return "F";

g = float(input("Enter your CMPSC 131 grade: "));
letter = getLetterGrade(g);
print(f"Your letter grade for CMPSC 131 is {letter}.");

