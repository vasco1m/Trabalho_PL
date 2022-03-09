# coding=utf-8
import re

def ex0():
    f = open("teste.txt")
    for linha in f:
        if re.search(r'^Ola$',linha) != None:
            print("0")
        elif re.search(r'^Ola',linha) != None:
            print("1")
        elif re.search(r'Ola$',linha) != None:
            print("2")
        else:
            print("-1")

def json(f_nome):
    f = open(f_nome, encoding='utf-8')
    res = open("alunos.json", "w", encoding='utf-8')
    res.write("[\n")
    l = f.readline()
    for linha in f:
        aluno = linha.split("\n")[0].split(",")
        res.write("{\"id_aluno\" : " + aluno[0] + ", \"nome\" : " + aluno[1] + ", \"curso\" : " + aluno[2] +
                  ", \"tpc1\" : " + aluno[3] + ", \"tpc2\" : " + aluno[4] + ", \"tpc3\" : " + aluno[6] +
                  ", \"tpc\" : " + aluno[6] + "},\n")
    res.write("]")

def main():
    ex4()

if __name__ == "__main__":
    main()
