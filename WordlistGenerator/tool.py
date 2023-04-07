from bs4 import BeautifulSoup
import requests as rs

print(">>>>> GENERATE WORDLIST FROM WEBPAGE <<<<<","\n")
print("Enter webpage URL:")
url=input(">>>")

data = rs.get(url).text
soup=BeautifulSoup(data,"html.parser")
filtered_data = soup.find('body').text

filtered_data = filtered_data.replace("/"," ")
filtered_data = filtered_data.replace("'"," ")
filtered_data = filtered_data.replace(":"," ")

unwanted_characters = ["1","2","3","4","5","6","7","8","9","0","",",","(",")","/","-","_","`","~",".",";",":","<",">","?","{","}","[","]","|","\\","^","\n","\t",",","&"]
h_verbs = ["am","is","are","was","were","be","been","being","do","does","did","have","has","had","may","can","must","might","shall","will","should","would","could"]
pronouns = ["I","me", "She","her","He","him","They","them","We","us","You","this","that","what","which","who","whom","Myself","Yourself","Himself","Herself","Itself","Oneself","Ourselves","Yourselves","Themselves","Myself","Yourself","Himself","Herself","Itself","Oneself","Ourselves","Yourselves","Themselves","My","Your","Our","Their","His","Her","Its","Mine","Yours","Ours","His","Hers","Theirs","Its","Either","Each","Neither","Any","None","Who","what","which","whose","how"]
preposition = ["On","At","In","Over","Around","Through","Opposite","to","In","front","of","Behind","Beneath","Beside","Above","Below","Under","Underneath","Down","Up","Out With","Into","Onto","Across","After","Before","Near","Among","Along","Between","Toward","Away","From","To","Next","to","By","Until","About"]
other = ["a","an","the","and","for","since","all","with","if","or","no"]
for i in h_verbs + unwanted_characters + pronouns + preposition + other:
    filtered_data.replace(i," ")


#fetching title for file name ============================================================
title = soup.find('title').text
title = title.replace(" ","")

#generating wordlist =====================================================================
wordlist=filtered_data.split()

#removing bad elements from wordlist =====================================================
unwanted_characters = ["1","2","3","4","5","6","7","8","9","0","",",","(",")","/","-","_","`","~",".",";",":","<",">","?","{","}","[","]","|","\\","^","\n","\t",",","&"]
h_verbs = ["am","is","are","was","were","be","been","being","do","does","did","have","has","had","may","can","must","might","shall","will","should","would","could"]
pronouns = ["I","me", "She","her","He","him","They","them","We","us","You","this","that","what","which","who","whom","Myself","Yourself","Himself","Herself","Itself","Oneself","Ourselves","Yourselves","Themselves","Myself","Yourself","Himself","Herself","Itself","Oneself","Ourselves","Yourselves","Themselves","My","Your","Our","Their","His","Her","Its","Mine","Yours","Ours","His","Hers","Theirs","Its","Either","Each","Neither","Any","None","Who","what","which","whose","how"]
preposition = ["On","At","In","Over","Around","Through","Opposite","to","In","front","of","Behind","Beneath","Beside","Above","Below","Under","Underneath","Down","Up","Out With","Into","Onto","Across","After","Before","Near","Among","Along","Between","Toward","Away","From","To","Next","to","By","Until","About"]
other = ["a","an","the","and","for","since","all","with","if","or","no"]

new_wordlist = []
for i in wordlist:
    temp = i.strip("\n\t ")
    temp = temp.replace(",","")
    temp = temp.replace("\n","")
    temp = temp.replace("\t","")
    new_wordlist.append(temp)

for i in h_verbs+unwanted_characters+pronouns+preposition+other:
    for lower_case in range(new_wordlist.count(i.lower())):
        new_wordlist.remove(i.lower())
    for upper_case in range(new_wordlist.count(i.upper())):
        new_wordlist.remove(i.upper())
    for capitalize in range(new_wordlist.count(i.capitalize())):
        new_wordlist.remove(i.capitalize())

for i in unwanted_characters:
    for j in new_wordlist:
        new_wordlist[new_wordlist.index(j)] = j.strip(i+" ")



#removing duplicate values ---------------------------------------------------------------
for i in new_wordlist:
    if new_wordlist.count(i)>1:
        for j in range(new_wordlist.count(i)-1):
            new_wordlist.remove(i)
for i in new_wordlist:
    if new_wordlist.count(i)>1:
        for j in range(new_wordlist.count(i)-1):
            new_wordlist.remove(i)



#final part writing data on txt file =======================================================
title = title[:20]
with open(title+".txt", 'w', encoding="utf-8") as f:
    for tag in new_wordlist:
        text = tag.strip()
        f.write(f'{text}\n')

f.close()
print("........... File is created with title name of the page ...........")
print("......................... Task Completed ..........................")
