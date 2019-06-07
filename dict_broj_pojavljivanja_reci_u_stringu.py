zadati_string=input("Unesi neki string: ")
print(zadati_string)

string_lista=zadati_string.split(" ") #od stringa, niza reci, napravi listu
print(string_lista)                   #reci izmedju kojih je stajao razmak

dict={}                               #pravimo prazan dict
for rec in string_lista:              #for petljom prolazimo kroz sve elemente liste
    if rec in dict.keys():            #svaki element liste, odnosno rec ispitamo da li se
        dict[rec]+=1                  #nalazi u dict, ako se nalazi vrednost pojavljivanja 
    else:                             #povecamo za jedan
        dict[rec]=1                   #ako ne ubacujemo novi kljuc(rec) u recnik i dajemo vrednost u 1
print (dict)                          #prikazuje dict
print (dict.keys())                   #prikazuje kljuceve u dict, odnosno sve reci koje postoje u stringu