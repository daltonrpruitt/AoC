# 16
import time

debug = True
sample = False
def debug_log(output):
    if debug: print(output)

startTime = time.time()

encoding = {code: bits for code,bits in [line.split(" = ") for line in open("encoding.txt", 'r').read().splitlines()]}

# Loading
if not sample:
    code = open("input.txt", 'r').read().splitlines()[0]
else:
    code = open("sample_input5.txt", 'r').read().splitlines()[0]

bits = ""
for char in code:
    bits+=encoding[char]

debug_log(code[:4] + " => " + bits[:4*4])

def compute_binary(bits):
    val = 0
    for i in range(len(bits)):
        val += (bits[i]=="1")*2**(len(bits)-i-1)
    return val


def process_literal(bit_code, pos):
    cur_pos = pos+6
    val = 0
    num_groups = 0
    while True:
        val = val*16 + compute_binary(bit_code[cur_pos+1:cur_pos+5])
        num_groups += 1
        if cur_pos > len(bit_code) or bit_code[cur_pos] == "0":
            cur_pos +=5
            break
        cur_pos += 5
    num_bits = 6 + 5*num_groups
    # if num_bits %4 != 0:
        # num_bits_rounded = num_bits + (4-num_bits%4) 
        # for i in range(num_bits, num_bits_rounded):
        #     assert(bit_code[i] == "0")
        # num_bits = num_bits_rounded
    return val, pos + num_bits

def process_operator(bit_code, pos):
    cur_pos = pos+6
    I = bit_code[cur_pos]=="1"
    cur_pos += 1
    num_packets = 0 
    version_totals = 0
    next_pos = 0
    vals = []
    if I:
        num_packets = compute_binary(bit_code[cur_pos:cur_pos+11])
        cur_pos += 11
        for i in range(num_packets):
            val, next_pos, temp_vers_sum = get_packet(bit_code,cur_pos)
            vals.append(val)
            cur_pos = next_pos
            version_totals += temp_vers_sum
    else:
        num_bits = compute_binary(bit_code[cur_pos:cur_pos+15])
        cur_pos += 15
        start_pos = cur_pos
        while next_pos - start_pos < num_bits:
            val, next_pos, temp_vers_sum = get_packet(bit_code,cur_pos)
            vals.append(val)
            cur_pos = next_pos
            version_totals += temp_vers_sum
            num_packets += 1
        assert(next_pos - start_pos == num_bits)
    
    return vals, next_pos, version_totals


def get_packet(bit_code, start_pos=0):
    pos = start_pos
    if start_pos > len(bit_code) -20:
        end = True
        for d in bit_code[start_pos:]:
            if d != "0": 
                end = False
                break
        if end:
            return 0, len(bit_code)
    debug_log(bit_code[pos:pos+3])
    debug_log(bit_code[pos+3:pos+6])

    _vers = compute_binary(bit_code[pos:pos+3])
    _id = compute_binary(bit_code[pos+3:pos+6])
    print(_vers,_id)
    # pos += 6
    next_pos = pos
    out_vers_sum = _vers
    out = 0
    if _id == 4:
        out, next_pos = process_literal(bit_code,pos)
        # out_vers_sum += _vers
    else:
        vals, next_pos, temp_vers_sum = process_operator(bit_code,pos)
        out_vers_sum += temp_vers_sum
        if _id == 0: # Sum
            out = vals[0]
            for v in vals[1:]:
                out += v
        elif _id == 1: # product
            out = vals[0]
            for v in vals[1:]:
                out *= v
        elif _id == 2: # min
            out = vals[0]
            for v in vals[1:]:
                out = min(v,out)
        elif _id == 3: # max
            out = vals[0]
            for v in vals[1:]:
                out = max(v,out)
        elif _id == 5: # greater than
            out = int(vals[0] > vals[1])
        elif _id == 6: # less than
            out = int(vals[0] < vals[1])
        elif _id == 7: # equal to
            out = int(vals[0] == vals[1])

    return out, next_pos, out_vers_sum

pos = 0 
value, x, version_totals = get_packet(bits, pos)


print(f"Total versions = {version_totals} Time={time.time() - startTime}s") #  875 
print(f"output value = {value} Time={time.time() - startTime}s")            #  1264857437203  