# ==========================================
# STRING MANIPULATION
# ==========================================
# 1. Keyword: string.center() - https://docs.python.org/3/library/stdtypes.html#str.center
# Return centered in a string of length width.
def center_word(text,width):
  return text.center(width)
def center_word_with(text,width,symbol):
  return text.center(width,symbol)
print(center_word("test",10))
print(center_word_with("test",10,"*"))
# ==========================================
# CYCLIC PATTERN (Cycling through strings/lists) ---
# ==========================================
# Used to wrap around an index without using 'if' statements.
# Concept: Modulo (%) operator gives the remainder, creating a loop-back effect.
def print_cyclic_grid(text, num):
    index = 0
    for i in range(num):
        for j in range(num):
            # This cycles through the text indefinitely
            print(text[index % len(text)], end="")
            index += 1
        print()
  print_cyclic_grid("ab",3)
# Example: print_cyclic_grid("ab", 3) -> Output: 
# aba
# bab
# aba
# ==========================================
