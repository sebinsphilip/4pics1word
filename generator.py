from nltk.corpus import sentiwordnet as swn
import itertools
def main():
    # str=['s','a','f','e','v','i','w','j','k','x','k']
    # for i in str:
    #     for j in str:
    #
    i = raw_input("Length:")
    str = raw_input("Letter sequence:")
    f = open("combinations.txt",'w')
    k = list(itertools.permutations(str,int(i)))

    for i in k:
        for l in i:
            f.write(l)
        f.write('\n')
    f.close()

    h = []
    with open('combinations.txt') as hai:
        h = [word.lower().strip() for word in hai ]

    dic = {}
    for o in h:
        if o not in dic:
            dic [o]= 0
        else:
            dic[o] += 1

    m = open("out.txt",'w')

    for l in dic:
        v= list(swn.senti_synsets(l))
        if v:
            m.write(l)
            m.write('\n')


if __name__ == '__main__':
    main()
