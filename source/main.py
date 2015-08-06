from lib import *
import os.path
import datetime

welcome = "Hello! My name is Winston Jr. I read newspaper articles to expand my vocabulary. Let me know when you want me to try and make my own sentence! Enter help at any time for a list of available commands."

errors = {
          100:'Invalid input from root. Enter "help" for a list of available commands',
          101:'Too many arguments.',
          102:'Invalid argument.',
          200:'File not found. Please reselect database.',
          201:'Entry out of list range.',
          202:'Entry not found.',
          300:'Unknown error.',
          301:'Function unavailable.'
}

err_log = []
def error(code):
    err_log.append([code, datetime.datetime.now()])
    print("Error " + str(code) + ": " + errors[code])

commands = {
            'add':'Add data to the database.\n    -s to add a single sentence\n    -f to add a text file',
            'edit':'Modify the selected property of the database.\n    -n alters the name\n    -w allows you to tweak the data associated with a word',
            'error':'List possible errors.\n    -l to view the log',
            'help':'List all available commands.',
            'intro':'Reprints the intro message.',
            'list':'Lists the selected data. Defaults to naming the selected database.\n    -d to list dictionaries in selected database\n    -s to list sentences in selected dictionary\n    -w to list words in selected dictionary',
            'quit':'Exit the program.\n    -a quits all sub-programs',
            'select':'Select item to manipulate.\n    -f indicates that a file containing the dictionary database is being selected\n    -d indicates a dictionary is being chosen from the loaded file\n    Function assumes that file contains a list of dictionaries.',
            'sort':'Alphabetizes the selected dictionary',
            'trim':'Remove "None" value from precursor word lists.'
}

dataFile = ""
dictionary = []

print("\n" + welcome + "\n")
while True:
    if os.path.exists(dataFile):
        database = load(dataFile)
    usrIn = get()
    usrAr = usrIn.split(" ")
    numIn = len(usrAr)
    if re.match('^q', usrIn):
        print("Goodbye!")
        break
    
    #============HELP FUNCTION============#
    elif re.match('^h', usrIn):
        for k in commands:
            if k == 'error' or k == 'sort':
                print(k + " (" + k[0].upper() + "): " + commands[k])
            else:
                print(k + " (" + k[0] + "): " + commands[k])
    
    #============INTRO FUNCTION============#
    elif re.match('^i', usrIn):
        print(welcome)
     
    #============SELECT FUNCTION============#   
    elif re.match('^s', usrIn):
        if numIn == 1:
            dataFile = manualSelect()
        elif numIn == 2:
            if usrAr[1][1] not in 'fc':
                error(102)
            elif usrAr[1][1] == 'f':
                print("Enter path:")
                dataFile = get()
            elif usrAr[1][1] == 'c':
                print("Database selection cleared.")
                dataFile = ''
        elif numIn == 3:
            if usrAr[1][1] not in 'fc':
                error(102)
            elif usrAr[1][1] == 'f':
                dataFile = usrAr[2]
            elif usrAr[1][1] == 'd':
                dictionary = usrAr[2]
        else:
            error(101)
        if not os.path.exists(dataFile):
            error(200)
            dataFile = ""
    
    #============LIST FUNCTION============#        
    elif re.match('^l', usrIn):
        if not os.path.exists(dataFile):
            error(200)
        else:
            if numIn == 1:
                print("Dictionary name: " + database.name)
            elif numIn == 2:
                if usrAr[1] == '-d':
                    print(dataFile)
                    for d in database:
                        print(d)
                elif usrAr[1] == '-s':
                    for s in database.sentences:
                        print(s.string)
                elif usrAr[1] == '-w':
                    i = 0
                    for w in database.words:
                        print("#====[" + str(i) + "]====#")
                        print(w.string)
                        print(w.data)
                        print(w.pre)
                        i += 1
                else:
                    error(202)
            else:
                error(101)
                
    #============ERROR FUNCTION============#           
    elif re.match('^E', usrIn):
        if numIn == 1:
            for e in errors:
                print(str(e) + ": " + errors[e])
        elif numIn == 2:
            if usrAr[1] == '-l':
                for err in err_log:
                    print("Error " + str(err[0]) + " @ " + str(err[1]))
                    print(errors[err[0]])
    
    #============EDIT FUNCTION============#               
    elif re.match('^e', usrIn):
        if numIn == 1:
            print("Edit [n]ame or [w]ord:")
            select = get()
            if re.match('^n', select):
                print("New dictionary name:")
                database.name = get()
                save(database, dataFile)
            elif re.match('^w', select):
                print("Word to edit (integer to search by index):")
                select = get()
                if re.match('[0-9]+', select):
                    print(database.words[int(select)].string)
                    print(database.words[int(select)].data)
                    print("")
                    print("Edit [d]ata or [s]pelling:")
                    select = get()
                    if re.match('^s', select):
                        print("Enter new spelling:")
                        database.words[int(select)].string = get()
                        save(database, dataFile)
                    elif re.match('^d', select):
                        error(301)
                    else:
                        error(102)
                else:
                    i = database.find(select)
                    if i == -1:
                        error(201)
                    else:
                        print(database.words[i].string)
                        print(database.words[i].data)
                        print("")
                        print("Edit [d]ata or [s]pelling:")
                        select = get()
                        if re.match('^s', select):
                            print("Enter new spelling:")
                            database.words[i].string = get()
                            save(database, dataFile)
                        elif re.match('^d', select):
                            error(301)
                        else:
                            error(102)
            else:
                error(102)
    #============SORT FUNCTION============#            
    elif re.match('^S', usrIn):
        if os.path.exists(dataFile):
            for i in range(int(len(database.words)*0.9)):
                database.sort()
                save(database, dataFile)
        else:
            error(200)   
    #============ADD FUNCTION============#        
    elif re.match('^a', usrIn):
        if not os.path.exists(dataFile):
            error(200)
        else:
            if numIn == 1:
                print("Add [s]entence or [f]ile:")
                select = get()
                if re.match('^s[entence]*', select):
                    print("Enter sentence text with punctuation:")
                    text = get()
                    database.addSent(text)
                    save(database, dataFile)
                elif re.match('^f[ile]*', select):
                    print("Enter path to file:")
                    path = get()
                    database.addFile(path)
                    save(database, dataFile)
                else:
                    error(102)
            elif numIn == 2:
                if re.match('s', usrAr[1]):
                    print("Enter sentence text with punctuation:")
                    text = get()
                    database.addSent(text)
                    save(database, dataFile)
                elif re.match('f', usrAr[1]):
                    print("Enter path to file:")
                    path = get()
                    database.addFile(path)
                    save(database, dataFile)
                else:
                    error(102)
            elif numIn == 3 and re.match('.*f', usrAr[1]) and re.match('\w+\.txt', usrAr[2]):
                if not os.path.exists(usrAr[2]):
                    error(200)
                else:
                    database.addFile(usrAr[2])
                    save(database, dataFile)
            else:
                error(101)
                
    #============TRIM/STRIP FUNCTION============#
    elif re.match('^t', usrIn):
        if os.path.exists(dataFile):
            database.strip()
            save(database, dataFile)
        else:
            error(200)
    else:
        error(100)
    print("")
    