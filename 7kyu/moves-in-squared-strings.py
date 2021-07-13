def vert_mirror(st):
    new_str = ''
    st = st.split('\n')
    for word in st:
        new_str += word[::-1] + '\n'
    return new_str[:-1]

def hor_mirror(st):
  st = st.split('\n')[::-1]
  return '\n'.join(st)

def oper(fct, s):
    if fct == hor_mirror:
        return hor_mirror(s)
    else:
        return vert_mirror(s)