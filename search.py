# This is the code through which user can search information from database by using database

from database import get_connection   # This helps data to connect with database

def search_document():   

    print("\nSearch Mode Started")
    print("Type EXIT to return to Main Menu")

    conn = get_connection()     # help to retrieve data from daabase
    cursor = conn.cursor()      # help to run quaries in SQL daabase

    while True:     

        keyword = input("\nAsk Question: ")     #Take keyword from user

        if keyword.upper() == "EXIT":  
            break

        cursor.execute(              # To execute given query in SQL 
            """
            SELECT file_name, paragraph          
            FROM documents
            WHERE paragraph LIKE %s
            """,
            (f"%{keyword}%",)
        )

        results = cursor.fetchall()        # Fetch all results related to that keyword

        if results:

            print("\nResults Found:\n")

            for file_name, paragraph in results:

                print(f"File: {file_name}")
                print(paragraph)
                print("-" * 50)

        else:

            print("No Results Found")

    cursor.close()
    conn.close()