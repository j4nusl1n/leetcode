def get_tc_by_fname(fname):
    tc = []
    with open(fname, "r") as f:
        for line in f:
            yield line
