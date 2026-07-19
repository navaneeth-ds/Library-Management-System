books = {}
while True :
  print("\n----- Library Management System -----")
  print("1. Add Books")
  print("2. View Books")
  print("3. Search Book")
  print("4. Borrow Book")
  print("5. Return Book")
  print("6. Delete Book")
  print("7. Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    title = input("Enter book title: ")
    author = input("Enter auther name: ")
    books[title] = {
      "author":author,
      "available":True
    }
    print("Book added Successfully!")

  elif choice == "2":
    for title in books:
      print("Title:",title)
      print("Aurthor:",author)
      print("Availabale:",books[title]["available"])
  
  elif choice == "3":
    title = input("Enter book title:")
    if title in books:
      print("Title:",title)
      print("Author:",books[title]["author"])
      print("Available:",books[title]["available"])
    else:
      print("Book not found!")

  elif choice == "4":
    title = input("Enter book title:")
    if title in books:
      if books[title]["available"]:
        books[title]["available"] = False
        print("Book borrowed successfully!")
      else:
        print("Book is not available!")
    else:
      print("Book not found!")

  elif choice == "5":
    title = input("Enter book title:")
    if title in books:
      if books[title]["available"] :
        books[title]["available"] = True
        print("Book returned successfully!")
      else:
        print("Book is already in the library!")
    else :
      print("Book not found!")

  elif choice == "6":
    title = input("Enter book name to delete:")
    if title in books:
      del books[title]
      print("Book has been deleted succesfully!")
    else:
      print("Book not found")

  elif choice == "7":
    print("Thankyou for visiting")
    break

  else:
    print("Invalid choice! Please try again")
