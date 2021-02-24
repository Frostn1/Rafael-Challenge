'''
 Sql database extractor for Rafael's Ninja Project
 Code by Sean Dahan
'''

import sqlite3
import json
def openSubFields(currentKey,currentField, currentIndent):
    if type(currentField) == list:
        for subField in currentField:
            openSubFields(currentKey,subField, currentIndent+1)
    elif type(currentField) == dict:
        # print("Type is dict")
        for subFieldsDict in currentField.keys():
            # print("Sub fields in dict",subFieldsDict,currentField[subFieldsDict])
            openSubFields(subFieldsDict,currentField[subFieldsDict], currentIndent+1)
    else:
        print("\t" * currentIndent + "Sub Field <> ",currentKey,"=>",currentField)
def openJson(path = ""):
    with open(path) as json1:
        data = json.load(json1)
        for key in data.keys():
            if type(data[key]) == list or type(data[key]) == dict:
                openSubFields(key,data[key], 1)
            else:
                print("Main Field <> ",key,"=>" ,data[key])

def sqlFetch(path = ""):

    print("Hello Sql for Rafael")
    # Connecting to said data base
    data_base_connection = sqlite3.connect(path)

    # initializing cursor
    data_base_cursor = data_base_connection.cursor()
    data_base_cursor.execute("SELECT * FROM emp")  
  
    # Store all the fetched data in the ans variable 
    ans = data_base_cursor.fetchall()  
    for field in ans:
       
        for index in field:
             print(index, end=" ")
        print()
    # data_base_connection.commit() 
    data_base_connection.close()
def main():
    
    
    openJson("../KnownAttacks/attack-pattern--0a3ead4e-6d47-4ccb-854c-a6a4f9d96b22.json")
    # sqlFetch("attacks-data.db")
    
if __name__ == "__main__":
    main()