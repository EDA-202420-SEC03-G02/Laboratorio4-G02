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

def is_present(lst,elem, cmp_function):

    size=lst["size"]
    if size>0:
        existe

   
   
    return lst 
def insert_element(lst, elem, pos) 
def change_info(lst, pos, new_info):
          
                
def exchange(lst, pos1, pos2):   
  
  
def sub_list(lst,pos,numelem):
