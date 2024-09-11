import mysql.connector
from mysql.connector import errorcode
import pandas as pd
from pandas import DataFrame

#introface
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
print("MUSEUM 43\n")
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
print("Welcome to our online Museum Database!")
print("Before you embark on your journey to discover our objects, \nare you a guest or an employee?\n")

#checking for employee or guest
#skips guest login but asks for employee password
tries = 0
while tries < 5:
    loginpass = input("Enter Password for SQL Login Here ----> ")
    userrole = input("Type 0 for guest, or 1 for employee----> ")
    if (userrole == '0') or (userrole == '1'):
        userrole = int(userrole)
        if userrole == 0:
            tries2 = 0
            while tries2 < 5:
                loginpass = input("Enter Password for SQL Login Here ----> ")
                try:
                    cnxn = mysql.connector.connect( user='root',
                                                    password = loginpass,
                                                    host = 'localhost',
                                                    database='Museumdb' )
                    if cnxn.is_connected():
                        break
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print(f"Something is wrong with your user name or password. You have {4-tries2} tries left.")
                        tries2 += 1
                        if tries2 == 5:
                            print("You have exceeded the maximum number of attempts. Exiting program.")
                            exit()
                    else:
                        print(err)
            break
        elif userrole == 1:
            #authentication for employee
            tries2 = 0
            while tries2 < 5:
                loginpass = input("Enter Password for Employee Login Here ----> ")
                try:
                    cnxn = mysql.connector.connect( user='root',
                                                    password = loginpass,
                                                    host = 'localhost',
                                                    database='Museumdb' )
                    if cnxn.is_connected():
                        break
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print(f"Something is wrong with your user name or password. You have {4-tries2} tries left.")
                        tries2 += 1
                        if tries2 == 5:
                            print("You have exceeded the maximum number of attempts. Exiting program.")
                            exit()
                    else:
                        print(err)
            break
    elif (userrole != '0') and (userrole != '1'):
        print(f"Please enter either a 0 for guest, or a 1 for employee! You have {4-tries} tries left.")
        tries += 1
        if tries == 5:
            print("You have exceeded the maximum number of attempts. Exiting program.")
            exit()
cur = cnxn.cursor()
cur.execute('use Museumdb')
#guest privileges
if userrole == 0:
    print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
    print("Welcome to our Guest Browsing Options!")
    print("What would you like to see first? Input the number of the table you would like to see first.")
    print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
    ginput = input('\nEnter choice here---> ')
    print()

    #iterates through each Table and Value according to User input
    while ginput != '10':
        if ginput == '0':
            cur.execute('Select * From Art_Object')
            rows = cur.fetchall()
            attributes = cur.column_names
            df = pd.DataFrame(rows, columns=attributes)
            print(f'\n{df.iloc[:, :2]}')
            while True:
                gart = input("Enter the ID number of the object you would like to see (or 'exit' to go back) --> ")
                print()
                if gart.lower() == 'exit':
                    break
            
                if gart.isdigit():
                    gart = int(gart)
                    selected_object = df[df['ID_No'] == gart]
                    if not selected_object.empty:
                        print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                        for att, value in selected_object.iloc[0].items():
                            print(f'{att}: {value}')
                            print()
                        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                        break
                    else:
                        print("Invalid input. Please enter a valid ID number.")
                else:
                    print("Invalid input. Please enter a valid ID number or 'exit' to go back.")
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
            ginput = input('Enter next option choice here---> ')
            continue

        elif ginput == '1':
            cur.execute('Select * From Exhibition')
            rows = cur.fetchall()
            attributes = cur.column_names
            df = pd.DataFrame(rows, columns=attributes)
            df = df.rename(columns={'Ename': 'Name of Exhibition'})
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print(df)
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
            ginput = input('Enter next option choice here---> ')
            continue

        elif ginput == '2':
            cur.execute('Select * From Artist')
            rows = cur.fetchall()
            attributes = cur.column_names
            df = pd.DataFrame(rows, columns=attributes)
            df = df.rename(columns={'Aname': 'Artist Name'})
            print(f'\n{df.iloc[:, :2]}')
            while True:
                gart = input("Enter the name of the artist you would like to see (or 'exit' to go back) --> ")
                print()
                if gart.lower() == 'exit':
                    break
                
                selected_object = df[df['Artist Name'].str.lower() == gart.lower()]
                if not selected_object.empty:
                    print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                    for att, value in selected_object.iloc[0].items():
                        print(f'{att}: {value}')
                        print()
                    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                    break
                else:
                    print("Invalid input. Please enter a valid artist name or 'exit' to go back.")
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
            ginput = input('Enter next option choice here---> ')
            continue

        elif ginput == '3':
            cur.execute('Select * From Painting')
            rows = cur.fetchall()
            attributes = cur.column_names
            df = pd.DataFrame(rows, columns=attributes)
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print(df)
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
            ginput = input('Enter next option choice here---> ')
            continue
        
        elif ginput == '4':
            cur.execute('Select * From Statue')
            rows = cur.fetchall()
            attributes = cur.column_names
            df = pd.DataFrame(rows, columns=attributes)
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print(df)
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
            ginput = input('Enter next option choice here---> ')
            continue

        elif ginput == '5':
            cur.execute('Select * From Sculpture')
            rows = cur.fetchall()
            attributes = cur.column_names
            df = pd.DataFrame(rows, columns=attributes)
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print(df)
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
            ginput = input('Enter next option choice here---> ')
            continue

        elif ginput == '6':
            cur.execute('Select * From Other')
            rows = cur.fetchall()
            attributes = cur.column_names
            df = pd.DataFrame(rows, columns=attributes)
            df = df.rename(columns={'Otype': 'Type'})
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print(df)
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
            ginput = input('Enter next option choice here---> ')
            continue

        elif ginput == '7':
            cur.execute('Select * From Collections')
            rows = cur.fetchall()
            attributes = cur.column_names
            df = pd.DataFrame(rows, columns=attributes)
            df = df.rename(columns={'Ctype': 'Collection Type', 'Cdesc': 'Collection Description', 'Phone': 'Phone Number'})
            print(f'\n{df.iloc[:, :1]}')
            while True:
                gart = input("Enter the name of the collection you would like to see (or 'exit' to go back) --> ")
                print()
                if gart.lower() == 'exit':
                    break
                
                selected_object = df[df['Collection_name'].str.lower() == gart.lower()]
                if not selected_object.empty:
                    print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                    for att, value in selected_object.iloc[0].items():
                        print(f'{att}: {value}')
                        print()
                    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                    break
                else:
                    print("Invalid input. Please enter a valid collection name or 'exit' to go back.")
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
            ginput = input('Enter next option choice here---> ')
            continue

        elif ginput == '8':
            cur.execute('Select * From Permanent_Collection')
            rows = cur.fetchall()
            attributes = cur.column_names
            df = pd.DataFrame(rows, columns=attributes)
            df = df.rename(columns={'Pstatus': 'Status'})
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print(df)
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
            ginput = input('Enter next option choice here---> ')
            continue

        elif ginput == '9':
            cur.execute('Select * From Borrowed_Collection')
            rows = cur.fetchall()
            attributes = cur.column_names
            df = pd.DataFrame(rows, columns=attributes)
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print(df)
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
            ginput = input('Enter next option choice here---> ')
            continue

        else:
            print("\nEnter a valid option please.")
            print("0-Art Objects\n1-Exhibitions\n2-Artists\n3-Paintings\n4-Statues\n5-Scultpures\n6-Other\n7-Collections\n8-Permanent Collections\n9-Borrowed Collections\n10-Exit Program")
            ginput = input('\nEnter choice here---> ')

#employee privileges
elif userrole == 1:
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
    print("Welcome to our Employee Options!")
    print("What would you like to do first? Enter the corresponding number when asked to.")
    print("0-Add\n1-Remove\n2-Edit\n3-Exit Program")
    einput = input('\nEnter choice here---> ')
    print()
    while einput != '3':
        if einput == '0':
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("What would you like to add?")
            print("1-Add Art Object\n2-Add Collection\n3-Add Exhibition\n")
            eart = input("Enter your choice here---> ")
            if eart == '1':
                print("Disclaimer, you may write \'Null\' ONLY for artist name, and exhibition name if not known.\n")
                aoid = input("Enter 5 numbers for your art_object (XXXXX)----> ")
                atitle = input("Enter a short title for your object----> ")
                adesc = input("Enter a short description for your object---> ")
                ayear = input("Enter the year your object was created----> ")
                aepoch = input("Enter the epoch of your object---> ")
                acog = input("Enter the culture of origin of your object---> ")
                acn = input("Enter the collection name of your object---> ")
                
                cexist = "Select Collection_name From Collections Where Collection_name = %s"
                cur.execute(cexist, (acn,))
                exists = cur.fetchone()

                if not exists:
                    ct = input("Enter if your collection is \'Permanent\' or \'Borrowed\'---> ")
                    cdesc = input("Enter a short description of the collection--> ")
                    caddress = input("Enter the address of the collection--> ")
                    cphone = input("Enter the phone number of the collection in format (xxxxxxxxxx)--> ")
                    ccp = input ("Enter the current contact person name---> ")
                    insertc = """Insert Into Collections (Collection_name, Ctype, Cdesc, Address, Phone, Current_Contact_Person)
                                Values (%s,%s,%s,%s,%s,%s)"""
                    cur.execute(insertc, (acn,ct,cdesc,caddress,cphone,ccp))

                    if ct.lower()=='permanent':
                        pst = input("Enter whether your collection status is \n-is stored\n-on display\n-on loan\n---> ")
                        cost = input("Enter the cost of your collection as an integer---> ")
                        dateaq = input("Enter the date this collection was acquired in the format \'MM-DD-YYYY\'----> ")
                        insertcp = """Insert Into Permanent_Collection (Collection_name, Pstatus, Cost, Date_acquired)
                                        Values (%s,%s,%s,%s)"""
                        cur.execute(insertcp, (acn,pst,cost,dateaq))


                    elif ct.lower() == 'borrowed':
                        bf = input("Enter who this collection was borrowed from---> ")
                        db = input("Enter the date this collection was borrowed in the format \'MM-DD-YYYY\'----> ")                        
                        dr = input("Enter the date this collection was returned in the format \'MM-DD-YYYY\'----> ")
                        insertcb = """Insert Into Borrowed_Collection (Collection_name, Borrowed_from, Date_borrowed, Date_returned)
                                        Values (%s,%s,%s,%s)"""
                        cur.execute(insertcb, (acn,bf,db,dr))
                    
                    cnxn.commit()
                

                aen = input("Enter the exhibition name of your object (you may write \'Null\')---> ")
                existe = "Select Ename From Exhibition Where Ename = %s"
                cur.execute(existe, (aen,))
                existes = cur.fetchone()

                if not existes:
                    if (aen.lower()!= 'null'):
                        print("Disclaimer, you may not write \'Null\'\n")
                        endd = input("Enter the date the exhibition ended in the format \'MM-DD-YYYY\'----> ")
                        estart = input("Enter the date the exhibition started in the format \'MM-DD-YYYY\'----> ")
                        Inserte = """Insert Into Exhibition (Ename, End_date, Start_date)
                                    Values (%s,%s,%s)"""
                        cur.execute(Inserte, (aen,endd,estart))
                        cnxn.commit()
                

                aan = input("Enter the artist name of your object (you may write \'Null\')---> ")
                if (aan.lower()!= 'null'):
                    print("Disclaimer, you may write \'Null\' ONLY for date died, and date born if not known.\n")
                    ad = input("Enter a very short description of the artist--> ")
                    aacog = input("Enter the culture of origin of the artist---> ")
                    aaepoch = input("Enter the epoch of the artist---> ")
                    ams = input("Enter the main style of the artist---> ")
                    aadd = input("Enter the date the artist died in the format \'MM-DD-YYYY\'(you may write \'Null\')----> ")
                    aadb = input("Enter the date the artist was born in the format \'MM-DD-YYYY\'(you may write \'Null\')----> ")
                    Inserta = """ Insert Into Art_Object (ID_No, Title, Descript, Yearcr, Epoch, Culture_of_origin, Collection_name, Exhibition_name)
                                    Values (%s,%s,%s,%s,%s,%s,%s,%s)"""
                    cur.execute(Inserta, (aoid, atitle, adesc, ayear, aepoch, acog, acn, aen))
                    Insertaa = """Insert Into Artist (Aname, Obj_ID, Adescription, Country_of_origin, Epoch, main_style, Date_died, Date_born)
                                    Values (%s,%s,%s,%s,%s,%s,%s,%s)"""
                    cur.execute(Insertaa, (aan,aoid,ad,aacog,aaepoch,ams, aadd, aadb))

                    updatea = """Update Art_Object Set Artist_name = %s Where ID_No = %s"""
                    cur.execute(updatea, (aan,aoid))
                    cnxn.commit()

                elif (aan.lower() == 'null'):
                    Inserta = """ Insert Into Art_Object (ID_No, Title, Descript, Yearcr, Epoch, Culture_of_origin, Collection_name, Exhibition_name)
                                    Values (%s,%s,%s,%s,%s,%s,%s,%s)"""
                    cur.execute(Inserta, (aoid,atitle,ad,ayear,aepoch,acog,acn,aen))
                    cnxn.commit()
                
                atype = input("Enter if your object is either a:\n\'Statue\'\n\'Sculpture\'\n\'Painting\'\n\'Other\'\nEnter choice here (You may not write \'Null\')---> ")
                
                while 1: 
                    if atype.lower() == 'statue':
                        sts = input("Enter the style of the statue---> ")
                        stw = input("Enter the weight of the statue in pounds(lb) as an integer---> ")
                        sth = input("Enter the height of the statue in centimetres(cm) as an integer---> ")
                        stm = input("Enter the material used to make the statue---> ")

                        Insertst = """Insert Into Statue (ID_no, Style, Weight_lb, Height_cm, Material)
                                    Values (%s,%s,%s,%s,%s)"""
                        cur.execute(Insertst, (aoid, sts, stw, sth, stm))
                        cnxn.commit()
                        
                        print("Art Object added successfully")
                        break
                    
                    elif atype.lower() == 'sculpture':
                        scs = input("Enter the style of the sculpture---> ")
                        scw = input("Enter the weight of the sculpture in pounds(lb) as an integer---> ")
                        sch = input("Enter the height of the sculpture in centimetres(cm) as an integer---> ")
                        scm = input("Enter the material used to make the sculpture---> ")

                        Insertsc = """Insert Into Sculpture (ID_no, Style, Weight_lb, Height_cm, Material)
                                    Values (%s,%s,%s,%s,%s)"""
                        cur.execute(Insertsc, (aoid, scs, scw, sch, scm))
                        cnxn.commit()

                        print("Art Object added successfully")
                        break
                    
                    elif atype.lower() == 'painting':
                        pt = input("Enter the type of paint used---> ")
                        pst = input("Enter the style of the painting---> ")
                        pdo = input("Enter what th painting was drawn on---> ")

                        Insertp = """Insert Into Painting (ID_no, Paint_Type, Style, Drawn_on)
                                    Values (%s,%s,%s,%s)"""
                        cur.execute(Insertp, (aoid, pt, pst, pdo))
                        cnxn.commit()

                        print("Art Object added successfully")
                        break
                    
                    elif atype.lower() == 'other':
                        ot = input("Enter the type of this \'other\' art object---> ")
                        os = input("Enter the style of this \'other\' art object---> ")

                        Inserto = """Insert Into Other (ID_no, Otype, Style)
                                    Values (%s,%s,%s)"""
                        cur.execute(Inserto, (aoid, ot, os))
                        cnxn.commit()

                        print("Art Object added successfully")
                        break
                   
                    else:
                        print("Please make sure your spelling is correct and enter a valid option")
                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                print("What would you like to do next? Enter the corresponding number when asked to.")
                print("0-Add\n1-Remove\n2-Edit\n3-Exit Program")
                einput = input('\nEnter choice here---> ')
                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

            elif eart == '2':
                acn = input("Enter the collection name of your object---> ")
                cexist = "Select Collection_name From Collections Where Collection_name = %s"
                cur.execute(cexist, (acn,))
                exists = cur.fetchone()

                if not exists:
                    ct = input("Enter if your collection is \'Permanent\' or \'Borrowed\'---> ")
                    cdesc = input("Enter a short description of the collection--> ")
                    caddress = input("Enter the address of the collection--> ")
                    cphone = input("Enter the phone number of the collection in format (xxxxxxxxxx)--> ")
                    ccp = input ("Enter the current contact person name---> ")
                    insertc = """Insert Into Collections (Collection_name, Ctype, Cdesc, Address, Phone, Current_Contact_Person)
                                Values (%s,%s,%s,%s,%s,%s)"""
                    cur.execute(insertc, (acn,ct,cdesc,caddress,cphone,ccp))

                    if ct.lower()=='permanent':
                        pst = input("Enter whether your collection status is \n-is stored\n-on display\n-on loan\n---> ")
                        cost = input("Enter the cost of your collection as an integer---> ")
                        dateaq = input("Enter the date this collection was acquired in the format \'MM-DD-YYYY\'----> ")
                        insertcp = """Insert Into Permanent_Collection (Collection_name, Pstatus, Cost, Date_acquired)
                                        Values (%s,%s,%s,%s)"""
                        cur.execute(insertcp, (acn,pst,cost,dateaq))


                    elif ct.lower() == 'borrowed':
                        bf = input("Enter who this collection was borrowed from---> ")
                        db = input("Enter the date this collection was borrowed in the format \'MM-DD-YYYY\'----> ")                        
                        dr = input("Enter the date this collection was returned in the format \'MM-DD-YYYY\'----> ")
                        insertcb = """Insert Into Borrowed_Collection (Collection_name, Borrowed_from, Date_borrowed, Date_returned)
                                        Values (%s,%s,%s,%s)"""
                        cur.execute(insertcb, (acn,bf,db,dr))
                    
                    cnxn.commit()
                else:
                    print("Collection is already in the database")
                
                print("Collection Successfully Added")
                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                print("What would you like to do next? Enter the corresponding number when asked to.")
                print("0-Add\n1-Remove\n2-Edit\n3-Exit Program")
                einput = input('\nEnter choice here---> ')
                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                 
            elif eart == '3':
                aen = input("Enter the exhibition name of your object (you may not write \'Null\')---> ")
                existe = "Select Ename From Exhibition Where Ename = %s"
                cur.execute(existe, (aen,))
                existes = cur.fetchone()

                if not existes:
                    if (aen.lower()!= 'null'):
                        print("Disclaimer, you may not write \'Null\'\n")
                        endd = input("Enter the date the exhibition ended in the format \'MM-DD-YYYY\'----> ")
                        estart = input("Enter the date the exhibition started in the format \'MM-DD-YYYY\'----> ")
                        Inserte = """Insert Into Exhibition (Ename, End_date, Start_date)
                                    Values (%s,%s,%s)"""
                        cur.execute(Inserte, (aen,endd,estart))
                        cnxn.commit()
                
                else:
                    print("Exhibition is already in the database")
                
                print("Exhibition Successfully Added")
                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                print("What would you like to do next? Enter the corresponding number when asked to.")
                print("0-Add\n1-Remove\n2-Edit\n3-Exit Program")
                einput = input('\nEnter choice here---> ')
                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
        
        elif einput == '1':
            print("What would you like to remove")
            print("1-Art Object\n2-Collection\n3-Exhibition")
            eart = input("Enter number of choice here---> ")
            if eart == '1':
                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                cur.execute('Select * From Art_Object')
                rows = cur.fetchall()
                attributes = cur.column_names
                df = pd.DataFrame(rows, columns=attributes)
                print(f'\n{df.iloc[:, :2]}')

                print("Which object would you like to remove? Enter the corresponding number when asked to.")
                artoid = input('\nEnter object ID here---> ')

                artexists = f"Select Aname From Artist Where Obj_ID = {artoid}"
                cur.execute(artexists)
                allartist = cur.fetchall()
                if allartist:
                    for artist in allartist:
                        aname = artist[0]
                        reartist = f"Delete From Artist Where aname = {aname}"
                        cur.execute(reartist)
                        cnxn.commit()

                reart = f"Delete From Art_Object Where ID_No = {artoid}"
                cur.execute(reart)
                cnxn.commit()
            
                print("Object Deleted successfully, along with associated Artist")

                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                print("What would you like to do next? Enter the corresponding number when asked to.")
                print("0-Add\n1-Remove\n2-Edit\n3-Exit Program")
                einput = input('\nEnter choice here---> ')
                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

            elif eart == '2':
                cur.execute('Select * From Collections')
                rows = cur.fetchall()
                attributes = cur.column_names
                df = pd.DataFrame(rows, columns=attributes)
                df = df.rename(columns={'Ctype': 'Collection Type', 'Cdesc': 'Collection Description', 'Phone': 'Phone Number'})
                print(f'\n{df.iloc[:, :1]}')

                print("Which collection would you like to remove? Enter the corresponding name when asked to.")
                rcname = input('\nEnter collection name here---> ')

                dcname = f"Delete From Collections Where Collection_name = {rcname}"
                cur.execute(dcname)
                cnxn.commit()
            
                print("Collection Deleted successfully, along with associated Artist")

                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                print("What would you like to do next? Enter the corresponding number when asked to.")
                print("0-Add\n1-Remove\n2-Edit\n3-Exit Program")
                einput = input('\nEnter choice here---> ')
                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

            elif eart == '3':
                cur.execute('Select * From Exhibition')
                rows = cur.fetchall()
                attributes = cur.column_names
                df = pd.DataFrame(rows, columns=attributes)
                df = df.rename(columns={'Ename': 'Name of Exhibition'})
                print(df)

                print("Which exhibition would you like to remove? Enter the corresponding name when asked to.")
                rename = input('\nEnter exhibition name here---> ')

                dename = f"Delete From Exhibition Where Ename = {rename}"
                cur.execute(dename)
                cnxn.commit()
            
                print("Exhibition Deleted successfully, along with associated Artist")

                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
                print("What would you like to do next? Enter the corresponding number when asked to.")
                print("0-Add\n1-Remove\n2-Edit\n3-Exit Program")
                einput = input('\nEnter choice here---> ')
                print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

        elif einput == '2':
            print("This area of the website is under maintenance!!!")
            print("Meant for Updating Specific Values")
            print("Please wait until ENSF 300 Marks are released to begin updating values")
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("What would you like to do next? Enter the corresponding number when asked to.")
            print("0-Add\n1-Remove\n2-Edit\n3-Exit Program")
            einput = input('\nEnter choice here---> ')
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
        
        else:
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
            print("\nEnter a valid option please.")
            print("0-Add\n1-Remove\n2-Edit\n3-Exit Program")
            einput = input('\nEnter choice here---> ')
            print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

cur.close()
cnxn.close()