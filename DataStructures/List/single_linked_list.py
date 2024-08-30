from DataStructures.List import list_node as node
def add_last(lst,elem):
    nodo= node.new_single_node(elem)
    if lst["size"]==0:
        lst["first"]=nodo
        lst["size"]+=1
    else:
        lst["last"]["next"]=nodo
        lst["last"]=nodo
        lst["size"]+=1
    return lst
 
 def add_first(lst, elem):   
     if lst["size"]==0:
        lst["first"]=nodo
        lst["size"]+=1
     else:
        lst["first"]["next"]=nodo
        lst["first"]=nodo
        lst["size"]+=1
     return lst