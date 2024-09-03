from DataStructures.List import list_node as node
def new_list():
    lst = {'first': None, 'last': None, 'size': 0}
    return lst

def add_last(lst, elem):
    nodo = node.new_single_node(elem)
    if lst["size"] == 0:
        lst["first"] = nodo
        lst["last"] = nodo
    else:
        lst["last"]["next"] = nodo
        lst["last"] = nodo
    lst["size"] += 1
    return lst

def add_first(lst, elem):
    nodo = node.new_single_node(elem)
    if lst["size"] == 0:
        lst["first"] = nodo
        lst["last"] = nodo
    else:
        nodo["next"] = lst["first"]
        lst["first"] = nodo
    lst["size"] += 1
    return lst

def size(lst):
    return lst["size"]

def get_first_element(lst):
    if lst['first'] is not None:
        return lst['first']['info']
    else:
        return None

def remove_first(lst):
    if lst["first"] is not None:
        first_elem = lst["first"]["info"]
        lst["first"] = lst["first"]["next"]
        lst["size"] -= 1
        if lst["first"] is None:
            lst["last"] = None
        return first_elem
    else:
        return None

def is_empty(lst):
    return lst["first"] is None

def remove_last(lst):
    if lst["first"] is None:
        return None
    
    if lst["first"]["next"] is None:
        data = lst["first"]["info"]
        lst["first"] = lst["last"] = None
        lst["size"] -= 1
        return data
    
    current = lst["first"]
    while current["next"]["next"] is not None:
        current = current["next"]
    
    data = current["next"]["info"]
    current["next"] = None
    lst["last"] = current
    lst["size"] -= 1
    return data

def last_element(lst):
    if lst["last"] is not None:
        return lst["last"]["info"]
    return None

def get_element(lst, pos):
    if pos < 0 or pos >= lst["size"]:
        return None

    current = lst["first"]
    index = 0

    while current is not None:
        if index == pos:
            return current["info"]
        current = current["next"]
        index += 1

    return None

def delete_element(lst, pos):
    if pos < 0 or pos >= lst["size"]:
        return None

    if pos == 0: 
        return remove_first(lst)

    current = lst["first"]
    index = 0

    while current is not None and index < pos - 1:
        current = current["next"]
        index += 1

    if current is None or current["next"] is None:
        return None

    d = current["next"]["info"]
    current["next"] = current["next"]["next"]
    if current["next"] is None:
        lst["last"] = current
    lst["size"] -= 1
    return d

def is_present(lst, elem, cmp_function):
    current = lst["first"]
    pos = 0

    while current is not None:
        if cmp_function(current["info"], elem) == 0:
            return pos
        current = current["next"]
        pos += 1

    return -1

def change_info(lst, pos, new_info):
    current = lst["first"]
    index = 0

    while current is not None:
        if index == pos:
            current["info"] = new_info
            return lst
        current = current["next"]
        index += 1

    return lst 

def exchange(lst, pos1, pos2):
    if pos1 == pos2:
        return lst 

    node1 = node2 = None
    current = lst["first"]

    for index in range(max(pos1, pos2) + 1):
        if current is None:
            break
        if index == pos1:
            node1 = current
        if index == pos2:
            node2 = current
        current = current["next"]

    if node1 is not None and node2 is not None:
        node1["info"], node2["info"] = node2["info"], node1["info"]

    return lst
  
def sub_list(lst, pos, numelem):
    sub_lst = new_list()
    current = lst["first"]
    
    for index in range(pos):
        if current is None:
            return sub_lst
        current = current["next"]
        
    for _ in range(numelem):
        if current is None:
            break
        add_last(sub_lst, current["info"])
        current = current["next"]

    return sub_lst

def insert_element(lst, elem, pos):
    new_node = node.new_single_node(elem)

    if pos == 0:
        new_node["next"] = lst["first"]
        lst["first"] = new_node
        if lst["size"] == 0:
            lst["last"] = new_node  
    else:
        current = lst["first"]
        prev = None
        for index in range(pos):
            if current is None:
                raise IndexError("La posición está fuera de los límites de la lista.")
            prev = current
            current = current["next"]
        
        new_node["next"] = current
        if prev is not None:
            prev["next"] = new_node
        if current is None:
            lst["last"] = new_node  
    
    lst["size"] += 1
    return lst

