from sensors import gps, accel, clock
import threading


outfile = 'results.txt'
work = []
col_order = []


def write_data(data):
    global col_order
    to_write = []

    for col in col_order:
        to_write.append(str(data[col]))

    with open(outfile, 'a') as f:
       vals = ','.join(to_write)
       f.write(vals + '\n')

def worker():
    global work
    while True:
        backlog = len(work)
        print('backlog:', backlog)
        if backlog > 0:
            data = work.pop(0)
            write_data(data)

def begin():
    thread = threading.Thread(target = worker)
    thread.start()

    jobs = [accel, gps, clock]
    cols = []
    for job in jobs:
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
    
    while True:
        local_work = {}
        for job in jobs:
            ans = job.get_data()
            for key in ans.keys():
               local_work[key] = ans[key]
        
        work.append(local_work)






if __name__ == '__main__':
    begin()

