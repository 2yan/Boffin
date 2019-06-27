from sensors import gps, accel, clock
import threading
import time

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
        if not keep_working:
            return
        backlog = len(work)
        if backlog > 0:
            now = time.monotonic()
            if abs(last_print - now) > 5:
                print('Adding new data: {} '.format(not done), 'backlog:', backlog)
                last_print = now



            datas = []
            while (len(work) > 0 ) and (len(datas) < 100):
                datas.append(work.pop(0))
            write_data(datas)

def begin():
    workers = []
    global keep_working
    keep_working = True
    for num in range(1):
        print("Starting worker {}".format(num))
        worker_thread = threading.Thread(target = worker)
        worker_thread.start()
        workers.append(worker_thread)


    jobs = [accel, gps, clock]
    cols = []
    for job in jobs:
        job.init()
        test_val = job.get_data()
        keys = test_val.keys()
        for key in keys:
            cols.append(key)

    t = {}
    for c in cols:
        t[c] = c
    global col_order
    global work

    col_order = cols
    work  = [t]
    

    def data_log_func():
        global done
        done = False

        while not done:
            local_work = {}
            for job in jobs:
                ans = job.get_data()
                for key in ans.keys():
                   local_work[key] = ans[key]
            
            work.append(local_work)

        print("Stopping logging")
        print("need to process remaining data:")
        
        while len(work) > 0:
            continue
        keep_working = False
        return 
    
    data_log_thread = threading.Thread(target = data_log_func)
    data_log_thread.start()
    


def end():
    global done
    done = True



if __name__ == '__main__':
    begin()

