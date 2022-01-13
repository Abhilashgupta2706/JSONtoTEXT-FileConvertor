import os

# Folder path of JSON files
TestJSONFolderPath = "E:/01 Studies Related/PYTHON/Programs/Codes/FIle Handling/JSON to TEXT/Sample files"
# Make sure folder path is correct and has "/" not "\"

TestJSONFilePath = os.listdir(TestJSONFolderPath)  # Loading Dir

for files in TestJSONFilePath:  # Iterating every file in folder
    if files.endswith('.json'):  # Filtering files talking ONLY JSON files
        with open(os.path.join(TestJSONFolderPath, files)) as rf:  # Reading file
            content_rf = str(rf.read())  # Converting file to Str
            temp_Str = ""  # Creating Temp string to store the file
            for words in content_rf:
                # LOGIC
                if words != '{' and words != '}' and words != '[' and words != ']' and words != '"' and words != ',':
                    temp_Str += words

            temp_Str1 = temp_Str.replace(" ", "")  # Removing extra spaces form the line
            temp_Str2 = temp_Str1.replace(':', " ")  # Replacing : with spaces in respected lines
            final_str = temp_Str2  # Storing final output in variable

            with open(rf.name[:-5] + '.txt', 'w') as wf:  # Writing the output in new file
                for line in final_str:  # Copying every line to new file
                    print(line)
                    wf.write(line)
            print(f"Conversion successful for {rf.name} to {wf.name}")
            print("-------------------")
