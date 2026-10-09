INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

math = []
python = []
english = []
names = []
with open(INPUT_FILE) as f:
    next(f)
    for line in f:
        line.strip()
        pieces = line.split(",")
        name = pieces[0]
        names.append(name)
        math_score = int(pieces[1])
        math.append(math_score)
        python_score = int(pieces[2])
        python.append(python_score)
        english_score = int(pieces[3])
        english.append(english_score)


math_gpa = sum(math) / len(math)
python_gpa = sum(python) / len(python)
english_gpa = sum(english) / len(english)
math_gpa = round(math_gpa, 1)
python_gpa = round(python_gpa, 1)
english_gpa = round(english_gpa, 1)



with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(f"середній бал з математики: {math_gpa}\n")
    f.write(f"середній бал з пітона: {python_gpa}\n")
    f.write(f"середній бал з англійської: {english_gpa}\n")

print(f"середній бал по класу: math: {math_gpa}  python: {python_gpa}  english: {english_gpa} ")

