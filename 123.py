def didziausias_skaicius(*args):
    didziausias = args[0]
    for sk in args:
        if sk > didziausias:
             didziausias = sk
    return didziausias




print(didziausias_skaicius(5, 8, 789, 94, 78))