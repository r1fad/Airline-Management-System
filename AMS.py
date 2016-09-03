import time
import os
import random
import getpass
def BookFlight():#User
    class Passenger():#Used to define Passenger objects
        def __init__(self):
            self.fname=None
            self.lname=None
            self.phone=None
            self.age=None
            self.address=None
            self.email=None
            self.mpref=None
            self.price=0
            self.classtype=None
            self.bookref=0
        def Input(self):
            self.fname=raw_input("First Name:")
            self.lname=raw_input("Last Name:")
            self.phone=raw_input("Phone:")
            self.age=raw_input("Age:")
            self.address=raw_input("Address:")
            self.email=raw_input("Email ID:")
            self.mpref=raw_input("Meal Preference:")
            con=True
            while con==True:
                self.classtype=raw_input("Preffered Class(First/Business/Economy):")
                con=self.PriceAssign()
            self.bookref=BookRefGen()
        def PriceAssign(self):#Assigns price based on which Class user has selected
            self.classtype1=self.classtype.lower()
            if self.classtype1=='economy':
                if self.age>=12:
                    self.price=3000
                elif self.age<12 and self.age>=2:
                    self.price=2500
                elif self.age<2 and self.age>=0:
                    self.price=1500
                return False
            elif self.classtype1=='business':
                self.price=1000
                if self.age>=12:
                    self.price+=3000
                elif self.age<12 and self.age>=2:
                    self.price+=2500
                elif self.age<2 and self.age>=0:
                    self.price+=1500
                return False
            elif self.classtype1=='first':
                self.price=2000
                if self.age>=12:
                    self.price+=3000
                elif self.age<12 and self.age>=2:
                    self.price+=2500
                elif self.age<2 and self.age>=0:
                    self.price+=1500
                return False
            else:
                print 'Invalid class, enter again'
                return True
    n=input("Enter number of passengers")
    plist=[]
    for i in range(n):
        x=Passenger()
        print "Enter information for passenger number"+" "+str(i+1)
        x.Input()
        plist.append(x)
        os.system('cls')
    IniPrice=0
    tax=840
    for i in range(n):#Price Calculation
        IniPrice=int(IniPrice)+int(plist[i].price)+int(tax)
    TotPrice=int(IniPrice)
    print "Fare for"+' '+str(n)+' '+"passenger(s):",str(TotPrice)
    for i in range(n):
        print 'Booking Reference Number for'+' '+str(plist[i].fname)+' '+str(plist[i].lname)+':'+''+str(plist[i].bookref)
    print
    print 'Please note down the reference numbers for cancellation and confirmation purpose'
    print
    for i in range(n):#Writing information to the file
        '''
        The following code is the reason why the PNR looks neat and organised
        '''
        p1=str(plist[i].bookref)#Start
        flightinfo.write(p1)
        flightinfo.seek(12,1)
        p2=str(plist[i].fname)
        flightinfo.write(p2)
        x=int(10-len(p2))
        x=x+9
        flightinfo.seek(x,1)
        p3=str(plist[i].lname)
        flightinfo.write(p3)
        x=int(9-len(p3))                      
        x=x+4
        flightinfo.seek(x,1)
        p7=str(plist[i].age)
        flightinfo.write(p7)
        x=int(3-len(p7))
        x=x+5
        flightinfo.seek(x,1)
        p4=str(plist[i].phone)
        flightinfo.write(p4)
        if len(p4)<8:
            x=(5-len(p4))
            x=x+10
            flightinfo.seek(x,1)
        else:
            flightinfo.seek(7,1)
        p5=str(plist[i].mpref)
        flightinfo.write(p5)
        x=int(10-len(p5))
        x=x+9
        flightinfo.seek(x,1)
        p6=str(plist[i].classtype)+'\n'
        flightinfo.write(p6)#End
    flightinfo.close()
    ex=raw_input("Press Enter to continue")
    os.system('cls')
    return TotPrice    
def BookRefGen():#Ticket reference number generator
    l1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    l2=[]
    for i in range(5):
        n=random.randint(0,35)
        l2.append(n)
    ref=''
    for i in range(5):
        ref=ref+l1[l2[i]]#generate reference number
    return ref
def FleetStatus():#Admin
    def timen():#generates time at that instant
        x=0
        import datetime
        c=True
        while c==True:
            p= datetime.datetime.now()
            p=str(p)
            length=len(p)
            x=0
            for i in p:
                if i==' ':
                    lint=p[x:length]
                x=x+1
            count=0
            for j in lint:
                if j=='.':
                    timen=lint[0:count]
                    return timen
                count=count+1
    n1='QR'
    countries=['Colombo','Doha','Dubai','Muscat','Riyadh','Jeddah','Tokyo', 'Seoul', 'Shanghai', 'Karachi', 'Delhi', 'Beijing', 'Mumbai', 'New York','Moscow', 'Osaka', 'Cairo', 'Kolkata', 'Istanbul', 'London', 'Los Angeles', 'Buenos Aires', 'Dhaka', 'Paris', 'Rio De Janeiro', 'Manila', 'Lahore']
    l2=['1','2','3','4','5','6','7','8','9','0']
    c=0
    LaBoa=[]#will store all flights whose status is 'Landed' or 'Boarding'
    var='x'
    while var=='x':
        r=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,len(countries)-1)]
        s=["Departed","Landed","Now Boarding","Delayed","Diverted"]
        n=random.randint(0,4)
        a=n1+l2[r[0]]+l2[r[1]]+l2[r[2]]+' '+s[n]+' '+'at'+' '+countries[r[3]]
        b=n1+l2[r[0]]+l2[r[1]]+l2[r[2]]
        var1=random.randint(0,1)
        if n==0:
            timet=timen()
            print b+' '+'Departed from'+' '+countries[r[3]]+' '+str(timet)
            c=c+1
            time.sleep(1.5)
        elif n==1:
            timet=timen()
            print a+' '+str(timet)
            c=c+1
            f1=b+' '+'Now Boarding at'+' '+countries[r[3]]
            LaBoa.append(f1)
            f2=b+' '+'Departed from'+' '+countries[r[3]]
            LaBoa.append(f2)
            time.sleep(1.5)
        elif n==2:
            timet=timen()
            print a+' '+str(timet)
            c=c+1
            f2=b+' '+'Departed from'+' '+countries[r[3]]
            LaBoa.append(f2)
            time.sleep(1.5)
        elif n==4:
            timet=timen()
            print b+' '+'Diverted to'+' '+countries[r[3]]+' '+str(timet)
            c=c+1
            time.sleep(1.5)
        else:
            timet=timen()
            print a+' '+str(timet)
            c=c+1
            time.sleep(1.5)
        if var1==1:
            try:
                timet=timen()
                print LaBoa[0]+' '+str(timet)
                c=c+1
                LaBoa.remove(LaBoa[0])
                time.sleep(1.5)
            except IndexError:
                pass
        if c%10==0:
            os.system('cls')
            print "------------------Fleet Status------------------"
        if c%20==0:
            c=0
            os.system('cls')
            ask=raw_input("Do you wish to continue?(Y/N)")
            ask=ask.upper()
            if ask =='Y':
                os.system('cls')
                print "------------------Fleet Status------------------"
            elif ask=='N':
                os.system('cls')
                var='y'
                break
        else:
            var=='x'
def DeleteReservation():#User
    fno=raw_input("Flight Number:")
    refno=raw_input("Enter your booking reference number:")
    FareSubtraction(fno,refno)#Calling function to subtract the money from total fare of flight
    open1=str(fno)+'.txt'
    reflist=[]
    try:
        fobj=open(open1,'r')
        f1=fobj.readline()
        while f1:
            chk=f1[0:5]
            reflist.append(chk)
            f1=fobj.readline()
        fobj.close()
        fobj=open(open1,'r+')
        conf=0
        if refno in reflist:
            temp=open('temp.txt','w')
            conf=1
            f1=fobj.readline()
            while f1:
                chk=f1[0:5]
                if refno==chk:
                    f1=fobj.readline()
                else:
                    temp.write(f1)
                    f1=fobj.readline()
            fobj.close()
            os.remove(open1)
            temp.close()
            temp=open('temp.txt','r+')
            cont=temp.readlines()
            cont1=[]
            for i in range(0,7):
                cont1.append(cont[i])
            for i in range(7,len(cont)):
                if cont[i]!='\n':
                    cont1.append(cont[i])
            temp.seek(0,0)
            temp.writelines(cont1)
            temp.close()
            os.rename('temp.txt',open1)
        else:
            conf=2
            print 'Reference number not found'
        if conf==1:
            print "Your reseravation has been cancelled"
            ent=raw_input("Press enter to continue")
        elif conf==2:
            time.sleep(2)
    except IOError:
        print 'No such flight exists'
        time.sleep(2)
    os.system('cls')
def FareCalculation(flname,totPrice):#Used to calculate the total amount of money generated by flight.Called whenever a booking is made
    file1=open(flname,'r+')
    l1=file1.readlines()
    file1.seek(0,0)
    p=l1[5]
    cfare=p[23::]
    cfare=int(cfare)
    cfare=cfare+totPrice
    pmod='Total fare for flight: '+str(cfare)+'\n'
    l1[5]=pmod
    file1.writelines(l1)
    file1.close()
def BoardingPass(fno,refno):#Prints boarding pass
    try:
        fno=str(fno)+'.txt'
        myfile=open(fno,'r')
        l=myfile.readlines()
        l1=l[1].split()
        l2=l[2].split()
        l3=l[3].split()
        x=None
        confirm=False
        for i in range(len(l)):
            if refno in l[i]:
                a=l[i]
                a=a.split(" ")
                x=[]
                for i in range(len(a)):
                    a[i]=a[i].replace('\x00',' ')
                    a[i]=a[i].strip()
                    a[i]=a[i].split()     
                for i in range(2):
                    t=a[i]
                    for j in range(len(t)):
                        x.append(t[j])    
                print "Booking confirmed, Below is your Boarding Pass. Seat will be assigned at the airport"
                print
                print l1[0],l1[1]
                print l2[0],l2[1]
                print l3[0],l3[1]
                print
                print "Reference Number:",x[0]
                print "Name:"+' '+x[1]+" "+x[2]
                print "Meal Preference:"+' '+x[5]+' '+x[6]
                print "Class:",x[7]
                if x[7]=="First":
                    print "Baggage Allowance: 50kgs"
                elif x[7]=="Business":
                    print "Baggage Allowance: 40 kgs"
                elif x[7]=="Economy":
                    print "Baggage Allowance: 30kgs"
                print
                confirm=True
                break
            else:
                confirm=False
        if confirm==True:
            pass
        else:
            print "Reference Number not found"
        myfile.close()
    except IOError:
        print "Flight does not exist"
    
    ent=raw_input("Press enter to continue")
    os.system('cls')
def FareSubtraction(fname,refno):#Will subtract the price of 1 passenger based on his class from the total fare of the flight
    economy={"Adults":3000,"Children":2500,"Infants":1500}
    business={"Adults":4000,"Children":3500,"Infants":2500}
    first={"Adults":5000,"Children":4500,"Infants":3500}
    tax=840
    fname=str(fname)+'.txt'
    file1=open(fname,"r+")
    l1=file1.readlines()
    file1.seek(0,0)
    p=l1[5]
    cfare=p[23::]
    cfare=int(cfare)
    pos=0
    for i in range(len(l1)):
        if refno in l1[i]:
            pos=i
            rec=l1[pos].split()
            rec1=[]
            for i in range(len(rec)):
                rec[i]=rec[i].replace('\x00',' ')
                rec1=rec1+rec[i].split()
            age=rec1[3]
            if rec1[-1]=='First':
                if age>=12:
                    pricesub=first["Adults"]+tax
                elif age<12 and age>=2:
                    pricesub=first["Children"]+tax
                elif age<2 and age>=0:
                    pricesub=first["Infants"]+tax
            elif rec1[-1]=='Business':
                if age>=12:
                    pricesub=business["Adults"]+tax
                elif age<12 and age>=2:
                    pricesub=business["Children"]+tax
                elif age<2 and age>=0:
                    pricesub=business["Infants"]+tax
            elif rec1[-1]=='Economy':
                if age>=12:
                    pricesub=economy["Adults"]+tax
                elif age<12 and age>=2:
                    pricesub=economy["Children"]+tax
                elif age<2 and age>=0:
                    pricesub=economy["Infants"]+tax
            cfare=cfare-pricesub
            ncfare="Total fare for flight:"+' '+str(cfare)+'\n'
            l1[5]=ncfare
            file1.writelines(l1)
            file1.seek(0,0)
            file1.close()
            break
    else:
        pass    
def CFlightPlan():#Admin
    class Flight:#Used to create flight objects
        def __init__(self):
            self.fname='Qatar Airways'
            self.fno="QR100"
            self.ftype=""
            self.atime=0.0
            self.dtime=0.0
            self.dur=None
            self.destination=""
            self.origin=""
            self.ddate=""
            self.adate=""
            self.chk=1
            self.pcap=0
            self.alist=[]
            self.dlist=[]
        def Input(self):
            self.fno= raw_input("Flight Number:")
            self.ftype= raw_input("Aircraft Type:")
            self.ddate=raw_input("Departure date(dd/mm/yyyy):")
            self.dtime= raw_input("Departure time:")
            self.adate=raw_input("Arrival date(dd/mm/yyyy):")
            self.atime= raw_input("Arrival time:")
            self.dur=raw_input("Duration(hrs/mins):")
            self.origin= raw_input("Origin:")
            self.origin=self.origin.replace(" ","")
            self.destination= raw_input("Destination:")
            self.destination=self.destination.replace(" ","")
            self.pcap=self.FlightCapacityAssign(self.ftype)#Assigns number of passengers in the aircraft
            self.compare()#check for any wrong dates
        def compare(self):
            self.alist=self.adate.split('/')
            self.dlist=self.ddate.split('/')        
            self.true=self.alist[2]==self.dlist[2] and self.alist[1]==self.dlist[1]
            if (self.alist[2]<self.dlist[2]):
                self.chk=1            
            elif (self.alist[2]==self.dlist[2] and self.alist[1]<self.dlist[1]):            
                self.chk=1
            elif (self.true and self.alist[0]<self.dlist[0]):            
                self.chk=1
            else:
                self.chk=0
        def FlightCapacityAssign(self,ftype):
            PCap={'A320':150,'A321':220,'A330':250,'A340':350,'A350':270,'A380':544,'B737':120,'B747':416,'B767':181,'B777':314,'B787':210}
            if ftype in PCap:
                return PCap[ftype]
            else:
                cap=input("Enter flight capacity(number of passengers):")
                return cap 
    p=Flight()#Object defined
    p.Input()
    dchk=False
    while dchk==False:#Checks for inconsistency of dates, example: arrival date is before departure date
        if p.chk==1:
            os.system('cls')
            print 'Flaw detected in arrival and departure dates'
            print 'Please reenter the dates'
            ent=raw_input("press Enter to continue")
            p.ddate=raw_input("Enter Departure Date:")
            p.adate=raw_input("Enter Arrival Date:")
            p.compare()
            dchk=False
        else:
            dchk=True
            break
    if dchk==True:#Works only if dates are consistent
        fname=str(p.fno)+'.txt'
        myfile=open(fname,'a+')#stores flight details and details of passenger
        avflights=open("Available Flights.txt",'a+')#stores available flights
        av=str(p.fno)+' '+'from'+' '+str(p.origin)+' '+'to'+' '+str(p.destination)+','+'Depart:'+''+str(p.ddate)+' '+'at'+' '+str(p.dtime)+','+'Arrive:'+''+str(p.adate)+' '+'at'+' '+str(p.atime)+'\n'#text to write in avflights
        avflights.write(av)#writing to available flights.txt
        avflights.close()
        f1='Airline:'+''+str(p.fname)+'   '+'Flight Number:'+''+str(p.fno)+'  '+'Flight Type:'+''+str(p.ftype)+'\n'
        f2='Origin:'+''+str(p.origin)+'  '+'Destination:'+''+str(p.destination)+'\n'
        f3='DepartureDate:'+''+str(p.ddate)+'  '+'DepartureTime:'+''+str(p.dtime)+'\n'
        f4='ArrivalDate:'+''+str(p.adate)+'  '+'ArrivalTime:'+''+str(p.atime)+'\n'
        f5='Duration:'+''+str(p.dur)+'  '+'Capacity:'+''+str(p.pcap)+' '+'passengers'+'\n'
        f6='Total fare for flight: '+'0'+'\n'
        f7='\n'
        info=[f1,f2,f3,f4,f5,f6,f7]
        myfile.writelines(info)#Writing flight info to file
        h1='BookRef'+'          '+'FirstName'+'          '+'LastName'+'     '+'Age'+'     '+'Phone'+'          '+'MealPref.'+'          '+'ClassType'+'\n'
        h2='----------------------------------------------------------------------------------------------------------'+'\n'
        myfile.write(h1)
        myfile.write(h2)
        myfile.close()
        os.system('cls')
        #Creating return flight
        if p.origin=="Doha":
            ask=raw_input("Do you wish to create the return flight(Y/N):")
            ask=ask.upper()
            if ask=='Y':
                os.system('cls')
                pR=Flight()#return flight created
                pR.destination=p.origin
                pR.origin=p.destination
                pR.fno=raw_input("Enter flight number:")
                pR.ftype=p.ftype
                pR.ddate=raw_input("Departure Date(dd/mm/yyy:")
                pR.adate=raw_input("Arrival Date(dd/mm/yyy:")
                pR.dtime=raw_input("Departure Time:")
                pR.atime=raw_input("Arrival Time:")
                pR.dur=p.dur
                pR.pcap=p.pcap
                f1='Airline:'+''+str(pR.fname)+'   '+'Flight Number:'+''+str(pR.fno)+'  '+'Flight Type:'+''+str(pR.ftype)+'\n'
                f2='Origin:'+''+str(pR.origin)+'  '+'Destination:'+''+str(pR.destination)+'\n'
                f3='DepartureDate:'+''+str(pR.ddate)+'  '+'DepartureTime:'+''+str(pR.dtime)+'\n'
                f4='ArrivalDate:'+''+str(pR.adate)+'  '+'ArrivalTime:'+''+str(pR.atime)+'\n'
                f5='Duration:'+''+str(pR.dur)+'  '+'Capacity:'+''+str(pR.pcap)+' '+'passengers'+'\n'
                f6='Total fare for flight: '+'0'+'\n'
                f7='\n'
                info=[f1,f2,f3,f4,f5,f6,f7]
                avflights=open("Available Flights.txt",'a+')#stores available flights
                av=str(pR.fname)+', '+str(pR.fno)+' '+'from'+' '+str(pR.origin)+' '+'to'+' '+str(pR.destination)+','+'Depart:'+''+str(pR.ddate)+' '+'at'+' '+str(pR.dtime)+','+'Arrive:'+''+str(pR.adate)+' '+'at'+' '+str(pR.atime)+'\n'#text to write in avflights
                avflights.write(av)#writing return flight to available flights.txt
                avflights.close()
                frname=pR.fno+'.txt'
                myfiler=open(frname,'w')#creating return flight file
                myfiler.writelines(info)
                h1='BookRef'+'          '+'FirstName'+'          '+'LastName'+'     '+'Age'+'     '+'Phone'+'          '+'MealPref.'+'          '+'ClassType'+'\n'
                h2='---------------------------------------------------------------------------------------------------------'+'\n'
                myfiler.write(h1)
                myfiler.write(h2)
                myfiler.close()
                os.system('cls')
            elif ask=='N':
                os.system('cls')
        os.system('cls')
def DFlightPlan():#Admin, deletes flight plan
    try:
        avflights=open('Available Flights.txt','r')
        fnolist=[]
        f=avflights.readline()
        while f:
            no=f[0:5]
            fnolist.append(no)
            f=avflights.readline()
        avflights.close()
        if fnolist!=[]:
            print 'Available Flights:'
            for i in fnolist:
                print i
            fno=raw_input("Enter flight number to cancel:")
            fno1=str(fno)+'.txt'
            os.system('cls')
            avflights=open('Available Flights.txt','r')
            if fno in fnolist:
                tempo=open('temp.txt','w')
                l1=avflights.readline()
                while l1:
                    chk=l1[0:5]
                    if chk!=str(fno):
                        tempo.write(l1)
                        l1=avflights.readline()
                    else:
                        l1=avflights.readline()
                avflights.close()
                os.remove('Available Flights.txt')
                tempo.close()
                os.rename('temp.txt','Available Flights.txt')
                print 'Flight cancelled'
                time.sleep(2)
                os.system('cls')
                try:
                    os.remove(fno1)
                except:
                    time.sleep(1)
            else:
                print 'No such flight exists'
                time.sleep(2)
                os.system('cls')
        else:
            print 'No Flight Plans filed'
            time.sleep(2)
            os.system('cls')
    except IOError:
        print 'No Flight Plans filed'
        time.sleep(2)
        os.system('cls')
def DisplayFlight():#Admin, displays all passengers on the flight
    fno=raw_input("Enter flight number:")
    fno1=str(fno)+'.txt'
    try:
        dflight=open(fno1,'r')
        l=dflight.readlines()
        os.system('cls')
        for i in l:
            print i
        ent=raw_input("Press Enter to continue")
        os.system('cls')
        dflight.close()
    except IOError:
        print "Flight doesn't exist"
        time.sleep(2)
        os.system('cls')
#Coding for menu
username='fd945'
password='drs12d'
import string
c='True'
while c=='True':
    print "Welcome to Qatar Airways Airline Management System"
    print
    print "For bookings and other related options, press 1"
    print "For Flight Dispatcher, press 2"
    print "To close the program, press 3"
    print
    opt=raw_input("Enter your choice:") #getting the choice
    os.system("cls")
    if opt=='1': 
        cont='True'
        while cont=='True':
            print "Thank you for choosing to fly with Qatar Airways"
            print
            print "To book a flight, press 1"
            print "To cancel your reservation, press 2"
            print "To display your boarding pass, press 3"
            print "To exit, press 4"
            print
            choice=raw_input("Enter your choice")
            if choice=='1':
                os.system('cls')
                try:
                    avflights=open('Available Flights.txt','r')
                    LF=avflights.readlines()
                    if LF!=[]:
                        print 'Available Flights'
                        print
                        for i in range(len(LF)):
                            print LF[i]#Prints all available flights
                        print
                        optf=raw_input("Enter flight number:")
                        openfinfo=str(optf)+'.txt'
                        try:
                            flightinfo=open(openfinfo,'r+')
                            flightinfo.seek(0,2)
                            os.system('cls')
                            price=BookFlight()
                            FareCalculation(openfinfo,price)
                        except IOError:
                            print "No such flight exist"
                            time.sleep(2)
                            os.system('cls')
                    else:
                        print 'No Flights available'
                        time.sleep(2)
                        os.system('cls')
                except IOError:
                    print 'Flight Plans not found, please contact Flight Dispatch'
                    time.sleep(2)
                    os.system('cls')
           
            elif choice=='2':
                os.system('cls')
                print "Please have your flight number and booking reference number with you"
                time.sleep(1)
                DeleteReservation()
            elif choice=='3':
                os.system('cls')
                print "Please have your flight number and booking reference number with you"
                time.sleep(1)
                fno=raw_input("Please enter flight number:")
                refno=raw_input("Please enter your booking reference number:")
                os.system('cls')
                BoardingPass(fno,refno)
            elif choice=='4':
                os.system('cls')
                break
            else:
                print "Enter a valid option"
                cont="True"
                os.system('cls')
    elif opt=='2':
        user=raw_input("Enter Username:")
        pass1=getpass.getpass(prompt='Enter Password:')
        if user==username and pass1==password:
            os.system('cls')
            cont='True'
            while cont=="True":
                print 'Qatar Airways Flight Dispatch'
                print 
                print "1.File a Flight Plan"
                print "2.Delete Flight Plan"
                print "3.Display PNR for particular flight"
                print "4.View Fleet Status"
                print "5.Exit"
                print
                opt=raw_input("Enter your option:")
                if opt=='1':
                    os.system('cls')
                    CFlightPlan()
                elif opt=='2':
                    os.system('cls')
                    DFlightPlan()
                elif opt=='3':
                    os.system('cls')
                    DisplayFlight()
                elif opt=='5':
                    cont=='False'
                    os.system('cls')
                    break
                elif opt=='4':
                    os.system('cls')
                    print "------------------Fleet Status------------------"
                    FleetStatus()
                else:
                    print "Enter valid option:"
                    cont=='True'
                    os.system('cls')
        else:
            print "Username or Password is wrong"
            time.sleep(2)
            os.system('cls')
    elif opt=='3':
        break
    else:
        print "Enter a valid option"
        time.sleep(1)
        os.system('cls')
        c="True"
ent=raw_input("Press Enter to close")
    
