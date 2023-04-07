import numpy as np

def in2out(fr,to,hoplen):
    out = []
    length = (to - fr) / hoplen + 1
    former = 0
    latter = 0
    if divmod(to, 10)[0] > divmod(fr, 10)[0]:
        former = divmod(10.0-fr, hoplen)[0] + 1
        if divmod(10.0-fr, hoplen)[1] == 0:
            former = former - 1
        latter = divmod(to-10.0, hoplen)[0] + 1
        # if divmod(to-10.0, hoplen)[1] == 0:
        #     latter = latter + 1
    if former == 0:
        for i in range(np.int(length)):
            if i == 0:
                out = fr
            else:
                out = np.rowstack((out, fr+hoplen*i))
    else:
        for i in range(np.int(length)):
            if i < latter:
                out_tmp = fr+hoplen*(former+i)
            else:
                out_tmp = fr+(i-latter)*hoplen
            if i == 0:
                out = out_tmp
            else:
                out = np.row_stack((out, out_tmp))
    return out
