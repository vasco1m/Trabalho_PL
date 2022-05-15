# encoding=utf-8
import ply.yacc as yacc
import re
from tp2_lex import tokens, literals


def p_Commands(p):
    "Commands : Commands Command"
    return p


def p_Commands_single(p):
    "Commands : Command"
    return p


def p_Command(p):
    "Command : Indents str"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
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





def p_Command_strpoint(p):
    "Command : Indents str '.'"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
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
        parser.inParagraph = True
        parser.paragraphLen = p[1]
    return p


def p_Command_pointClass(p):
    "Command : Indents str '.' str '.'"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
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


def p_Command_ClassDotClass(p):
    "Command : Indents str '.' str"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
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
    return p


def p_Command_bracketsOpen(p):
    "Command : Indents str '{'"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + '{\n'
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
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + p[2] + "{\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + p[2] + "{\n"
        parser.inParagraph = True
        parser.paragraphLen = p[1]
    return p


def p_Command_bracketsClose(p):
    "Command : Indents '}'"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        html = html + "\t" * p[1] + "}\n"
        parser.inParagraph = False
        parser.paragraphLen = 0
    return p


def p_Command_divClass(p):
    "Command : Indents '.' str"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
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
    if parser.eachFlag:
        writeEach()
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
    "Command : Indents input Atribs ')'"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
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
    "Command : Indents str '(' Atribs ')'"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
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
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<" + p[2] + " " + p[4] + ">\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + "<" + p[2] + " " + p[4] + ">\n"
    return p


def p_Command_AtribStr(p):
    "Command : Indents str '(' Atribs ')' STR"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + " " + p[3] + p[4] + p[5] + p[6] + '\n'
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
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<" + p[2] + " " + p[4] + ">" + p[6] + "</" + p[2] + ">\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + "<" + p[2] + " " + p[4] + ">" + p[6] + "</" + p[2] + ">\n"
    return p


def p_Command_atribClass(p):
    "Command : Indents str '.' str '(' str '=' str ')'"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
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
    "Command : Indents const str '=' '[' LqStr ']'"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + '\n'
        flag = False
    elif p[1] <= parser.paragraphLen:
        parser.inParagraph = False
        parser.paragraphLen = 0
    if flag:
        htmlDict[p[3]] = p[6]
    return p


def p_Command_href(p):
    "Command : Indents href link STR"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
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
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n" + "\t" * p[1] + "<" + p[2] + p[3] + ">" + p[4] + "</a>\n"
            dictionary.pop(p[1])
        else:
            html = html + "\t" * p[1] + "<" + p[2] + p[3] + ">" + p[4] + "</a>\n"
    return p


def p_Command_titule(p):
    "Command : Indents str STR"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
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


def p_Command_eachFor(p):
    "Command : Indents Cycle str in Range"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
    if parser.inParagraph and int(p[1]) > parser.paragraphLen:
        html = html + '\t' * p[1] + p[2] + " " + p[3] + p[4] + p[5] + p[6] + '\n'
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
            html = html + "\t" * p[1] + "</" + dictionary[p[1]] + ">\n"
            dictionary.pop(p[1])
        parser.eachIterator = p[3]
        parser.eachTabs = p[1]
        parser.eachFlag = True
    return p


def p_Command_CycleLine(p):
    "Command : Indents dSign str '=' Op"
    parser.eachVar.append(p[3])
    parser.each.append(p[5])
    parser.eachLen += 1


def matrixSum(p1, p2):
    if isinstance(p1,int):
        if isinstance(p2,int):
            return p1 + p2
        elif isinstance(p2,list):
            res = []
            for elem in p2:
                res.append(elem + p1)
            return res
    elif isinstance(p1,list):
        if isinstance(p2,int):
            res = []
            for elem in p1:
                res.append(elem + p2)
            return res
        elif isinstance(p2,list):
            res = []
            i = 0
            for elem in p2:
                res.append(elem + p1[i])
                i += 1
            return res


def matrixSub(p1, p2):
    if isinstance(p1,int):
        if isinstance(p2,int):
            return p1 - p2
        elif isinstance(p2,list):
            res = []
            for elem in p2:
                res.append(p1 - elem)
            return res
    elif isinstance(p1,list):
        if isinstance(p2,int):
            res = []
            for elem in p1:
                res.append(elem - p2)
            return res
        elif isinstance(p2,list):
            res = []
            i = 0
            for elem in p2:
                res.append(p1[i] - elem)
                i += 1
            return res


def matrixMul(p1, p2):
    if isinstance(p1,int):
        if isinstance(p2,int):
            return p1 * p2
        elif isinstance(p2,list):
            res = []
            for elem in p2:
                res.append(p1 * elem)
            return res
    elif isinstance(p1,list):
        if isinstance(p2,int):
            res = []
            for elem in p1:
                res.append(elem * p2)
            return res
        elif isinstance(p2,list):
            res = []
            i = 0
            for elem in p2:
                res.append(p1[i] * elem)
                i += 1
            return res


def matrixDiv(p1, p2):
    if isinstance(p1,int):
        if isinstance(p2,int):
            return p1 / p2
        elif isinstance(p2,list):
            res = []
            for elem in p2:
                res.append(p1 / elem)
            return res
    elif isinstance(p1,list):
        if isinstance(p2,int):
            res = []
            for elem in p1:
                res.append(elem / p2)
            return res
        elif isinstance(p2,list):
            res = []
            i = 0
            for elem in p2:
                res.append(p1[i] / elem)
                i += 1
            return res


def p_Op_sum(p):
    "Op : Op '+' Op"
    p[0] = matrixSum(p[1],p[3])
    return p


def p_Op_sub(p):
    "Op : Op '-' Op"
    p[0] = matrixSub(p[1],p[3])
    return p


def p_Op_mul(p):
    "Op : Op '*' Op"
    p[0] = matrixMul(p[1],p[3])
    return p


def p_Op_div(p):
    "Op : Op '/' Op"
    p[0] = matrixDiv(p[1],p[3])
    return p


def p_Op_val(p):
    "Op : str"
    if p[1].isdigit():
        p[0] = int(p[1])
    elif parser.eachIterator == p[1]:
        p[0] = parser.eachRange
    return p


def p_eachFor_each(p):
    "Cycle : each"
    return p


def p_eachFor_for(p):
    "Cycle : for"
    return p


def p_Range_list(p):
    "Range : '[' STR ']'"
    range = p[2].split(",")
    i = 0
    for elem in range:
        parser.eachRange.append(int(elem))
    parser.eachLen = i
    return p


def p_Range_var(p):
    "Range : str"
    if htmlDict.__contains__(p[1]):
        parser.eachRange = htmlDict[p[1]]
    else:
        parser.eachRange = None
    return p


def p_Command_class(p):
    "Command : Indents str hash str STR"
    global html
    flag = True
    if parser.eachFlag:
        writeEach()
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
    "Command : doctype str"
    global html
    if p[2] == "html":
        parser.htmlFlag = True
        html = html + "<!DOCTYPE " + p[2] + ">\n"
    else:
        parser.succsess = False
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
    "Atrib : str '=' qStr"
    p[0] = p[1] + "=" + p[3]
    return p


def p_Atrib_link(p):
    "Atrib : str '=' link"
    p[0] = p[1] + "=" + p[3]
    return p


def p_Atrib_str(p):
    "Atrib : str '=' str"
    if htmlDict.__contains__(p[3]):
        p[0] = p[1] + "=" + htmlDict[p[3]]
    else:
        p[0] = p[1] + "=" + p[3]
    return p


def p_str(p):
    "STR : STR str"
    p[0] = p[1] + " " + p[2]
    return p


def p_str_Atribs(p):
    "STR : STR Atrib"
    p[0] = p[1] + " " + p[2]
    return p


def p_str_var(p):
    "STR : dSign str dSign"
    p[0] = htmlDict[p[2]]
    return p


def p_str_varDotVar(p):
    "STR : dSign str '.' str dSign"
    p[0] = htmlDict[p[2]].p[4]
    return p


def p_str_single(p):
    "STR : str"
    p[0] = p[1]
    return p


def p_str_attribute(p):
    "STR : Atrib"
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


def helpCommand():
    return """Hi, I'm here to help.
This program is a parser from simple files to HTML, to use it you have to insert the header \"doctype html\", and write your code in a very simple way.
Use tabs to indent your code and create nested resources.
\n\n\nVersion: 1.0"""


def writeEach():
    global html
    for i in range(0, len(parser.eachRange)):
        j = 0
        for elem in parser.each:
            html = html + "\t" * parser.eachTabs + "<" + parser.eachVar[j] + ">" + str(elem[i]) + "</" + parser.eachVar[j] + ">\n"
            j += 1
    parser.eachFlag = False
    parser.eachVar = []
    parser.eachTabs = 0
    parser.each = []
    parser.eachLen = 0
    parser.eachRange = []
        


# Build the parser
parser = yacc.yacc()

dictionary = {}
testsDict = {"1":"aaaa", "2":"bbbb", "3":"cccc"}
testsDict['myList'] = ['Ana', 'João', 'Luís', 'Rita']
html = ""

import sys
import yaml

if sys.argv[1] == "-h":
    print(helpCommand())
    quit()
file = open(sys.argv[1])
if file == None:
    print("The file you selected can't be opened. Please check the problem")
else:
    if len(sys.argv) > 2:
        with open(sys.argv[2]) as fileD:
            htmlDict = yaml.load(fileD, Loader=yaml.FullLoader)
    else:
        htmlDict = testsDict
    parser.success = True
    parser.validFileFormat = True
    parser.htmlFlag = False
    parser.inParagraph = False
    parser.paragraphLen = 0
    parser.each = False
    parser.list = []
    parser.iteration = 0
    parser.each = []
    parser.eachLen = 0
    parser.eachFlag = False
    parser.eachVar = []
    parser.eachTabs = 0
    parser.eachRange = []
    parser.eachIterator = ""
    program = file.read()
    parser.parse(program)
    if parser.htmlFlag:
        fileName = re.sub(r'(.*)\..*', r'\1.html', file.name)
    if parser.validFileFormat == False:
        print("Error: Invalid File Format. Please check the help options with -h")
    elif parser.success:
        print("All worked out! Check your document: " + fileName)
    else:
        print("Programa Inválido... Corrija e tente novamente")
    for item in reversed(sorted(dictionary.keys())):
        html = html + "\t" * item + "</" + dictionary[item] + ">\n"
        dictionary.pop(item)
    endFile = open(fileName, "w", encoding='utf-8')
    endFile.write(html)

