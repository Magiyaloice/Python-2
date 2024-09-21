try:

   with open ("my_file.txt", "w")  as file:
  
     file.write(" This is wonderful.\n")
     file.write("Another wonderful day: 15\n")
     file.write("The year : 2022\n")

   print("File 'my_file.txt' created and written successfully." )

except PermissionError:
    print("Error : You do not have permission to write to the file.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")

#file reading and displaying

try:
    with open ("my_file.txt", "r") as file: 
       content = file.read()
       print("\nContents of 'my_file.txt':")
       print(content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")  

#file Appending

try:
    with open ("my_file.txt", "a") as file:
        file.write(" This is an appended line.\n")
        file.write("Another appended line: 15\n")
        file.write("The final appended line: 2022\n")

    print("\nFile 'my_file.txt' appended successfully." )

except PermissionError:
    print("Error : You do not have permission to append to the file.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")






