INSERT INTO user (user_id, email, first_name, last_name, password, role_no)
VALUES
-- ADMIN
('saitama', 'admin@ncsu.test', 'adminFirst', 'adminLast', 'password@123', 1),
-- FACULTY
('KeOg1024', 'kogan@ncsu.edu', 'Kemafor', 'Ogan', 'Ko2024!rpc', 2),
('JoDo1024', 'john.doe@example.com', 'John', 'Doe', 'Jd2024!abc', 2),
('SaMi1024', 'sarah.miller@domain.com', 'Sarah', 'Miller', 'Sm#Secure2024', 2),
('DaBr1024', 'david.b@webmail.com', 'David', 'Brown', 'DbPass123!', 2),
('EmDa1024', 'emily.davis@email.com', 'Emily', 'Davis', 'Emily#2024!', 2),
('MiWi1024', 'michael.w@service.com', 'Michael', 'Wilson', 'Mw987secure', 2),
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
('JaWi1024', 'jwilliams@ncsu.edu', 'James', 'Williams', 'jwilliams@1234', 4),
('LiAl0924', 'lalberti@ncsu.edu', 'Lisa', 'Alberti', 'lalberti&5678@', 4),
('DaJo1024', 'djohnson@ncsu.edu', 'David', 'Johnson', 'djohnson%@1122', 4),
('ElCl1024', 'eclark@ncsu.edu', 'Ellie', 'Clark', 'eclark^#3654', 4),
('JeGi0924', 'jgibson@ncsu.edu', 'Jeff', 'Gibson', 'jgibson$#9877', 4);

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

INSERT INTO teaching_assistant (ta_id, course_id, fac_id) VALUES
('JaWi1024', 'NCSUOganCSC440F24', 'KeOg1024'),
('LiAl0924', 'NCSUOganCSC540F24', 'KeOg1024'),
('DaJo1024', 'NCSUSaraCSC326F24', 'SaMi1024'),
('ElCl1024', 'NCSUJegiCSC522F24', 'JeGi0524'),
('JeGi0924', 'NCSUSaraCSC326F25', 'SaMi1024');

INSERT INTO faculty (fac_id) VALUES
('KeOg1024'),
('JoDo1024'),
('SaMi1024'),
('DaBr1024'),
('EmDa1024'),
('MiWi1024');