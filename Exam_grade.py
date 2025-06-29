import numpy as np
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
        #Read file and check if N# is valid
        lines = file2.readlines()
        invalid = 0
        valid = 0
        #Analyzing and checking the data
        print("***ANALYZING***")
        for idx, line in enumerate(lines, 1):
            item = line.strip().split(",")
            #Checking if the items are valid (N followed by 8 digits) and include 26 items    
            if len(item) == 26 and item[0][0] == "N" and item[0][1:].isdigit() and len(item[0]) == 9:
                valid += 1
            else:
                print(f"Invalid line of data: N# is invalid \n")
                print(item)
                invalid += 1
        if invalid == 0:
            print("No errors found!") 
        else:
            print("\n*** REPORT ***")
            print(f"Total valid lines of data: {valid}")
            print(f"Total invalid lines of data: {invalid}")       
except FileNotFoundError:
    print(f"Can not find file {file_name}, please check again file name")
except Exception as e:
    print(f"Error occur:{e}")

file3 = input("Enter file name to report: ")
try:
    with open(file3,'r') as file3:
        lines = file3.readlines()
        scores = []
        all_skipped =[]
        all_incorrect = []
        for idx, line in enumerate(lines, 1):
            item = line.strip().split(",")
            correct = 0
            incorrect = 0
            skipped = 0
            skipped_idx = []
            incorrect_idx = []
            answer = ("B", "A", "D", "D", "C", "B", "D", "A", "C", "C",
          "D", "B", "A", "B", "A", "C", "B", "D", "A", "C",
          "A", "A", "B", "D", "D")
            for q_index,(i,j) in enumerate(zip(item[1:],answer),1):
                if i == j:
                    correct += 1
                elif i == "":
                    skipped += 1
                    skipped_idx.append(q_index)
                else:
                    incorrect += 1
                    incorrect_idx.append(q_index)
            score = 4*correct - incorrect
            scores.append(score)
            scores.sort()
            all_skipped.append(skipped_idx)
            all_incorrect.append(incorrect_idx)
        highest_score = max(scores)
        lowest_score = min(scores)
        average_score = np.mean(scores)
        range = highest_score - lowest_score
        number_of_highscore = sum(1 for s in scores if s > 80)
        median = np.median(scores)
        print(all_skipped, all_incorrect)
except FileNotFoundError:
    print(f"Can not find file {file_name}, please check again file name")
except Exception as e:
    print(f"Error occur:{e}")








    
