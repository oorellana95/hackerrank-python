def caesarCipher(s, k):
    alphabet_count = 26
    encrypted_string = ''
    for c in s:
        if c.isalpha():
            caesar_ascii = ord(c) + k % alphabet_count  # k_effect
            if c.isupper():
                encrypted_string += chr(caesar_ascii) if caesar_ascii < 91 else chr(caesar_ascii - alphabet_count)
            else:
                encrypted_string += chr(caesar_ascii) if caesar_ascii < 123 else chr(caesar_ascii - alphabet_count)
        else:
            encrypted_string += c
    return encrypted_string


if __name__ == '__main__':
    s = 'middle-Outz'
    k = 2
    print(caesarCipher(s, k))
