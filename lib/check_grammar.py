# def check_grammar(text):
#     punct_list = [".","!","?"]
#     if not isinstance(text,str):
#         raise Exception("Not a string!")
#     elif text[0].isupper() and text[-1] in punct_list:
#         return "No grammar problems!" 
#     elif text[0].isupper():
#         return "Incorrect punctuation detected"
#     elif text[-1] in punct_list:
#         return "No capital letter detected" 
#     return "Grammar error, no capital letter and punctuation detected" 
# 