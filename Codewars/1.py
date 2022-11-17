#  Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

list = ["Keep", "Remove", "Keep", "Remove", "Keep"]


def remove_every_other(my_list):
    for word in my_list + 1:
        list.remove(word)
    pass


remove_every_other(list)