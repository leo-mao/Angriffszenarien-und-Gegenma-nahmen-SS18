from Code.de.aug.Uebung1.rc4.rc4_part import KSA_PRGA as gen_keystream
from Code.de.aug.Uebung1.rc4.iv_loader import load_iv_keystream as read_IVKeystream


def crack_rc4_under_restrictions(scrambling_step=3):
    '''
    This function implements the crack of rc4, the algorithm is shown in the scripts(page 40).
    '''


    count = {}
    (IV_tuple_sets, keystream_firstbyte_set) = read_IVKeystream('/home/geek/Dropbox/Semester 6/AuG/rc4_testdata_2.txt')
    for index, IV_tuple in enumerate(IV_tuple_sets):
        x = int(IV_tuple[2], 16)
        j_2 = 5 + x
        keystream = gen_keystream(IV_tuple, scrambling_step)

        if len(keystream) != 0:
            z = hex(int(keystream_firstbyte_set[index], 16))
            j_3 = keystream.index(z)
            k_3 = j_3 - int(keystream[3], 16) - j_2
            if k_3 < 0:
                k_3 += 256
            k_3_hex = hex(k_3)

            if k_3_hex in count:
                count[k_3_hex] += 1
            else:
                count[k_3_hex] = 1
            # print(hex(k_3_hex))
    ordered_count = [(i, count[i]) for i in sorted(count, key=count.__getitem__, reverse=True)]
    print(ordered_count)

crack_rc4_under_restrictions()


