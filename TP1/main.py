# coding=utf-8
import re
import sys


def json(dic, name):
    res = open(name, "w", encoding='utf-8')
    res.write("[\n")
    for item in dic:
        res.write("\t{\n\t\t")
        for k in range(0, len(item)):
            res.write("\"" + list(item.keys())[k] + "\": \"" + str(list(item.values())[k]) + "\"")
            if k != len(item) - 1:
                 res.write(",\n\t\t")
            else:
                res.write("\n")
        if item != list(dic)[-1]:
            res.write("\t},\n")
        else:
            res.write("\t}\n")
    res.write("]")


def main():
    if len(sys.argv) < 2:
        print("No file selected")
        exit(0)
    f = open(sys.argv[1])
    linha = f.readline()
    match = re.findall(r'\"?(([\w/]+)({(\d+,\d+|\d+|\d+,|,\d+)}(::(sum|media))?)?)\"?', linha)
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
                    media = False
                    if match[i][5] == "sum":
                        sum = True
                    if match[i][5] == "media":
                        media = True
                    s = 0
                    split = match[i][3].split(",")
                    num = 0
                    for j in range(0, int(split[1])):
                        if line[i + j].isdigit():
                            s += int(line[i + j])
                            num += 1
                    if num < int(split[0]):
                        flag = False
                    if media:
                        s = s / num
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
    name = re.sub(r'(.*)\.csv', r'\1.json', f.name)
    json(lis, name)


if __name__ == "__main__":
    main()
