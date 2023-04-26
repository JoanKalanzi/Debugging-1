"""Return to this example and debug it using Discovery Debugging.

If you can, forget about trying to solve it. Instead, discover as much as you can about what is going on in the program.
"""

def encode(text, key):
    print( f" text arg {text}")
    print( f" key arg {key}")
    cipher = make_cipher(key)
    ciphertext_chars = []
    for i in text:
      if i in cipher:   
        print(f" replace {i} with:")
        ciphered_char = chr(65 + cipher.index(i))
        print( f" ciphered_char {ciphered_char}")
        ciphertext_chars.append(ciphered_char)
        print(ciphertext_chars)
      else:
        continue
    return "".join(ciphertext_chars)
   


def decode(encrypted, key):
    cipher = make_cipher(key)
    print(f"\nKEY: {key}")

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[65 - ord(i)]
        print(f"plain_char {plain_char}")
        plaintext_chars.append(plain_char)
        print(f"plaintext_chars , {plaintext_chars}")

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 98) for i in range(1, 26)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")