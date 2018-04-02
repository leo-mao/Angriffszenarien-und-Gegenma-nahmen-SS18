def KSA_PRGA(key, scrambling_step = 256):
    """
    Function to generate key steam
    :param key: a.k.a IV, in format Hex
    :param text_length
    :return: key stream
    """

    # Initialization
    # Preparation

    pre_stream = [0] * 256
    for i in range(0, 256):
        pre_stream[i] = i
    j = 0
    key = [int(i) for i in key]
    print("key={key}".format(key=key))

    # Scrambling the pre_stream with key
    for i in range(0, scrambling_step):
        j = (pre_stream[i] + j + key[i % len(key)]) % 256
        if i == 2 and (j == 1 or j == 0):
            print("pre_stream={pre_stream}".format(pre_stream=pre_stream))
            print('S[0] or S[1] will be modified, thrown the result.')
            return []
        tmp = pre_stream[i]
        pre_stream[i] = pre_stream[j]
        pre_stream[j] = tmp

    # Generate the key_stream, PRGA(key)

    i = 0
    j = 0
    key_stream = [0] * 256

    for index in range(0, 256):
        i = (i + 1) % 256
        j = (j + pre_stream[i]) % 256

        tmp = pre_stream[i]
        pre_stream[i] = pre_stream[j]
        pre_stream[j] = tmp

        key_stream[index] = pre_stream[(pre_stream[i] + pre_stream[j]) % 256]

    key_stream = [hex(i) for i in key_stream]
    print('key_stream={key_stream}'.format(key_stream=key_stream))
    return key_stream


def Encrypt_Decrypt(key, text):

    key_stream = KSA_PRGA(key, len(text))
    text = [int(i) for i in text]
    # print("plaintext={plaintext}".format(plaintext=text))

    results = []
    for i in range(len(text)):
        results.append(text[i] ^ int(key_stream[i], 16))

    results = [hex(i) for i in results]
    print('result={results}'.format(results=results))
    return results


key_text = 'Key'
key = [ord(i) for i in key_text]
plain_text = 'Plaintext'
plain_text = [ord(i) for i in plain_text]
crypto_text = Encrypt_Decrypt(key, plain_text)
# result_text = Encrypt_Decrypt(key , crypto_text)

