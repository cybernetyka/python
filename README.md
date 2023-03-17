# python
python examples of bioton, cobit, process




## CoBIT


### Podstawowe:

  + organizm
  + waga podziału - pochodna energii i czasu, skutek
  + energia
  + datownik
  

## Cecha, własciwość
  + typ
  + relacja
  + proporcja


### zdarzenie 

  + Datownik
  + Akcja
  + Wiązanie

  
### Akcja

  //+ waga => Intencja = informacja wyjściowa - jaki chcielibyśmy widzieć układ, jaką zmianę chcielibyśmy zainicjować   
  //+ Waga - sposób podziału energii pomiędzy 1 i 2 np. 1/2 2/3 3/4 dotyczy pierwszego elementu  
  //+ Informacja/intencja: 
  //+ Energia = energia wyjściowa, siła intencji
  //+ Czas trwania
  Biton
  Waga(3/4)


### InterAkcja, Transakcja, Wiązanie
  
    aplikacja( Akcja( Biton, Waga(3/4) ) ){
      
      Biton1->setWaga(3/4)
      Biton1->setInfo(Biton)
      
      Biton1->setWaga(1/4)
      Biton1->setInfo(Biton)
    }
    
  + Akcja - otrzymana energia i informacja dla każdego elementu  
  + Biton 1, waga 2/3
  + Biton 2, waga 1/3
  
  

### Biton - Materia (proporcje informacji i energii)
  
  cechy[]
    
    typ:  wygląd
    relacja: czarny/biały
    proporcja: 1/2
    
    typ: energia:
    relacja: akumulacja/konsumpcja
    proporcja: 1/2
  
  


### CoBIT - świadomy organizm, składa się z materii z Bitonów
  
  //getWaga()
  //getAkumulacja()
  //getKonsumpcja()
  
  + transakcje, zdarzenia wiązań: 
    InterAkcja(Akcja, Waga, Biter1, Biter2)
  
  
  
  
  
CoBIT

  Wartości pobranej energii i zdobytej informacji
  
  getCecha()->filtrowanie(energia)
  sprawdzanie proporcji dla już sitniejących
  jesli nie istnieje, to przyjmuje się 1 o ile nie zadecyduje waga
  

  Interakcja

    aplikacjaEnergii(
      Biton, // Akcja(czarny, 10J, 10s)
      Waga(3/4), - intencja podziału energii
      Biton1
      Biton2
    )
    
    

Intencja -  to możliwość poukładania w odpowiednim porzadku nadchodzacych Bitonów do Cobitu, zmieniając jego wrażliwosć na kolejne wiadomosci (Bitony)
Jako pętla spreparowanych Bitonów dla Cobitu

### EXAMPLE

```python



```


### CORE

```python

```        
  

