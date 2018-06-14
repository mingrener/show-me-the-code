import re


def words_set(infors):
    words_li = words_list(infors)
    # print(words_li)
    return set(words_li)


def words_list(infors):
    return re.split(r'[^a-zA-Z]+\s*', infors)


def count_num(infors):
    words_se = words_set(infors)
    words_li = words_list(infors)
    for word in words_se:
        num = words_li.count(word)
        print('The number of the word "%s":  [%d]' %(word, num))



if __name__ == '__main__':

    file_name = input('Please input a file name:')
    f = open('./text/' + file_name, 'r')
    file_infors = f.read()
    count_num(file_infors)

    f.close()