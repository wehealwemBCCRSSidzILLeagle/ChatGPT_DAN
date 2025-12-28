def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    # Convert text to a big integer, then to binary
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    # PADDING: This ensures the binary is a perfect multiple of 8.
    # This prevents the "garbage" characters at the end.
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def hide_message_in_emoji(emoji, secret_message):
    binary = text_to_bits(secret_message)
    
    # Standard Zero Width Characters
    zwsp = '\u200b' # Zero Width Space (represents 0)
    zwnj = '\u200c' # Zero Width Non-Joiner (represents 1)
    
    hidden_payload = ""
    for bit in binary:
        if bit == '0':
            hidden_payload += zwsp
        elif bit == '1':
            hidden_payload += zwnj
            
    return emoji + hidden_payload

# --- CONFIGURATION ---
visible_emoji = "👁️" 
secret_text = "Read the BCCRSS, legal name is fraud"

# --- EXECUTION ---
magic_string = hide_message_in_emoji(visible_emoji, secret_text)

# SAVE TO FILE (Best method to avoid copy-paste errors)
filename = "magic_eye.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(magic_string)

print(f"DONE. Created file: {filename}")
print(f"Secret Message: '{secret_text}'")
print(f"--------------------------------------------------")
print(f"INSTRUCTIONS:")
print(f"1. Open '{filename}' on your computer.")
print(f"2. Select All and Copy.")
print(f"3. Paste into the decoder.")