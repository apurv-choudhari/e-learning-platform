CREATE TABLE user (
    user_id VARCHAR(255) PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    role_no INT NOT NULL
);

CREATE TABLE textbook (
    textbook_id INT PRIMARY KEY,          
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

CREATE TABLE course (
    course_id  VARCHAR(255) PRIMARY KEY,
    textbook_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    admin_id VARCHAR(255) NOT NULL,
    fac_id VARCHAR(255) NOT NULL,
    FOREIGN KEY (admin_id) REFERENCES admin(admin_id),
    FOREIGN KEY (fac_id) REFERENCES faculty(fac_id),
    FOREIGN KEY (textbook_id) REFERENCES textbook(textbook_id)
);

CREATE TABLE teaching_assistant (
    ta_id VARCHAR(255) PRIMARY KEY,
    course_id VARCHAR(255) NOT NULL,
    fac_id VARCHAR(255) NOT NULL,
    FOREIGN KEY (ta_id) REFERENCES user(user_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id),
    FOREIGN KEY (fac_id) REFERENCES faculty(fac_id)
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
    textbook_id INT NOT NULL,
    chapter_id VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    is_hidden BOOLEAN NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255) NOT NULL,
    PRIMARY KEY (textbook_id, chapter_id),
    FOREIGN KEY (textbook_id) REFERENCES textbook(textbook_id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE section (
    textbook_id INT NOT NULL,
    chapter_id VARCHAR(255) NOT NULL,
    section_id VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    is_hidden BOOLEAN NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255) NOT NULL,
    PRIMARY KEY (textbook_id, chapter_id, section_id),
    FOREIGN KEY (textbook_id, chapter_id) REFERENCES chapter(textbook_id, chapter_id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES user(user_id),
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE content_block (
    textbook_id INT NOT NULL,
    chapter_id VARCHAR(255) NOT NULL,
    section_id VARCHAR(255) NOT NULL,
    block_id VARCHAR(255) NOT NULL,
    is_type VARCHAR(50) NOT NULL,
    is_hidden BOOLEAN NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255) NOT NULL,
    PRIMARY KEY (textbook_id, chapter_id, section_id, block_id),
    FOREIGN KEY (textbook_id, chapter_id, section_id) REFERENCES section(textbook_id, chapter_id, section_id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE text (
    textbook_id INT NOT NULL,
    chapter_id VARCHAR(255) NOT NULL,
    section_id VARCHAR(255) NOT NULL,
    block_id VARCHAR(255) NOT NULL,
    text_id INT NOT NULL,
    text_content TEXT NOT NULL,
    PRIMARY KEY (textbook_id, chapter_id, section_id, block_id, text_id),
    FOREIGN KEY (textbook_id, chapter_id, section_id, block_id) REFERENCES content_block(textbook_id, chapter_id, section_id, block_id) ON DELETE CASCADE
);

CREATE TABLE image (
    textbook_id INT NOT NULL,
    chapter_id VARCHAR(255) NOT NULL,
    section_id VARCHAR(255) NOT NULL,
    block_id VARCHAR(255) NOT NULL,
    image_id INT NOT NULL,
    image_content VARCHAR(255) NOT NULL,
    alt_text VARCHAR(255),
    PRIMARY KEY (textbook_id, chapter_id, section_id, block_id, image_id),
    FOREIGN KEY (textbook_id, chapter_id, section_id, block_id) REFERENCES content_block(textbook_id, chapter_id, section_id, block_id) ON DELETE CASCADE
);

CREATE TABLE activity (
    textbook_id INT NOT NULL,
    chapter_id VARCHAR(255) NOT NULL,
    section_id VARCHAR(255) NOT NULL,
    block_id VARCHAR(255) NOT NULL,
    activity_id VARCHAR(255) NOT NULL,
    is_hidden BOOLEAN NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255) NOT NULL,
    PRIMARY KEY (textbook_id, chapter_id, section_id, block_id, activity_id),
    FOREIGN KEY (textbook_id, chapter_id, section_id, block_id) REFERENCES content_block(textbook_id, chapter_id, section_id, block_id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES user(user_id), 
    FOREIGN KEY (updated_by) REFERENCES user(user_id)
);

CREATE TABLE question (
    textbook_id INT NOT NULL,
    chapter_id VARCHAR(255) NOT NULL,
    section_id VARCHAR(255) NOT NULL,
    block_id VARCHAR(255) NOT NULL,
    activity_id VARCHAR(255) NOT NULL,
    question_id VARCHAR(255) NOT NULL,
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
    is_hidden BOOLEAN NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255) NOT NULL,
    PRIMARY KEY (textbook_id, chapter_id, section_id, block_id, activity_id, question_id),
    FOREIGN KEY (textbook_id, chapter_id, section_id, block_id, activity_id) REFERENCES activity(textbook_id, chapter_id, section_id, block_id, activity_id) ON DELETE CASCADE,
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
    course_id VARCHAR(255) NOT NULL,
    textbook_id INT NOT NULL,
    chapter_id VARCHAR(255) NOT NULL,
    section_id VARCHAR(255) NOT NULL,
    block_id VARCHAR(255) NOT NULL,
    activity_id VARCHAR(255) NOT NULL,
    question_id VARCHAR(255) NOT NULL,
    score INT NOT NULL,
    timestamp DATETIME NOT NULL,
    stud_id VARCHAR(255) NOT NULL,
    PRIMARY KEY (course_id, stud_id, textbook_id, chapter_id, section_id, block_id, activity_id, question_id),
    FOREIGN KEY (textbook_id, chapter_id, section_id, block_id, activity_id, question_id) REFERENCES question(textbook_id, chapter_id, section_id, block_id, activity_id, question_id)ON DELETE CASCADE,
    FOREIGN KEY (stud_id) REFERENCES student(stud_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);
