import re, os
def write_on_json_file(line, json_headers, f):    
    f.write("    {\n")

    line_splitted = re.split(",", line)
    print(line_splitted)
    for (i,entry) in enumerate(line_splitted):
        header = json_headers[i]
        if type(header) is dict and ("{" and "}") in list(header.keys())[0]:
            print(i)
            print("ola mundo")
            print(header)
        else:
            f.write(f"       \"{header}\": \"{entry}\"")
        
        if i != len(line_splitted)-1:
            f.write(f",\n")
        else:
            f.write("\n")
        
    
