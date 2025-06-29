file_name = input("Enter file name: ")
try:
    #Open file and print out content
    with open(file_name,'r') as file:
        content = file.read()
        print("\n File content")
        print(content)
except FileNotFoundError:
    print(f"Can not find file {file_name}, please check again file name")
except Exception as e:
    print(f"Error occur:{e}")

file_name2 = input("Enter file name to check: ")
try:
    with open(file_name2, 'r') as file2:
        lines = file2.readlines()
        invalid = 0
        valid = 0
        print("***ANALYZING***")
        for idx, line in enumerate(lines, 1):
            item = line.strip().split(",")      
            if len(item) == 26 and item[0][0] == "N" and item[0][1:].isdigit() and len(item[0]) == 9:
                valid += 1
            else:
                print(f"Invalid line of data: N# is invalid \n")
                print(item)
                invalid += 1
        if invalid ==0:
            print("No errors found!") 
        else:
            print("\n*** REPORT ***")
            print(f"Total valid lines of data: {valid}")
            print(f"Total invalid lines of data: {invalid}")
except FileNotFoundError:
    print(f"Can not find file {file_name}, please check again file name")
except Exception as e:
    print(f"Error occur:{e}")








    
