import ply.lex as lex

# defining the tokens section

tokens = (
    "SEMICOLON",
    "COMMA",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "ID",
    "NUMBER",
    "PLUS",
    "MINUS",
    "MULTIPLY",
    "DIVIDE",
    "EQUALS",
    "STRING_LITERAL",
)

# Regular expressions for simple tokens
t_SEMICOLON = r";"
t_COMMA = r","
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"


# Regular expressions for complex tokens
t_PLUS = r"\+"
t_MINUS = r"-"
t_MULTIPLY = r"\*"
t_DIVIDE = r"/"
# t_MOD = r"%"
t_EQUALS = r"="


def t_STRING_LITERAL(token):
    r'"[^"]*"'
    token.value = token.value[1:-1]  # remove the quotes from the value
    return token


# ID Token
def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = "ID"
    return t


# Number Token
def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Newline handling
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Ignore whitespace
t_ignore = " \t"


# Ignore comments
t_ignore_COMMENT = r"\/\/.*"


# Error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test the lexer on sample code
data = """

int main() {
    int x, a = 2, b = 3, c = 5;
    x = a + b * 5 * (c - 3 / a);
    printf("The value of x is %d", x);
    return 0;
}
"""
tokens = []
lexer.input(data)
for token in lexer:
    tokens.append(token)
    print(token)
