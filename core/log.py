from datetime import datetime
import zipfile, os, traceback
#file to log
logFileName=os.path.join('.','logs','latest.log')


current_dir = os.getcwd()
while True:
    if os.path.basename(current_dir) == "Astroheads": break
    else:
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir: print("got root lol")
        os.chdir(parent_dir)

#file to log
logFileName=os.path.join('logs','latest.log')

def create_zip_archive(zip_name,file):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        zipf.write(file,os.path.basename(file))

def prepareNewLog():
    #check folder
    if not os.path.exists('logs'):
        os.makedirs(os.path.join('logs'))
    # read first and archive
    if os.path.isfile(logFileName):
        with open(logFileName) as f:
            name=f.readline()
            f.close()
        create_zip_archive(str(os.path.join('logs',name))+".zip",logFileName)
        os.remove(logFileName)
    # create new
    with open(logFileName,"w") as f:
        date=datetime.now()
        formatted_date = date.strftime("%-d-%-m-%Y-%H:%M")
        f.write(formatted_date+"\n")
        f.close()
def log(module,text,importance=0):
    # 0=log  1=info  2=warn  3=error  4=fatal
    #colors
    LIGHT_BLUE = "\033[38;2;150;215;255m"  # Light Blue
    YELLOW = "\033[93m"  # Yellow
    RED_ORANGE = "\033[38;2;255;125;0m"  # Red-Orange (using RGB)
    RED = "\033[91m"  # Red
    RESET = "\033[0m"  # Reset to default color

    time=datetime.now()
    formatted_time = time.strftime("%H:%M:%S")

    def writeToFile(ftext):
        with open(logFileName, "a") as f:
            f.write(ftext+"\n")
            f.close()

    logtext=""
    color=RESET
    if importance==0:
        logtext='['+formatted_time+']'+'['+"LOG/"+module+']:'+text
    elif importance==1:
        logtext='['+formatted_time+']'+'['+"INFO/"+module+']:'+text
        color=LIGHT_BLUE
    elif importance==2:
        logtext='['+formatted_time+']'+'['+"WARN/"+module+']:'+text
        color = YELLOW
    elif importance==3:
        logtext='['+formatted_time+']'+'['+"ERROR/"+module+']:'+text
        color = RED_ORANGE
    elif importance==4:
        logtext='['+formatted_time+']'+'['+"FATAL/"+module+']:'+text
        color = RED

    if not os.path.exists(logFileName): prepareNewLog()
    writeToFile(logtext)
    print(color+logtext+RESET)
def crash(exception):
    log("CRASH",type(exception).__name__,4)
    log("CRASH", str(exception), 4)
    log("CRASH",traceback.format_exc(),4)
    date = datetime.now()
    formatted_date = date.strftime("%-d-%-m-%Y-%H:%M")
    crashFileName=os.path.join("crash-reports",("crash-"+formatted_date+".log"))
    #check folder
    if not os.path.exists('crash-reports'):
        os.makedirs('crash-reports')
    with open(crashFileName,"w") as f:
        f.write("--crash report--\n")
        #some info here
        f.write(f"Exception Type: {type(exception).__name__}\n")
        f.write(f"Exception Message: {str(exception)}\n")
        f.write("Stack Trace:\n")
        f.write(traceback.format_exc())
        f.write("\n" + "=" * 40 + "\n")