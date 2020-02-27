import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time

#Récupérer l’url des 25 meilleures performances en triple saut de l’année 2019
#http://trackfield.brinkster.net/25BestPerf.asp?EventCode=MF4&P=F

#Récupérer les informations que vous jugez utiles sous forme de DataFrame
####################
# x = requests.get('http://trackfield.brinkster.net/25BestPerf.asp?EventCode=MF4&P=F')

# soup = BeautifulSoup(x.content,'html.parser')


# ls=[]


# for p in soup.find_all('td', attrs={"bgcolor":"#F3F2EE"}):
    
#     ls.append(p.text)    


# ls = np.reshape(ls, (int(len(ls)/9), 9))


# df = pd.DataFrame(data=ls,columns=['rang','Perf','Null','?','N','Nom','Nationalité','Ville','Date'])

##########################""""
# x = requests.get('http://trackfield.brinkster.net/More.asp?Year=2019&EventCode=MF4&Gender=M')

# soup = BeautifulSoup(x.content,'html.parser')


# ls=[]


# for p in soup.find_all('td', attrs={"bgcolor":"#F3F2EE"}):
    
#     ls.append(p.text)    

# ls = ls[1:]
# ls = np.reshape(ls, (int(len(ls)/8), 8))



# df = pd.DataFrame(data=ls,columns=['rang','Noms','Pays','Performances','Null','Nb','Ville','Date'])



#Ecrire un programme qui permet d’extraire les 25 meilleures performances de l’année 1891 à 2019 en
#triple saut homme et femme dans un fichier Excel.



annee=1891
sexe = 'M'
url = []
years=[]
genre=[]

while annee<=2019 :
    
    b = 'http://trackfield.brinkster.net/More.asp?Year={}&EventCode={}F4'.format(annee, sexe)
    url.append(b)
    years.append(annee)
    genre.append(sexe)
    annee=annee+1
annee=1891
sexe = 'W'
while annee<=2019 :
    
    b = 'http://trackfield.brinkster.net/More.asp?Year={}&EventCode={}F4'.format(annee, sexe)
    url.append(b)
    years.append(annee)
    genre.append(sexe)
    annee=annee+1


test = True
tb=[]



        
for i,b,s in zip(years,url,genre) :
    
    # b = 'http://trackfield.brinkster.net/More.asp?Year={}&EventCode={}F4'.format(i, sexe)
    
    test = True
    print(b)
    while test :
        try:
            print('try')
            x = requests.get(b)
            print('requet ok')
            test = False

        except :
            print('except')
            time.sleep(2)
            test = True
            
            
    print('debut traitement')
    ls=[]
    
    soup = BeautifulSoup(x.content,'html.parser')

        
    
    for p in soup.find_all('td', attrs={"bgcolor":"#F3F2EE"}):
        if p.text !=   'Indoor Results'  :
            ls.append(p.text)          
        

    ls = ls[1:]   
    temp=[]
        
    ls = np.reshape(ls, (int(len(ls)/8), 8))
    print(len(ls))
    
    for lign in range(len(ls)) :        
        an=(i,s)
        temp=np.append(ls[lign,:],an)          
        tb.append(temp)




df = pd.DataFrame(data=tb,columns=['rang','Noms','Pays','Performances','Null','Nb','Ville','Date','Annee','Sexe'])

    

writer = pd.ExcelWriter(r'C:\Users\utilisateur\Documents\Python\Scraping\Briefs_projet.xlsx')
df.to_excel(writer,'Sheet1')

writer.save()