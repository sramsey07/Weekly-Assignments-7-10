def printAll(seq, level=0):
    indent = "  " * level
    print(f"{indent}printAll({seq})")
    if seq:
        print(f"{indent}  {seq[0]}")
        printAll(seq[1:], level=level+1)

seq = [1, 2, 3, 4, 5]
printAll(seq)
