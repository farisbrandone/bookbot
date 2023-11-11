import string
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(counts_words(file_contents))
    #print(count_alphabet(file_contents))
    sort_result=count_alphabet(file_contents)
    print(sort_list(sort_result))
   
def counts_words(world):
    count=world.split()
    return len(count)


def count_alphabet(world):
    result={}
    list_leter=list(string.ascii_lowercase)
    world.lower()
    for i in list_leter:
        result[i]=world.count(i)
    
    return result

def myfunc(e):
    return e[1]

def sort_list(dicts):
   tab=[]
   for key in dicts:
     elt=(key,dicts[key])
     tab.append(elt)
   #print(tab)
   tab.sort(key=myfunc, reverse=True)
   return tab


main()


