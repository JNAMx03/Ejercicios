
date = input().upper()
date_split = date.split()
if date_split[0] == "OCT" or date_split[0] == "DEC":
    if date_split[1] == "31" or date_split[1] == "25":
        print("yup")
    else:
        print("nope")
else:
    print("nope")

