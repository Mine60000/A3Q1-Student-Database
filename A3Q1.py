import psycopg

def getAllStudents(conn: psycopg.Connection):
    with conn.cursor() as cur:
        cur.execute(" SELECT * FROM students")
        for record in cur:
            print(record)
        delay = input("Press Enter to continue")

def addStudent(conn: psycopg.Connection,first_name: str, last_name:str, email:str, enrollment_date:str):
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s,%s,%s,%s)",
                (first_name,last_name,email,enrollment_date))
    except BaseException:
        conn.rollback()
        print("re-enter option")
    else: 
        conn.commit()
        print("Student created")
    finally:
        delay = input("Press Enter to continue")

def updateStudentEmail(conn: psycopg.Connection, student_id: int, new_email:str):
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE students (first_name, last_name, email, enrollment_date) SET email = %s WHERE student_id = %s",
                (new_email,student_id))
    except BaseException:
        conn.rollback()
        print("re-enter option")
    else: 
        conn.commit()
        print("Student Email changed")
    finally:
        delay = input("Press Enter to continue")

def deleteStudent(conn: psycopg.Connection, student_id: int):
    try:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM students (first_name, last_name, email, enrollment_date) WHERE student_id = %s",
                (student_id))
    except BaseException:
        conn.rollback()
        print("re-enter option")
    else: 
        conn.commit()
        print("Student Deleted")
    finally:
        delay = input("Press Enter to continue")



def main():
    user_name = input("User Name: ")
    password = input("Password: ")
    conn = psycopg.connect("host=localhost port=5432 user="+user_name+" dbname='Student Database' password="+password)
    programRun = True
    while programRun:
        print("Options:")
        print("getAllStudents")
        print("addStudent")
        print("updateStudentEmail")
        print("deleteStudent")
        print("Quit")
        print("Enter an option: ")
        while True:
            menuchoice = input("")
            if menuchoice.lower() == 'getallstudents':
                getAllStudents(conn)
            if menuchoice.lower() == 'addstudent':
                first_name = input("First name: ")
                last_name = input("Last name: ")
                email = input("Email: ")
                enrollment_date = input("Enrollment Date (YYYY-MM-DD): ")
                addStudent(conn, first_name, last_name, email, enrollment_date)
            if menuchoice.lower() == 'updatestudentemail':
                student_id=input ("Student ID: ")
                new_email = input ("New Email: ")
                updateStudentEmail(conn,student_id,new_email)
            if menuchoice.lower() == 'deletestudent':
                student_id=input ("Student ID: ")
                deleteStudent(conn,student_id)
            if menuchoice.upper() == 'QUIT':
                programRun = False
                break
            else:
                print("re-enter option")
    conn.close()

main()