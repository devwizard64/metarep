import main
import hvc

def i_aa(addr):
    return "#%s" % hvc.sym_addr(addr, 2)

def i_hi(sym, addr):
    return ("#>%s" % sym[addr].label,)

def i_lo(sym, addr):
    return ("#<%s" % sym[addr].label,)

def i_hiword(sym, addr):
    return ("#.hiword(%s)" % sym[addr].label,)

def i_loword(sym, addr):
    return ("#.loword(%s)" % sym[addr].label,)

def s_def(s, l=0, r=0):
    return [main.s_str, "\n"*l + s + "\n"*(1+r)]

def s_ifdef(s, l=0, r=0):   return s_def(".ifdef %s"        % s, l, r)
def s_ifndef(s, l=0, r=0):  return s_def(".ifndef %s"       % s, l, r)
def s_define(s, l=0, r=0):  return s_def(".define %s"       % s, l, r)
def s_else(s, l=0, r=0):    return s_def(".else /* %s */"   % s, l, r)
def s_endif(s, l=0, r=0):   return s_def(".endif /* %s */"  % s, l, r)

def s_segment(s):
    return [main.s_str, "\n.segment \"%s\"\n" % s]

def s_file(addr, fn, lst):
    return [main.s_call, [
        [main.s_addr, addr],
        [main.s_file, fn],
            [main.s_call, lst],
        [main.s_write],
    ]]

def s_code(start, end, data=None):
    if data == None:
        data = c_data
    return [hvc.asm.s_code, start, end, data, c_type]

def s_data(start, end, lst=None, data=None):
    if data == None:
        data = c_data
    return [hvc.asm.s_data, start, end, data, c_type, lst]

def s_bin(start, end, name, data=None):
    if data == None:
        data = c_data
    fn = name + ".bin"
    return [main.s_call, [
        [main.s_str, ".incbin \"%s\"\n" % fn],
        [main.s_bin, start, end, data, [fn]],
    ]]
