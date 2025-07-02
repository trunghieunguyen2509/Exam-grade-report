import numpy as np
import pandas as pd
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
        #Open the file, read the content and set up variables
        lines = file3.readlines()
        scores = []
        all_skipped =[]
        all_incorrect = []
        invalid = 0
        valid = 0
        valid_lines = []
        for idx, line in enumerate(lines, 1):
            item = line.strip().split(",")
            #Checking if the items are valid (N followed by 8 digits) and include 26 items, filter only valid lines   
            if len(item) == 26 and item[0][0] == "N" and item[0][1:].isdigit() and len(item[0]) == 9:
                valid += 1
                valid_lines.append(line)
            else:
                print(f"Invalid line of data: N# is invalid \n")
                print(item)
                invalid += 1
        if invalid == 0:
            print("***ANALYZING***")
            print("No errors found!")
            print("***REPORT***")
        else:
            print("\n*** REPORT ***")
            print(f"Total valid lines of data: {valid}")
            print(f"Total invalid lines of data: {invalid}")
        #Loop through each line, split the items, and calculate scores
        for idx, line in enumerate(valid_lines, 1):
            item = line.strip().split(",")
            correct = 0
            incorrect = 0
            skipped = 0
            skipped_idx = []
            incorrect_idx = []
            answer = ("B", "A", "D", "D", "C", "B", "D", "A", "C", "C",
          "D", "B", "A", "B", "A", "C", "B", "D", "A", "C",
          "A", "A", "B", "D", "D")
            #Loop through each item in the line, compare with the answer key, and calculate scores
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
        #Calculate and print out the results
        highest_score = max(scores)
        lowest_score = min(scores)
        average_score = np.mean(scores)
        range = highest_score - lowest_score
        number_of_highscore = sum(1 for s in scores if s > 80)
        median = np.median(scores)
        flattened_skipped = np.concatenate(all_skipped)
        counts_s = pd.Series(flattened_skipped).value_counts()
        max_count_s = counts_s.iloc[0]
        frequent_s = counts_s[counts_s == max_count_s].index.tolist()
        #Get the most frequent skipped and incorrect questions
        flattened_incorrect = np.concatenate(all_incorrect)
        count_i = pd.Series(flattened_incorrect).value_counts()
        max_count_i = count_i.iloc[0]
        frequent_i = count_i[count_i == max_count_i].index.tolist()
        print(f"Average score: {average_score:.2f}")
        print(f"Highest score: {highest_score}")
        print(f"Lowest score: {lowest_score}")
        print(f"Range of scores: {range}")
        print(f"Median score: {median}")
        print(f"Question that most people skipped: {int(frequent_s[0])} - {max_count_s} - {max_count_s/len(all_skipped):.3f}")
        print(f"Question that most people answer incorrect: {int(frequent_i[0])} - {max_count_i} - {max_count_i/len(all_incorrect):.3f}")
except FileNotFoundError:
    print(f"Can not find file {file_name}, please check again file name")
except Exception as e:
    print(f"Error occur:{e}")

file4 = input("Enter file name here: ")
try:
    with open(file4, 'r') as file4:
        lines = file4.readlines()
        scores = []
        valid_lines = []
        for idx, line in enumerate(lines, 1):
            item = line.strip().split(",")
            #Checking if the items are valid (N followed by 8 digits) and include 26 items    
            if len(item) == 26 and item[0][0] == "N" and item[0][1:].isdigit() and len(item[0]) == 9:
                valid += 1
                valid_lines.append(line)
            else:
                invalid += 1
        for idx, line in enumerate(valid_lines, 1):
            item = line.strip().split(",")
            correct = 0
            incorrect = 0
            skipped = 0
            answer = ("B", "A", "D", "D", "C", "B", "D", "A", "C", "C",
                "D", "B", "A", "B", "A", "C", "B", "D", "A", "C",
                "A", "A", "B", "D", "D")
            for i,j in zip(item[1:],answer):
                if i == j:
                    correct += 1
                elif i == "":
                    skipped += 1
                else:
                        incorrect += 1
            score = 4*correct - incorrect
            scores.append(score)
            print(item[0],score)
except FileNotFoundError:
    print(f"Can not find file {file_name}, please check again file name")
except Exception as e:
    print(f"Error occur:{e}")

    
        








    
