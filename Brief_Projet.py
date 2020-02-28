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


#Création d'une liste des URL (hommes+femmes), d'une liste de genre(M ou W) et d'une liste des années
######################################################################################################
annee=1891
sexe = 'M'
url = []
years=[]
genre=[]

while annee<=2019 :
    
    u = 'http://trackfield.brinkster.net/More.asp?Year={}&EventCode={}F4'.format(annee, sexe)
    url.append(u)
    years.append(annee)
    genre.append(sexe)
    annee=annee+1
annee=1891
sexe = 'W'
while annee<=2019 :
    
    u = 'http://trackfield.brinkster.net/More.asp?Year={}&EventCode={}F4'.format(annee, sexe)
    url.append(u)
    years.append(annee)
    genre.append(sexe)
    annee=annee+1

######################################################################################################
test = True
tab_final=[]
#Récupération des données (Boucle sur les trois liste)        
for ann,u,s in zip(years,url,genre) :
    
    #Try / except en cas de saturation du serveur######################################################
    test = True
    print(u)
    while test :
        try:
            print('try')
            x = requests.get(u)
            print('requet ok')
            test = False

        except :
            print('except')
            time.sleep(2)
            test = True
            
    ##########################################################################################        
    print('debut traitement')
    lst=[]
    
    soup = BeautifulSoup(x.content,'html.parser')

        
    
    for p in soup.find_all('td', attrs={"bgcolor":"#F3F2EE"}):
        #on enregistre pas les lignes == indoor
        if p.text !=   'Indoor Results'  :
            lst.append(p.text)          
        
    #Suppression de la 1ere ligne (le titre)
    lst = lst[1:]   
    
    lst_temp=[]
    #Redimension de la liste en colonnes    
    lst = np.reshape(lst, (int(len(lst)/8), 8))
    print(len(lst))
    
    #Ajout ds une liste temp puis ds tab final des données + l'année et le sexe
    for lign in range(len(lst)) :        
        an=(ann,s)
        lst_temp=np.append(lst[lign,:],an)          
        tab_final.append(lst_temp)


#création du data frame avec les différentes colonnes########################################################################

df = pd.DataFrame(data=tab_final,columns=['rang','Noms','Pays','Performances','Null','Nb','Ville','Date','Annee','Sexe'])

    
#Conversion data frame en xls#################################################################################################
# writer = pd.ExcelWriter(r'C:\Users\utilisateur\Documents\Python\Scraping\Briefs_projet.xlsx')
# df.to_excel(writer,'Sheet1')

# writer.save()
#Conversion data frame en csv#################################################################################################
df.to_csv(r'C:\Users\utilisateur\Documents\Python\Scraping\Briefs_projet.csv')