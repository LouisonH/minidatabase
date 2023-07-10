import os
import ast
import sys
import json
import requests

#MiniDataBase
#Developed By HansenL
#version 1.5.2

class web_connect:
    def __init__(self,psswd,adress,prt):
        global passwsd
        global adsdress
        global port
        passwsd=psswd
        adsdress=adress
        port=prt
    def len(self):
        lenth=int(geta("/len"))
        return lenth
    
    def items(self):
        items=geta("/items")
        return items
        
    def get(self,n):
        value=str(geta("/get/%s"%n))
        return value
    
    def clean(self):
        geta("/clean")
        
    def commit(self):
        geta("/commit")
        
    def append(self,tag,value):
        if len(tag) != 0 and len(value) != 0:
            geta("/append/%s/"%tag+str(value))
    
    def delete(self,tag):
        geta("/delete/%s"%tag)
        
    def close(self):
        pass
        
    def search(self,keyword):
        return geta("/search/%s"%keyword)
    def search_tag(self,keyword):
        return geta("/search_tag/%s"%keyword)
    def search_value(self,keyword):
        return geta("/search_value/%s"%keyword)
class connect:
    '''
connect to your minidatabase.

you can use "append","delete",
"search","get" and so on ways
to deal with the data.
    '''
    def __init__(self,database):
        if os.path.exists(database):
            if '.minidb' in database:
                global temp
                global db_file_backup
                global db
                db_file_backup=str(database)
                temp=open(database,"a+")
                temp.seek(0)
                db_temp=temp.read()
                if len(db_temp) == 0:
                    db_temp="{}"
                else:
                    pass
                db=ast.literal_eval(db_temp)
            else:
                print("The file is not MDB File, please pass the correct file path.")
                exit()
        else:
            create(database)
            connect(database)
        
    def len(self):
        return len(db)
    
    def items(self):
        temp_item=[]
        for i in db.items():
            temp_item.append(i)
        return temp_item
    
    def list(self):
        print("="*16)
        for i in db:
            print(i,db.get(i))
        print("="*16)
    def get(self,n):
        
        return db.get(n,"Tag not found.")
    
    def clean(self):
        db.clear()
        
    def commit(self):
        temp.close()
        temp_c=open(db_file_backup,"w")
        temp_c.truncate()
        temp_c.write(str(db))
        temp_c.close()
        
    def append(self,tag,value):
        if len(tag) != 0 and len(value) != 0:
            db[tag]=value
    def delete(self,tag):
        if tag in db:
            del db[tag]
        else:
            pass
        
    def close(self):
        temp.close()
        
    def search(self,keyword):
        result=[]
        for i in db.items():
            if keyword in str(i):
                result.append(i)
        return result
    
    def search_tag(self,keyword):
        result=[]
        for i in db:
            if keyword in str(i):
                result.append(i)
        return result
    
    def search_value(self,keyword):
        result=[]
        for i in db.values():
            if keyword in str(i):
                result.append(i)
        return result
    
def create(name):
    with open(name,"w") as d:
        d.write("{}")
def geta(url):
    re=requests.get(str(adsdress)+":"+str(port)+"/"+str(passwsd)+str(url))
    return str(re.text)
def input_datas():
    while 1:
        print("===============")
        c=input("tag:")
        d=input("value:")
        if c != "leave":
            a.append(c,d)
            a.list()
        else:
            break
    print("================")
    if input("ready to save? please input 1>"):
        a.commit()
        print("completed.")
    else:
        print("program completed,but the data was not saved.")
        pass
    
def search_datas():
    a.list()
    v=input("input the things you want to search>")
    print("=======search result=======")
    b=a.search_value(v)
    print(b)
def main():
    if len(sys.argv) == 1:
        print("Welcome to use MiniDataBase. Type 'minidb -h' for more information.")
    elif len(sys.argv) > 3:
        print("Unknown command.Type 'minidb -h' for help.")
    elif sys.argv[1] == '-h':
        print('''
MiniDataBase 1.3 By HansenL

Method
minidb [-options] command

e.g. minidb test.minidb <--Open a MiniDataBase File.
     minidb -c new.minidb <--Create a new MiniDataBase File.

COMMANDS:
-c Create a MiniDataBase File.
-h Output help informations.
-w Running WEB MDB Services.
''')
    elif sys.argv[1] == '-c':
        if len(sys.argv) == 3:
            if '.minidb' in sys.argv[2]:
                create(sys.argv[2])
            else:
                print("Please input a correct file name.")
        else:
            print("Please type the file name after -c.")
    elif sys.argv[1] == '-w':
        os.system('WebMDB')
        os.system('python WebMDB.py')
    elif '.minidb' in sys.argv[1]:
        file=sys.argv[1]
        print("="*36)
        print("Welcome to MiniDataBase Monitor")
        print("Developed By HansenL")
        print("Copyright <c> 2020,2023,Origin Studio")
        print("="*36)
        print("Connecting to the database '%s'"%file)
        try:
            cursor=connect(file)
            print("Successfully connected.")
            print("Type 'help' for help. Type 'exit' to leave.")
            while True:
                ci=str(input("\nMiniDataBase>"))
                if ci == 'exit':
                    t=input("Do you want to save the changes?[Y/N]")
                    if t == 'Y' or t == 'y':
                        cursor.commit()
                        print("Changes have been saved.")
                    break
                elif ci == 'help':
#help informations.
                    print('''
===================COMMANDS===================

append : Appending tags and values into the database.

delete : Deleting a value from a tag in the database.

list : Listing all the values and the tags in the database.

search : Searching all the tags and the values in the database.

search_tag : Only search the tags in the database.

search_value : Only search the values in the database.

get : Getting a value from a tag.

len : Output the lenth of the database.

clean : Clean all the data in the database.

commit : Save the changes in the database.

exit : Close the connection to the database,
before you leave, you may commit your changes
to the database.

==============================================
                        ''')
                elif ci == 'list':
                    cursor.list()
                elif ci == 'commit':
                    cursor.commit()
                elif ci == 'len':
                    print("The lenth of the database:"+str(cursor.len()))
                elif ci == 'append':
                    tg=input('Input the tag-->')
                    ve=input('Input the value-->')
                    if len(tg) != 0 and len(ve) != 0:
                        cursor.append(tg,ve)
                    else:
                        print("Tag or value mustn't be empty")
                elif ci == 'delete':
                    tg=input("Input the tag-->")
                    if len(tg) != 0:
                        cursor.delete(tg)
                    else:
                        print("Tag mustn't be empty")
                elif ci == 'search':
                    kw=input("Input the keyword-->")
                    if len(kw) != 0:
                        print("==========RESULT==========")
                        for i in cursor.search(kw):
                            print(i)
                        print("="*20)
                    else:
                        print("Keyword mustn't be empty.")
                elif ci == 'search_tag':
                    kw=input("Input the keyword-->")
                    if len(kw) != 0:
                        print("==========RESULT==========")
                        for i in cursor.search_tag(kw):
                            print(i)
                        print("="*20)
                    else:
                        print("Keyword mustn't be empty.")
                elif ci == 'search_value':
                    kw=input("Input the keyword-->")
                    if len(kw) != 0:
                        print("==========RESULT==========")
                        for i in cursor.search_value(kw):
                            print(i)
                        print("="*25)
                    else:
                        print("Keyword mustn't be empty.")
                elif ci == "get":
                    kw=input("Input the tag-->")
                    if len(kw) != 0:
                        print("RESULT:"+str(cursor.get(kw)))
                    else:
                        print("Tag mustn't be empty.")
                elif ci == "clean":
                    cursor.clean()
                else:
                    print("Unknown command. Type 'help' for help.")
        except IOError:
            print("Connected failed.")
            print("The database file was not exist. Please try again.")
    else:
        print("The file is not the MiniDataBase File, please open a correct file.")
if __name__ == "__main__":
    main()

            
