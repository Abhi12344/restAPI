from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

import pyttsx3
#import wolframalpha
import wikipedia
import webbrowser
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from tensorflow.python.framework import ops
import numpy
import tflearn
import tensorflow
import random
import pickle
import pyodbc
import urllib.request, urllib.error, urllib.parse
from IPython.display import Javascript
from IPython.display import display
from newspaper import Article
import random
import string
import urllib.request, urllib.error, urllib.parse
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
import re
from difflib import SequenceMatcher
warnings.filterwarnings('ignore')


urllist = {'A':'https://www.godrejinfotech.com/Careers.aspx','B':'https://www.godrej.com/What-we-do'}
#tech = ["infor","microsoft","digital","IOT","AI"]
#tech = ["infor","microsoft","digital","iot","ai","digital automation","rpa"]
offering = ["solutions","solution","services","service","industry","industry focus","focus", "insights","insight","contact","contact us","contactus","careers","career","about","us","aboutus"]

enterpriseapplist = ["enterprise","application","technology","digital","in","house","application","open","source","tech"]
serviceslist = ["business", "process", "consulting", "implementation","global","rollout","managed","migration","enhance","advancement","upgrade","infrastructure","legacy","modernisation","devops","platform","engineer","ops","mobile","mobileapp","app","app development","development","android","androidapp","ios","app","iosapp","dev","data","data protection","hacking","hack protection","hack","information protection","protection","security","information"]
industryfocuslist = ["manufacturing","production","assemble","manufacture","compose","retail","marketing","merchandising","direct sale","sale","trading","distribution","trade","logistics","exchange","deal","deals","dispersal","sorting","delivery","transportation","project","projects","idea","plan","concept","conception","specification", "professional","expert advice","advice","expert","special","skilled","help"]
insightslist = ["collateral","media","case","studies","case studies","dossier","study","case history","history","accounts","broucher","brouchers","pamphlet","booklet","prospectus","catalogue","circular","leaflet","handout","flyer","ad","advertisement"]

enterpriseapp = ["infor","ln","inforln","erp","enterprise", "resource", "planning", "baan", "cloudsuite","d365finance","d365","d365scm","finance","supply", "chain", "management", "supply chain management","f&o", "bc","central","bcentral","b","microsoft","commerce","trade", "dynamics","ax","axapta","xapta", "microsoftax","nav","navision","ls","central","point","of","oracle","pl/sql","pl","sql","dba"]
techlist = ["infor","microsoft","erp","dnynamics"]
digitalsol = ["sales","crm","salesforce","low","code","application","development","lcad","ai","artificial","intelligence","ml","machine","learning","language","assembler","machinecode","oriented","programming","expert","systems","intelligent", "retrieval", "intelligent retrieval","natural","processing","natural language processing","nlp","expert systems","iiot","internet","of","things","industrial","advanced","analytics","sentiment", "analysis","sentiment analysis","comples", "event", "processing","comples event processing","data","mining","data mining", "big", "analytics","sentiment", "analysis","sentiment analysis","comples", "event", "processing","comples event processing","data","mining","data mining", "big", "science", "automation","autonetics","telemechanics","ecommerce","e","ebusiness","online","onlinebusiness","oscommerce","e-marketing","emarketing","marketing"]
inhouseapplist = ["encompass","erp","payroll","salary","management","exim","export","import","export import"]
opensourcetechlist = ["java","open","source"]
collateral = ["success","successes","win", "stories","testimonials","testimonial","user experience", "experience", "user","testament","reference","evidence","proof","videos","video","vid","clip","stream","streaming","short video"]
media = ["webinars","webinar","seminar","forum", "summit", "conference", "meeting", "convention", "session","blogs","blog","journal","log","microblog", "newsletter", "weblog", "record", "news","report","announcement","article", "headline", "press", "press release","release","bulletin","achievements","achievement","effort","accomplishment","gain"]

inforlist = ["wms","cs","warehouse","epm","d","performance","factory","track","tracking","eam","enterprise asset","asset","os","xi", "operating", "xm","expense", "control", "expense control", "birst"]
microsoftlist = ["power","bi","microsoftbi","bianalytics","azure","cloud computing","cloud","computing","windows","office365","office","word","power","point","power point","wmsnav","navwms","disaster","recovery","dr","net","dot","dot net", "tld","sharepoint","share","pointshare"]

tech = ["infor","microsoft","digital","iot","ai","rpa","automation"]
data = {"intents": [
                {"tag": "greeting",
                "patterns": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day", "Whats up","Hey","my Pleasure","my","pleasure"],
                "responses": ["Hello!", "Good day.!", "Hi there, how can I help?","Hey!"],
                "context_set": ""
                },
                {"tag": "goodbye",
                "patterns": ["cya", "See you later", "Goodbye", "I am Leaving", "Have a Good day","Bye","Talk to you later"],
                "responses": ["Thanks for visiting!", "Talk to you later", "Goodbye!","Nice talking with you.!"],
                "context_set": ""
                },
                #{"tag": "technology",
                #"patterns": ["infor ln", "infor cloudsuite", "infor os", "power bi", "microsoft azure","digital","iot","AI","Artificial intelligence","Automation","RPA", "Digital Automation","Robotics Process Automation"],
                #"responses": ["tech", "tech1", "tech2"],
                #"context_set": ""
                #},
                {"tag": "leaves",
                "patterns": ["how many sick leaves", "leaves taken becaus of sickness?", "how many holidays taken?", "sick leaves?", "leaves?","leaves for"],
                "responses": ["Random", "I am Random"],
                "context_set": ""
                },
                {"tag": "order",
                "patterns": ["what is total sales for order?", "total sales amount?", "total order amount for order?"],
                "responses": ["order", "I'm order", "I'm Order aka Sales Order."],
                "context_set": ""
                },
                {"tag": "business",#Solution
                "patterns": ["What solutions do you offer?","What solutions you offer?","business", "solution","solutions", "power","bi", "microsoftbi","bianalytics","azure","cloud computing","cloud","computing","windows","office365","office","word","power","point","power point","wmsnav","navwms","disaster","recovery","dr","net","dot","dot net", "tld","sharepoint", "share","pointshare","wms","cs","warehouse","epm","d","performance","factory","track","tracking","eam","enterprise asset","asset","os","xi", "operating","xm","expense", "control", "expense control","birst", "sales","crm","salesforce","low","code","application","development","lcad","ai","artificial","intelligence","ml","machine","learning","language","assembler","machinecode","oriented","programming","expert","systems","intelligent", "retrieval", "intelligent retrieval","natural","processing","natural language processing","nlp","expert systems", "iot","iiot","internet","of","things","industrial", "advanced","analytics","sentiment", "analysis","sentiment analysis","comples", "event", "processing","comples event processing","data","mining","data mining", "big", "analytics", "science","automation","autonetics","telemechanics","ecommerce","e","ebusiness","online","onlinebusiness","oscommerce","e-marketing","emarketing","marketing", "java", "encompass","erp", "payroll","salary","management", "exim","export","import","export import", "infor","ln","inforln", "erp","enterprise", "resource", "planning", "baan", "cloudsuite","infor cloudsuite", "D365finance& D365SCM", "finance","supply", "chain", "management", "supply chain management","f&o", "D365 BC", "bc","central","bcentral","b","LS Central", "Microsoft Dynamics NAV","Microsoft Dynamics AX","ax", "axapta","xapta", "microsoftax","Microsoft D365 commerce","commerce","trade", "D365finance","D365","D365SCM","BC","Microsoft","Commerce","Dynamics","AX","NAV","navision","LS","Central","point", "of", "oracle","pl/sql","pl","sql","dba", "enterprise","application","technology","digital","in","house","application","open","source","tech", "Solutions","Business Verticals", "what solutions do you Sell?","what servies can I chose from ?","What services do you offer ?", "what are your offerings ?","Offerings"],
                "responses": [urllist['B'],"We offer [1].Infor  [2].Microsoft  [3].IOT/AI. Enter what service you looking?"],
                "context_set": ""
                }, 
                {"tag": "software",#services
                "patterns": ["services", "service", "process", "what services?" "consulting", "implementation","global","rollout","managed","migration","upgrade","enhance","advancement","infrastructure","legacy","modernisation","devops","platform","engineer","ops","dev","mobileapp","app","app development","development","android","androidapp","ios","app","iosapp","data","data protection","hacking","hack protection","hack","information protection","protection","security", "What services?","Services Offered", "What services you provide?", "Service provider?"],
                "responses": [urllist['B'],"We offer [1].Consulting  [2].Implemntation  [3].Rollout/Upgrade. Enter what service you looking?"],
                "context_set": ""
                }, 
                {"tag": "industryfocus",
                "patterns": ["manufacturing","production","assemble","manufacture","compose","industryfocus","retail","marketing","merchandising","direct sale","sale","trading","distribution","trade","logistics","exchange","deal","deals","dispersal","sorting","delivery","transportation","project","projects","idea","plan","concept","conception","specification", "professional","expert advice","advice","expert","special","skilled","help","industry","focus"],
                "responses": ["Industry Focus"],
                "context_set": ""
                }, 
                {"tag": "insights",
                "patterns": ["insights","insight","Collateral","successes","win","webinars","webinar","seminar","forum", "summit", "conference", "meeting", "convention", "session", "blogs","blog","journal","log","microblog", "newsletter", "weblog", "record", "news","report","announcement","article", "headline", "press", "press release","release","bulletin","achievements","achievement", "effort","accomplishment","gain", "media","case","studies","case studies","dossier","study","case history","accounts", "brouchers", "broucher","pamphlet","booklet","prospectus","catalogue","circular","leaflet","handout","flyer","ad","advertisement", "success","stories","testimonials","testimonial","user experience", "experience", "user","testament","reference","evidence","proof","videos","video","vid","clip","stream","streaming","short video"],
                "responses": ["Industry Focus"],
                "context_set": ""
                }, 
                {"tag": "aboutus",
                "patterns": ["about", "us","godrej","infotech", "godrejinfotech","about us","aboutus", "what we do", "introduction", "aboutus", "our introduction","who we are?" ],
                "responses": ["About US"],
                "context_set": ""
                },
                {"tag": "contactus",
                "patterns": ["contact", "call", "phone","number", "email", "address", "mail", "id", "get in touch", "reach", "contact us","contactus", "email","mobile","number","connect with us","contact details"],
                "responses": ["Contact US"],
                "context_set": ""
                },
                {"tag": "outofreach",
                "patterns": ["outofreach", "out of context"],
                "responses": ["Sorry, send relevant option","Sorry, I am trained on relevant questions only","Sorry, I don't get what you say.!","I don’t think I understood you clearly.!"],
                "context_set": ""
                },
                {"tag": "careers",
                "patterns": ["Vacancy","opening","cv", "resume", "vacancy for technical consultant","vacancy for finance?","hire", "careers","are you hiring now ?", "are there any openings for finance consultant?","openings for technical consultants?", "career", "Any position vacant", "Looking for job opportunity", "Apply for a job", "Job", "jobs", "Career Opportunity" ],
                "responses": [urllist['A']],
                "context_set": ""
                }
                     ]
            }

conx_string = "driver={SQL SERVER}; server=DESKTOP-9SBDH1C; database=AdventureWorks2014; trusted_connection=YES;"
Lquery = "select SickLeaveHours from [HumanResources].[Employee]"
Userquery = "select LoginID from [HumanResources].[Employee]"
Oquery = "select TotalDue from [Sales].[SalesOrderHeader] where SalesOrderID = 43659"
listvisits = [] 
query1 = []
check = []
visitordetails = []
vdetails = []

@api_view(["POST","GET"])
def index(request):
    return JsonResponse("Hi There",safe = False)


@api_view(["POST","GET"])
def bot_search(request):
    try:
        with open("words.pickle", "rb") as f1:
            words = pickle.load(f1) 
        with open("labels.pickle", "rb") as f2:
            labels = pickle.load(f2) 
        with open("training.pickle", "rb") as f3:
            training = pickle.load(f3) 
        with open("output.pickle", "rb") as f4:
            output = pickle.load(f4)  
    except:    
        words = []
        labels = []
        docs_x = []
        docs_y = []

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"])

                if intent["tag"] not in labels:
                    labels.append(intent["tag"])

        words = [stemmer.stem(w.lower()) for w in words if w != "?"]	
        words = sorted(list(set(words)))

        labels = sorted(labels)	

        training = []
        output = []	

        out_empty = [0 for _ in range(len(labels))]
      
        for x, doc in enumerate(docs_x):
            bag = []

            wrds = [stemmer.stem(w) for w in doc]

            for w in words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)	

            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1

            training.append(bag)
            output.append(output_row)
            with open("words.pickle", "wb") as f1:
                pickle.dump(words, f1)
            with open("labels.pickle", "wb") as f2:
                pickle.dump(labels, f2)
            with open("training.pickle", "wb") as f3:
                pickle.dump(training, f3)
            with open("output.pickle", "wb") as f4:
                pickle.dump(output, f4) 

        training = numpy.array(training)
        output = numpy.array(output)

    ops.reset_default_graph()	

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

    try:
        model.load("model.tflearn")
    except:    
        model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
        model.save("model.tflearn")

    def bag_of_words(s, words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1

        return numpy.array(bag)

    Userlist = []
    vname = ""
    vsurname = ""
    vnumber = ""
    vemail = ""
    query = request.GET.get('query')
    vname = request.GET.get('vname')
    vsurname = request.GET.get('vsurname')
    vnumber = request.GET.get('vnumber')
    vemail = request.GET.get('vemail')
    print(query)
    print(vname)
    print(vsurname)
    print(vnumber)
    print(vemail)
    if vname != None or vsurname != None or vnumber != None or vemail != None:
        vdetails.append(vname)
        vdetails.append(vsurname)
        vdetails.append(vnumber)
        vdetails.append(vemail)
        if len(query1) == 1:
                #query = query1[0]
                query = "solutions"
        else:
            query = "goodbye"    
        print(query + " 12333 " + str(len(query1)))
        for ele in query1:
            print(ele)
        cntd = ""
        query1.clear()

    flag = False
    check.append(False)
    flag3 = True
    for ele in check:
        if ele == True:
            flag3 = False
            check.clear()

    querylw = query.lower()
    print(querylw)
    if querylw == "continue":
        lngth = len(query1) - 1
        query = query1[lngth]
        print("123321")
        print(lngth)
        print(query1)
        print(query)
        print("123321")

    listvisits.append(1)
    bye = False
    dt = ""
    length = len(listvisits)
    vlength = len(visitordetails)
    vdlength = len(vdetails)
    glength = len(query1)
    for ele in query1:
        if ele == "goodbye":
            bye = True
    print(flag3)
    print(" shbhsbh " + str(vlength))
    print(length)
    if length % 5 == 0 and vlength == 0 and vdlength == 0 and bye == False:
        query1.append(query)
        #query = "outofreach"
        dt = "details"
        print(query + " 123432 ")
        print(query1)
        print(query + " 123432 ")
        for ele in query1:
            print(ele)
    print("shsv")
    print(vdetails)
    print("shsv")
    print(len(listvisits))
    print(query1)
    MobileNumber = 0
    Name = ""
    Surname = ""
    Email = ""
    MobileString = ""
    print(query)
    if query == "":
        query = "random"

    FirstTen = query[0:10]
    if (isMobileNo(FirstTen)):
        Details = query.split('_')
        length = len(Details)
        for ele in Details:
            visitordetails.append(ele)
        if length == 4 :
            MobileString = Details[0]
            MobileNumber = int(MobileString)
            Name = Details[1]
            Surname = Details[2]
            Email = Details[3]
            #insertdetails( MobileString,Name,Surname,Email)
            if len(query1) == 1:
                query = query1[0]
            else:
                print("nknckjnck")
                query = "goodbye"
            print(query + " 12333 " + str(len(query1)))
            for ele in query1:
                print(ele)
            query1.clear()

    print(MobileString)
    print(MobileNumber)
    print(Name)
    print(Surname)
    print(Email)

    partt = query.split()

    print(partt)
    ans = "random"
    url = ""
    urlc = ""
    cnt = ""
    if vdlength == 0:
        cntd = "Contact"
    else:
        cntd = ""
        
    bus1 = ""
    bus2 = ""
    bus3 = ""
    bus4 = ""
    bus5 = ""
    bus6 = ""
    bus7 = ""
    bus8 = ""
    bus9 = ""
   
    d1 = ""
    d2 = ""
    d3 = ""
    d4 = ""
    d5 = ""
    d9 = ""
    part = [word.lower() for word in partt]

    print(part)
    #x = part
    #userlist1= connection1(Userquery)
    #for tpl in userlist1:
        #(ans1, ) = tpl
        #Userlist.append(ans1)
        
    username = "adventure-works\ken0" 
    print(username)
    print(part)
   
    content2 = ""
    content3 = ""
    content4 = ""
    content5 = ""
    content1 = "error"
    tech = ""
    print(len(part))
    if len(part) == 1:
        if part[0] == "infor" or part[0] == "inforln" or part[0] == "erp" or part[0] == "ln":
            tech = "infor"
        elif part[0] == "microsoft":
            tech = "microsoft"

    print(tech + "  qqssjn")
    print("jbvuvvjvj")
    print(flag)
    print("bdvdvdv")
    for element in part:
        print(element)    
        if element in offering: 
            content2 = element
            content3 = ""
            print("element1234")
            print(content2)           
        elif element in serviceslist:
                content2 = "services"            
                content3 = element  
                print("element1234578")
                print(content3) 
        elif element in enterpriseapplist:
                content2 = "solutions"
                content4 = element
        elif element in enterpriseapp: 
                content2 = "solutions"
                content3 = element
                print("gdgdgdy")
        elif element in industryfocuslist:
                content2 = "industryfocus"
                content3 = element
        elif element in insightslist:
                content2 = "insights"
                content4 = element
        elif element in collateral:
                content2 = "insights"
                content3 = element
        elif element in media:
                content2 = "insights"
                content3 = element  
        elif element in inhouseapplist:
                content2 = "solutions"
                content3 = element
        elif element in digitalsol:
                content2 = "solutions"
                content3 = element
        elif element in opensourcetechlist:
                content2 = "solutions"
                content3 = element
        elif element in techlist:
                content2 = "solutions"
                content3 = element
        elif element in inforlist:
                content2 = "solutions"
                content3 = "infor"
                content4 = element
        elif element in microsoftlist:
                content2 = "solutions"
                content3 = "microsoft"
                content4 = element

    print(username)
    print(query)
    print(content2 + " 12cbbc")
    print(content3 + " bshbsh")
    print(content4 + " bjhbsjv")
    inp = 'Hi'

    results = model.predict([bag_of_words(str(query), words)])  
    results_index = numpy.argmax(results)
    tag = labels[results_index] 

    data1 = random.choice(data["intents"][10]["responses"]) 
    data2 = random.choice(data["intents"][10]["responses"])
    data3 = 'Please select from one of the following options :'  
    data4 = "Solutions"
    data5 = "Services"
    data6 = "Industry Focus"
    data7 = "Insights"
    data8 = "Contact Us"
    data9 = "Careers"
    data10 = "About Us"
    print(tag)
    print(content2 + "  343")
    print(content3)
    for tg in data["intents"]:
        if tg['tag'] == tag:
            #if tg['tag'] != "leaves" and tg['tag'] != "order" and tg['tag'] != "technology" and tg['tag'] != "business" and tg['tag'] != "careers" and tg['tag'] != "goodbye" :
            if tg['tag'] == "greeting" :  
                responses = tg['responses']
                url = ""
                urlc = ""
                cnt = ""
                #ans = random.choice(responses) 
                ans = ""
                data1 = ""
                data2 = random.choice(responses) + ' Hope you are doing great today, How can I help you ? '
                data3 = "" 
                b1 = '' 
                d1 = data2 + 'Please select from one of the following options :' 
                b2 = "Solutions"
                b3 = "Services"
                b4 = "Industry Focus"
                b5 = "Insights"
                b6 = "Contact Us"
                b7 = "Careers"
                b8 = "About Us"
                b9 = ""
                d9 = "or just simply type what you looking for?"
                bus1 = b1
                bus2 = b2
                bus3 = b3
                bus4 = b4
                bus5 = b5
                bus6 = b6
                bus7 = b7
                bus8 = b8
                bus9 = b9
                #noclicks = noclicks + 1
                print(ans) 
            elif tg['tag'] == "goodbye":
                print(len(visitordetails))
                if len(vdetails) == 0:
                    responses = tg['responses'] 
                    ans = ""
                    print(ans) 
                    url = ""
                    urlc = ""
                    b1 = ""
                    d1 = random.choice(responses)
                    b2 = '' 
                    d2 = 'To help you better, our representative will get in touch with you.' 
                    b3 = ""
                    d3 = "Would you like to share your contact details?"
                    dt = "details"
                    b4 = ""
                    d4 = ""
                    b5 = ""
                    d5 = ""
                    bus1 = b1
                    bus2 = b2
                    bus3 = b3
                    bus4 = b4
                    bus5 = b5
                    cnt = ""
                    data1 = ""
                    query1.append("goodbye")
                    #noclicks = noclicks + 1 
                    print(Name+"!!" + str(MobileNumber) + Surname)
                    if MobileString !="" or MobileNumber != 0 or Name !=""  or Surname != "":
                        data2 = "Nice talking you!"
                        data3 = "Our Consultant will Get Back to you shortly, Thanks!"
                    else:
                        data2 = ans
                        data3 = "" 
                else:
                    responses = tg['responses'] 
                    ans = ""
                    print(ans) 
                    url = ""
                    urlc = ""
                    b1 = ""
                    if vname != None or vsurname != None or vnumber != None or vemail != None:
                        d1 = random.choice(responses) + " "+ vname + " " + vsurname +" " +' Thanks for sharing details.! ' + " " + vnumber + " " +  vemail + " "
                    else:
                        d1 = "Goodbye! Nice Talking to you.Have a nice day.!"

                    b2 = "" 
                    d2 = "Our representative will get in touch with you shortly.!!"
                    b3 = ""
                    b4 = ""
                    b5 = ""
                    bus1 = b1
                    bus2 = b2
                    bus3 = b3
                    bus4 = b4
                    bus5 = b5
                    cnt = ""
                    data1 = ""
            elif tg['tag'] == "outofreach": 
                 responses = tg['responses']
                 ans = ""
                # ans = "For career related queries :" 
                 data2 = ""
                 data3 = ""
                 url = ''
                 urlc = ""
                 cnt = ""
                 b1 = '' 
                 d1 = '' 
                 b2 = ""
                 d2 = ""
                 b3 = ""
                 d3 = ""
                 dt = "details"
                 b4 = ""
                 d4 = ""
                 b5 = ""
                 b6 = ""
                 b7 = ""
                 b8 = ""
                 b9 = ""
                 bus1 = b1
                 bus2 = b2
                 bus3 = b3
                 bus4 = b4
                 bus5 = b5
                 bus6 = b6
                 bus7 = b7
                 bus8 = b8
                 bus9 = b9 
                 flag = True
                 #listvisits.clear()
                 #noclicks = 0
                 check.append(True)
                 query = ""
                 print(tg['tag'])
                 print(ans)
                 print(url)          
            elif tg['tag'] == "careers": 
                 responses = tg['responses']
                 #ans = random.choice(responses)
                 ans = "" 
                 b1 = ""
                 d1 = "You have a great choice, let me give you an insider look, Godrej is one of the finest places to work, with beautiful campus and superb workmates, I wish you the best and hope to see you soon in one of our teams.  "
                 b2 = ""
                 bus1 = b1
                 bus2 = b2
                 url = 'https://www.godrejinfotech.com/Careers.aspx'
                 urlc = ""
                 cnt = ""
                 print(tg['tag'])
                 print(ans)
                 print(url)
                 #noclicks = noclicks + 1
                 #open_web()
            elif tg['tag'] == "aboutus": 
                 responses = tg['responses']
                 #ans = random.choice(responses)
                 ans = "" 
                 data2 = ""
                 data3 = ""
                 url = 'https://www.godrejinfotech.com/aboutUs.aspx'
                 urlc = ""
                 cnt = ""
                 b1 = ""
                 d1 = "To know more about us, "
                 b2 = ""
                 bus1 = b1
                 bus2 = b2
                 #noclicks = noclicks + 1
                 print(tg['tag'])
                 print(ans)
                 print(url)
            elif tg['tag'] == "contactus": 
                 responses = tg['responses']
                 #ans = random.choice(responses)
                 ans = "" 
                 data2 = ""
                 data3 = ""
                 url = 'https://www.godrejinfotech.com/contact-us.aspx'
                 urlc = ""
                 cnt = ""
                 #noclicks = noclicks + 1
                 b1 = ""
                 d1 = "For contact details :"
                 b2 = ""
                 bus1 = b1
                 bus2 = b2
                 print(tg['tag'])
                 print(ans)
                 print(url)
           # elif tg['tag'] == "technology":
                 #if content1 == "infor":
                   # link1 = 'https://www.godrejinfotech.com/solutions/enterpriseApp/infor-ln.aspx'
                    #url = link1
                   # urlc = ""
                   # cnt = "Intrested? Please share Mobile no_name_surname_location. Our representative will get in touch with you"
                   # data1 = get_webdata(link1)
                   # data2 = data1[0:37]
                   # data2 = data2 + " : "
                    #data3 = data1[37:]
                # elif content1 == "microsoft":
                    #link1 = 'https://www.godrejinfotech.com/solutions/enterpriseApp/ms-axapta.aspx'
                    #url = link1
                   # urlc = ""
                   # cnt = "Intrested? Please share Mobile no_name_surname_location. Our representative will get in touch with you"
                   # data1 = get_webdata(link1) 
                    #data2 = data1[0:21]
                   # data2 = data2 + " : "
                    #data3 = data1[21:]
                # elif content1 == "iot" or content1 == "ai":
                    #link1 = 'https://www.godrejinfotech.com/solutions/digitalSolutions/Digital_IIOT.aspx'
                    #url = link1
                    #urlc = ""
                    #cnt = "Intrested? Please share Mobile no_name_surname_location. Our representative will get in touch with you"
                    #data1 = get_webdata(link1) 
                    #data2 = data1[0:45]
                    #data2 = data2 + " : "
                    #data3 = data1[45:]
                    #print(link1)
                # elif content1 == "rpa" or content1 == "automation":
                    #link1 = 'https://www.godrejinfotech.com/solutions/digitalSolutions/Digital_Automation.aspx'
                    #url = link1
                    #urlc = ""
                    #cnt = "Intrested? Please share Mobile no_name_surname_location. Our representative will get in touch with you"
                    #data1 = get_webdata(link1) 
                    #data2 = data1[0:41]
                    #data2 = data2 + " : "
                    #data3 = data1[41:]
                 #elif content1 == "error":
                    #data1 = "Please enter relevant option" 
                    #data2 = "Please enter relevant option"
                    #data3 = ""
                    #url = "" 
                    #urlc = ""
                    #cnt = "" 
                 #ans = data1 
            elif tg['tag'] == "business": 
                print(content2 + " 2abcd")
                #noclicks = noclicks + 1
                if content2 == "solutions" or content2 =="solution":
                    if content3 == "":
                        print(content3)
                        if content4 == "":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrej.com/What-we-do'
                            urlc = ""
                            b1 = ""
                            d1 = "Our solutions includes : "
                            b2 = "Enterprise Application"
                            b3 = "Technology"
                            b4 = "Digital Solutions"
                            b5 = "Applications In House"
                            b6 = "Open Source Tech"
                            b7 = ""
                            d7 = "What Solution you looking for?"
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = ""
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""
                            #open_web()
                        elif content4 =="enterprise" or content4 == "application": 
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrej.com/What-we-do'
                            urlc = ""
                            b1 = ""
                            d1 = "Our enterprise application includes : "
                            b2 = "Infor CloudSuite"
                            b3 = "D365finance& D365SCM"
                            b4 = "D365 BC"
                            b5 = "Microsoft D365 commerce"
                            b6 = "Microsoft Dynamics AX"
                            b7 = "Microsoft Dynamics NAV"
                            b8 = "LS Central"
                            b9 = "Oracle"
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            bus9 = b9
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = "" 
                        elif content4 =="technology" or content4 == "technologies": 
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrej.com/What-we-do'
                            urlc = ""
                            b1 = ""
                            d1 = "Our technological solutions includes : "
                            b2 = "Infor "
                            b3 = "Microsoft"
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b9 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            bus9 = b9
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""
                        elif content4 =="digital" or content4 == "solutions" or content4=="solution": 
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrej.com/What-we-do'
                            urlc = ""
                            b1 = ""
                            d1 = "Our digital solution includes : "
                            b2 = "D365 Sales CRM"
                            b3 = "Salesforce"
                            b4 = "Low Code Application Development"
                            b5 = "AI and ML"
                            b6 = "IIOT"
                            b7 = "Advanced Analytics"
                            b8 = "Digital Automation"
                            b9 = "E-Commerce"
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            bus9 = b9
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""
                        elif content4 =="in" or content4 == "house" or content4=="applications" or content4=="applications": 
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrej.com/What-we-do'
                            urlc = ""
                            b1 = ""
                            d1 = "Our In House Application includes : "
                            b2 = "eNcompass"
                            b3 = "Payroll D365"
                            b4 = "Payroll NAV"
                            b5 = "EXIM"
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b9 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            bus9 = b9
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""  
                        elif content4 =="open" or content4 == "source" or content4=="tech": 
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrej.com/What-we-do'
                            urlc = ""
                            b1 = ""
                            d1 = "Our Open Source Tech includes : "
                            b2 = "JAVA"
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b9 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            bus9 = b9
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""  
                    elif content3 == "infor" or content3 =="cloudsuite" or content3 =="ln" or content3 == "inforln" or content3 == "erp" or content3 == "enterprise" or content3 == "resource" or content3 == "planning" or content3 == "baan":
                            print(content3 + "  12343  " + content4 + "   4gdgd   " + tech)
                            if tech == "" and content4 == "":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/WorldLargestManufacturerSheetMetal.pdf'
                                b1 = " "
                                d1 = "Would yo like to see brouchers/case studies of Infor Cloudsuite ? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b9 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""
                            else:
                                if content4 == "":
                                    responses = tg['responses']
                                    #ans = random.choice(responses)
                                    print(tg['tag']) 
                                    ans = ""
                                    url = 'https://www.godrejinfotech.com/solutions/surroundTechnology/InforCloudSuiteWMS.aspx'
                                    urlc = ""
                                    b1 = ""
                                    d1 = "Our Infor solution includes : "
                                    b2 = "Infor Cloudsuite WMS"
                                    b3 = "Infor d/EPM"
                                    b4 = "Infor Factory Track"
                                    b5 = "Infor EAM"
                                    b6 = "Infor OS"
                                    b7 = "Infor Xm"
                                    b8 = "Birst"
                                    b9 = ""
                                    bus1 = b1
                                    bus2 = b2
                                    bus3 = b3
                                    bus4 = b4
                                    bus5 = b5
                                    bus6 = b6
                                    bus7 = b7
                                    bus8 = b8
                                    bus9 = b9
                                    print(bus1  + bus2 + bus3 + bus4)
                                    cnt = ""
                                elif content4 == "infor" or content4 == "cloudsuite" or content4 == "wms" or content4 == "cs" or content4 == "warehouse":
                                    responses = tg['responses']
                                    #ans = random.choice(responses)
                                    print(tg['tag']) 
                                    ans = ""
                                    url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                    urlc = ''
                                    b1 = ""
                                    d1 = "Would yo like to see brouchers/case studies of Infor Cloudsuite WMS? "
                                    b2 = ""
                                    b3 = ""
                                    b4 = ""
                                    b5 = ""
                                    b6 = ""
                                    b7 = ""
                                    b8 = ""
                                    b9 = ""
                                    bus1 = b1
                                    bus2 = b2
                                    bus3 = b3
                                    bus4 = b4
                                    bus5 = b5
                                    bus6 = b6
                                    bus7 = b7
                                    bus8 = b8
                                    print(bus1  + bus2 + bus3 + bus4)
                                    cnt = ""
                                elif content4 == "infor" or content4 == "d" or content4 == "epm" or content4 == "performance":
                                    responses = tg['responses']
                                    #ans = random.choice(responses)
                                    print(tg['tag']) 
                                    ans = ""
                                    url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                    urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/IndustrialValveManufacturer_Infor_UAE.pdf'
                                    b1 = ""
                                    d1 = "Would yo like to see brouchers/case studies of Infor d/EPM ? "
                                    b2 = ""
                                    b3 = ""
                                    b4 = ""
                                    b5 = ""
                                    b6 = ""
                                    b7 = ""
                                    b8 = ""
                                    b9 = ""
                                    bus1 = b1
                                    bus2 = b2
                                    bus3 = b3
                                    bus4 = b4
                                    bus5 = b5
                                    bus6 = b6
                                    bus7 = b7
                                    bus8 = b8
                                    print(bus1  + bus2 + bus3 + bus4)
                                    cnt = ""
                                elif content4 == "infor" or content4 == "factory" or content4 == "track" or content4 =="tracking":
                                    responses = tg['responses']
                                    #ans = random.choice(responses)
                                    print(tg['tag']) 
                                    ans = ""
                                    url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                    urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/WesternEuropeLeadingManufacturer.pdf'
                                    b1 = ""
                                    d1 = "Would yo like to see brouchers/case studies of Infor Factory Track ? "
                                    b2 = ""
                                    b3 = ""
                                    b4 = ""
                                    b5 = ""
                                    b6 = ""
                                    b7 = ""
                                    b8 = ""
                                    b9 = ""
                                    bus1 = b1
                                    bus2 = b2
                                    bus3 = b3
                                    bus4 = b4
                                    bus5 = b5
                                    bus6 = b6
                                    bus7 = b7
                                    bus8 = b8
                                    print(bus1  + bus2 + bus3 + bus4)
                                    cnt = ""
                                elif content4 == "infor" or content4 == "eam" or content4 == "enterprise asset" or content4 == "asset":
                                    responses = tg['responses']
                                    #ans = random.choice(responses)
                                    print(tg['tag']) 
                                    ans = ""
                                    url = 'https://www.godrejinfotech.com/solutions/surroundTechnology/infor-EAM.aspx'
                                    urlc = ''
                                    b1 = ""
                                    d1 = "To Know more about Infor EAM, "
                                    b2 = ""
                                    b3 = ""
                                    b4 = ""
                                    b5 = ""
                                    b6 = ""
                                    b7 = ""
                                    b8 = ""
                                    b9 = ""
                                    bus1 = b1
                                    bus2 = b2
                                    bus3 = b3
                                    bus4 = b4
                                    bus5 = b5
                                    bus6 = b6
                                    bus7 = b7
                                    bus8 = b8
                                    print(bus1  + bus2 + bus3 + bus4)
                                    cnt = ""
                                elif content4 == "infor" or content4 == "os" or content4 == "xi" or content4 == "operating":
                                    responses = tg['responses']
                                    #ans = random.choice(responses)
                                    print(tg['tag']) 
                                    ans = ""
                                    url = 'https://www.godrejinfotech.com/solutions/surroundTechnology/infor-OS.aspx'
                                    urlc = ''
                                    b1 = ""
                                    d1 = " To know more about Infor OS, "
                                    b2 = ""
                                    b3 = ""
                                    b4 = ""
                                    b5 = ""
                                    b6 = ""
                                    b7 = ""
                                    b8 = ""
                                    b9 = ""
                                    bus1 = b1
                                    bus2 = b2
                                    bus3 = b3
                                    bus4 = b4
                                    bus5 = b5
                                    bus6 = b6
                                    bus7 = b7
                                    bus8 = b8
                                    print(bus1  + bus2 + bus3 + bus4)
                                    cnt = ""
                                elif content4 == "infor" or content4 == "xm" or content4 == "expense" or content4 == "control" or content4 == "expense control":
                                    responses = tg['responses']
                                    #ans = random.choice(responses)
                                    print(tg['tag']) 
                                    ans = ""
                                    url = 'https://www.godrejinfotech.com/solutions/surroundTechnology/infor-XM.aspx'
                                    urlc = ''
                                    b1 = ""
                                    d1 = "To know more about Infor XM, "
                                    b2 = ""
                                    b3 = ""
                                    b4 = ""
                                    b5 = ""
                                    b6 = ""
                                    b7 = ""
                                    b8 = ""
                                    b9 = ""
                                    bus1 = b1
                                    bus2 = b2
                                    bus3 = b3
                                    bus4 = b4
                                    bus5 = b5
                                    bus6 = b6
                                    bus7 = b7
                                    bus8 = b8
                                    print(bus1  + bus2 + bus3 + bus4)
                                    cnt = ""
                                elif content4 == "birst":
                                    responses = tg['responses']
                                    #ans = random.choice(responses)
                                    print(tg['tag']) 
                                    ans = ""
                                    url = 'https://www.godrejinfotech.com/solutions/surroundTechnology/infor-birst.aspx'
                                    urlc = ''
                                    b1 = ""
                                    d1 = " To know more about Birst, "
                                    b2 = ""
                                    b3 = ""
                                    b4 = ""
                                    b5 = ""
                                    b6 = ""
                                    b7 = ""
                                    b8 = ""
                                    b9 = ""
                                    bus1 = b1
                                    bus2 = b2
                                    bus3 = b3
                                    bus4 = b4
                                    bus5 = b5
                                    bus6 = b6
                                    bus7 = b7
                                    bus8 = b8
                                    print(bus1  + bus2 + bus3 + bus4)
                                    cnt = ""
                    elif content3 == "d365finance" or content3 =="d365scm" or content3 =="finance" or content3 =="supply" or content3 == "chain" or content3 == "management" or content3 == "supply chain management" or content3 =="f&o":
                         responses = tg['responses']
                         #ans = random.choice(responses)
                         print(tg['tag']) 
                         ans = ""
                         url = 'https://www.godrejinfotech.com/assets/pdf/brochures/Microsoft-Dynamics-Brochure.pdf'
                         urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/IndiasLeadingWildlifeNatureConservation_MD365.pdf'
                         b1 = ""
                         d1 = "Would yo like to see brouchers/case studies of D365finance& D365SCM ? "
                         b2 = ""
                         b3 = ""
                         b4 = ""
                         b5 = ""
                         b6 = ""
                         b7 = ""
                         b8 = ""
                         b8 = ""
                         bus1 = b1
                         bus2 = b2
                         bus3 = b3
                         bus4 = b4
                         bus5 = b5
                         bus6 = b6
                         bus7 = b7
                         bus8 = b8
                         print(bus1  + bus2 + bus3 + bus4)
                         cnt = "" 
                    elif content3 == "d365 bc" or content3 =="bc" or content3 =="central" or content3 == "bcentral" or content3 == "b":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/KSA-LeadingDistributor_ElectricalComponents.pdf'
                                b1 = ""
                                d1 = "Would yo like to see brouchers/case studies of D365 Business? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""  
                    elif content3 == "microsoft" or content3 =="d365" or content3 == "commerce" or content3 == "trade":
                                if tech == "" and content4 == "":
                                    responses = tg['responses']
                                    #ans = random.choice(responses)
                                    print(tg['tag']) 
                                    ans = ""
                                    url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                    urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/SaudiCompanySuccessfullyImplementsLSCentralandBusinessCentral.pdf'
                                    b1 = ""
                                    d1 = "Would yo like to see brouchers/case studies of Microsoft D365 commerce? "
                                    b2 = ""
                                    b3 = ""
                                    b4 = ""
                                    b5 = ""
                                    b6 = ""
                                    b7 = ""
                                    b8 = ""
                                    b8 = ""
                                    bus1 = b1
                                    bus2 = b2
                                    bus3 = b3
                                    bus4 = b4
                                    bus5 = b5
                                    bus6 = b6
                                    bus7 = b7
                                    bus8 = b8
                                    print(bus1  + bus2 + bus3 + bus4)
                                    cnt = ""
                                else:
                                    if content4 == "": 
                                        responses = tg['responses']
                                        #ans = random.choice(responses)
                                        print(tg['tag']) 
                                        ans = ""
                                        url = 'https://www.godrej.com/What-we-do'
                                        urlc = ""
                                        b1 = ""
                                        d1 = "Our Microsoft solution includes : "
                                        b2 = "Power BI"
                                        b3 = "Azure"
                                        b4 = "Office365"
                                        b5 = "WMS NAV"
                                        b6 = "Disaster recovery"
                                        b7 = ". NET"
                                        b8 = "Sharepoint"
                                        b9 = ""
                                        bus1 = b1
                                        bus2 = b2
                                        bus3 = b3
                                        bus4 = b4
                                        bus5 = b5
                                        bus6 = b6
                                        bus7 = b7
                                        bus8 = b8
                                        bus9 = b9
                                        print(bus1  + bus2 + bus3 + bus4)
                                        cnt = "" 
                                    elif content4 == "power" or content4 == "bi" or content4 == "microsoftbi" or content4 == "bianalytics":
                                        responses = tg['responses']
                                        #ans = random.choice(responses)
                                        print(tg['tag']) 
                                        ans = ""
                                        url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                        urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/KSA-LeadingDistributor_ElectricalComponents.pdf'
                                        b1 = ""
                                        d1 = "Would you like to see brouchers/case studies of Power BI? "
                                        b2 = ""
                                        b3 = ""
                                        b4 = ""
                                        b5 = ""
                                        b6 = ""
                                        b7 = ""
                                        b8 = ""
                                        b8 = ""
                                        bus1 = b1
                                        bus2 = b2
                                        bus3 = b3
                                        bus4 = b4
                                        bus5 = b5
                                        bus6 = b6
                                        bus7 = b7
                                        bus8 = b8
                                        print(bus1  + bus2 + bus3 + bus4)
                                        cnt = ""
                                    elif content4 == "azure" or content4 == "cloud computing" or content4 == "cloud" or content4 == "computing"or content4 == "windows":
                                        responses = tg['responses']
                                        #ans = random.choice(responses)
                                        print(tg['tag']) 
                                        ans = ""
                                        url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                        urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/KSA-LeadingDistributor_ElectricalComponents.pdf'
                                        b1 = ""
                                        d1 = "Would you like to see brouchers/case studies of Azure? "
                                        b2 = ""
                                        b3 = ""
                                        b4 = ""
                                        b5 = ""
                                        b6 = ""
                                        b7 = ""
                                        b8 = ""
                                        b8 = ""
                                        bus1 = b1
                                        bus2 = b2
                                        bus3 = b3
                                        bus4 = b4
                                        bus5 = b5
                                        bus6 = b6
                                        bus7 = b7
                                        bus8 = b8
                                        print(bus1  + bus2 + bus3 + bus4)
                                        cnt = ""
                                    elif content4 == "office365" or content4 == "office" or content4 == "word" or content4 == "power" or content4 == "point" or content4 == "power point":
                                        responses = tg['responses']
                                        #ans = random.choice(responses)
                                        print(tg['tag']) 
                                        ans = ""
                                        url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                        urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/KSA-LeadingDistributor_ElectricalComponents.pdf'
                                        b1 = ""
                                        d1 = "Would you like to see brouchers/case studies of Office 365 ? "
                                        b2 = ""
                                        b3 = ""
                                        b4 = ""
                                        b5 = ""
                                        b6 = ""
                                        b7 = ""
                                        b8 = ""
                                        b8 = ""
                                        bus1 = b1
                                        bus2 = b2
                                        bus3 = b3
                                        bus4 = b4
                                        bus5 = b5
                                        bus6 = b6
                                        bus7 = b7
                                        bus8 = b8
                                        print(bus1  + bus2 + bus3 + bus4)
                                        cnt = ""
                                    elif content4 == "office365":
                                        responses = tg['responses']
                                        #ans = random.choice(responses)
                                        print(tg['tag']) 
                                        ans = ""
                                        url = 'https://www.godrejinfotech.com/assets/pdf/brochures/Microsoft-Dynamics-Brochure.pdf'
                                        urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/TechnologyOrganization_O365_India.pdf'
                                        b1 = ""
                                        d1 = "Would you like to see brouchers/case studies of Office 365 ? "
                                        b2 = ""
                                        b3 = ""
                                        b4 = ""
                                        b5 = ""
                                        b6 = ""
                                        b7 = ""
                                        b8 = ""
                                        b8 = ""
                                        bus1 = b1
                                        bus2 = b2
                                        bus3 = b3
                                        bus4 = b4
                                        bus5 = b5
                                        bus6 = b6
                                        bus7 = b7
                                        bus8 = b8
                                        print(bus1  + bus2 + bus3 + bus4)
                                        cnt = ""
                                    elif content4 == "wms" or content4 == "nav" or content4 == "navwms" or content4 == "navision wms":
                                        responses = tg['responses']
                                        #ans = random.choice(responses)
                                        print(tg['tag']) 
                                        ans = ""
                                        url = 'https://www.godrejinfotech.com/assets/pdf/brochures/InforBrochure.pdf'
                                        urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/Superstore_LS%20NAV%20Solution_KSA%20Payroll.pdf'
                                        b1 = ""
                                        d1 = "Would you like to see brouchers/case studies of WMS NAV ? "
                                        b2 = ""
                                        b3 = ""
                                        b4 = ""
                                        b5 = ""
                                        b6 = ""
                                        b7 = ""
                                        b8 = ""
                                        b8 = ""
                                        bus1 = b1
                                        bus2 = b2
                                        bus3 = b3
                                        bus4 = b4
                                        bus5 = b5
                                        bus6 = b6
                                        bus7 = b7
                                        bus8 = b8
                                        print(bus1  + bus2 + bus3 + bus4)
                                        cnt = ""
                                    elif content4 == "disaster" or content4 == "recovery" or content4 =="dr":
                                        responses = tg['responses']
                                        #ans = random.choice(responses)
                                        print(tg['tag']) 
                                        ans = ""
                                        url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                        urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/Agro_Producer_NAV.pdf'
                                        b1 = ""
                                        d1 = "Would you like to see brouchers/case studies of Disaster Recovery ? "
                                        b2 = ""
                                        b3 = ""
                                        b4 = ""
                                        b5 = ""
                                        b6 = ""
                                        b7 = ""
                                        b8 = ""
                                        b8 = ""
                                        bus1 = b1
                                        bus2 = b2
                                        bus3 = b3
                                        bus4 = b4
                                        bus5 = b5
                                        bus6 = b6
                                        bus7 = b7
                                        bus8 = b8
                                        print(bus1  + bus2 + bus3 + bus4)
                                        cnt = ""
                                    elif content4 == "net" or content4 == "dot" or content4 == "dot net" or content4 == "tld":
                                        responses = tg['responses']
                                        #ans = random.choice(responses)
                                        print(tg['tag']) 
                                        ans = ""
                                        url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                        urlc = ''
                                        b1 = ""
                                        d1 = "Would you like to see brouchers/case studies of .NET ? "
                                        b2 = ""
                                        b3 = ""
                                        b4 = ""
                                        b5 = ""
                                        b6 = ""
                                        b7 = ""
                                        b8 = ""
                                        b8 = ""
                                        bus1 = b1
                                        bus2 = b2
                                        bus3 = b3
                                        bus4 = b4
                                        bus5 = b5
                                        bus6 = b6
                                        bus7 = b7
                                        bus8 = b8
                                        print(bus1  + bus2 + bus3 + bus4)
                                        cnt = ""
                                    elif content4 == "sharepoint" or content4 == "share" or content4 == "pointshare":
                                        responses = tg['responses']
                                        #ans = random.choice(responses)
                                        print(tg['tag']) 
                                        ans = ""
                                        url = 'https://www.godrejinfotech.com/assets/pdf/brochures/Microsoft-Dynamics-Brochure.pdf'
                                        urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/KSA_CableManufacturer_Sharepoint.pdf'
                                        b1 = ""
                                        d1 = "Would you like to see brouchers/case studies of Sharepoint? "
                                        b2 = ""
                                        b3 = ""
                                        b4 = ""
                                        b5 = ""
                                        b6 = ""
                                        b7 = ""
                                        b8 = ""
                                        b8 = ""
                                        bus1 = b1
                                        bus2 = b2
                                        bus3 = b3
                                        bus4 = b4
                                        bus5 = b5
                                        bus6 = b6
                                        bus7 = b7
                                        bus8 = b8
                                        print(bus1  + bus2 + bus3 + bus4)
                                        cnt = ""
                    elif content3 == "microsoft" or content3 =="dynamics" or content3 == "ax":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/AbuDhabiMultiBusinessCo-operation.pdf'
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of Microsoft Dynamics AX? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""
                    elif content3 == "microsoft" or content3 =="dynamics" or content3 == "nav" or content3 =="navision":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/Microsoft-Dynamics-Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/GlobalTravelRetailer_NAVLS_IndiaUAE.pdf'
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of Microsoft Dynamics NAV? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = "" 
                    elif content3 == "ls" or content3 =="central" or content3 == "point" or content3 == "of":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/LargeRetailerinMauritiusSuccessfullyImplementsMSNAV2017andLSRetail.pdf'
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of LS Central? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""
                    elif content3 == "oracle" or content3 == "pl/sql"  or content3 == "pl"  or content3 == "sql"  or content3 =="dba":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/WorldLargestManufacturerSheetMetal.pdf'
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of Oracle? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""
                    elif content3 == "encompass" or content3 == "erp":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/WorldLargestManufacturerSheetMetal.pdf'
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of eNcompass? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""
                    elif content3 == "payroll" or content3 =="salary" or content3 =="management":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/Microsoft-Dynamics-Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/IndiasLeadingWildlifeNatureConservation_MD365.pdf'
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of Payroll? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""
                    elif content3 == "exim" or content3 =="export" or content3 =="import":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/Leading_Global_Electronics_Manufacturer_%20Dealer_Management_Portal.pdf'
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of EXIM ? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""
                    elif content3 == "java" or content3 == "open" or content3 == "source":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/India_s_Leading_Wildlife_Nature_Conservation_Md365.pdf'
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of JAVA ? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""   
                    elif content3 == "sales" or content3 == "crm":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/LargeRetailerMauritiusSuccessfullyImplements_MSD365CRM.pdf'
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of D365 Sales CRM ? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = "" 
                    elif content3 == "salesforce":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/WorldLargestManufacturerSheetMetal.pdf'
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of D365 SalesForce ? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""
                    elif content3 == "low" or content3 ==  "code" or content3 == "application" or content3 == "development" or content3 == "lcad":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/WorldLargestManufacturerSheetMetal.pdf'
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of Low Code Application Development ? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = "" 
                    elif content3 == "ai" or content3 ==  "ml" or content3 == "artificial" or content3 == "intelligence" or content3 =="language" or content3 =="assembler" or content3 =="machinecode" or content3 =="oriented" or content3 =="programming" or content3 =="expert" or content3 =="systems" or content3 =="intelligent" or content3 == "retrieval" or content3 =="intelligent retrieval" or content3 =="natural" or content3 =="processing" or content3 =="natural language processing" or content3 =="nlp" or content3 =="expert systems":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = ''
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of AI or ML ? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = "" 
                    elif content3 == "iiot" or content3 ==  "iot" or content3 == "internet" or content3 == "of" or content3 == "things" or content3 == "industrial":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = ''
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of IIoT ? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""
                    elif content3 == "advanced" or content3 ==  "analytics" or content3 == "sentiment" or content3 == "analysis" or content3 == "sentiment analysis" or content3 == "comples" or content3 == "event" or content3 == "processing" or content3 =="comples event processing" or content3 =="data" or content3 =="mining" or content3 =="data mining" or content3 =="big" or content3 == "analytics" or content3 == "science":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = ''
                                b1 = " "
                                d1 = "Would you like to see brouchers/case studies of Advanced Analytics ? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = "" 
                    elif content3 == "automation" or content3 == "autonetics" or content3 == "telemechanics":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = ''
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of Digital Automation ? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = ""   
                    elif content3 == "ecommerce" or content3 == "e" or content3 == "ebusiness" or content3 == "online" or content3 == "onlinebusiness" or content3 == "oscommerce" or content3 == "e-marketing" or content3 == "emarketing" or content3 == "marketing":
                                responses = tg['responses']
                                #ans = random.choice(responses)
                                print(tg['tag']) 
                                ans = ""
                                url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                                urlc = ''
                                b1 = ""
                                d1 = "Would you like to see brouchers/case studies of E-Commerce ? "
                                b2 = ""
                                b3 = ""
                                b4 = ""
                                b5 = ""
                                b6 = ""
                                b7 = ""
                                b8 = ""
                                b8 = ""
                                bus1 = b1
                                bus2 = b2
                                bus3 = b3
                                bus4 = b4
                                bus5 = b5
                                bus6 = b6
                                bus7 = b7
                                bus8 = b8
                                print(bus1  + bus2 + bus3 + bus4)
                                cnt = "" 
                else:
                    responses = tg['responses']
                    #ans = random.choice(responses)
                    print(tg['tag']) 
                    ans = ""
                    url = 'https://www.godrej.com/What-we-do'
                    urlc = ""
                    b1 = ""
                    d1 = "Our solutions includes : "
                    b2 = "Enterprise Application"
                    b3 = "Technology"
                    b4 = "Digital Solutions"
                    b5 = "Applications In House"
                    b6 = "Open Source Tech"
                    b7 = ""
                    d7 = "What Solution you looking for?"
                    bus1 = b1
                    bus2 = b2
                    bus3 = b3
                    bus4 = b4
                    bus5 = b5
                    bus6 = b6
                    bus7 = b7
                    bus8 = ""
                    print(bus1  + bus2 + bus3 + bus4)
                    cnt = ""                   
            elif tg['tag'] == "insights": 
                 #noclicks = noclicks + 1
                 if content2 == "insights" or content2 == "insight":
                    print(content2)
                    print(content3)
                    print(content4)   
                    if content3 == "":
                        if content4 == "":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrej.com/What-we-do'
                            urlc = ""
                            b1 = ""
                            d1 = "Our insights includes : "
                            b2 = "Collateral"
                            b3 = "Media"
                            b4 = "Case Studies"
                            b5 = "Brouchers"
                            b6 = ""
                            b7 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = ""
                            bus8 = ""
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""
                            #open_web()
                        elif content4 =="collateral": 
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrej.com/What-we-do'
                            urlc = ""
                            b1 = ""
                            d1 = "Our collateral domain includes : "
                            b2 = "Success Stories"
                            b3 = "Testimonials"
                            b4 = "Videos"
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b9 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            bus9 = b9
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = "" 
                        elif content4 =="media": 
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrej.com/What-we-do'
                            urlc = ""
                            b1 = ""
                            d1 = "Please select one of following media : "
                            b2 = "Webinars"
                            b3 = "Blogs"
                            b4 = "News"
                            b5 = "Achievements"
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b9 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            bus9 = b9
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""
                        elif content4 =="case" or content4=="studies" or content4=="dossier" or content4=="study" or content4=="history" or content4=="accounts": 
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/knowledge-center/case-studies.aspx'
                            urlc = ""
                            b1 = ""
                            d1 = " For Case Studies, "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b9 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            bus9 = b9
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = "" 
                        elif content4 =="broucher" or content4=="brouchers" or content4=="pamphlet" or content4=="booklet" or content4=="prospectus" or content4=="catalogue" or content4=="circular" or content4=="leaflet" or content4=="handout" or content4=="flyer" or content4=="ad" or content4=="advertisement": 
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/knowledge-center/brochures.aspx'
                            urlc = ""
                            b1 = ""
                            d1 = " For Brouchers, "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b9 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            bus9 = b9
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""   
                    elif content3 == "success" or content3 =="stories" or content3 =="successes" or content3 =="win":
                         responses = tg['responses']
                         #ans = random.choice(responses)
                         print(tg['tag']) 
                         ans = ""
                         url = 'https://www.godrejinfotech.com/knowledge-center/success-story.aspx'
                         urlc = ''
                         b1 = ""
                         d1 = " For Success Stories, "
                         b2 = ""
                         b3 = ""
                         b4 = ""
                         b5 = ""
                         b6 = ""
                         b7 = ""
                         b8 = ""
                         b9 = ""
                         bus1 = b1
                         bus2 = b2
                         bus3 = b3
                         bus4 = b4
                         bus5 = b5
                         bus6 = b6
                         bus7 = b7
                         bus8 = b8
                         print(bus1  + bus2 + bus3 + bus4)
                         cnt = "" 
                    elif content3 == "testimonials" or content3 =="testimonial"  or content3 =="user experience"  or content3 =="experience"  or content3 =="user"  or content3 =="testament" or content3 =="reference" or content3 =="evidence"  or content3 =="proof":
                         responses = tg['responses']
                         #ans = random.choice(responses)
                         print(tg['tag']) 
                         ans = ""
                         url = 'https://www.godrejinfotech.com/knowledge-center/testimonial.aspx'
                         urlc = ''
                         b1 = ""
                         d1 = "For Testimonials, "
                         b2 = ""
                         b3 = ""
                         b4 = ""
                         b5 = ""
                         b6 = ""
                         b7 = ""
                         b8 = ""
                         b9 = ""
                         bus1 = b1
                         bus2 = b2
                         bus3 = b3
                         bus4 = b4
                         bus5 = b5
                         bus6 = b6
                         bus7 = b7
                         bus8 = b8
                         print(bus1  + bus2 + bus3 + bus4)
                         cnt = ""  
                    elif content3 == "videos" or content3 =="video" or content3 =="vid" or content3 =="clip" or content3 =="stream" or content3 =="streaming" or content3 =="short video":
                         responses = tg['responses']
                         #ans = random.choice(responses)
                         print(tg['tag']) 
                         ans = ""
                         url = 'https://www.godrejinfotech.com/knowledge-center/videos.aspx'
                         urlc = ''
                         b1 = ""
                         d1 = "For Videos, "
                         b2 = ""
                         b3 = ""
                         b4 = ""
                         b5 = ""
                         b6 = ""
                         b7 = ""
                         b8 = ""
                         b9 = ""
                         bus1 = b1
                         bus2 = b2
                         bus3 = b3
                         bus4 = b4
                         bus5 = b5
                         bus6 = b6
                         bus7 = b7
                         bus8 = b8
                         print(bus1  + bus2 + bus3 + bus4)
                         cnt = ""
                    elif content3 == "webinar" or content3 =="webinars" or content3 =="seminar" or content3 =="forum" or content3 == "summit" or content3 == "conference" or content3 == "meeting" or content3 =="convention" or content3 =="session":
                         responses = tg['responses']
                         #ans = random.choice(responses)
                         print(tg['tag']) 
                         ans = ""
                         url = 'https://www.godrejinfotech.com/media/webinar.aspx'
                         urlc = ''
                         b1 = ""
                         d1 = "For Webinar, "
                         b2 = ""
                         b3 = ""
                         b4 = ""
                         b5 = ""
                         b6 = ""
                         b7 = ""
                         b8 = ""
                         b9 = ""
                         bus1 = b1
                         bus2 = b2
                         bus3 = b3
                         bus4 = b4
                         bus5 = b5
                         bus6 = b6
                         bus7 = b7
                         bus8 = b8
                         print(bus1  + bus2 + bus3 + bus4)
                         cnt = "" 
                    elif content3 == "blog" or content3 =="blogs" or content3 =="journal" or content3 =="log" or content3 =="microblog" or content3 =="newsletter" or content3 =="weblog" or content3 =="record":
                         responses = tg['responses']
                         #ans = random.choice(responses)
                         print(tg['tag']) 
                         ans = ""
                         url = 'https://www.godrejinfotech.com/blog.aspx'
                         urlc = ''
                         b1 = ""
                         d1 = "For Blog, "
                         b2 = ""
                         b3 = ""
                         b4 = ""
                         b5 = ""
                         b6 = ""
                         b7 = ""
                         b8 = ""
                         b9 = ""
                         bus1 = b1
                         bus2 = b2
                         bus3 = b3
                         bus4 = b4
                         bus5 = b5
                         bus6 = b6
                         bus7 = b7
                         bus8 = b8
                         print(bus1  + bus2 + bus3 + bus4)
                         cnt = "" 
                    elif content3 == "news" or content3 =="report" or content3 =="announcement" or content3 =="article" or content3 =="headline"  or content3 =="press" or content3 =="press release" or content3 =="release" or content3 =="bulletin":
                         responses = tg['responses']
                         #ans = random.choice(responses)
                         print(tg['tag']) 
                         ans = ""
                         url = 'https://www.godrejinfotech.com/media/news.aspx'
                         urlc = ''
                         b1 = ""
                         d1 = "For News, "
                         b2 = ""
                         b3 = ""
                         b4 = ""
                         b5 = ""
                         b6 = ""
                         b7 = ""
                         b8 = ""
                         b9 = ""
                         bus1 = b1
                         bus2 = b2
                         bus3 = b3
                         bus4 = b4
                         bus5 = b5
                         bus6 = b6
                         bus7 = b7
                         bus8 = b8
                         print(bus1  + bus2 + bus3 + bus4)
                         cnt = "" 
                    elif content3 == "achievement" or content3 == "achievements" or content3 =="effort" or content3 =="accomplishment" or content3 =="gain":
                         responses = tg['responses']
                         #ans = random.choice(responses)
                         print(tg['tag']) 
                         ans = ""
                         url = 'https://www.godrejinfotech.com/media/achievement.aspx'
                         urlc = ''
                         b1 = ""
                         d1 = "For Achievements, "
                         b2 = ""
                         b3 = ""
                         b4 = ""
                         b5 = ""
                         b6 = ""
                         b7 = ""
                         b8 = ""
                         b9 = ""
                         bus1 = b1
                         bus2 = b2
                         bus3 = b3
                         bus4 = b4
                         bus5 = b5
                         bus6 = b6
                         bus7 = b7
                         bus8 = b8
                         print(bus1  + bus2 + bus3 + bus4)
                         cnt = "" 
                                                          
            elif tg['tag'] == "industryfocus":
                 #noclicks = noclicks + 1
                 print(content2+"   2abcd")
                 print(content3+"   3abcd")
                 if content2 == "focus" or content2 == "industry" or content2 == "industryfocus" :
                    if content3 == "":
                        responses = tg['responses']
                        #ans = random.choice(responses)
                        print(tg['tag']) 
                        ans = ""
                        url = 'https://www.godrej.com/What-we-do'
                        urlc = ""
                        b1 = ""
                        d1 = "Our industry focus includes : "
                        b2 = "Manufacturing"
                        b3 = "Retail"
                        b4 = "Trading and Distribution"
                        b5 = "Project"
                        b6 = "Professional"
                        b7 = ""
                        b8 = ""
                        b8 = ""
                        bus1 = b1
                        bus2 = b2
                        bus3 = b3
                        bus4 = b4
                        bus5 = b5
                        bus6 = b6
                        bus7 = b7
                        bus8 = b8
                        print(bus1  + bus2 + bus3 + bus4)
                        cnt = ""
                        #open_web()  
                    else :
                        if content3 == "manufacturing" or content3 =="production" or content3 =="assemble" or content3 =="manufacture" or content3 =="compose":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                            urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/SubsidiaryLeadingGlobalDairyProductManufacturer_MD365FinanceOperation.pdf'
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Manufacturing ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""
                        elif content3 == "retail" or content3 =="marketing" or content3 =="merchandising" or content3 =="direct sale" or content3 =="sale":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                            urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/GlobalTravelRetailer_NAVLS_IndiaUAE.pdf'
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Retail ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""
                        elif content3 == "trading" or content3 == "distribution" or content3 =="trade" or content3 =="logistics" or content3 =="exchange" or content3 =="deal" or content3 =="deals" or content3 =="dispersal" or content3 =="sorting" or content3 =="delivery" or content3 =="transportation":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                            urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/LeadingDistributorofFruitsVegetablesinthePhilippinesGoesLivewithD365FandOCloudSolution.pdf'
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Trading and Distribution ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""
                        elif content3 == "project" or content3 == "projects" or content3 =="idea" or content3 =="plan" or content3 =="concept" or content3 =="conception" or content3 =="specification":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                            urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/WorldLargestManufacturerSheetMetal.pdf'
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Project ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""
                        elif content3 == "professional" or content3 =="expert advice" or content3 =="advice" or content3 =="expert" or content3 =="special" or content3 =="skilled" or content3 =="help":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                            urlc = ''
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Professional ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""                                                                                                                                                            
            elif tg['tag'] == "software":
                 #noclicks = noclicks + 1             
                 if content2 == "services" or content2 == "service" :
                    if content3 == "":
                        responses = tg['responses']
                        #ans = random.choice(responses)
                        print(tg['tag']) 
                        ans = ""
                        url = 'https://www.godrej.com/What-we-do'
                        urlc = ""
                        b1 = ""
                        d1 = "Our services includes : "
                        b2 = "Process Consulting"
                        b3 = "Implementation & Global Rollout"
                        b4 = "Services Managed"
                        b5 = "Migration & Upgrade"
                        b6 = "Service - Infrastructure"
                        b7 = "Legacy modernization & DevOps"
                        b8 = "Application - Mobile "
                        b8 = "Data & Information Security "
                        bus1 = b1
                        bus2 = b2
                        bus3 = b3
                        bus4 = b4
                        bus5 = b5
                        bus6 = b6
                        bus7 = b7
                        bus8 = b8
                        print(bus1  + bus2 + bus3 + bus4)
                        cnt = ""
                        #open_web()  
                    else :
                        if content3 == "business" or content3 == "process" or content3 == "consulting":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/Microsoft-Dynamics-Brochure.pdf'
                            urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/WorldLargestManufacturerSheetMetal.pdf'
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Business Consulting ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""
                        elif content3 == "implementation" or content3 == "global" or content3 == "rollout":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                            urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/GlobalLeaderIndustrialPackagingServices_InforLN.pdf'                   
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Implementation and Global Rollout ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = "" 
                        elif content3 == "managed" or content3 == "services":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                            urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/SaudiCompanySuccessfullyImplementsLSCentralandBusinessCentral.pdf'
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Managed services ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""  
                        elif content3 == "migration" or content3 == "upgrade" or content3 =="enhance" or content3 =="advancement":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/InforBrochure.pdf'
                            urlc = ''
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Migration and Upgrade ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""   
                        elif content3 == "infrastructure":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/Microsoft-Dynamics-Brochure.pdf'
                            urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/EuropeLeadingMarineService_InforLN.pdf'
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Infrastructure as a service ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""   
                        elif content3 == "legacy" or content3 == "modernisation" or content3 == "devops" or content3 == "platform" or content3 =="engineer" or content3 =="ops" or content3 =="dev":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                            urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/saudiTradingCompany.pdf'
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Legacy Modernisation and DevOps ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = "" 
                        elif content3 == "mobile" or content3 == "mobileapp" or content3 =="app" or content3 =="app development" or content3 =="development" or content3 =="android" or content3 =="androidapp" or content3 =="ios" or content3 =="app" or content3 =="iosapp":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                            urlc = 'https://www.godrejinfotech.com/assets/pdf/case-studies/India_s_Leading_Wildlife_Nature_Conservation_Md365.pdf'
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Mobile Aplication ? "
                            b2 = " "
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""  
                        elif content3 == "data" or content3 == "information" or content3 == "security" or content3 =="data protection"  or content3 =="hacking" or content3 =="hack protection" or content3 =="hack" or content3 =="information protection" or content3 =="protection" or content3 =="security":
                            responses = tg['responses']
                            #ans = random.choice(responses)
                            print(tg['tag']) 
                            ans = ""
                            url = 'https://www.godrejinfotech.com/assets/pdf/brochures/GITL_Corporate_Brochure.pdf'
                            urlc = ''
                            b1 = ""
                            d1 = "Would yo like to see brouchers/case studies of Data and Information Security ? "
                            b2 = ""
                            b3 = ""
                            b4 = ""
                            b5 = ""
                            b6 = ""
                            b7 = ""
                            b8 = ""
                            b8 = ""
                            bus1 = b1
                            bus2 = b2
                            bus3 = b3
                            bus4 = b4
                            bus5 = b5
                            bus6 = b6
                            bus7 = b7
                            bus8 = b8
                            print(bus1  + bus2 + bus3 + bus4)
                            cnt = ""                                  
            elif tg['tag'] == "leaves":
                 Qappend=" where LoginID = '{}'".format(username)
                 SQLQuery = (Lquery + Qappend)
                 print(SQLQuery)
                 url = ""
                 cnt = ""
                 ans = ""
                 #noclicks = noclicks + 1
                # ans = connection(SQLQuery)
                 #data1 = ans
                 #data2 = ans
                 #data3 = ""
            elif tg['tag'] == "order":
                 SQLQuery = Oquery
                 url = ""
                 cnt = ""
                 ans = ""
                 #noclicks = noclicks + 1
                 #ans = connection(SQLQuery) 
                 #data1 = round(ans)
                 #data2 = round(ans)
                 #data3 = ""                       
    
    d={'ans': ans, 'dt' : dt, 'd1' : d1, 'd2' : d2, 'd3' : d3, 'd4' : d4, 'd5' : d5, 'd9' : d9, 'cntd' : cntd,'data2' : data2, 'data3' : data3, 'data4' : data4, 'data5' : data5, 'data6' : data6, 'data7' : data7, 'data8' : data8, 'data9' : data9, 'data10' : data10, 'query': query, 'url' : url, 'urlc' : urlc, 'cnt' : cnt, 'bus1' : bus1, 'bus1' : bus1, 'bus2' : bus2, 'bus3' : bus3, 'bus4' : bus4, 'bus5' : bus5, 'bus6' : bus6, 'bus7' : bus7, 'bus8' : bus8, 'bus9' : bus9}
    response = json.dumps(d)
    return JsonResponse(response,safe = False)
           	               
def connection(Squery):
    with pyodbc.connect(conx_string) as conx:
        cursor = conx.cursor()
        cursor.execute(Squery)
        data = cursor.fetchall() 
        ans2 = data
        for tpl in ans2:
            (ans1, ) = tpl
            print(ans1)
    return ans1

def connection1(Squery):
    with pyodbc.connect(conx_string) as conx:
        cursor = conx.cursor()
        cursor.execute(Squery)
        data = cursor.fetchall() 
        ans2 = data
    return ans2  

def insertdetails(Number,Name,Surname,Location) :
    with pyodbc.connect(conx_string) as conx:
        cursor = conx.cursor()
        Iquery = "INSERT INTO [dbo].[VisitorDetails] (VisitorMobile, VisitorName, VisitorSurname, VisitorLocation) VALUES('{}','{}','{}','{}')"
        IQuery = Iquery.format(Number,Name,Surname,Location)
        print(IQuery)
        cursor.execute(IQuery)     

def open_web():
    urllist = {'A':'https://www.godrej.com/careers','B':'https://www.godrej.com/What-we-do#Business-verticals'}
    url = urllist['A']
    display(Javascript('window.open("{url}");'.format(url=url)))

def get_webdata(link):
    article = Article(link)
    article.download()
    article.parse()
    article.nlp()
    data2 = article.text
    return data2

def isMobileNo(s):
    Pattern = re.compile("[7-9][0-9]{9}")
    return Pattern.match(s)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()








