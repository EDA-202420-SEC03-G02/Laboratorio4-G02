from DataStructures.List import list_node as node
def new_list():
    lst={'first': None,'last': None,'size': 0}
    return lst
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
    nodo= node.new_single_node(elem)
     if lst["size"]==0:
        lst["first"]=nodo
        lst["size"]+=1
     else:
        lst["next"]["first"]=nodo
        lst["first"]=nodo
        lst["size"]+=1
     return lst
    nodo_nuevo= node.new_single_node(elem)
    if lst["size"] == 0:
        lst["first"] = nodo_nuevo 
    else:
        lst["last"]["next"] = nodo_nuevo
    lst["last"] = nodo_nuevo
    lst["size"] += 1
    
    return lst   
def size(lst):
    return lst["size"]

def get_first_element(lst): 
    if lst['first'] is not None:
        return lst['first']['value']
    else:
        return None 
def remove_first(lst):
    if lst["first"] is not None:
        first_elem=lst["first"]["value"]
        lst["first"]=lst["first"]["next"]
        lst["size"]-=1
        if lst["first"] is None:
            lst["last"]=None
        return first_elem    
            
    else:
        return None        
def is_present(lst,elem, cmp_function):

    size=lst["size"]
    if size>0:
        existe

   
   
