class List:
    pass

class Item:
    pass

def make_list():
    """ Funkcja tworząda listę dynamiczną

        Args:

        Returns:
            Lista : pusta lista 
    """
    lista = List()
    lista.start = None
    lista.end = None
    return lista

def listend(lista, variable):
    """ Funkcja dodająca wartość na koniec listy

        Args:
            lista : do której listy
            variable : wartość zmiennej do dodania
        Returns:
    """
    item = Item()
    item.value = variable
    item.next = None
    if lista.start is None:
        lista.start = item
    else:
        lista.end.next = item
    lista.end = item

def show_list(lista):
    """ Funkcja wypisująca wszystkie elementy listy

        Args:

        Returns:
    """
    item = lista.start
    while item is not None:
        print(item.value, end = " ")
        item = item.next

def show_list_index(lista, index):
    """ Funkcja zwracająca wartość danego elementu listy o wskazanym indeksie

        Args:
            lista : w której liście jest ten element
            index : indeks tego elementu
        Returns:
            item.value : wartość szukanenego elementu listy
    """
    assert lista is not None and index>=0, "Error of index"
    item = lista.start
    i = 0
    while i <= index:
        if i == index:
            return item.value
        i+=1
        item = item.next

def length_of_list(lista):
    """ Funkcja zwracająca długość wskazanej listy

        Args:
            lista: wskazana lista
        Returns:
            i : długość tej listy
    """
    if lista.start is None:
        return 0
    else:
        item = lista.start
        i = 0 
        while item is not None:
            i+=1
            item = item.next
        return i

def find_in_list(lista, value):
    """ Funkcja zwracająca indeks szukanej wartości we wskazanej liście
    
        Args:
            lista: wskazana lista
            value: szukana wartość
        Returns:
            i: indeks szukanej wartości
    """
    if lista.start is None:
        return None
    else:
        item = lista.start
        i = 0
        while i <= (length_of_list(lista)-1):
            if show_list_index(lista, i) == value:
                return i
            i+=1
            item = item.next
        return None

