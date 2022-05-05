# encoding=utf-8
import ply.yacc as yacc
from tp2_lex import tokens, literals


def p_Commands(p):
    "Commands : Commands Command"
    return p


def p_Commands_single(p):
    "Commands : Command"
    return p


def p_Command(p):
    "Command : Indents id"
    global html
    for it in reversed(sorted(dictionary.keys())):
        if it > p[1]:
            html = html + "\t" * it + "</" + dictionary[it] + ">\n"
            dictionary.pop(it)
    if dictionary.keys().__contains__(p[1]):
        html = html + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<" + p[2] + ">\n"
    else:
        html = html + "\t" * p[1] + "<" + p[2] + ">\n"
    dictionary[p[1]] = p[2]
    return p


def p_Command_input(p):
    "Command : Indents input Atribs fp"
    global html
    for it in reversed(sorted(dictionary.keys())):
        if it > p[1]:
            html = html + "\t" * it + "</" + dictionary[it] + ">\n"
            dictionary.pop(it)
    if dictionary.keys().__contains__(p[1]):
        html = html + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<input " + p[3] + ">\n"
        dictionary.pop(p[1])
    else:
        html = html + "\t" * p[1] + "<" + p[3] + ">\n"
    return p


def p_Command_list(p):
    "Command : Indents const str equal apR LqStr fpR"
    global html
    global htmlDict
    htmlDict[p[3]] = p[6]
    return p


def p_Command_titule(p):
    "Command : Indents id STR"
    global html
    html = html + "\t" * p[1] + "<" + p[2] + ">" + p[3] + "</" + p[2] + ">\n"
    return p


def p_Command_class(p):
    "Command : Indents id hash id STR"
    global html
    # Falta fechar todas as coisas abertas para trás
    html = html + "\t" * p[1] + "<" + p[2] + " id=" + p[4] + ">" + p[5] + "</" + p[2] + ">\n"
    return p


def p_Command_point(p):
    "Command : Indents id point"
    for it in reversed(sorted(dictionary.keys())):
        if it > p[1]:
            html = html + "\t" * it + "</" + dictionary[it] + ">\n"
            dictionary.pop(it)
    if dictionary.keys().__contains__(p[1]):
        html = html + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<" + p[2] + ">\n"
    else:
        html = html + "\t" * p[1] + "<" + p[2] + ">\n"
    dictionary[p[1]] = p[2]
    return p


def p_Command_p(p):
    "Command : Indents p STR"
    global html
    for it in reversed(sorted(dictionary.keys())):
        if it > p[1]:
            html = html + "\t" * it + "</" + dictionary[it] + ">\n"
            dictionary.pop(it)
    if dictionary.keys().__contains__(p[1]):
        html = html + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<p>" + p[3] + "\n"
    else:
        html = html + "\t" * p[1] + "<" + p[2] + ">\n"
    dictionary[p[1]] = p[2]
    return p
    

def p_Command_doctype(p):
    "Command : doctype id"
    global html
    html = html + "<!DOCTYPE " + p[2] + ">\n"
    return p


def p_LqStr(p):
    "LqStr : LqStr comma qStr"
    p[0] = p[1] + ", " + p[3]
    return p


def p_LqStr_single(p):
    "LqStr : qStr"
    p[0] = p[1]
    return p


def p_Atribs(p):
    "Atribs : Atribs Atrib"
    p[0] = p[1] + " " + p[2]
    return p


def p_Atribs_single(p):
    "Atribs : Atrib"
    p[0] = p[1]
    return p


def p_Atrib(p):
    "Atrib : id equal qStr"
    p[0] = p[1] + "=" + p[3]
    return p


def p_str(p):
    "STR : STR str"
    p[0] = p[1] + " " + p[3]
    return p


def p_str_var(p):
    "STR : dSign str dSign"
    global htmlDict
    p[0] = htmlDict[p[2]]
    return p


def p_str_single(p):
    "STR : str"
    p[0] = p[1]
    return p


def p_Indents(p):
    "Indents : Indents Indent"
    p[0] = p[1] + p[2]
    return p


def p_Indents_empty(p):
    "Indents : "
    p[0] = 0
    return p


def p_Indent(p):
    "Indent : tab"
    p[0] = 1
    return p


def p_error(p):
    print('Erro Sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()

dictionary = {}
htmlDict = {"1":"aaaa", "2":"bbbb", "3":"cccc"}
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
