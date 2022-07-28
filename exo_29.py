import textwrap
paragraph="Python is widely used high-level,general-purpose,interpreted,dynamic programming"
text_without_ident=paragraph.dedent(paragraph).strip()

print(textwrap.fill(text_without_ident,initial_indent='',subsequent_indent=' '*4,width=80,))