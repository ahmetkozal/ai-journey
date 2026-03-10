# ==========================================
# PART 3 - STRING MANIPULATION [https://programming-26.mooc.fi/part-3]
# ==========================================
# 1. Keyword: string.center() - https://docs.python.org/3/library/stdtypes.html#str.center
# Return centered in a string of length width.
# Context: Python Programming MOOC 2026 Part 3/2 [https://programming-26.mooc.fi/part-3/2-working-with-strings], Exercise "A framed word"
def center_word(text,width):
  return text.center(width)
def center_word_with(text,width,symbol):
  return text.center(width,symbol)
print(center_word("test",10))
print(center_word_with("test",10,"*"))
# ==========================================
# PART 3/4 - LOOPS AND FUNCTIONS [https://programming-26.mooc.fi/part-3/4-defining-functions]
# ==========================================
# --- Cyclic Pattern (Cycling through strings/lists) ---
# Used to wrap around an index without using 'if' statements.
# Concept: Modulo (%) operator gives the remainder, creating a loop-back effect. Exercise "A word squared"

def squared(text, num):
    index = 0
    for i in range(num):
        for j in range(num):
            # This cycles through the text indefinitely
            print(text[index % len(text)], end="")
            index += 1
        print()
  squared("ab",3)
# Example: squared("ab", 3) -> Output: 
# aba
# bab
# aba
# ==========================================
