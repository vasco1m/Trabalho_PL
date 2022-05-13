# encoding=utf-8
import ply.lex as lex


literals = ['.', '(', '{', '}', ':', '[', ']', '+', '-', '*', '/']
tokens = ['doctype', 'tab', 'str', 'dSign', 'hash', 'input', 'fp', 'equal', 'qStr',
        'comma', 'ppoint', 'apR', 'fpR', 'const', 'each', 'in', 'for', 'size', 'language']


def t_doctype(t):
    r'doctype'
    return t


# def t_chapiter(t):
#     r'chapiter'
#     return t


def t_input(t):
    r'input\('
    return t


def t_const(t):
    r'\-const'
    return t


def t_apR(t):
    r'\['
    return t


def t_fpR(t):
    r'\]'
    return t


def t_comma(t):
    r','
    return t


def t_equal(t):
    r'='
    return t


def t_qStr(t):
    r'\"\w+\"'
    return t


def t_fp(t):
    r'\)'
    return t


def t_hash(t):
    r'\#'
    return t


def t_dSign(t):
    r'\$'
    return t


def t_tab(t):
    r'\t'
    return t


def t_ppoint(t):
    r'p\.'
    return t


def t_each(t):
    r'each'
    return t


def t_for(t):
    r'for'
    return t


def t_in(t):
    r'in'
    return t


def t_size(t):
    r'size='
    return t


def t_language(t):
    r'language='
    return t


def t_str(t):
    r'[\w,\?\!\'\-\:\;]+'
    return t


t_ignore = " \n"


def t_error(t):
    print("Caractér ilegal: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
# import sys
# for line in sys.stdin:
#    lexer.input(line)
#    for tok in lexer:
#        print(tok)
