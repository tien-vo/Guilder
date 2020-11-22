#introduction
print("Welcome to Guider")
print("Before starting, please answer these simple questions.")

#creating the questionaires
question1 = input("These are some of the biggest events of recent years, which one concerns you the most?\
\n\tA. Australian bushfires\
\n\tB. Covid-19 pandemic\
\n\tC. Black Lives Matter protests\
\n\tD. #metoo movement\
\n\tE. Legalization of same-sex marriage\
\n\tYour Answer: ")
print("")

while question1 != "a" and question1 !="A" and \
      question1 != "b" and question1 != "B" and \
      question1 != "c" and question1 !="C" and \
      question1 != "d" and question1 != "D" and \
      question1 != "e" and question1 != "E":
    question1 = input("Please enter the corresponding letter: ") 

print("")

question2 = input("Out of all these individuals, who do you share the same value with?\
\n\tA. Greta Thunberg\
\n\tB. Anthony Fauci\
\n\tc. John Lewis\
\n\tD. Angela Davis\
\n\tE. Marsha P. Johnson\
\n\tYour Answer: ")
print("")

while question2 != "a" and question2 !="A" and \
      question2 != "b" and question2 != "B" and \
      question2 != "c" and question2 !="C" and \
      question2 != "d" and question2 != "D" and \
      question2 != "e" and question2 != "E":
    question2 = input("Please enter the corresponding letter: ")
                      
print("")
                      
question3 = input("If you only have the fund to donate for one of these organizations,\
which on will that be?\
\n\tA. Friends of the Earth\
\n\tB. St. Jude’s Children’s Research Hospital\
\n\tC. Color of Change\
\n\tD. Planned Parenthood\
\n\tE. Pride Foundation\
\n\tYour Answers: ")
print("")

while question3 != "a" and question3 !="A" and \
      question3 != "b" and question3 != "B" and \
      question3 != "c" and question3 !="C" and \
      question3 != "d" and question3 != "D" and \
      question3 != "e" and question3 != "E":
    question3 = input("Please enter the corresponding letter: ") 

print("")

question4 = input("Which of these movies do you prefer?\
\n\tA. Princess Momonoke\
\n\tB. Outbreak\
\n\tC. Black Panther\
\n\tD. Wonder Woman\
\n\tE. Love, Simon\
\n\tYour Answer: ")
                      
print("")

while question4 != "a" and question4 !="A" and \
      question4 != "b" and question4 != "B" and \
      question4 != "c" and question4 !="C" and \
      question4 != "d" and question4 != "D" and \
      question4 != "e" and question4 != "E":
    question1 = input("Please enter the corresponding letter: ")                       

print("")

print("The questions help us to navigate for you which organizations\
are the best fit for your value and belief.")
print("")

#create a chain to evaluate
result = question1 + question2 + question3 + question4
num_a = 0
num_b = 0
num_c = 0
num_d = 0
num_e = 0

for s in range (0,len(result)):
    if result[s] == "A" or result[s] == "a":
        num_a+=1

for s in range (0,len(result)):
    if result[s] == "B" or result[s] == "b":
        num_b+=1

for s in range (0,len(result)):
    if result[s] == "C" or result[s] == "c":
        num_c+=1

for s in range (0,len(result)):
    if result[s] == "D" or result[s] == "d":
        num_d+=1

for s in range (0,len(result)):
    if result[s] == "E" or result[s] == "e":
        num_e+=1

#define the web resources
import requests
from bs4 import BeautifulSoup

def americanforests():
        URL = 'https://www.americanforests.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("Their mission is to stop deforestation and conserve the forests we already have")
        print(URL)
        print("")

def edf():
        URL = 'https://www.edf.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("")
        print("The organization aims to raise awareness about the issues of climate change by planning trees")
        print("")
        print(URL)

def greenpeace():
        URL = 'https://www.greenpeace.org/usa/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("")
        print("The organization works to defend the environment and mother nature\
peacefully by investigating, exposing, and confronting environmental abuse, and advocating\
for the rights and we;;-being of all")
        print("")
        print(URL)

def directrelief():
        URL = 'https://www.directrelief.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("Their mission is to improve the health and lives of people\
affected by poverty or other hardships by providing essential medical resources.")
        print(URL)
        print("")

def operationsmile():
        URL = 'https://www.operationsmile.org/?_ga=2.83500624.755316894.1606001233-969147131.1606001233&_gac=1.86395626.1606001233.Cj0KCQiAkuP9BRCkARIsAKGLE8WCZt4T9AucVvGCC_ARIYSHuJBu4z8zF_IOcFqRQkY-L7O2OMjdLycaAvfNEALw_wcB'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("")
        print("The organization works to reduce the occurence of cleft lips and aletes wordwide\
by provifing repair surgeries to children with the condition.")
        print("")
        print(URL)

def dwb():
        URL = 'https://www.doctorswithoutborders.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("")
        print("The organization's mission is to provide medical care\
to conflict zones and to countries affected by endemic diseases.")
        print("")
        print(URL)

def naacp():
        URL = 'https://naacp.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("NAACP - National Association for the Advancement of Colored People -\
strives to secure the political, educational, social, and economic rights of Black people.")
        print(URL)
        print("")

def aclu():
        URL = 'https://www.aclu.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("")
        print("ACLU - The American Civil Lberties Union - defends and reserve\
the rights and the life of Black people")
        print("")
        print(URL)

def kind():
        URL = 'https://supportkind.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("")
        print("KIND - Kids in Need of Defense - works to protect refugee and immigrant children.")
        print("")
        print(URL)

def wge():
        URL = 'https://wgefund.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("The organization's mission is to support women through economic \
social and political programs, creating opportunities while addressing inequality.")
        print(URL)
        print("")

def shecode():
        URL = 'https://girlswhocode.com/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("")
        print("The organization's mission is to create opportunities\
for more womne in technology.")
        print("")
        print(URL)

def sherun():
        URL = 'https://www.sheshouldrun.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("")
        print("The organization works for more women representation \
in politic.")
        print("")
        print(URL)

def glad():
        URL = 'http://www.glad.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("The organization's mission is to end discrimination based on \
sexual orientation, HIV status, and gender identity and expression.")
        print(URL)
        print("")

def hrc():
        URL = 'https://www.hrc.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("")
        print("The Human Rights Campaign is an advocay group and political \
lobbying organization for the LGBTQ+ community.")
        print("")
        print(URL)

def tgl():
        URL = 'https://marshap.org/'
        page = requests.get(URL)
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        page_title = soup.title.text
        print(page_title)
        print("")
        print("The organization advocates for the rights of the black transgender people.")
        print("")
        print(URL)

#assign the case to approriate possibility
import random

k = 0
l = 0
m = 0

def rand():
    if k == 1 or l == 1 or m == 1:
        americanforests()
    elif k ==2 or l == 2 or m == 2:
        greenpeace()
    elif k == 3 or l == 3 or m == 3:
        edf()
    elif k ==4 or l == 4 or m == 4:
        directrelief()
    elif k == 5 or l == 5 or m == 5:
        operationsmile()
    elif k == 6 or l == 6 or m == 6:
        dwb()
    elif k == 7 or l == 7 or m == 7:
        naacp()
    elif k == 8 or l == 8 or m == 8:
        aclu()
    elif k == 9 or l == 9 or m == 9:
        eji()
    elif k == 10 or l == 10 or m == 10:
        wge()
    elif k == 11 or l == 11 or m == 11:
        shecode()
    elif k == 12 or l == 12 or m == 12:
        sherun()
    elif k == 13 or l == 13 or m == 13:
        glad()
    elif k == 14 or l == 14 or m ==14:
        hrc()
    else:
        tgl()

#case 1: when the majority is a
if num_a > 2 or (num_a == 2 and (num_b == 1 or num_c == 1 or num_d == 1 or num_e == 1)):
    print ("These are the environmental organizations that you might like.")
    print("")
    americanforests()

    i = 0
    count = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                edf()
                
            if i == 1:
                greenpeace()
                
            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1
    

#case 2: when the majority is b
elif num_b > 2 or (num_b == 2 and (num_a == 1 or num_c == 1 or num_d == 1 or num_e == 1)):
    print ("These are the healthcare and medical services organizations that you might like.")
    print("")
    directrelief()

    i = 0
    count = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                operationsmile()
                    
            if i == 1:
                dwb()
                    
            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

#when the majority is c
elif num_c > 2 or (num_c == 2 and (num_b == 1 or num_a == 1 or num_d == 1 or num_e == 1)):
    print ("These are the racial justice organizations that you might like.")
    print("")
    naacp()
 
    i = 0
    count = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                aclu()
                
            if i == 1:
                eji()
                
            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

#when the majority is d
elif num_d > 2 or (num_d == 2 and (num_b == 1 or num_c == 1 or num_a == 1 or num_e == 1)):
    print ("These are the feminist organizations that you might like.")
    print("")
    wge()    
        
    i = 0
    count = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                shecode()
                
            if i == 1:
                sherun()
                
            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

#when the majority is E
elif num_e > 2 or (num_e == 2 and (num_b == 1 or num_c == 1 or num_d == 1 or num_a == 1)):
    print ("These are the LGBTQIA+ organizations that you might like.")
    print("")
    glad()
    
    i = 0
    count = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                hrc()
                
            if i == 1:
                tgl()
                
            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

#when the majority are both a and b
elif (num_a == 2 and num__b == 2):
    print ("You might interest in these organizations." )
    k = random.randint(1,6)
    rand()

    n = k  
    i = 0
    count = 0
    k = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                l = random.randint(1,6)
                while l == n:
                    l = random.randint(1,6)
                rand()
                    
            p = l
            l = 0
                
            if i == 1:
                m = random.randint(1,6)
                while m == n or m == p:
                    m = random.randint(1,6)
                rand()

            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

#when the majority are both b and c            
elif (num_b == 2 and num_c == 2):
    print ("You might interest in these organizations." )
    k = random.randint(4,9)
    rand()

    n = k  
    i = 0
    count = 0
    k = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                l = random.randint(4,9)
                while l == n:
                    l = random.randint(4,9)
                rand()
                    
            p = l
            l = 0
                
            if i == 1:
                m = random.randint(4,9)
                while m == n or m == p:
                    m = random.randint(4,9)
                rand()

            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

#when the majority are both c and d            
elif (num_c == 2 and num_d == 2):
    print ("You might interest in these organizations." )
    k = random.randint(7,12)
    rand()

    n = k  
    i = 0
    count = 0
    k = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                l = random.randint(7,12)
                while l == n:
                    l = random.randint(7,12)
                rand()
                    
            p = l
            l = 0
                
            if i == 1:
                m = random.randint(7,12)
                while m == n or m == p:
                    m = random.randint(7,12)
                rand()

            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1
            
        
#when the majority are both d and e            
elif (num_d == 2 and num_d == 2):
    print ("You might interest in these organizations." )
    k = random.randint(10,15)
    rand()

    n = k  
    i = 0
    count = 0
    k = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                l = random.randint(10,15)
                while l == n:
                    l = random.randint(10,15)
                rand()
                    
            p = l
            l = 0
                
            if i == 1:
                m = random.randint(10,15)
                while m == n or m == p:
                    m = random.randint(10,15)
                rand()

            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

#when the majority are both a and c            
elif (num_c == 2 and num_a == 2):
    print ("You might interest in these organizations." )
    k = random.randint (1,9)
    while 3 < k < 7:
        k = random.randint(1,9)
    rand()

    n = k  
    i = 0
    count = 0
    k = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                l = random.randint(1,9)
                while l == n or 3 < l < 7:
                    l = random.randint(1,9)
                rand()
                    
            p = l
            l = 0
                
            if i == 1:
                m = random.randint(1,9)
                while m == n or m == p or 3 < m < 7:
                    m = random.randint(1,9)
                rand()

            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

#when the majority are both a and d            
elif (num_d == 2 and num_a == 2):
    print ("You might interest in these organizations." )
    k = random.randint (1,12)
    while 3 < k < 10:
        k = random.randint(1,12)
    rand()

    n = k  
    i = 0
    count = 0
    k = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                l = random.randint(1,12)
                while l == n or 3 < l < 10:
                    l = random.randint(1,12)
                rand()
                    
            p = l
            l = 0
                
            if i == 1:
                m = random.randint(1,12)
                while m == n or m == p or 3 < m < 10:
                    m = random.randint(1,12)
                rand()

            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

#when the majority are both a and e            
elif (num_e == 2 and num_a == 2):
    print ("You might interest in these organizations." )
    k = random.randint (1,15)
    while 3 < k < 13:
        k = random.randint(1,15)
    rand()

    n = k  
    i = 0
    count = 0
    k = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                l = random.randint(1,15)
                while l == n or 3 < l < 13:
                    l = random.randint(1,15)
                rand()
                    
            p = l
            l = 0
                
            if i == 1:
                m = random.randint(1,15)
                while m == n or m == p or 3 < m < 13:
                    m = random.randint(1,15)
                rand()

            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

#when the majority are both b and d:            
elif (num_b == 2 and num_d == 2):
    print ("You might interest in these organizations." )
    k = random.randint (4,12)
    while 6 < k < 10:
        k = random.randint(4,12)
    rand()

    n = k  
    i = 0
    count = 0
    k = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                l = random.randint(4,12)
                while l == n or 6 < l < 10:
                    l = random.randint(4,12)
                rand()
                    
            p = l
            l = 0
                
            if i == 1:
                m = random.randint(4,12)
                while m == n or m == p or 6 < m < 10:
                    m = random.randint(4,12)
                rand()

            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

#when the majority are both b and e            
elif (num_e == 2 and num_b == 2):
    print ("You might interest in these organizations." )
    k = random.randint (4,15)
    while 6 < k < 13:
        k = random.randint(4,15)
    rand()

    n = k  
    i = 0
    count = 0
    k = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                l = random.randint(4,15)
                while l == n or 6 < l < 13:
                    l = random.randint(4,15)
                rand()
                    
            p = l
            l = 0
                
            if i == 1:
                m = random.randint(4,15)
                while m == n or m == p or 6 < m < 13:
                    m = random.randint(1,15)
                rand()

#when the majority are both c and e            
elif (num_e == 2 and num_c == 2):
    print ("You might interest in these organizations." )
    k = random.randint (7,15)
    while 3 < k < 13:
        k = random.randint(1,15)
    rand()

    n = k  
    i = 0
    count = 0
    k = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                l = random.randint(7,15)
                while l == n or 3 < l < 13:
                    l = random.randint(7,15)
                rand()
                    
            p = l
            l = 0
                
            if i == 1:
                m = random.randint(7,15)
                while m == n or m == p or 3 < m < 13:
                    m = random.randint(7,15)
                rand()

            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

else:
    print ("You might interest in these organizations." )
    k = random.randint (1,15)
    rand()

    n = k  
    i = 0
    count = 0
    k = 0
    while i < 3:
        more = str(input("Do you want to look for more? "))
        print("")
        if (more == "yes" or more == "Yes" or more == "YES"):
            i+=count
            if i == 0:
                l = random.randint(1,15)
                while l == n:
                    l = random.randint(1,15)
                rand()
                    
            p = l
            l = 0
                
            if i == 1:
                m = random.randint(1,15)
                while m == n or m == p:
                    m = random.randint(1,15)
                rand()

            if i > 1:
                print("We will update you with more organizations in the future. No matter how big or small, your action today\
will make the world tomorrow a better place.")
            i+=1
                
        elif (more == "no" or more == "No" or more == "NO"):
            print("We glad to assist you")
            break
        else:
            print("Please enter Yes or No")
            i-=1
            count += 1

        
        

        
     

            
            



        


                
                  
                  
                

                 


