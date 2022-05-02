# encoding=utf-8
import ply.lex as lex


literals = []
tokens = ['id', 'tab']


def t_id(t):
    r'[a-zA-Z_]\w*'
    return t


def t_tab(t):
    r'\t'
    return t


t_ignore = "\n"


def t_error(t):
    print("Caractér ilegal: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

