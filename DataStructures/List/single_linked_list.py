from DataStructures.List import list_node as node
def add_last(lst,elem):
    nodo= node.new_single_node(elem)
    lst["last"]["next"]=nodo
    lst["last"]=nodo
    lst["size"]+=1
    if lst["size"]==1:
        lst["first"]=nodo
    return lst    

def first_element(lst):
    if not lst.head:  
        return None
    
    return lst.head.data 

def is_empty(lst):
    return lst.head is None

def remove_last(lst):
    if not lst.head:  
        return None
    
    if lst.head.next is None:  
        data = lst.head.data
        lst.head = None
        return data
    

    actual= lst.head
    while actual.next.next:
        actual = actual.next
    
    data = actual.next.data  
    actual.next = None  
    return data

        
    
def last_element(lst):
    if not lst.head:  
        return None
    
    ultimo = lst.head
    while ultimo.next:  
        ultimo = ultimo.next
    
    return ultimo.data  

def get_element(lst, pos):
    if not lst.head:  
        return None
    
    añadir = lst.head
    index = 0
    
    while añadir and añadir < pos:
        añadir = añadir.next
        index += 1
    
    if añadir is None:  
        return None
    
    return añadir.data  

def delete_element(lst, pos):
    if not lst.head:  
        return None
    
    if pos == 0: 
        data = lst.head.data
        lst.head = lst.head.next
        return data
    
    actual = lst.head
    index = 0
    
    while actual and index < pos - 1:
        actual = actual.next
        index += 1
    
    if actual is None or actual.next is None:  
        return None
    
    data = actual.next.data  
    actual.next = actual.next.next  
    return data
d