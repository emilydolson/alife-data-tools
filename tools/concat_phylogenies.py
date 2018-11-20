import sys

ids = {}
header = ""

for arg in sys.argv[1:]:
    with open(arg) as phylofile:
        if header == "":
            header = phylofile.readline()
            idpos = header.find("id")
        else:
            assert(header == phylofile.readline())
        for line in phylofile:
            ids[line.split(",")[idpos]] = line

with open("all_phylogenies.csv", "w") as outfile:
    outfile.write(header)
    outfile.writelines(ids.values())
    
            
