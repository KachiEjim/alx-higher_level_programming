#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C",1, 2, 4,  5, "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl", 1, 2, 4, 5 }
c_set = common_elements(set_1, set_2)
print((list(c_set)))
