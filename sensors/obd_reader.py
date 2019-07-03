import obd


con = False


def init():
    global con
    con = obd.OBD()



def get_data():
    cmd = obd.commands.THROTTLE_POS
    r = con.query(cmd)
    return {"accel": r}
