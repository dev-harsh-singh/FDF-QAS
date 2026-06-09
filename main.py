# This the main page wher user get options to upload or search from database

from upload import upload_document   
from search import search_document

while True:
    print("\n===== PDF SEARCH SYSTEM =====")
    print("1. Upload Document")
    print("2. Search Document")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":        # This will redirect user to load page content where they can add pdf to database
        upload_document()

    elif choice == "2":      # This will redirect function to search where uswe can search keyword related to his search
       search_document()

    elif choice == "3":      # If user dont want to search anyrhing he can exit from hear
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")
