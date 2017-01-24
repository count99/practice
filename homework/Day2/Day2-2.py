# Count the found word and chang color & highlight

def search_info():
    search_word = input("Please input search word? \t")
    with open("1.txt",mode="r", encoding="utf-8") as article:
        article_list = article.readlines()
    count = 0
    new_article = []
    for i in article_list:
        if search_word in i:
            count += 1
            a = i.replace(search_word, "\033[1;31;40m" + search_word + "\033[0m")
            new_article.append(a)
        else:
            new_article.append(i)

    print("Found record {}".format(count))
    print(" ".join(new_article))

if __name__ == '__main__':
    search_info()