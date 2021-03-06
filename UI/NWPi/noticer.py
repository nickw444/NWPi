
# Global logging and error management method.
# Will be turning this on silent after final realease and only Fatal errors and errors will be shown in the console.
from time import strftime, localtime

def noticer(message, level=0, object=False, thread=0):
    if level > 1:                               # Only log fatal errors and errors
        f = open('log.txt', 'a')
        if object == False:
            object = "nil"
        if level == 0:
            output = ("[Notice][Thread " + str(thread) + "]: " + message + " on object: " + str(object))
        elif level == 1:
            output = ("[Warning][Thread " + str(thread) + "]: " + message + " on object: " + str(object))
        elif level == 2:
            output = ("[Error][Thread " + str(thread) + "]: " + message + " on object: " + str(object))
        elif level == 3:
            output = ("[Fatal Error][Thread " + str(thread) + "]: " + message + " on object: " + str(object))
        now = strftime("%Y-%m-%d %H:%M:%S", localtime())
        f.write("[" + now + "]" + output + "\n")
        f.close()
        print(output)