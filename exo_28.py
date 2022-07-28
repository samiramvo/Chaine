import textwrap
paragraph="Python is widely used high-level,general-purpose,interpreted,dynamic programming"
paragraph_without_identation=textwrap.dedent(paragraph)
wrapped=textwrap.fill(paragraph_without_identation,width=50)
result=textwrap.indent(wrapped,'> ')
print(result)