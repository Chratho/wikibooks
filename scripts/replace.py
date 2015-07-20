import re

in_file = "xml/enwikibooks-20150703-pages-no-markup.xml"
out_file = "xml/new.xml"

with open(in_file,"r") as inf:
    with open(out_file,"w") as outf:
        for line in inf:
            if not re.search("<(?![\/]{0,1}doc).*",line):
                outf.write(line)
