PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    birth_year INTEGER
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

INSERT INTO students (id, full_name, birth_year) VALUES
(1, 'Alice Johnson', 2005),
(2, 'Brian Smith', 2004),
(3, 'Carla Reyes', 2006),
(4, 'Daniel Kim', 2005),
(5, 'Eva Thompson', 2003),
(6, 'Felix Nguyen', 2007),
(7, 'Grace Patel', 2005),
(8, 'Henry Lopez', 2004),
(9, 'Isabella Martinez', 2006);


INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
(2, 'Math', 75), (2, 'History', 83), (2, 'English', 78),
(3, 'English', 95), (3, 'Math', 91), (3, 'Art', 89),
(4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
(5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
(6, 'Science', 72), (6, 'Math', 76), (6, 'English', 81),
(7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
(8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
(9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92);


CREATE INDEX idx_student_name ON students (full_name);
CREATE INDEX idx_grades_student_id ON grades (student_id);
CREATE INDEX idx_grades_subject ON grades (subject);
CREATE INDEX idx_grades_grade ON grades (grade);


SELECT
    s.full_name,
    g.subject,
    g.grade
FROM
    students s
JOIN
    grades g ON s.id = g.student_id
WHERE
    s.full_name = 'Alice Johnson';


SELECT
    s.full_name,
    ROUND(AVG(g.grade), 2) AS AverageGrade
FROM
    students s
JOIN
    grades g ON s.id = g.student_id
GROUP BY
    s.full_name
ORDER BY
    AverageGrade DESC;


SELECT
    full_name,
    birth_year
FROM
    students
WHERE
    birth_year > 2004
ORDER BY
    birth_year;


SELECT
    subject,
    ROUND(AVG(grade), 2) AS AverageGrade
FROM
    grades
GROUP BY
    subject
ORDER BY
    AverageGrade DESC;


SELECT
    s.full_name,
    ROUND(AVG(g.grade), 2) AS AverageGrade
FROM
    students s
JOIN
    grades g ON s.id = g.student_id
GROUP BY
    s.full_name
ORDER BY
    AverageGrade DESC
LIMIT 3;


SELECT DISTINCT
    s.full_name,
    g.subject,
    g.grade
FROM
    students s
JOIN
    grades g ON s.id = g.student_id
WHERE
    g.grade < 80
ORDER BY
    s.full_name, g.grade;