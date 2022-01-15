# Program pisany metodą prób i błędów, rozpocząłem od prostego znajdowania słowa w tekście.
# Za tekst bazowy posługują pliki, które użytkownik może wybrać po wpisaniu lokalizacji folderu.
# Podczas wybierania lokalizacji pliki są poddawane weryfikacji 
# Program sprawdza zarówno czy Folder, jak i plik o podanej ścieżce istnieją i czy aby na pewno nie są puste.
# Następnie rozbudowałem go o możliwość wprowadzania jednego, a następnie 3 słów do sprawdzenia.
# Użytkownik przy pierwszym wpisywaniu nie może zostawić pustego pola, natomiast przy następnych już tak.
# Słowa są wyszukiwane, określana jest ich pozycja na podstawie numeru linii, w której występują, a także
# są zliczane ich wystąpienia.
# Otrzymane wyniki są następnie wypisane w konsoli.
# Niestety nie wiem dlaczego, ale w przypadku naprawdę dużych dokumentów, program się wykrusza.


import os

def FindAny(SearchIn, SearchFor):
    with open(SearchIn, 'r') as f:  # w trybie odczytu
        for line in f:              # Sprawdź każdą linię kodu po kolei
            if SearchFor in line:   # Dla każdej linii sprawdź czy plik zawiera string
                return True
    return False

def FindOne(SearchIn, SearchFor): # Znajduje pojedynczy string + numer linii, w których występuje
    index = 0
    results = []
    with open(SearchIn, 'r') as f:
        for line in f:
            index += 1 #licznik
            if SearchFor in line:
                #  który w przypadku wystąpienia słowa-klucza, dopisuje krotkę do listy
                results.append((index, line.rstrip()))
    # Zwraca listę krotek ze słowem oraz linią wystąpienia
    return results

def FindMany(SearchIn, list_of_strings): #zmodyfikowana funkcja do wyszukiwania wielu stringów
    index = 0
    results = []
    with open(SearchIn, 'r') as f:
        for line in f:
            index += 1
            for SearchFor in list_of_strings:
                if SearchFor in line:
                    results.append((SearchFor, index, line.rstrip()))
    return results

def main():
    while True:
        try:
            DirPath=input("\nWprowadź ścieżkę folderu z plikami: ")
            dir_list = os.listdir(DirPath) # Lista wszystkich plików i folderów
        except:
            print("\nBłędna ścieżka, wprowadź ponownie: ")
            continue
        else:
            #podano dobrą ścieżkę, opuszczanie pętli
            break

    print("\nPliki i foldery w: '", DirPath, "' :")
  
    print(dir_list) # Wyświetl wszystkie pliki
    
    while True:
        try:
            file=input("\nWprowadź nazwę pliku, który chcesz przeszukać: ")
            SearchIn=DirPath+file
            fn=open("{}".format(SearchIn), "r") #spróbuj otworzyć plik o zadanej ścieżce
            
        except (FileNotFoundError, IOError):
            print("\nPlik o wskazanej nazwie nie istnieje w podanym folderze, spróbuj ponownie")
            continue
        else:
            if os.stat(SearchIn).st_size > 0:   # sprawdź czy plik nie jest pusty
                print('\nPlik nie jest pusty')
                break
            else:            
                print('\nPlik jest pusty! Spróbuj ponownie')
        
    
    print("\nBędziesz szukał w pliku o ścieżce:", SearchIn)
    
    while True:
        SearchFor=input("\nCo chciałbyś wyszukać?: ")
        if len(SearchFor)>0:
            break
        else:
            print("\nPierwsze wprowadzone słowo do wyszukania nie może pozostać puste. Spróbuj jeszcze raz: ")
    
    SearchFor2=input("\nCzy coś jeszcze?: ")
    if SearchFor2 == "":
        SearchFor2+="XYZXYZXYZXYZXYZXYZ"
    SearchFor3=input("\nA może coś jeszcze?: ")
    if SearchFor3 == "":
        SearchFor3+="XYZXYZXYZXYZXYZXYZ"
    #Jedyny sposób jaki znalazłem na rozwiązanie problemu, 
    # w którym użytkownik nie chce wprowadzać żadnej wartości, a ta nie może pozostać pusta

    print("****************************************************************************************************************************************************")
    print('\nSprawdzam, czy string znajduje się w tekście...')
    if FindAny(SearchIn, SearchFor):
        print('\nTak, "{}" został znaleziony w tekście'.format(SearchFor))
    else:
        print('\nNie, "{}" nie został znaleziony w tekście'.format(SearchFor)) 
    #Nie wiem dlaczego, ale nie działa w przypadku dużych plików, np. Chłopi.txt 
    
    print("****************************************************************************************************************************************************")

    print('\nPojedynczy string i jego występowanie: ')
    MatchLine = FindOne(SearchIn, SearchFor)
    
    print('\nLiczba wystąpień: ', len(MatchLine))
    for part in MatchLine:
        print('\nNumer Linii = ', part[0], ' :: Linia = ', part[1])
    
    print("****************************************************************************************************************************************************")

    print('\nZnajdź wiele stringów (w tym przypadku 3)')
    # search for given strings in the file 'SearchIn'
    MatchLine = FindMany(SearchIn, [SearchFor, SearchFor2, SearchFor3])
    print('\nWszystkie znalezione dopsaowania : ', len(MatchLine))
    for part in MatchLine:
        print('\nSłowo = ', part[0], ' :: Numer linii = ', part[1], ' :: Linia = ', part[2] )
main()

k=input("Press anything to exit")