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
    "Command : Indents str" #id
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        for it in reversed(sorted(dictionary.keys())):
            if it > p[1]:
                html = html + "\t" * it + "</" + dictionary[it] + ">\n"
                dictionary.pop(it)
        if dictionary.keys().__contains__(p[1]):
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<" + p[2] + ">\n"
        else:
            html = html + "\t" * p[1] + "<" + p[2] + ">\n"
        dictionary[p[1]] = p[2]
    return p


def p_Command_point(p):
    "Command : Indents ppoint" #id
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        for it in reversed(sorted(dictionary.keys())):
            if it > p[1]:
                html = html + "\t" * it + "</" + dictionary[it] + ">\n"
                dictionary.pop(it)
        if dictionary.keys().__contains__(p[1]):
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<p>\n"
        else:
            html = html + "\t" * p[1] + "<p>\n"
        dictionary[p[1]] = "p"
        parser.inParagraph = True
        parser.paragraphLen = p[1]
    return p


def p_Command_pointClass(p):
    "Command : Indents str '.' str '.'"
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        for it in reversed(sorted(dictionary.keys())):
            if it > p[1]:
                html = html + "\t" * it + "</" + dictionary[it] + ">\n"
                dictionary.pop(it)
        if dictionary.keys().__contains__(p[1]):
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<" + p[2] + " class=\"" + p[4] + "\">\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + "<" + p[2] + " class=\"" + p[4] + "\">\n"
        dictionary[p[1]] = p[2]
        parser.inParagraph = True
        parser.paragraphLen = p[1]
    return p


def p_Command_pointClassp(p):
    "Command : Indents ppoint str '.'"
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        for it in reversed(sorted(dictionary.keys())):
            if it > p[1]:
                html = html + "\t" * it + "</" + dictionary[it] + ">\n"
                dictionary.pop(it)
        if dictionary.keys().__contains__(p[1]):
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<p class=\"" + p[3] + "\">\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + "<p class=\"" + p[3] + "\">\n"
        dictionary[p[1]] = "p"
        parser.inParagraph = True
        parser.paragraphLen = p[1]
    return p


def p_Command_divClass(p):
    "Command : Indents '.' str"
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        for it in reversed(sorted(dictionary.keys())):
            if it > p[1]:
                html = html + "\t" * it + "</" + dictionary[it] + ">\n"
                dictionary.pop(it)
        if dictionary.keys().__contains__(p[1]):
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<div class=\"" + p[3] + "\"></div>\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + "<div class=\"" + p[3] + "\"></div>\n"
        parser.inParagraph = True
        parser.paragraphLen = p[1]
    return p


def p_Command_divHash(p):
    "Command : Indents hash str"
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        for it in reversed(sorted(dictionary.keys())):
            if it > p[1]:
                html = html + "\t" * it + "</" + dictionary[it] + ">\n"
                dictionary.pop(it)
        if dictionary.keys().__contains__(p[1]):
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<div id=\"" + p[3] + "\"></div>\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + "<div id=\"" + p[3] + "\"></div>\n"
        parser.inParagraph = True
        parser.paragraphLen = p[1]
    return p


def p_Command_input(p):
    "Command : Indents input Atribs fp"
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + " " + p[3] + p[4] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        for it in reversed(sorted(dictionary.keys())):
            if it > p[1]:
                html = html + "\t" * it + "</" + dictionary[it] + ">\n"
                dictionary.pop(it)
        if dictionary.keys().__contains__(p[1]):
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<input " + p[3] + ">\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + "<input " + p[3] + ">\n"
    return p


def p_Command_Atrib(p):
    "Command : Indents str '(' Atrib fp"
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + " " + p[3] + p[4] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        for it in reversed(sorted(dictionary.keys())):
            if it > p[1]:
                html = html + "\t" * it + "</" + dictionary[it] + ">\n"
                dictionary.pop(it)
        if dictionary.keys().__contains__(p[1]):
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<div " + p[4] + ">\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + "<div " + p[4] + ">\n"
    return p


def p_Command_atribClass(p):
    "Command : Indents str '.' str '(' str equal str fp"
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        for it in reversed(sorted(dictionary.keys())):
            if it > p[1]:
                html = html + "\t" * it + "</" + dictionary[it] + ">\n"
                dictionary.pop(it)
        if htmlDict.__contains__(p[8]):
            value = htmlDict[p[8]]
        else:
            value = "error"
        if dictionary.keys().__contains__(p[1]):
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<" + p[2] + " class=\"" + p[4] + " " + value + "\"></" + p[2] + "\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + "<" + p[2] + " class=\"" + p[4] + " " + value + "\"></" + p[2] + "\n"
    return p


def p_Command_list(p):
    "Command : Indents const str equal apR LqStr fpR"
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        htmlDict[p[3]] = p[6]
    return p


def p_Command_titule(p):
    "Command : Indents str STR" #id
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + " " + p[3] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        for it in reversed(sorted(dictionary.keys())):
            if it > p[1]:
                html = html + "\t" * it + "</" + dictionary[it] + ">\n"
                dictionary.pop(it)
        if dictionary.keys().__contains__(p[1]):
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<" + p[2] + ">" + p[3] + "</" + p[2] + ">\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + "<" + p[2] + ">" + p[3] + "</" + p[2] + ">\n"
    return p


def p_Command_class(p):
    "Command : Indents str hash str STR" #id hash id
    global html
    flag = True
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + p[3] + p[4] + p[5] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        # Falta fechar todas as coisas abertas para trás
        html = html + "\t" * p[1] + "<" + p[2] + " id=" + p[4] + ">" + p[5] + "</" + p[2] + ">\n"
    return p
    

def p_Command_doctype(p):
    "Command : doctype str" # id
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
    "Atrib : str equal qStr"
    p[0] = p[1] + "=" + p[3]
    return p


def p_Atrib_str(p):
    "Atrib : str equal str"
    if htmlDict.__contains__(p[3]):
        p[0] = p[1] + "=" + htmlDict[p[3]]
    else:
        p[0] = p[1] + "=" + p[3]
    return p


def p_str(p):
    "STR : STR str"
    p[0] = p[1] + " " + p[2]
    return p


def p_str_var(p):
    "STR : dSign str dSign"
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
parser.inParagraph = False
parser.paragraphLen = 0
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
