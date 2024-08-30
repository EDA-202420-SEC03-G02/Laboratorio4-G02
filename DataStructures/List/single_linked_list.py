from DataStructures.List import list_node as node
def add_last(lst,elem):
    nodo= node.new_single_node(elem)
    lst["last"]["next"]=nodo
    lst["last"]=nodo
    lst["size"]+=1
    if lst["size"]==1:
        lst["first"]=nodo
    return lst    
    
    