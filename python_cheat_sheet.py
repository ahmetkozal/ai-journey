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
