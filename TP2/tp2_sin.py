# encoding=utf-8
import ply.yacc as yacc
from tp2_lex import tokens, literals


def p_Command(p):
    "Command : Idents id"
    global html
    global dictionary
    print("Idents = ", p[1])
    for it in reversed(sorted(dictionary.keys())):
        if it > p[1]:
            html = html + "\t" * it + "</" + dictionary[it] + ">\n"
            dictionary.pop(it)
    if dictionary.keys().__contains__(p[1]):
        html = html + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<" + p[2] + ">\n"
    else:
        html = html + "\t" * p[1] + "<" + p[2] + ">\n"
    dictionary[p[1]] = p[2]


def p_Idents(p):
    "Idents : Idents Ident"
    p[0] = p[1] + p[2]
    return p


def p_Idents_single(p):
    "Idents : "
    p[0] = 0
    return p


def p_Ident(p):
    "Ident : tab"
    p[0] = 1
    return p


def p_error(p):
    print('Erro Sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()

dictionary = {}

html = ""

import sys
parser.success = True
program = sys.stdin.read()
parser.parse(program)
if parser.success:
    print("Programa Válido")
else:
    print("Programa Inválido... Corrija e tente novamente")
for item in reversed(sorted(dictionary.keys())):
    html = html + "\t" * item + "</" + dictionary[item] + ">\n"
    dictionary.pop(item)
print(html)
