-- POPULATE USER DATA

INSERT INTO user (user_id, email, first_name, last_name, password, role_no)
VALUES
-- ADMIN
('saitama', 'admin@ncsu.test', 'adminFirst', 'adminLast', 'password@123', 1),
-- FACULTY
('testFacultyID', 'fac@gmail.com', 'fac_name', 'fac_surname', 'test', 2),
('KeOg1024', 'kogan@ncsu.edu', 'Kemafor', 'Ogan', 'Ko2024!rpc', 2),
('JoDo1024', 'john.doe@example.com', 'John', 'Doe', 'Jd2024!abc', 2),
('SaMi1024', 'sarah.miller@domain.com', 'Sarah', 'Miller', 'Sm#Secure2024', 2),
('DaBr1024', 'david.b@webmail.com', 'David', 'Brown', 'DbPass123!', 2),
('EmDa1024', 'emily.davis@email.com', 'Emily', 'Davis', 'Emily#2024!', 2),
('MiWi1024', 'michael.w@service.com', 'Michael', 'Wilson', 'Mw987secure', 2),
('JeGi0524', 'jerry.giovani@email.com', 'Jerry', 'Giovani', 'jerryvstop123',2),
-- STUDENT
('ErPe1024', 'ez356@example.mail', 'Eric', 'Perrig', 'qwdmq', 3),
('AlAr1024', 'aa23@edu.mail', 'Alice', 'Artho', 'omdsws', 3),
('BoTe1024', 'bt163@template.mail', 'Bob', 'Temple', 'sak+=', 3),
('LiGa1024', 'li123@example.edu', 'Lily', 'Gaddy', 'cnaos', 3),
('ArMo1024', 'am213@example.edu', 'Aria', 'Morrow', 'jwocals', 3),
('KeRh1014', 'kr21@example.edu', 'Kellan', 'Rhodes', 'camome', 3),
('SiHa1024', 'sh13@example.edu', 'Sienna', 'Hayes', 'asdqm', 3),
('FiWi1024', 'fw23@example.edu', 'Finn', 'Wilder', 'f13mas', 3),
('LeMe1024', 'lm56@example.edu', 'Leona', 'Mercer', 'ca32', 3),
-- TA
('test', 'test@gmail.com', 'TestTA', 'TestTA', 'test', 4),
('JaWi1024', 'jwilliams@ncsu.edu', 'James', 'Williams', 'jwilliams@1234', 4),
('LiAl0924', 'lalberti@ncsu.edu', 'Lisa', 'Alberti', 'lalberti&5678@', 4),
('DaJo1024', 'djohnson@ncsu.edu', 'David', 'Johnson', 'djohnson%@1122', 4),
('ElCl1024', 'eclark@ncsu.edu', 'Ellie', 'Clark', 'eclark^#3654', 4),
('JeGi0924', 'jgibson@ncsu.edu', 'Jeff', 'Gibson', 'jgibson$#9877', 4);

INSERT INTO admin (admin_id)
VALUES 
('saitama');

INSERT INTO textbook (textbook_id, title, created_by, updated_by)
VALUES 
    (777, 'Sample Textbook', 'saitama', 'saitama'),
    (101, 'Database Management Systems', 'saitama', 'saitama'),
    (102, 'Fundamentals of Software Engineering', 'saitama', 'saitama'),
    (103, 'Fundamentals of Machine Learning', 'saitama', 'saitama');

INSERT INTO student (stud_id)
VALUES 
('ErPe1024'),
('AlAr1024'),
('BoTe1024'),
('LiGa1024'),
('ArMo1024'),
('KeRh1014'),
('SiHa1024'),
('FiWi1024'),
('LeMe1024');

INSERT INTO faculty (fac_id) VALUES
('testFacultyID'),
('KeOg1024'),
('JoDo1024'),
('SaMi1024'),
('DaBr1024'),
('EmDa1024'),
('MiWi1024'),
('JeGi0524');

INSERT INTO course (course_id, textbook_id, title, start_date, end_date, admin_id, fac_id) VALUES
('testCourseID', 777, "Sample Textbook", '2024-08-15', '2024-12-15', 'saitama', 'testFacultyID'),
('NCSUOganCSC440F24', 101, 'CSC440 Database Systems', '2024-08-15', '2024-12-15', 'saitama', 'KeOg1024'),
('NCSUOganCSC540F24', 101, 'CSC540 Database Systems', '2024-08-17', '2024-12-15', 'saitama', 'KeOg1024'),
('NCSUSaraCSC326F24', 102, 'CSC326 Software Engineering', '2024-08-23', '2024-10-23', 'saitama', 'SaMi1024'),
('NCSUJegiCSC522F24', 103, 'CSC522 Fundamentals of Machine Learning', '2025-08-25', '2025-12-18', 'saitama', 'JoDo1024'),
('NCSUSaraCSC326F25', 102, 'CSC326 Software Engineering', '2025-08-27', '2025-12-19', 'saitama', 'SaMi1024');

INSERT INTO active_course (token, capacity, course_id) VALUES
('XYJKLM', 60, 'NCSUOganCSC440F24'),
('STUKZT', 50, 'NCSUOganCSC540F24'),
('LRUFND', 100, 'NCSUSaraCSC326F24');

INSERT INTO enroll (is_approved, stud_id, course_id) VALUES
(TRUE, 'ErPe1024', 'NCSUOganCSC440F24'),
(TRUE, 'ErPe1024', 'NCSUOganCSC540F24'),
(TRUE, 'AlAr1024', 'NCSUOganCSC440F24'),
(TRUE, 'BoTe1024', 'NCSUOganCSC440F24'),
(TRUE, 'LiGa1024', 'NCSUOganCSC440F24'),
(TRUE, 'LiGa1024', 'NCSUOganCSC540F24'),
(TRUE, 'ArMo1024', 'NCSUOganCSC540F24'),
(TRUE, 'ArMo1024', 'NCSUOganCSC440F24'),
(TRUE, 'SiHa1024', 'NCSUOganCSC440F24'),
(TRUE, 'FiWi1024', 'NCSUSaraCSC326F24'),
(TRUE, 'LeMe1024', 'NCSUOganCSC440F24'),
(FALSE, 'FiWi1024', 'NCSUOganCSC440F24'),
(FALSE, 'LeMe1024', 'NCSUOganCSC540F24'),
(FALSE, 'AlAr1024', 'NCSUOganCSC540F24'),
(FALSE, 'SiHa1024', 'NCSUOganCSC540F24'),
(FALSE, 'FiWi1024', 'NCSUOganCSC540F24');

INSERT INTO teaching_assistant (ta_id, course_id, fac_id) VALUES
('test', 'testCourseID', 'testFacultyID'),
('JaWi1024', 'NCSUOganCSC440F24', 'KeOg1024'),
('LiAl0924', 'NCSUOganCSC540F24', 'KeOg1024'),
('DaJo1024', 'NCSUSaraCSC326F24', 'SaMi1024'),
('ElCl1024', 'NCSUJegiCSC522F24', 'JeGi0524'),
('JeGi0924', 'NCSUSaraCSC326F25', 'SaMi1024');

INSERT INTO chapter (textbook_id, chapter_id, title, is_hidden, created_by, updated_by)
VALUES 
    (101, 'chap01', 'Introduction to Database', FALSE, 'saitama', 'saitama'),
    (101, 'chap02', 'The Relational Model', FALSE, 'saitama', 'saitama'),
    (102, 'chap01', 'Introduction to Software Engineering', FALSE, 'saitama', 'saitama'),
    (102, 'chap02', 'Introduction to Software Development Life Cycle (SDLC)', FALSE, 'saitama', 'saitama'),
    (103, 'chap01', 'Introduction to Machine Learning', FALSE, 'saitama', 'saitama');

INSERT INTO section (textbook_id, chapter_id, section_id, title, is_hidden, created_by, updated_by)
VALUES 
    -- Sections for textbook 101, chapter 'chap01'
    (101, 'chap01', 'sec01', 'Introduction and Overview', FALSE, 'saitama', 'saitama'),
    (101, 'chap01', 'sec02', 'Database System Concepts', FALSE, 'saitama', 'saitama'),

    -- Sections for textbook 101, chapter 'chap02'
    (101, 'chap02', 'sec01', 'The Relational Database Structure', FALSE, 'saitama', 'saitama'),
    (101, 'chap02', 'sec02', 'Integrity Constraints', FALSE, 'saitama', 'saitama'),

    -- Sections for textbook 102, chapter 'chap01'
    (102, 'chap01', 'sec01', 'Introduction to Software Processes', FALSE, 'saitama', 'saitama'),
    (102, 'chap01', 'sec02', 'Software Project Planning', FALSE, 'saitama', 'saitama'),

    -- Sections for textbook 102, chapter 'chap02'
    (102, 'chap02', 'sec01', 'Phases of SDLC', FALSE, 'saitama', 'saitama'),
    (102, 'chap02', 'sec02', 'SDLC Models', FALSE, 'saitama', 'saitama'),

    -- Sections for textbook 103, chapter 'chap01'
    (103, 'chap01', 'sec01', 'What is Machine Learning?', FALSE, 'saitama', 'saitama'),
    (103, 'chap01', 'sec02', 'Supervised vs Unsupervised Learning', FALSE, 'saitama', 'saitama');

-- Insert content blocks
INSERT INTO content_block (textbook_id, chapter_id, section_id, block_id, is_type, is_hidden, created_by, updated_by)
VALUES 
    (101, 'chap01', 'Sec01', 'Block01', 'text', FALSE, 'saitama', 'saitama'),
    (101, 'chap01', 'Sec02', 'Block01', 'activity', FALSE, 'saitama', 'saitama'),
    (101, 'chap02', 'Sec01', 'Block01', 'text', FALSE, 'saitama', 'saitama'),
    (101, 'chap02', 'Sec02', 'Block01', 'picture', FALSE, 'saitama', 'saitama'),
    (102, 'chap01', 'Sec01', 'Block01', 'text', FALSE, 'saitama', 'saitama'),
    (102, 'chap01', 'Sec02', 'Block01', 'activity', FALSE, 'saitama', 'saitama'),
    (102, 'chap02', 'Sec01', 'Block01', 'text', FALSE, 'saitama', 'saitama'),
    (102, 'chap02', 'Sec02', 'Block01', 'picture', FALSE, 'saitama', 'saitama'),
    (103, 'chap01', 'Sec01', 'Block01', 'text', FALSE, 'saitama', 'saitama'),
    (103, 'chap01', 'Sec02', 'Block01', 'activity', FALSE, 'saitama', 'saitama');

-- Insert text content
INSERT INTO text (textbook_id, chapter_id, section_id, block_id, text_id, text_content)
VALUES 
    (101, 'chap01', 'Sec01', 'Block01', 1, 'A Database Management System (DBMS) is software that enables users to efficiently create, manage, and manipulate databases. It serves as an interface between the database and end users, ensuring data is stored securely, retrieved accurately, and maintained consistently. Key features of a DBMS include data organization, transaction management, and support for multiple users accessing data concurrently.'),
    (101, 'chap02', 'Sec01', 'Block01', 1, 'DBMS systems provide structured storage and ensure that data is accessible through queries using languages like SQL. They handle critical tasks such as maintaining data integrity, enforcing security protocols, and optimizing data retrieval, making them essential for both small-scale and enterprise-level applications. Examples of popular DBMS include MySQL, Oracle, and PostgreSQL.'),
    (102, 'chap01', 'Sec01', 'Block01', 1, 'The history of software engineering dates back to the 1960s, when the "software crisis" highlighted the need for structured approaches to software development due to rising complexity and project failures. Over time, methodologies such as Waterfall, Agile, and DevOps evolved, transforming software engineering into a disciplined, iterative process that emphasizes efficiency, collaboration, and adaptability.'),
    (102, 'chap02', 'Sec01', 'Block01', 1, 'The Software Development Life Cycle (SDLC) consists of key phases including requirements gathering, design, development, testing, deployment, and maintenance. Each phase plays a crucial role in ensuring that software is built systematically, with feedback and revisions incorporated at each step to deliver a high-quality product.'),
    (103, 'chap01', 'Sec01', 'Block01', 1, 'Machine learning is a subset of artificial intelligence that enables systems to learn from data, identify patterns, and make decisions with minimal human intervention. By training algorithms on vast datasets, machine learning models can improve their accuracy over time, driving advancements in fields like healthcare, finance, and autonomous systems.');

INSERT INTO image (textbook_id, chapter_id, section_id, block_id, image_id, image_content, alt_text)
VALUES 
    (101, 'chap02', 'Sec02', 'Block01', 1, 'sample.png', 'Sample image for DBMS examples'),
    (102, 'chap02', 'Sec02', 'Block01', 1, 'sample2.png', 'Sample image for SDLC phases');


-- Insert activities
INSERT INTO activity (textbook_id, chapter_id, section_id, block_id, activity_id, is_hidden, created_by, updated_by)
VALUES
(101, 'chap01', 'Sec02', 'Block01', 'ACT0', FALSE, 'saitama', 'saitama'),
(102, 'chap01', 'Sec02', 'Block01', 'ACT0', FALSE, 'saitama', 'saitama'),
(103, 'chap01', 'Sec02', 'Block01', 'ACT0', FALSE, 'saitama', 'saitama');

-- Insert Questions
INSERT INTO question (textbook_id, chapter_id, section_id, block_id, activity_id, question_id, question_text, option1, option1_explanation, option2, option2_explanation, option3, option3_explanation, option4, option4_explanation, correct_answer, is_hidden, created_by, updated_by)
VALUES
-- Questions for Activity ACT0 in DBMS Chapter 1, Section 2
(101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 'What does a DBMS provide?', 'Data storage only', 'Incorrect: DBMS provides more than just storage', 'Data storage and retrieval', 'Correct: DBMS manages both storing and retrieving data', 'Only security features', 'Incorrect: DBMS also handles other functions', 'Network management', 'Incorrect: DBMS does not manage network infrastructure', 2, FALSE, 'saitama', 'saitama'),
(101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q2', 'Which of these is an example of a DBMS?', 'Microsoft Excel', 'Incorrect: Excel is a spreadsheet application', 'MySQL', 'Correct: MySQL is a popular DBMS', 'Google Chrome', 'Incorrect: Chrome is a web browser', 'Windows 10', 'Incorrect: Windows is an operating system', 2, FALSE, 'saitama', 'saitama'),
(101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q3', 'What type of data does a DBMS manage?', 'Structured data', 'Correct: DBMS primarily manages structured data', 'Unstructured multimedia', 'Incorrect: While some DBMS systems can handle it, it''s not core', 'Network traffic data', 'Incorrect: DBMS doesn’t manage network data', 'Hardware usage statistics', 'Incorrect: DBMS does not handle hardware usage data', 1, FALSE, 'saitama', 'saitama'),

-- Questions for Activity ACT0 in Software Engineering Chapter 1, Section 2
(102, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 'What was the "software crisis"?', 'A hardware shortage', 'Incorrect: The crisis was related to software development issues', 'Difficulty in software creation', 'Correct: The crisis was due to the complexity and unreliability of software', 'A network issue', 'Incorrect: It was not related to networking', 'Lack of storage devices', 'Incorrect: The crisis was not about physical storage limitations', 2, FALSE, 'saitama', 'saitama'),
(102, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q2', 'Which methodology was first introduced in software engineering?', 'Waterfall model', 'Correct: Waterfall was the first formal software development model', 'Agile methodology', 'Incorrect: Agile was introduced much later', 'DevOps', 'Incorrect: DevOps is a more recent development approach', 'Scrum', 'Incorrect: Scrum is a part of Agile, not the first methodology', 1, FALSE, 'saitama', 'saitama'),
(102, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q3', 'What challenge did early software engineering face?', 'Lack of programming languages', 'Incorrect: Programming languages existed but were difficult to manage', 'Increasing complexity of software', 'Correct: Early engineers struggled with managing large, complex systems', 'Poor hardware development', 'Incorrect: The issue was primarily with software, not hardware', 'Internet connectivity issues', 'Incorrect: Internet connectivity wasn''t a challenge in early software', 2, FALSE, 'saitama', 'saitama'),

-- Questions for Activity ACT0 in Machine Learning Chapter 1, Section 2
(103, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 'What is the primary goal of supervised learning?', 'Predict outcomes', 'Correct: The goal is to learn a mapping from inputs to outputs for prediction.', 'Group similar data', 'Incorrect: This is more aligned with unsupervised learning.', 'Discover patterns', 'Incorrect: This is not the main goal of supervised learning.', 'Optimize cluster groups', 'Incorrect: This is not applicable to supervised learning.', 1, FALSE, 'saitama', 'saitama'),
(103, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q2', 'Which type of data is used in unsupervised learning?', 'Labeled data', 'Incorrect: Unsupervised learning uses unlabeled data.', 'Unlabeled data', 'Correct: It analyzes data without pre-existing labels.', 'Structured data', 'Incorrect: Unlabeled data can be structured or unstructured.', 'Time-series data', 'Incorrect: Unsupervised learning does not specifically focus on time-series.', 2, FALSE, 'saitama', 'saitama'),
(103, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q3', 'In which scenario would you typically use supervised learning?', 'Customer segmentation', 'Incorrect: This is more relevant to unsupervised learning.', 'Fraud detection', 'Correct: Supervised learning is ideal for predicting fraud based on labeled examples.', 'Market basket analysis', 'Incorrect: This is generally done using unsupervised methods.', 'Anomaly detection', 'Incorrect: While applicable, it is less common than fraud detection in supervised learning.', 2, FALSE, 'saitama', 'saitama');

INSERT INTO score (course_id, textbook_id, chapter_id, section_id, block_id, activity_id, question_id, score, timestamp, stud_id) VALUES
('NCSUOganCSC440F24', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 3, '2024-08-01 11:10:00', 'ErPe1024'),
('NCSUOganCSC440F24', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q2', 1, '2024-08-01 14:18:00', 'ErPe1024'),
('NCSUOganCSC540F24', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 1, '2024-08-02 19:06:00', 'ErPe1024'),
('NCSUOganCSC440F24', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 3, '2024-08-01 13:24:00', 'AlAr1024'),
('NCSUOganCSC440F24', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 0, '2024-08-01 09:24:00', 'BoTe1024'),
('NCSUOganCSC440F24', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 3, '2024-08-01 07:45:00', 'LiGa1024'),
('NCSUOganCSC440F24', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q2', 3, '2024-08-01 12:30:00', 'LiGa1024'),
('NCSUOganCSC540F24', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 3, '2024-08-03 16:52:00', 'LiGa1024'),
('NCSUOganCSC440F24', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 1, '2024-08-01 21:18:00', 'ArMo1024'),
('NCSUOganCSC440F24', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q2', 3, '2024-08-01 05:03:00', 'ArMo1024'),
('NCSUSaraCSC326F24', 102, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 1, '2024-08-29 22:41:00', 'FiWi1024');