def doubled(hunny_jars):
    for x in range(0, len(hunny_jars)):
        hunny_jars[x] = hunny_jars[x] * 2

    return hunny_jars

print(doubled([1, 2, 3]))