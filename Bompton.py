bompton =  ""
compton = raw_input("Please enter term ")
for chr in compton:
    if chr == "c":
        bompton += "b"
    else:
        bompton += chr
print compton + "? Did you mean " + bompton + "?"
