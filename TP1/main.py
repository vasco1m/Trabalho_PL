# coding=utf-8
import re


def json(dic, f_nome):
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
    match = re.findall(r'\"?(([\w/]+)({(\d+,\d+|\d+|\d+,|,\d+)}(::(sum|media))?)?)\"?', linha)
    print(match)  # APAGAR!!
    if match:
        lis = []
        for linha in f:
            dic = {}
            line = re.findall(r'\"?([\w/ ]+)\"?', linha)
            for i in range(0, len(match)):
                flag = True
                if re.match(r'^(([\w/]+)({(\d+,\d+|\d+|\d+,|,\d+)}(::(sum|media))))$', match[i][0]):
                    # operation:
                    sum = False
                    if match[i][5] == "sum":
                        sum = True
                    s = 0
                    split = match[i][3].split(",")
                    num = 0
                    for j in range(0, int(split[1])):
                        if line[i + j].isdigit():
                            if sum:
                                s += int(line[i + j])
                            num += 1
                    if num < int(split[0]):
                        flag = False
                    dic[match[i][1]] = s
                    i += num
                elif re.match(r'^(([\w/]+)({(\d+,\d+|\d+|\d+,|,\d+)}))$', match[i][0]):
                    ls = []
                    split = match[i][3].split(",")
                    num = 0
                    for j in range(0, int(split[1])):
                        if line[i + j].isdigit():
                            ls.append(int(line[i + j]))
                            num += 1
                    if num < int(split[0]):
                        flag = False
                    dic[match[i][1]] = ls
                    i += num
                else:
                    dic[match[i][0]] = line[i]
            if flag:
                lis.append(dic)
        print(lis)  # APAGAR

    # json("datasets/dataSetNotas.csv")


if __name__ == "__main__":
    main()
