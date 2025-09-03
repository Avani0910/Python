import sqlite3


conn = sqlite3.connect("school.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id),
    FOREIGN KEY(subject_id) REFERENCES Subjects(subject_id)
)
""")


def add_student(name):
    cursor.execute("INSERT INTO Students (name) VALUES (?)", (name,))
    conn.commit()

def add_subject(subject_name):
    cursor.execute("INSERT INTO Subjects (subject_name) VALUES (?)", (subject_name,))
    conn.commit()


def enroll_student(student_id, subject_ids):
    for sid in subject_ids:
        cursor.execute("INSERT INTO Enrollments (student_id, subject_id) VALUES (?, ?)", (student_id, sid))
    conn.commit()


def get_enrollments():
    cursor.execute("""
    SELECT s.name, sub.subject_name
    FROM Students s
    JOIN Enrollments e ON s.student_id = e.student_id
    JOIN Subjects sub ON e.subject_id = sub.subject_id
    """)
    return cursor.fetchall()


def delete_enrollment(student_id, subject_id):
    cursor.execute("DELETE FROM Enrollments WHERE student_id=? AND subject_id=?", (student_id, subject_id))
    conn.commit()


add_student("Avni")
add_student("Saloni")


add_subject("Math")
add_subject("Science")
add_subject("History")


enroll_student(1, [1, 2])

enroll_student(2, [2, 3])


print("Current Enrollments:")
for row in get_enrollments():
    print(row)

delete_enrollment(1, 1)

print("\n After Deletion:")
for row in get_enrollments():
    print(row)


conn.close()
