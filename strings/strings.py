def removespace(string):
    return "".join(string.split())
string = " Pl ayTha tF u nkyM usi c "
print(removespace(string))


def getdigit(string):
    num = string
    for i in num:
        if i.isdigit():
            num+=i
        return num

print(getdigit('0s1a3y5w7h9a2t4?6!8?0'))


def acronym(string):
    word=string.split()
    acronym=""
    for i in word:
        acronym += i[0]
    return acronym

print(acronym("There's no free-lunch - gotta pay your way."))

arr1 = ["abc", 3, "yo"]
arr2 = [42, "wassup", True]
map=dict(zip(arr1,arr2))
print(map)


dict ={
    'Houston': 1,
    'Austin' : 2,
    'Dallas' : 3
}
dict = {value:key for key, value in dict.items()}
print(dict)