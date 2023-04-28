import ply.yacc as yacc
from Zlexer import tokens


# Grammar rules 

'''
    1st rule
       s >> id = E;
       an expression can be assigned to an identifier and the expression has to be followed by ";" the statement terminator
'''

def p_statement_assign(p):
    'statement : ID EQUALS expression SEMICOLON'
    print(f'{p[1]} = {p[3]}')


