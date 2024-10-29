CREATE TABLE user (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    role_no INT NOT NULL
);

CREATE TABLE textbook (
    textbook_id INT PRIMARY KEY AUTO_INCREMENT,          
    title VARCHAR(255) NOT NULL,         
    created_by INT NOT NULL,              
    updated_by INT NOT NULL,
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE admin (
    admin_id INT PRIMARY KEY,
    FOREIGN KEY (admin_id) REFERENCES user(user_id)
);

CREATE TABLE faculty (
    fac_id INT PRIMARY KEY,
    FOREIGN KEY (fac_id) REFERENCES user(user_id)
);

CREATE TABLE student (
    stud_id INT PRIMARY KEY,
    FOREIGN KEY (stud_id) REFERENCES user(user_id)
);

CREATE TABLE teaching_assistant (
    ta_id INT PRIMARY KEY,
    course_id INT,
    FOREIGN KEY (ta_id) REFERENCES user(user_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

CREATE TABLE course (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    admin_id INT NOT NULL,
    fac_id INT NOT NULL,
    textbook_id INT NOT NULL,
    FOREIGN KEY (admin_id) REFERENCES admin(admin_id),
    FOREIGN KEY (fac_id) REFERENCES faculty(fac_id),
    FOREIGN KEY (textbook_id) REFERENCES textbook(textbook_id)
);

CREATE TABLE active_course (
    token CHAR(7) PRIMARY KEY,
    capacity INT NOT NULL,
    course_id INT NOT NULL, 
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

CREATE TABLE enroll (
    is_approved BOOLEAN NOT NULL,
    is_waiting BOOLEAN NOT NULL,
    stud_id INT,
    token CHAR(7), 
    FOREIGN KEY (token) REFERENCES active_course(token),
    FOREIGN KEY (stud_id) REFERENCES student(stud_id),
    PRIMARY KEY (stud_id, token)
);

CREATE TABLE chapter (
    chapter_id INT PRIMARY KEY AUTO_INCREMENT,
    textbook_id INT,
    chapter_number INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    is_hidden BOOLEAN NOT NULL,
    created_by INT NOT NULL,
    updated_by INT NOT NULL,
    FOREIGN KEY (textbook_id) REFERENCES textbook(textbook_id),
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE section (
    section_id INT PRIMARY KEY AUTO_INCREMENT,
    chapter_id INT,
    section_no INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    is_hidden BOOLEAN NOT NULL,
    created_by INT NOT NULL,
    updated_by INT NOT NULL,
    FOREIGN KEY (chapter_id) REFERENCES chapter(chapter_id),
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE content_block (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(50) NOT NULL,
    section_id INT,
    is_hidden BOOLEAN NOT NULL,
    created_by INT NOT NULL,
    updated_by INT NOT NULL,
    FOREIGN KEY (section_id) REFERENCES section(section_id),
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE text (
    text_id INT PRIMARY KEY AUTO_INCREMENT,
    text_content TEXT NOT NULL
);

CREATE TABLE image (
    image_id INT PRIMARY KEY AUTO_INCREMENT,
    image_content BLOB NOT NULL,
    alt_text VARCHAR(255)
);

CREATE TABLE activity (
    activity_id INT PRIMARY KEY AUTO_INCREMENT,
    section_id INT,
    question_id INT,
    question_text TEXT NOT NULL,
    is_hidden BOOLEAN NOT NULL,
    created_by INT NOT NULL,
    updated_by INT NOT NULL,
    FOREIGN KEY (section_id) REFERENCES section(section_id),
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE answer_choice (
    option_id INT PRIMARY KEY AUTO_INCREMENT,
    option_text TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    explanation TEXT,
    activity_id INT,
    is_hidden BOOLEAN NOT NULL,
    created_by INT NOT NULL,
    updated_by INT NOT NULL,
    FOREIGN KEY (activity_id) REFERENCES activity(activity_id),
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE notification (
    notif_id INT PRIMARY KEY AUTO_INCREMENT,
    message TEXT NOT NULL,
    stud_id INT,
    FOREIGN KEY (stud_id) REFERENCES student(stud_id) 
);

CREATE TABLE score (
    score INT NOT NULL,
    timestamp DATETIME NOT NULL,
    stud_id INT,
    activity_id INT,
    PRIMARY KEY (stud_id, activity_id),
    FOREIGN KEY (stud_id) REFERENCES student(stud_id),
    FOREIGN KEY (activity_id) REFERENCES activity(activity_id) 
);
