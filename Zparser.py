import ply.yacc as yacc
from Zlexer import tokens


# Grammar rules
def p_statement_assign(p):
    "statement : ID EQUALS expression SEMICOLON"
    print("p_statement_assign:", p)
    p[0] = ("assign", p[1], p[3])


def p_expression_plus(p):
    "expression : expression PLUS term"
    print("p_expression_plus:", p)
    p[0] = ("plus", p[1], p[3])


def p_expression_minus(p):
    "expression : expression MINUS term"
    print("p_expression_minus:", p)
    p[0] = ("minus", p[1], p[3])


def p_expression_term(p):
    "expression : term"
    print("p_expression_term:", p)
    p[0] = p[1]


def p_term_multiply(p):
    "term : term MULTIPLY factor"
    print("p_term_multiply:", p)
    p[0] = ("multiply", p[1], p[3])


def p_term_divide(p):
    "term : term DIVIDE factor"
    print("p_term_divide:", p)
    p[0] = ("divide", p[1], p[3])


def p_term_factor(p):
    "term : factor"
    print("p_term_factor:", p)
    p[0] = p[1]


def p_factor_id(p):
    "factor : ID"
    print("p_factor_id:", p)
    p[0] = ("id", p[1])


def p_factor_num(p):
    "factor : NUMBER"
    print("p_factor_num:", p)
    p[0] = ("num", p[1])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
Zparser = yacc.yacc(
    debug=True,
    tabmodule="Zparsetab",
    optimize=False,
    write_tables=True,
    errorlog=yacc.NullLogger(),
)


ast = Zparser.parse(tokens)
