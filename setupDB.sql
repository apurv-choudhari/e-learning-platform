CREATE TABLE user (
    user_id VARCHAR(255) PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    role_no INT NOT NULL
);

CREATE TABLE textbook (
    textbook_id INT PRIMARY KEY AUTO_INCREMENT,          
    title VARCHAR(255) NOT NULL,         
    created_by VARCHAR(255) NOT NULL,             
    updated_by VARCHAR(255) NOT NULL,
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE admin (
    admin_id VARCHAR(255) PRIMARY KEY,
    FOREIGN KEY (admin_id) REFERENCES user(user_id)
);

CREATE TABLE faculty (
    fac_id VARCHAR(255) PRIMARY KEY,
    FOREIGN KEY (fac_id) REFERENCES user(user_id)
);

CREATE TABLE student (
    stud_id VARCHAR(255) PRIMARY KEY,
    FOREIGN KEY (stud_id) REFERENCES user(user_id)
);

CREATE TABLE teaching_assistant (
    ta_id VARCHAR(255) PRIMARY KEY,
    course_id VARCHAR(255),
    FOREIGN KEY (ta_id) REFERENCES user(user_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

CREATE TABLE course (
    course_id  VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    admin_id VARCHAR(255) NOT NULL,
    fac_id VARCHAR(255) NOT NULL,
    textbook_id INT NOT NULL,
    FOREIGN KEY (admin_id) REFERENCES admin(admin_id),
    FOREIGN KEY (fac_id) REFERENCES faculty(fac_id),
    FOREIGN KEY (textbook_id) REFERENCES textbook(textbook_id)
);

CREATE TABLE active_course (
    token CHAR(6) PRIMARY KEY,
    capacity INT NOT NULL,
    course_id VARCHAR(255) NOT NULL,
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

CREATE TABLE enroll (
    is_approved BOOLEAN NOT NULL,
    stud_id VARCHAR(255),
    course_id VARCHAR(255), 
    FOREIGN KEY (course_id) REFERENCES course(course_id),
    FOREIGN KEY (stud_id) REFERENCES student(stud_id),
    PRIMARY KEY (stud_id, course_id)
);

CREATE TABLE chapter (
    chapter_id INT PRIMARY KEY AUTO_INCREMENT,
    textbook_id INT,
    chapter_number VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    is_hidden BOOLEAN NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255) NOT NULL,
    FOREIGN KEY (textbook_id) REFERENCES textbook(textbook_id),
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE section (
    section_id INT PRIMARY KEY AUTO_INCREMENT,
    chapter_id INT,
    section_no VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    is_hidden BOOLEAN NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255) NOT NULL,
    FOREIGN KEY (chapter_id) REFERENCES chapter(chapter_id),
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE content_block (
    content_block_id INT PRIMARY KEY AUTO_INCREMENT,
    is_type VARCHAR(50) NOT NULL,
    section_id INT,
    block_no VARCHAR(255) NOT NULL,
    is_hidden BOOLEAN NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255) NOT NULL,
    FOREIGN KEY (section_id) REFERENCES section(section_id),
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE text (
    text_id INT PRIMARY KEY AUTO_INCREMENT,
    content_block_id INT NOT NULL,
    text_content TEXT NOT NULL,
    FOREIGN KEY (content_block_id) REFERENCES content_block(content_block_id)
);

CREATE TABLE image (
    image_id INT PRIMARY KEY AUTO_INCREMENT,
    content_block_id INT NOT NULL,
    image_content BLOB NOT NULL,
    alt_text VARCHAR(255),
    FOREIGN KEY (content_block_id) REFERENCES content_block(content_block_id)
);

CREATE TABLE activity (
    activity_id INT PRIMARY KEY AUTO_INCREMENT,
    section_id INT,
    is_hidden BOOLEAN NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255) NOT NULL,
    FOREIGN KEY (section_id) REFERENCES section(section_id),
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE question(
    question_id INT PRIMARY KEY AUTO_INCREMENT,
    question_no VARCHAR(255),
    question_text TEXT NOT NULL,
    option1 VARCHAR(255) NOT NULL,
    option1_explanation TEXT NOT NULL,
    option2 VARCHAR(255) NOT NULL,
    option2_explanation TEXT NOT NULL,
    option3 VARCHAR(255) NOT NULL,
    option3_explanation TEXT NOT NULL,
    option4 VARCHAR(255) NOT NULL,
    option4_explanation VARCHAR(255) NOT NULL,
    correct_answer INT NOT NULL,
    activity_id INT NOT NULL, 
    is_hidden BOOLEAN NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255) NOT NULL,
    FOREIGN KEY(activity_id) REFERENCES activity(activity_id),
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);


CREATE TABLE notification (
    notif_id INT PRIMARY KEY AUTO_INCREMENT,
    message TEXT NOT NULL,
    stud_id VARCHAR(255),
    FOREIGN KEY (stud_id) REFERENCES student(stud_id) 
);

CREATE TABLE score (
    score INT NOT NULL,
    timestamp DATETIME NOT NULL,
    stud_id VARCHAR(255),
    activity_id INT,
    PRIMARY KEY (stud_id, activity_id),
    FOREIGN KEY (stud_id) REFERENCES student(stud_id),
    FOREIGN KEY (activity_id) REFERENCES activity(activity_id) 
);
