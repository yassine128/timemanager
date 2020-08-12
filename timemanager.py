import time
from win10toast import ToastNotifier

taskname = []
tasktime = []
ntask = 0
m = 0
v2 = 0

def notification():
    global v2
    toast = ToastNotifier()
    toast.show_toast(str(taskname[m]),"Time is up for task "+str(m+1),duration=5)
    v2 = 1

def task_taker():
    print('Put the task in order.')
    try:
        global ntask
        ntask = int(input('Number of tasks you want me to remember: '))
        global tasktime
        global taskname
        taskname = []
        tasktime = []
        for i in range(ntask):
            if i == 0:
                print('=========================================================================')
                print('TASK NUMBER '+str(i+1))
                task = str(input('What is your task?: '))
                timer = input('How much time will you take to finish this task? (e.g: 10 minutes or 1 hour): ')
                print('=========================================================================')
                taskname.append(task)
                tasktime.append(timer)
            if i >= 1:
                print('=========================================================================')
                print('TASK NUMBER '+str(i+1))
                task = str(input('What is your task?: '))
                timer = input('How much time will you take to finish after the last task? (e.g: 10 minutes, ,1 hour, 1 hour and 10 minutes): ')
                print('=========================================================================')
                taskname.append(task)
                tasktime.append(timer)


    except:
        print('Enter an integer.')

try:
    m=0
    while True:
        if v2 == 0:
            task_taker()
            if ntask != m:
                print('TIMER LAUNCHED')
                timer = tasktime[m]
                timer = timer.lower()
                timer = timer.split() #1 hour and 10 minutes
                
                if 'hour' in timer:
                    hourindex = timer.index('hour')
                    nhour = int(timer[hourindex-1]) #1
                    if 'minute' in timer:
                        minuteindex = timer.index('minute')
                        nminute = int(timer[minuteindex-1]) #10

                        sleephour = (nhour*60)*60
                        sleepminute = (nminute*60)
                        time.sleep(sleephour+sleepminute)
                        notification()
                        m=m+1

                    if 'minutes' in timer:
                        minuteindex = timer.index('minutes')
                        nminute = int(timer[minuteindex-1]) #10  

                        sleephour = (nhour*60)*60
                        sleepminute = (nminute*60) 
                        time.sleep(sleephour+sleepminute)
                        notification()
                        m=m+1
                    else:
                        sleephour = (nhour*60)*60 
                        time.sleep(sleephour)
                        notification()
                        m=m+1

                if 'hours' in timer:
                    print('ok')
                    hourindex = timer.index('hours')
                    nhour = int(timer[hourindex-1]) #1    
                    if 'minute' in timer:
                        minuteindex = timer.index('minute')
                        nminute = int(timer[minuteindex-1]) #10

                        sleephour = (nhour*60)*60
                        sleepminute = (nminute*60) 
                        time.sleep(sleephour+sleepminute)
                        notification()
                        m=m+1

                    if 'minutes' in timer:
                        minuteindex = timer.index('minutes')
                        nminute = int(timer[minuteindex-1]) #10

                        sleephour = (nhour*60)*60
                        sleepminute = (nminute*60) 
                        time.sleep(sleephour+sleepminute)
                        notification()
                        m=m+1
                    else:
                        sleephour = (nhour*60)*60 
                        time.sleep(sleephour)
                        notification()
                        m=m+1

                if 'minute' in timer and 'hour' not in timer:
                    if 'hours' not in timer:
                        minuteindex = timer.index('minute')
                        nminute = int(timer[minuteindex-1]) #10

                        sleepminute = (nminute*60)
                        time.sleep(sleepminute)
                        notification()
                        m=m+1

                if 'minutes' in timer and 'hour' not in timer:
                    print('ok')
                    if 'hours' not in timer:
                        print('o2k')
                        minuteindex = timer.index('minutes')
                        nminute = int(timer[minuteindex-1]) #10
                    
                        sleepminute = (nminute*60)
                        time.sleep(sleepminute)
                        notification() 
                        m=m+1 

        if v2 == 1:
            if ntask != m:
                timer = tasktime[m]
                timer = timer.lower()
                timer = timer.split() #1 hour and 10 minutes
                
                if 'hour' in timer:
                    hourindex = timer.index('hour')
                    nhour = int(timer[hourindex-1]) #1
                    if 'minute' in timer:
                        minuteindex = timer.index('minute')
                        nminute = int(timer[minuteindex-1]) #10

                        sleephour = (nhour*60)*60
                        sleepminute = (nminute*60)
                        time.sleep(sleephour+sleepminute)
                        notification()
                        m=m+1

                    if 'minutes' in timer:
                        minuteindex = timer.index('minutes')
                        nminute = int(timer[minuteindex-1]) #10  

                        sleephour = (nhour*60)*60
                        sleepminute = (nminute*60) 
                        time.sleep(sleephour+sleepminute)
                        notification()
                        m=m+1
                    else:
                        sleephour = (nhour*60)*60 
                        time.sleep(sleephour)
                        notification()
                        m=m+1

                if 'hours' in timer:
                    hourindex = timer.index('hours')
                    nhour = int(timer[hourindex-1]) #1    
                    if 'minute' in timer:
                        minuteindex = timer.index('minute')
                        nminute = int(timer[minuteindex-1]) #10

                        sleephour = (nhour*60)*60
                        sleepminute = (nminute*60) 
                        time.sleep(sleephour+sleepminute)
                        notification()
                        m=m+1

                    if 'minutes' in timer:
                        minuteindex = timer.index('minutes')
                        nminute = int(timer[minuteindex-1]) #10

                        sleephour = (nhour*60)*60
                        sleepminute = (nminute*60) 
                        time.sleep(sleephour+sleepminute)
                        notification()
                        m=m+1
                    else:
                        sleephour = (nhour*60)*60 
                        time.sleep(sleephour)
                        notification()
                        m=m+1

                if 'minute' in timer and 'hour' not in timer:
                    if 'hours' not in timer:
                        minuteindex = timer.index('minute')
                        nminute = int(timer[minuteindex-1]) #10

                        sleepminute = (nminute*60)
                        time.sleep(sleepminute)
                        notification()
                        m=m+1

                if 'minutes' in timer and 'hour' not in timer:
                    if 'hours' not in timer:
                        print('o2k')
                        minuteindex = timer.index('minutes')
                        nminute = int(timer[minuteindex-1]) #10
                    
                        sleepminute = (nminute*60)
                        time.sleep(sleepminute)
                        notification() 
                        m=m+1


except:
    print('An error occured... please restart the progam.')