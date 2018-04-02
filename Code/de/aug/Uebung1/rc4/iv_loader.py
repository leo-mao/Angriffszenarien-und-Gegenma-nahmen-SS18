
def load_iv_keystream(path):
    '''
    :param path: path to file
    :return: (iv_set, keystream)
    '''
    #Save all the IVs in the form
        # [[iv, iv, iv], \
        # [iv, iv, iv], \
        # [iv, iv, iv]
        #...]
    IVs_set = []
    keystream_set = []
    with open(path ,'r') as file:
        for line in file:
            line_array = line.split()
            if len(line_array) < 5:
                continue
            if line_array[1] == '03' and line_array[2] == 'FF' :  # \
                    # and line_array[3] != 'FA' and line_array[3] != 'FB':  # array[0] is 'IV:',
                # If X in Step 2 == 'FA' or 'FB', S[0] and S[1] will be modified in the procession
                # Every iv tuper [iv, iv, iv]
                iv_cell = line_array[1:4]
                # iv_cell = [int(i, 16) for i in iv_cell]
                IVs_set.append(iv_cell)
                keystream_set.append(line_array[5])

        return (IVs_set, keystream_set)