# given a string

test_str = """
Asfweodsnkn
Sd;awjefsoi
___BEGIN___
La;jrgf;oi9
Weijsdnf;kl
Iwklasfnqdj
____END____
Asijfoijewd
"""

# return another string which contains only the lines between '___BEGIN___' and '____END____'

def cut_string(data):
    line_list = data.splitlines()
    line_list_cut = line_list[line_list.index('___BEGIN___') + 1:line_list.index('____END____')]
    result = '\n'.join((line_list_cut))

    return result

