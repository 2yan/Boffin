from sensors import gps, accel
import threading


outfile = 'outfile.txt'



def write_data(data):
    with open(outfile, 'a') as f:
        vals = ','.join(data)
        f.write(outfile)

def worker():
    while True:
        if len(work) > 0:
            data = work.pop()
            write_data(data)


def begin():
    global work
    work = []
    thread = threading.Thread(target = worker)
    thread.start()

    jobs = [accel, gps]
    cols = []
    for job in jobs:
        test_val = job.get_data()
        keys = test_val.keys()
        for key in keys:
            cols.append(key)

    print(cols)
    return


    while True:
        moment  = accel.get_data()
        pos = gps.get_data()
        






