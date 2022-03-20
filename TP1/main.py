# coding=utf-8
import re
import sys


def json(f_nome):
    f = open(f_nome, encoding='utf-8')
    res = open("alunos.json", "w", encoding='utf-8')
    res.write("[\n")
    f.readline()
    for linha in f:
        aluno = linha.split("\n")[0].split(",")
        res.write("{\n\t\"id_aluno\": ")
        res.write(aluno[0])
        res.write(",\n\t\"nome\": " + aluno[1] + ",\n\t\"curso\": " + aluno[2] +
                  ",\n\t\"tpc1\": " + aluno[3] + ",\n\t\"tpc2\": " + aluno[4] + ",\n\t\"tpc3\": " + aluno[6] +
                  ",\n\t\"tpc4\": " + aluno[6] + "\n}\n")
    res.write("]")

def main():
    f = open(input())
    linha = f.readline()
    if re.search(r'^\"?([\w/]+)\"?((\s?\,\s?\"?([\w/]+)\"?))*$',linha) != None: #Nome, Numero,Turma
        print("0")
    elif re.search(r'^\"?([\w/]+)\"?(\s?\,\s?\"?([\w/]+)(\{(\d+,\d+|\d+|\d+,|,\d+)\})?\"?)*$',linha) != None: # Nome,Numero,Turma{1,4}
        print("1")
    elif re.search(r'^\"?([\w/]+)\"?(\s?\,\s?\"?([\w/]+)(\{(\d+,\d+|\d+|\d+,|,\d+)\}\:\:(sum|media))?\"?)*$',linha) != None: #Nome,Numero,Turma{1,4}::media
        print("2")
    else:
        print("-1")
    #json("datasets/dataSetNotas.csv")

if __name__ == "__main__":
    main()
