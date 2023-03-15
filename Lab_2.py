################## Zmienne złożone: typ lista ####################
# Tworzenie listy i odwoływanie się do jej elementów
# cars = ['Audi', 'BMW', 'Mercedes']  # to jest zmienna cars, typ lista, do jej utworzenia użyj nawiasów []
# print(cars)
# ###### Odwoływanie się do poszczególnych elementów z listy
# print(cars[0]) # numeracja elementów jest od 0
# print(cars[2])
#################### Metody na listach (operacje na listach) ########
### metody/działania wykonujemy na obiektach np. obiektem może być nasza zmienna
### Zapamiętaj nazwy metod:

# # # list1.append(x) - Dodaje element x do końca listy o nazwie list1,
# # # list1.extend(L) rozszerza listę list1 poprzez dołączenie wszystkich elementów podanej listy L,
# # # list1.insert(i, x) - umieszcza element x na podaną i-pozycję (index) listy list1
# # # list1.remove(x) - usuwa pierwszy napotkany element x z listy list1
# # # list1.pop([i]) - usuwa element x z podanej i-pozycji na liście list1 i zwraca go jako wynik.
# # # list1.index(x) - zwraca indeks pierwszego elementu listy list1, którego wartością jest x.
# # # list1.count(x) - zwraca liczbę wystąpień elementu x na liście list1.
# # # list1.sort() - sortuje elementy na liście list1
# # # list1.reverse() - odwraca porządek elementów listy list1.

######### Przykłady #############################
# cars = ['Audi', 'BMW', 'Mercedes','BMW', 'BMW']
# print(cars)
# cars.append('Porsche') # na obiekcie o nazwie cars wywołana została metoda o nazwie append
# print(cars)

# Tworzenie pustej listy z użyciem konstruktora list i dodawanie elementów
# cars2 = list()    # lub równoważnie  cars2 = []
# print(cars2)
# cars2.append('Rowerek')
# print(cars2)

# cars = ['Audi', 'BMW', 'Mercedes','BMW']
# print(cars)
# cars.insert(2,'Porsche')
# cars2 = cars
# print(cars2)

###  Użycie metody index na obiekcie cars, sprawdzamy index elementu listy
# print(cars)
# ind = cars.index('BMW') # na obiekcie cars stosujemy metodę index
# print(ind)
# print(ind, type(ind))
# print(cars[ind])


### Usuwanie wybranego elementu z listy
# numbers = [1, 2, 3, 10, 18, 10, 13, 10]
# print(numbers)
# numbers.remove(10)
# print(numbers)

################## Zadanie 1
# Utwórz listę z imionami (conajmniej 10 imion, część powinna się powtarzać)
# określ indeks osoby, której imię podaje użytkownik
# ile osób o imieniu wskazanym przez użytkownika znajduje się na liście
# list_imiona = ['Aleksandra','Krzysztof','Beata','Zbigniew','Antoni','Krzysztof','Zbigniew','Maciej','Krzysztof','Aleksandra']
# imie = input('Podaj imię: ')
# id = list_imiona.index(imie)
# print('Pierwsza osoba o imieniu {} ma index: {}' .format(imie, id))
# number_osp = list_imiona.count(imie)
# print('Liczba osób o imieniu', imie, 'wynosi', number_osp)


################# Zmienne złożone: typ krotka 
# cars2 = ('A', 'B')  # krotka = tuple
# print(cars2)
# cars2.append('D')   # uwaga w krotce nie mogę zmieniać wartości, jej elementów
# print(cars2, type(cars2))

################# Zmienne złożone: typ słownik
# słownik = {klucz1:wartość klucza1, klucz2:wartość klucza2, itd}
# slownik1 = {'wojenne': 'Medal od honor, Call of Duty',
#            'romans ': 'Romeo i Julia',
#            'komiksy ': 'Kaczor Donald'}
# print(slownik1)

# cars_countries = {
#       'Germany': ['Audi', 'BMW'],
#       'Asia': {'Japan': ['Toyota', 'Honda']}
# }
# print(cars_countries)
# print(cars_countries['Germany'])
# print(cars_countries['Germany'][1])
# print(cars_countries['Asia']['Japan'][0])
# print(cars_countries['Korea'])  # nasz slownik nie ma takiego klucza

######################Zadanie 2
## Utwórz słownik zawierający  trzy klucze: imie, nazwisko, wiek
## jako wartości w/w kluczy wpisz listy 3-elementowe zawierające dowolne dane osobowe
## następnie wyświetl kompletne dane osoby o numerze wskazanej przez użytkownika

# persdata = {
#   'imie':['Adam','Kasia','Chris'],
#   'nazwisko':['Kosz','But','Rękas'],
#   'wiek':[18, 19, 20]
# }
# id = int(input('Podaj index od 0 do 2: '))
# print(persdata['imie'][id])
# print(persdata['nazwisko'][id])
# print(persdata['wiek'][id])

#################################################################
### 1 sposób: dodawanie nowego klucza do słownika
# cars_countries['Korea'] = 'Kia' 
# print(cars_countries)
# print(cars_countries['Korea'])

### 2 sposób: dodawanie nowego/ch klucza/kluczy do słownika
# cars_countries.update({
#     'France': 'Citroen',
#     'Spain': 'Seat'
#    })
# print(cars_countries)

### Tworzenie pustego słownika i dodawanie elementów
# new_dict = dict()  #  new_dict = {} 
# cars_countries['Korea'] = 'Kia'

### Przykłady tworzenia słownika 3-elementowego
# slownik1 = dict(a=1, b=2, c=3)                   
# slownik2 = dict([('d', 4), ('e', 5), ('f', 6)])  
### można mieszać w/w instrukcje
# slownik3 = dict([('a', 1)], b=2, c=3)            
# slownik4 = dict({'a' : 1, 'b' : 2}, c=3)         

# print(slownik1)
# print(slownik2)
# print(slownik3)
# print(slownik4)

######################Zadanie 3
## Do poprzednio utworzonego słownika dodaj nowy klucz o nazwie "Kierunek" 
## wartość klucza wpisuje użytkownik


# persdata = {
#   'imie':['Adam','Kasia','Chris'],
#   'nazwisko':['Kosz','But','Rękas'],
#   'wiek':[18, 19, 20]
# }
# persdata['kierunek'] = ['inf','kik']
# print(persdata)
# persdata.update({'kierunek2':['fiz','mat']})
# print(persdata)


#################### Metody na listach (operacje na listach) oraz funkcje ########
### Zapamiętaj nazwy metod i funkcji:
# cars_countries = {
#       'Germany': ['Audi', 'BMW'],
#       'Asia': {'Japan': ['Toyota', 'Honda']}
# }
# del cars_countries['Germany'] # usuwanie klucza słownika
# print(cars_countries)
# l = len(cars_countries.keys) # liczy długość, ilość elementów
# print(l)
# print(len(cars_countries)) 


# cars_countries2 = {
#       'Germany': 10000,
#       'Asia': 2000
# }

# ### Metody: dostęp do kluczy i wartości

# key_cars_countries = cars_countries2.keys() # lista kluczy
# values_cars_countries = cars_countries2.values() # lista wartości
# items_cars_countries = cars_countries2.items() # lista par

# print(key_cars_countries)
# print(values_cars_countries)
# print(items_cars_countries)

## Metoda update - dodawanie nowych elementów do słownika
# studenci = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}
# nowi_studenci = {"Romek": 3343, "Basia": 8573}
# studenci.update(nowi_studenci) # "dodaj/scal" słowniki
# print(studenci) # zwróć uwagę na Basię
# studenci.update(Jozek=2276)
# print(studenci)

## Metoda get - dostęp do wartości

# studenci = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}
# print(studenci.get("Kasia")) # Kasia jest w słowniku -> OK
# print(studenci.get("Ania"))  # Ani nie ma -> default = None
# print(studenci.get("Ania", 1234)) # Ani nie ma -> default = 1234

######################Zadanie 4
## Wyświetl nazwy kluczy swojego słownika, oraz ilość elementów

# persdata = {
#   'imie':['Adam','Kasia','Chris'],
#   'nazwisko':['Kosz','But','Rękas'],
#   'wiek':[18, 19, 20]
# }
# print(persdata.keys())
# l = len(persdata.keys()) # liczy długość, ilość elementów
# print(len(persdata))
######################Zadanie 5
## Zamień wszystkie nazwy imion w kluczu imie w swoim słowniku na inne.

# persdata = {
#   'imie':['Adam','Kasia','Chris'],
#   'nazwisko':['Kosz','But','Rękas'],
#   'wiek':[18, 19, 20]
# }

