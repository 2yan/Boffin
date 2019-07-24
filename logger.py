from sensors import gps, nine_dof, clock
import threading
import time
import os
import signal
import sys

outfile = 'results.txt'
work = []
col_order = []
done = False
keep_working = True

    
def write_data(datas):
    global col_order
    rows = []

    for data in datas:
        to_write = []
        for col in col_order:
            to_write.append(str(data[col]))
        row = ','.join(to_write)
        rows.append(row)



    with open(outfile, 'a') as f:
        for row in rows:
            f.write(row + '\n')




def worker():
    global work
    global keep_working

    last_print = time.monotonic()
    
    while True:
        
        if (not keep_working) and (len(work) == 0):
            print("DONE WORKING")
            return 
        backlog = len(work)
                
        if backlog > 0:
            print('Keep Working: ', keep_working, ' | BACKLOG :', backlog)
            now = time.monotonic()
            datas = []
            while (len(work) > 0 ) and (len(datas) < 500):
                datas.append(work.pop(0))
            write_data(datas)

workers = []

def begin():
    try:
        os.remove(outfile)

    except Exception as e:
        pass
    global workers
    workers = []
    global keep_working
    keep_working = True
    for num in range(1):
        print("Starting worker {}".format(num))
        worker_thread = threading.Thread(target = worker)
        worker_thread.start()
        workers.append(worker_thread)


    jobs = [nine_dof, gps, clock]
    jobs = [nine_dof, clock]
    cols = []
    for job in jobs:
        job.init()
        test_val = job.get_data()
        keys = test_val.keys()
        for key in keys:
            cols.append(key)

    print("ALL JOBS INITalized")
    t = {}
    for c in cols:
        t[c] = c
    global col_order
    global work

    col_order = cols
    work  = [t]
    

    def data_log_func():
        global done
        global work

        done = False

        while not done:
            local_work = {}
            for job in jobs:
                ans = job.get_data()
                for key in ans.keys():
                   local_work[key] = ans[key]
            
            work.append(local_work)

        print("Stopping logging")
        print("need to process remaining data: {}".format(len(work)))
        
        d = False

        while not d:
            print('work still remaining:',len(work))
            if len(work) == 0:
                d = True
                    
        print("DONE")
        global keep_working
        keep_working = False
        return 
    
    data_log_thread = threading.Thread(target = data_log_func)
    data_log_thread.start()
    

def signal_handler(sig, frame):
    end()
    
    for t in workers:
        t.join()
    sys.exit(0) 

signal.signal(signal.SIGINT, signal_handler)

def end():
    global done
    done = True



if __name__ == '__main__':
    begin()

