import sys
import os
import importlib

def mkdir(fn):
    path = []
    for f in fn.split(os.path.sep)[:-1]:
        path.append(f)
        p = os.path.sep.join(path)
        if p != "" and not os.path.isdir(p):
            os.mkdir(p)

def path_join(path):
    fn = path.pop(0)
    for p in path:
        fn = os.path.join(fn, p)
    return fn

def s_call(self, argv):
    lst, = argv
    for argv in lst:
        argv[0](self, argv[1:])

def s_dir(self, argv):
    fn, = argv
    self.path.append(fn)

def s_pop(self, argv):
    self.path.pop()

def s_addr(self, argv):
    addr, = argv
    self.addr = addr

def s_dev(self, argv):
    dev, = argv
    self.dev = dev

def s_data(self, argv):
    data, path = argv
    fn = path_join(path)
    with open(fn, "rb") as f:
        self.data[data] = f.read()

def s_file(self, argv):
    fn, = argv
    self.file.append((self.path_join([fn]), []))
    if os.path.isfile(self.file[-1][0]):
        with open(self.file[-1][0], "r") as f:
            self.file[-1][1].append(f.read())

def line_prc(line):
    data = "".join(line)
    while "\n\n\n" in data:
        data = data.replace("\n\n\n", "\n\n")
    data = data.strip("\n").replace("\t", "    ")
    if len(data) > 0:
        data += "\n"
    return data

def s_write(self, argv):
    fn, line = self.file.pop()
    data = line_prc(line)
    mkdir(fn)
    with open(fn, "w") as f:
        f.write(data)

def s_bin(self, argv):
    start, end, data, path = argv
    start -= self.addr
    end   -= self.addr
    fn = self.path_join(path)
    mkdir(fn)
    with open(fn, "wb") as f:
        f.write(self.data[data][start:end])

def s_str(self, argv):
    self.file[argv[1] if len(argv) > 1 else -1][1].append(argv[0])

class script:
    def __init__(self, path, name):
        self.name = name
        self.meta = importlib.import_module(name)
        self.root = path
        self.path = []
        self.addr = 0
        self.dev  = None
        self.data = {}
        self.file = []
        self.c_data = None
        self.c_addr = None
        self.c_dst  = None

    def main(self):
        s_call(self, [self.meta.lst])
    def path_join(self, path, i=0):
        return path_join(([self.root] + self.path + path)[i:])

    def cache(self, start, end, data, callback=None):
        fn = os.path.join(".cache", "%s%s_%08X.bin" % (self.name, data, start))
        if os.path.isfile(fn):
            with open(fn, "rb") as f:
                data = f.read()
        else:
            data = self.data[data][start:end]
            if callback != None:
                data = callback(data)
            with open(fn, "wb") as f:
                f.write(data)
        return data

    def c_dev(self, src=None):
        if src == None:
            src = self.c_dst
        return self.dev if self.dev != None else src-self.addr

    def c_init(self, start, data):
        self.c_data = data
        self.c_addr = start
    def c_push(self):
        self.c_dst = self.c_addr
    def c_pull(self):
        self.c_addr = self.c_dst
    def c_next(self, n):
        i = self.c_addr - self.addr
        self.c_addr += n
        data = self.data[self.c_data][i:i+n]
        if len(data) < n:
            data += B"\x00" * (n-len(data))
        return data

def main(argv):
    if len(argv) != 3:
        print("usage: %s <output> <meta>" % argv[0])
        return 1
    script(argv[1], argv[2]).main()
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
