from mysql.connector import Error
from flow.admin.admin_db_utils import connectDB

def execute_query(query_num, param_list):
    conn, cursor = connectDB()
    if conn is None or cursor is None:
        print("Database connection failed.")
        return

    # TODO:
    # Write queries here
    queries = {
        1: "SELECT COUNT(section_id) FROM section WHERE chapter_id = 'chap01' AND textbook_id = %s;",
        2: """SELECT 
                c.title AS Course_Title,
                u.first_name AS Person_First_Name,
                u.last_name AS Person_Last_Name,
                CASE 
                    WHEN f.fac_id IS NOT NULL THEN 'Faculty'
                    WHEN ta.ta_id IS NOT NULL THEN 'Teaching Assistant'
                END AS Role
            FROM 
                course c
            LEFT JOIN 
                faculty f ON c.fac_id = f.fac_id
            LEFT JOIN 
                teaching_assistant ta ON c.course_id = ta.course_id
            LEFT JOIN 
                user u ON (u.user_id = f.fac_id OR u.user_id = ta.ta_id)
            ORDER BY 
                c.title, Role, u.first_name, u.last_name;
            """,
        3: """SELECT c.course_id, c.fac_id AS faculty_member, COUNT(e.stud_id) AS total_students
            FROM course c
            JOIN active_course ac ON c.course_id = ac.course_id
            LEFT JOIN enroll e ON c.course_id = e.course_id AND e.is_approved = TRUE
            GROUP BY c.course_id, c.fac_id; """,
        4: """SELECT e.course_id, COUNT(e.stud_id) AS waiting_list_count
            FROM enroll e
            JOIN course c ON e.course_id = c.course_id
            WHERE e.is_approved = FALSE
            GROUP BY e.course_id
            ORDER BY waiting_list_count DESC
            LIMIT 1;
            ;""",
        5: """SELECT s.section_id,s.title AS section_title,c.block_id, c.is_type AS block_type,t.text_content AS text,i.image_content AS image,a.activity_id AS activity_id
            FROM section s
            JOIN content_block c ON s.textbook_id = c.textbook_id AND s.chapter_id = c.chapter_id AND s.section_id = c.section_id
            LEFT JOIN text t ON c.textbook_id = t.textbook_id AND c.chapter_id = t.chapter_id AND c.section_id = t.section_id AND c.block_id = t.block_id
            LEFT JOIN image i ON c.textbook_id = i.textbook_id AND c.chapter_id = i.chapter_id AND c.section_id = i.section_id AND c.block_id = i.block_id
            LEFT JOIN activity a ON c.textbook_id = a.textbook_id AND c.chapter_id = a.chapter_id AND c.section_id = a.section_id AND c.block_id = a.block_id
            WHERE s.textbook_id = 101 AND s.chapter_id = 'chap02'
            ORDER BY s.section_id, c.block_id""",
        6: """SELECT 
                CASE 
                    WHEN correct_answer != 1 THEN option1 
                    ELSE NULL 
                END AS incorrect_answer, 
                CASE 
                    WHEN correct_answer != 1 THEN option1_explanation 
                    ELSE NULL 
                END AS explanation
            FROM question
            WHERE textbook_id = 101 
                AND chapter_id = 'chap01' 
                AND section_id = 'Sec02' 
                AND block_id = 'Block01' 
                AND activity_id = 'ACT0' 
                AND question_id = 'Q2'
            UNION ALL
            SELECT 
                CASE 
                    WHEN correct_answer != 3 THEN option3 
                    ELSE NULL 
                END AS incorrect_answer, 
                CASE 
                    WHEN correct_answer != 3 THEN option3_explanation 
                    ELSE NULL 
                END AS explanation
            FROM question
            WHERE textbook_id = 101 
                AND chapter_id = 'chap01' 
                AND section_id = 'Sec02' 
                AND block_id = 'Block01' 
                AND activity_id = 'ACT0' 
                AND question_id = 'Q2'
            UNION ALL
            SELECT 
                CASE 
                    WHEN correct_answer != 4 THEN option4 
                    ELSE NULL 
                END AS incorrect_answer, 
                CASE 
                    WHEN correct_answer != 4 THEN option4_explanation 
                    ELSE NULL 
                END AS explanation
            FROM question
            WHERE textbook_id = 101 
                AND chapter_id = 'chap01' 
                AND section_id = 'Sec02' 
                AND block_id = 'Block01' 
                AND activity_id = 'ACT0' 
                AND question_id = 'Q2';
            """,
        7: """
            SELECT 
                t.title AS textbook_title,
                c1.course_id AS active_course_id,
                c1.fac_id AS active_instructor,
                c2.course_id AS evaluation_course_id,
                c2.fac_id AS evaluation_instructor
            FROM 
                textbook t
            JOIN 
                course c1 ON t.textbook_id = c1.textbook_id
            JOIN 
                active_course ac ON c1.course_id = ac.course_id
            JOIN 
                course c2 ON t.textbook_id = c2.textbook_id
            LEFT JOIN 
                active_course ac2 ON c2.course_id = ac2.course_id
            WHERE 
                c1.fac_id <> c2.fac_id
                AND ac2.course_id IS NULL
                AND c1.textbook_id = c2.textbook_id;
        """
    }

    try:
        query = queries.get(query_num)
        if query:
            cursor.execute(query, param_list)
            if query_num in {1, 2, 3, 4, 5, 6, 7}:
                results = cursor.fetchall()
                for row in results:
                    print(row)
            else:
                print("Invalid query number.")

    except Error as e:
        print(f"An error occurred while executing query {query_num}: {e}")

    finally:
        cursor.close()
        conn.close()


def params_for_query_1():
    tid = input("Provide Textbook-id: ")
    return [tid]

def no_params():
    return []

get_query_params = {
    "1": params_for_query_1,
    "2": no_params,
    "3": no_params,
    "4": no_params,
    "5" : no_params,
    "6": no_params,
    "7": no_params
}

def test_user_queries():
    while True:
        print("\n--- Query Executor ---")
        print("1. Query 1: Write a query that prints the number of sections of the first chapter of a textbook.")
        print("2. Execute Query 2: Print the names of faculty and TAs of all courses. For each person print their role next to their names.")
        print("3. Execute Query 3: For each active course, print the course id, faculty member and total number of students")
        print("4. Execute Query 4: Find the course which the largest waiting list, print the course id and the total number ofpeople on the list")
        print("5. Execute Query 5: Print the contents of Chapter 02 of textbook 101 in proper sequence.")
        print("6. Execute Query 6: For Q2 of Activity0 in Sec02 of Chap01 in textbook 101, print the incorrect answers for that question and their corresponding explanations.")
        print("7. Execute Query 7: Find any book that is in active status by one instructor but evaluation status by a different instructor.")
        print("8. Back to Main Menu")

        choice = input("Enter your choice (1-8): ")

        if choice in [str(i) for i in range(1, 8)]:
            param_list = get_query_params[choice]()
            execute_query(int(choice), param_list)
        elif choice == "8":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    test_user_queries()
