-- TODO: According to the new ER Diagrams, change the INSERT queries

INSERT INTO textbook (textbook_id, title, created_by, updated_by) VALUES 
(101, 'Database Management Systems', 1, 1),
(102, 'Fundamentals of Software Engineering', 1, 1),
(103, 'Fundamentals of Machine Learning', 1, 1);

INSERT INTO chapter (textbook_id, chapter_number, title, is_hidden, created_by, updated_by) VALUES 
(101, 'chap01', 'Introduction to Database', FALSE, 1, 1),
(101, 'chap02', 'The Relational Model', FALSE, 1, 1),
(102, 'chap01', 'Introduction to Software Engineering', FALSE, 1, 1),
(102, 'chap02', 'Introduction to Software Development Life Cycle (SDLC)', FALSE, 1, 1),
(103, 'chap01', 'Introduction to Machine Learning', FALSE, 1, 1);

INSERT INTO section (chapter_id, section_no, title, is_hidden, created_by, updated_by) VALUES 
(1, 'Sec01', 'Database Management Systems (DBMS) Overview', FALSE, 1, 1),
(1, 'Sec02', 'Data Models and Schemas', FALSE, 1, 1),
(2, 'Sec01', 'Entities, Attributes, and Relationships', FALSE, 1, 1),
(2, 'Sec02', 'Normalization and Integrity Constraints', FALSE, 1, 1),
(3, 'Sec01', 'History and Evolution of Software Engineering', FALSE, 1, 1),
(3, 'Sec02', 'Key Principles of Software Engineering', FALSE, 1, 1),
(4, 'Sec01', 'Phases of the SDLC', TRUE, 1, 1),
(4, 'Sec02', 'Agile vs. Waterfall Models', FALSE, 1, 1),
(5, 'Sec01', 'Overview of Machine Learning', TRUE, 1, 1),
(5, 'Sec02', 'Supervised vs Unsupervised Learning', FALSE, 1, 1);

INSERT INTO content_block (section_id, block_no, is_type, is_hidden, created_by, updated_by) VALUES 
(1, 'Block01', 'text', FALSE, 1, 1),
(1, 'Block02', 'activity', FALSE, 1, 1),
(2, 'Block01', 'text', FALSE, 1, 1),
(2, 'Block02', 'picture', FALSE, 1, 1),
(3, 'Block01', 'text', FALSE, 1, 1),
(3, 'Block02', 'activity', FALSE, 1, 1),
(4, 'Block01', 'text', FALSE, 1, 1),
(4, 'Block02', 'picture', FALSE, 1, 1),
(5, 'Block01', 'text', FALSE, 1, 1),
(5, 'Block02', 'activity', FALSE, 1, 1);

INSERT INTO text(content_block_id, text_content) VALUES
(1, 'A Database Management System (DBMS) is software that enables users to efficiently create, manage, and manipulate databases. It serves as an interface between the database and end users, ensuring data is stored securely, retrieved accurately, and maintained consistently. Key features of a DBMS include data organization, transaction management, and support for multiple users accessing data concurrently.'),
(3, 'DBMS systems provide structured storage and ensure that data is accessible through queries using languages like SQL. They handle critical tasks such as maintaining data integrity, enforcing security protocols, and optimizing data retrieval, making them essential for both small-scale and enterprise-level applications. Examples of popular DBMS include MySQL, Oracle, and PostgreSQL.'),
(5, 'The history of software engineering dates back to the 1960s, when the "software crisis" highlighted the need for structured approaches to software development due to rising complexity and project failures. Over time, methodologies such as Waterfall, Agile, and DevOps evolved, transforming software engineering into a disciplined, iterative process that emphasizes efficiency, collaboration, and adaptability.'),
(7, 'The Software Development Life Cycle (SDLC) consists of key phases including requirements gathering, design, development, testing, deployment, and maintenance. Each phase plays a crucial role in ensuring that software is built systematically, with feedback and revisions incorporated at each step to deliver a high-quality product.'),
(9, 'Machine learning is a subset of artificial intelligence that enables systems to learn from data, identify patterns, and make decisions with minimal human intervention. By training algorithms on vast datasets, machine learning models can improve their accuracy over time, driving advancements in fields like healthcare, finance, and autonomous systems.');

INSERT INTO image(content_block_id, image_content) VALUES
(4, 'sample.png'),
(8, 'sample2.png');

INSERT INTO activity(section_id, is_hidden, created_by, updated_by) VALUES
(2,FALSE,1,1),
(6,FALSE,1,1),
(10,FALSE,1,1);

INSERT INTO question (activity_id, question_no, question_text, option1, option1_explanation, option2, option2_explanation, option3, option3_explanation, option4, option4_explanation, correct_answer, is_hidden, created_by, updated_by) VALUES 
(1, 'Q1', 'What does a DBMS provide?', 'Data storage only', 'Incorrect: DBMS provides more than just storage', 'Data storage and retrieval', 'Correct: DBMS manages both storing and retrieving data', 'Only security features', 'Incorrect: DBMS also handles other functions', 'Network management', 'Incorrect: DBMS does not manage network infrastructure', 2, FALSE, 1, 1),
(1, 'Q2', 'Which of these is an example of a DBMS?', 'Microsoft Excel', 'Incorrect: Excel is a spreadsheet application', 'MySQL', 'Correct: MySQL is a popular DBMS', 'Google Chrome', 'Incorrect: Chrome is a web browser', 'Windows 10', 'Incorrect: Windows is an operating system', 2, FALSE, 1, 1),
(1, 'Q3', 'What type of data does a DBMS manage?', 'Structured data', 'Correct: DBMS primarily manages structured data', 'Unstructured multimedia', 'Incorrect: While some DBMS systems can handle it, it''s not core', 'Network traffic data', 'Incorrect: DBMS doesn’t manage network data', 'Hardware usage statistics', 'Incorrect: DBMS does not handle hardware usage data', 1, FALSE, 1, 1),
(2, 'Q1', 'What was the ''software crisis''?', 'A hardware shortage', 'Incorrect: The crisis was related to software development issues', 'Difficulty in software creation', 'Correct: The crisis was due to the complexity and unreliability of software', 'A network issue', 'Incorrect: It was not related to networking', 'Lack of storage devices', 'Incorrect: The crisis was not about physical storage limitations', 2, FALSE, 1, 1),
(2, 'Q2', 'Which methodology was first introduced in software engineering?', 'Waterfall model', 'Correct: Waterfall was the first formal software development model', 'Agile methodology', 'Incorrect: Agile was introduced much later', 'DevOps', 'Incorrect: DevOps is a more recent development approach', 'Scrum', 'Incorrect: Scrum is a part of Agile, not the first methodology', 1, FALSE, 1, 1),
(2, 'Q3', 'What challenge did early software engineering face?', 'Lack of programming languages', 'Incorrect: Programming languages existed but were difficult to manage', 'Increasing complexity of software', 'Correct: Early engineers struggled with managing large, complex systems', 'Poor hardware development', 'Incorrect: The issue was primarily with software, not hardware', 'Internet connectivity issues', 'Incorrect: Internet connectivity wasn''t a challenge in early software', 2, FALSE, 1, 1),
(3, 'Q1', 'What is the primary goal of supervised learning?', 'Predict outcomes', 'Correct: The goal is to learn a mapping from inputs to outputs for prediction.', 'Group similar data', 'Incorrect: This is more aligned with unsupervised learning.', 'Discover patterns', 'Incorrect: This is not the main goal of supervised learning.', 'Optimize cluster groups', 'Incorrect: This is not applicable to supervised learning.', 1, FALSE, 1, 1),
(3, 'Q2', 'Which type of data is used in unsupervised learning?', 'Labeled data', 'Incorrect: Unsupervised learning uses unlabeled data.', 'Unlabeled data', 'Correct: It analyzes data without pre-existing labels.', 'Structured data', 'Incorrect: Unlabeled data can be structured or unstructured.', 'Time-series data', 'Incorrect: Unsupervised learning does not specifically focus on time-series.', 2, FALSE, 1, 1),
(3, 'Q3', 'In which scenario would you typically use supervised learning?', 'Customer segmentation', 'Incorrect: This is more relevant to unsupervised learning.', 'Fraud detection', 'Correct: Supervised learning is ideal for predicting fraud based on labeled examples.', 'Market basket analysis', 'Incorrect: This is generally done using unsupervised methods.', 'Anomaly detection', 'Incorrect: While applicable, it is less common than fraud detection in supervised learning.', 2, FALSE, 1, 1);
