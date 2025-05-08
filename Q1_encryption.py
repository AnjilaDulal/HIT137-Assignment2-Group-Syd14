def verify(original, decrypted):
    return original == decrypted


def read_file(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None


def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def shift_char(c, shift, direction='forward'):
    base = ord('a') if c.islower() else ord('A')
    if direction == 'forward':
        return chr((ord(c) - base + shift) % 26 + base)
    else:
        return chr((ord(c) - base - shift) % 26 + base)


def encrypt(text, n, m):
    encrypted = ''
    for c in text:
        if c.islower():
            encrypted += shift_char(c, n + m, 'forward')
        elif c.isupper():
            encrypted += shift_char(c, m ** 2, 'forward')
        else:
            encrypted += c
    return encrypted


def decrypt(text, n, m):
    decrypted = ''
    for c in text:
        if c.islower():
            decrypted += shift_char(c, n + m, 'backward')
        elif c.isupper():
            decrypted += shift_char(c, m ** 2, 'backward')
        else:
            decrypted += c
    return decrypted


def main():
    try:
        n = int(input('Enter integer n: '))
        m = int(input('Enter integer m: '))
    except ValueError:
        print("Error: Please enter valid integers for n and m.")
        return

    raw_text = read_file('raw_text.txt')  
    if raw_text is None:
        return

    encrypted_text = encrypt(raw_text, n, m)
    write_file('encrypted_text.txt', encrypted_text)

    decrypted_text = decrypt(encrypted_text, n, m)
    write_file('decrypted_text.txt', decrypted_text)

    # Verify and write result
    result_text = f"Decryption Correct: {verify(raw_text, decrypted_text)}"
    write_file('result.txt', result_text)

    print("\nEncryption and decryption complete.")
    print("Results saved to:")
    print(" - encrypted_text.txt")
    print(" - decrypted_text.txt")
    print(" - result.txt")

    print("\nOutput saved to 'encrypted_text.txt', 'decrypted_text.txt', and 'result.txt'")

if __name__ == '__main__':
    main()
