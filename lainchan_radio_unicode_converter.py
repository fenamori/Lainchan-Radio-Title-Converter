import sys

title_unicode = ""
is_char = False
count = 0
char_raw = ""

if len(sys.argv) > 1: title_raw = str(sys.argv[1])
else: title_raw = input("Enter string: \n")

for x in title_raw:

    match x:
        case "#": is_char = True
        case ";": is_char = False

    if x.isnumeric() and is_char: 
        count += 1
        char_raw += x

    match count:
        case 5: 
            title_unicode += chr(int(char_raw))
            count = 0
            char_raw = ""
        case 0: title_unicode += x


print("\n", title_unicode.replace("&#", "").replace(";", ""))
