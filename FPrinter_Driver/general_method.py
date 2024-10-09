def read_code(p_code):
    v_res = []
    p_code = p_code.split('\n')
    for row in p_code:
        row = str(row)
        item = row.find(',')
        if item == -1:
            line = {
                'comand': row[0:],
                'param': ''
            }
        else:
            line = {
                'comand': row[0:item],
                'param': row[item + 1:]
            }
        v_res.append(line)

    return v_res
