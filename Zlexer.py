import ply.lex as lex

# defining the tokens section, acc to our scope it shd only have basic arithmetic operators so ................

tokens = (
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'PLUS', 
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
)

# error handler function

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#regular expressions 

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'

t_ignore = ' \t\n'     #to ignore the white spaces we dont want em to appear as errors cuz they aint defined 


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# instance for the imported lexer

lexer = lex.lex()

# Test for the lexer

data = '(3 + 4) * 10'
lexer.input(data)
for token in lexer:
    print(token)
