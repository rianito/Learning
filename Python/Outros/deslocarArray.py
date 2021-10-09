def deslocar(array,vezes):
    handle = []

    for i in range(len(array)):
        handle.append(0)

    for i in range(len(array)):

        if i - vezes < 0:
            handle[len(array) + (i - vezes)] = array[i]

        else:
            handle[i - vezes] = array[i]

    return handle

assert(deslocar([0,1,2,3,4,5],3) == [3,4,5,0,1,2])
assert(deslocar([1,2,3],0) == [1,2,3])