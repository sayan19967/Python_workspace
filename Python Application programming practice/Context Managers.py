#A Context Manager allows a programmer to perform required activities,
#automatically, while entering or exiting a Context.

#For example, opening a file, doing few file operations,
#and closing the file is manged using Context Manager as shown below.

##with open('a.txt', 'r') as fp:
##
##    content = fp.read()
##
##print(content)
##print(fp.read())


#Consider the following example, which tries to establish a connection to a
#database, perform few db operations and finally close the connection.

##import sqlite3
##try:
##    dbConnection = sqlite3.connect('TEST.db')
##    cursor = dbConnection.cursor()
##    '''
##    Few db operations
##    ...
##    '''
##except Exception:
##    print('No Connection.')
##finally:
##    dbConnection.close()



# Using Context Manager

##import sqlite3
##class DbConnect(object):
##    def __init__(self, dbname):
##        self.dbname = dbname
##    def __enter__(self):
##        self.dbConnection = sqlite3.connect(self.dbname)
##        return self.dbConnection
##    def __exit__(self, exc_type, exc_val, exc_tb):
##        self.dbConnection.close()
##with DbConnect('TEST.db') as db:
##    cursor = db.cursor()
##    '''
##   Few db operations
##   ...
##    '''


#quiz

##from contextlib import contextmanager
##
##@contextmanager
##def tag(name):
##    print("<%s>" % name)
##    yield
##    print("</%s>" % name)
##
##with tag('h1') :
##    print('Hello')


# Hackerrank -1

# Complete the function below.

##def writeTo(filename, input_text):
##    with open(filename, 'w') as fp:
##        fp.write(input_text)


# Hackerrank - 2

# Define 'writeTo' function below, such that 
# it writes input_text string to filename.
##def writeTo(filename, input_text):
##    with open(filename, 'w') as fp:
##        fp.write(input_text)
##    
### Define the function 'archive' below, such that
### it archives 'filename' into the 'zipfile'
##def archive(zfile, filename):
##    with zipfile.ZipFile(zfile, 'w') as myzip:
##        myzip.write(filename)


# Hackerrank - 3

# Complete the function below.

def run_process(cmd_args):
    with subprocess.Popen(cmd_args, stdout=subprocess.PIPE) as p:
        out1 = p.communicate()[0]
    return out1


























































