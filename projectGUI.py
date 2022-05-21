import mysql.connector as sqltor
import PySimpleGUI as sg
conn=sqltor.connect(host='localhost',user='root',password=password,db='COVID')
cur=conn.cursor()
cur.execute("create database if not exists COVID;")
cur.execute("USE COVID")
cur.execute("CREATE TABLE IF NOT EXISTS vaccine (vname CHAR(100) PRIMARY KEY, vcountry CHAR(50), quantity int, Refill datetime default now());")
cur.execute("CREATE TABLE IF NOT EXISTS patient (eid INT PRIMARY KEY, patname CHAR(100) not null, DOV1 date,DOV2 date,vname char(100), booster char(1))")
cur.execute("CREATE TABLE IF NOT EXISTS variant (cid INT PRIMARY KEY auto_increment,cname CHAR(100),DOO date) auto_increment=1")
cur.execute("CREATE TABLE IF NOT EXISTS infected (iid INT PRIMARY KEY auto_increment,pname CHAR(100) not null,DOP date,eid INT not null) auto_increment=1")
def a():
                layout=[   [sg.Text("a)Check Vaccine Records\nb)Check Vaccinated Records\nc)Go back")],
                           [sg.Text("Enter Your Choice"),sg.InputText()],
                           [sg.Button("OK")]]
                window=sg.Window("COVID 19 Database", layout)
                while True:
                    event1, values1 = window.read()
                    if event1 == sg.WIN_CLOSED or values1[0]=="c" :
                        window.close()
                        break
                    if values1[0]=='a':
                        window.close()
                        a1()
                    if values1[0]=='b':
                        window.close()
                        b1()
def a1():
                        layout=[ [sg.Text("Please Choose From the Following:")],
                                 [sg.Text("a)Insert\nb)Display\nc)Update\nd)Search\ne)Delete")],
                                 [sg.Text("Enter Your Choice"),sg.InputText()],
                                 [sg.Button("OK")],
                                 [sg.Button("Close")]]
                        window=sg.Window("COVID 19 Database", layout)
                        while True:
                            event2, values2 = window.read()
                            if event2=="Close" or event2==sg.WIN_CLOSED:
                                            window.close()
                                            break
                            elif values2[0]=='a':
                                            insert()
                                            display()
                            elif values2[0]=='b':
                                            display()
                            elif values2[0]=='c':
                                            update()
                                            display()
                            elif values2[0]=='d':
                                            search()
                            elif values2[0]=='e':
                                            delete()
                                            display()
def b1():
                        layout=[ [sg.Text("Please Choose From the Following:")],
                                 [sg.Text("a)Insert\nb)Display\nc)Update\nd)Search\ne)Delete")],
                                 [sg.Text("Enter Your Choice"),sg.InputText()],
                                 [sg.Button("OK")],
                                 [sg.Button("Close")]]
                        window=sg.Window("COVID 19 Database", layout)
                        while True:
                            event2, values2 = window.read()
                            if event2=="Close" or event2==sg.WIN_CLOSED:
                                            window.close()
                                            break
                            elif values2[0]=='a':
                                            insert_1()
                                            display_1()
                            elif values2[0]=='b':
                                            display_1()
                            elif values2[0]=='c':
                                            update_1()
                                            display_1()
                            elif values2[0]=='d':
                                            search_1()
                            elif values2[0]=='e':
                                            delete_1()
                                            display_1()

def b():
                layout=[   [sg.Text("a)Check Variant Records\nb)Check Infected Records\nc)Go Back")],
                           [sg.Text("Enter Your Choice"),sg.InputText()],
                           [sg.Button("OK")]]
                window=sg.Window("COVID 19 Database", layout)
                while True:
                    event1, values1 = window.read()
                    if event1 == sg.WIN_CLOSED or values1[0]=="c" :
                        window.close()
                        break
                    if values1[0]=='a':
                        window.close()
                        a2()
                    if values1[0]=='b':
                        window.close()
                        b2()
                        
def a2():
                        layout=[ [sg.Text("Please Choose From the Following:")],
                                 [sg.Text("a)Insert\nb)Display\nc)Update\nd)Search\ne)Delete")],
                                 [sg.Text("Enter Your Choice"),sg.InputText()],
                                 [sg.Button("OK")],
                                 [sg.Button("Close")]]
                        window=sg.Window("COVID 19 Database", layout)
                        while True:
                            event2, values2 = window.read()
                            if event2=="Close" or event2==sg.WIN_CLOSED:
                                            window.close()
                                            break
                            elif values2[0]=='a':
                                            insert_2()
                                            display_2()
                            elif values2[0]=='b':
                                            display_2()
                            elif values2[0]=='c':
                                            update_2()
                                            display_2()
                            elif values2[0]=='d':
                                            search_2()
                            elif values2[0]=='e':
                                            delete_2()
                                            display_2()
def b2():
                        layout=[ [sg.Text("Please Choose From the Following:")],
                                 [sg.Text("a)Insert\nb)Display\nc)Update\nd)Search\ne)Delete")],
                                 [sg.Text("Enter Your Choice"),sg.InputText()],
                                 [sg.Button("OK")],
                                 [sg.Button("Close")]]
                        window=sg.Window("COVID 19 Database", layout)
                        while True:
                            event2, values2 = window.read()
                            if event2=="Close" or event2==sg.WIN_CLOSED:
                                            window.close()
                                            break
                            elif values2[0]=='a':
                                            insert_3()
                                            display_3()
                            elif values2[0]=='b':
                                            display_3()
                            elif values2[0]=='c':
                                            update_3()
                                            display_3()
                            elif values2[0]=='d':
                                            search_3()
                            elif values2[0]=='e':
                                            delete_3()
                                            display_3()




                                            
        
def display():
    l=[]
    cur=conn.cursor()
    cur.execute("SELECT* FROM vaccine")
    data=cur.fetchall()
    for i in data:
        d=[i[0],i[1],i[2],i[3]]
        l.append(d)
    if len(data)>0:       
        headings=["Vaccine Name","Vaccine Country","Quantity","Refiil Date"]
        layout = [[sg.Table(values=l, headings=headings, max_col_width=25,
        auto_size_columns=True,
        justification='centre',
        num_rows=20,
        key='-TABLE-',
        row_height=25,
        tooltip='This is a table')],
        [sg.Button('Close')],
        [sg.Text('Read = read which rows are selected')]]
        window = sg.Window('The Table Element', layout)
        while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Close': 
                    window.close()
                    break
    else: 
        layout=[[sg.Text("No Records to Display")],
                [sg.Button("Ok")]]
        window=sg.Window("COVID 19 Database", layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok': 
                window.close()
def insert():
    layout=[ [sg.Text("Enter the Vaccine Name: "),sg.InputText('',key='vname')],
             [sg.Text("Enter Vaccine's Country of Origin: "),sg.InputText('',key='vcountry')],
             [sg.Text("Enter the Quantity of the Vaccine: "),sg.InputText('',key='quantity')],
             [sg.Button("Ok")]]    
    window=sg.Window("COVID 19 Database", layout)
    while True:
            event, values = window.read()
            if event =='Ok':
                window.close()
                vname=values['vname']
                vcountry=values['vcountry']
                quantity=int(values['quantity'])
                cur=conn.cursor()
                clause="INSERT INTO vaccine (vname,vcountry,quantity) VALUE ('{}','{}',{})".format(vname,vcountry,quantity)
                try:
                    cur.execute(clause)
                    conn.commit()
                except:
                    conn.rollback()
                break
            elif event == sg.WIN_CLOSED :
                    window.close()
                    break

  
def update():
    updated=False
    cur.execute("set sql_safe_updates=0")
    layout=[[sg.Text("Enter the Vaccine Name: "),sg.InputText('',key='vname')],
            [sg.Button("Ok")]]  
    window=sg.Window("COVID 19 Database", layout)
    while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED :
                    window.close()
                    break
            elif event == 'Ok':
                window.close()
                vname=values['vname']
                cur.execute("SELECT* FROM vaccine")
                data=cur.fetchall()
                for i in data:
                    if i[0]==vname:
                        updated=True
                        refill="now()"
                        layout=[[sg.Text("Enter Vaccine's Country of Origin: "),sg.InputText('',key='vcountry')],
                                [sg.Text("Enter the Quantity of the Vaccine: "),sg.InputText('',key='quantity')],
                                [sg.Button("Ok")]]
                        window=sg.Window("COVID 19 Database", layout)
                        while True:
                            event, values = window.read()
                            if event == sg.WIN_CLOSED or event == 'Ok': 
                                vcountry=values['vcountry']
                                quantity=int(values['quantity'])
                                window.close()
                                break                            
                if updated:
                        clause="UPDATE vaccine set vcountry='{}', quantity={},Refill={} where vname = '{}'".format(vcountry,quantity,refill,vname)
                        try:
                            cur.execute(clause)
                            conn.commit()
                        except:
                            conn.rollback()
                        break
 
                else: 
                    layout=[[sg.Text("Record not found")],
                            [sg.Button("Ok")]]
                    window=sg.Window("COVID 19 Database", layout)
                    event, values = window.read()
                    if event == sg.WIN_CLOSED or event == 'Ok': 
                        window.close()

def search():
    searched=False
    l=[]
    layout=[[sg.Text("Enter Name of Vaccine to Search: "),sg.InputText('',key="vname")],
            [sg.Button("Submit")]]
    window=sg.Window("COVID 19 Database", layout)
    event, values = window.read()
    if event =='Submit':
        window.close()
        vname=values['vname']
        clause="SELECT * from vaccine where vname = '{}'".format(vname)
        cur.execute(clause)
        data=cur.fetchall()
        for i in data:
            d=[i[0],i[1],i[2],i[3]]
            l.append(d)
            if d[0]==vname:
                searched=True
        if searched:   
            headings=["Vaccine Name","Vaccine Country","Quantity","Refiil Date"]
            layout = [[sg.Table(values=l, headings=headings, max_col_width=25,
            auto_size_columns=True,
            justification='centre',
            num_rows=20,
            key='-TABLE-',
            tooltip='This is a table')],
            [sg.Button('Close')],
            [sg.Text('Read = read which rows are selected')]]
            window = sg.Window('The Table Element', layout)
            while True:
                    event, values = window.read()
                    if event == sg.WIN_CLOSED or event == 'Close': 
                        window.close()
                        break
        else: 
            layout=[[sg.Text("No Records to Display")],
                    [sg.Button("Ok")]]
            window=sg.Window("COVID 19 Database", layout)
            event, values = window.read()
            while True:
                if event == sg.WIN_CLOSED or event == 'Ok': 
                        window.close()
                        break


def delete():
    deleted=False
    layout=[[sg.Text("Enter Name of Vaccine to Delete: "),sg.InputText('',key="vname")],
            [sg.Button("Submit")]]
    window=sg.Window("COVID 19 Database", layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Submit':
                window.close()
                vname=values['vname']
                cur.execute("SELECT* FROM vaccine")
                data=cur.fetchall()
                for i in data:
                    if i[0]==vname:
                        deleted=True
    if deleted:
        clause="delete from vaccine where vname = '{}'".format(vname)
        try:
            cur.execute(clause)
            conn.commit()
        except:
            conn.rollback()

    else: 
        layout=[[sg.Text("Record not found")],
                [sg.Button("Close")]]
        window=sg.Window("COVID 19 Database", layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close': 
            window.close()

def display_1():
    l=[]
    cur=conn.cursor()
    cur.execute("SELECT* FROM patient")
    data=cur.fetchall()
    for i in data:
        d=[i[0],i[1],i[2],i[3],i[4],i[5]]
        l.append(d)
    if len(data)>0:       
        headings=["Emirates ID","Patient Name","Date of Dose 1","Date of Dose 2","Vaccine","Booster"]
        layout = [[sg.Table(values=l, headings=headings, max_col_width=25,
        auto_size_columns=True,
        justification='centre',
        num_rows=20,
        key='-TABLE-',
        row_height=25)],
        [sg.Button('Close')]]
        window = sg.Window('The Table Element', layout)
        while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Close': 
                    window.close()
                    break
    else: 
        layout=[[sg.Text("No Records to Display")],
                [sg.Button("Ok")]]
        window=sg.Window("COVID 19 Database", layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok': 
                window.close()
def insert_1():
    layout=[ [sg.Text("Enter Emirates ID: "),sg.InputText('',key='eid')],
             [sg.Text("Enter Patient Name: "),sg.InputText('',key='patname')],
             [sg.Text("Enter Date of Dose 1: "),sg.InputText('',key='DOV1')],
             [sg.Text("Enter Date of Dose 2: "),sg.InputText('',key='DOV2')],
             [sg.Text("Enter Vaccine Name: "),sg.InputText('',key='vname')],
             [sg.Text("Booster(Y/N): "),sg.InputText('',key='booster')],
             [sg.Button("Ok")]]   
    window=sg.Window("COVID 19 Database", layout)
    while True:
            event, values = window.read()
            if event =='Ok':
                window.close()
                eid=int(values['eid'])
                patname=values['patname']
                DOV1=values['DOV1']
                DOV2=values['DOV2']
                vname=values['vname']
                booster=values['booster']
                cur=conn.cursor()
                clause="INSERT INTO patient VALUE({},'{}','{}','{}','{}','{}')".format(eid,patname,DOV1,DOV2,vname,booster)
                try:
                    cur.execute(clause)
                    conn.commit()
                except:
                    conn.rollback()
                cur.execute("update vaccine inner join patient on vaccine.vname=patient.vname set quantity=quantity-1")
                break
            elif event == sg.WIN_CLOSED :
                    window.close()
                    break

def update_1():
    updated=False
    cur=conn.cursor()
    cur.execute("set sql_safe_updates=0")
    layout=[[sg.Text("Enter Emirates ID: "),sg.InputText('',key='eid')],
            [sg.Button("Ok")]]
    window=sg.Window("COVID 19 Database", layout)
    while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED :
                    window.close()
                    break
            elif event == 'Ok':
                window.close()
                eid=int(values['eid'])
                cur.execute("SELECT* FROM patient")
                data=cur.fetchall()
                for i in data:
                    if i[0]==eid:
                        updated=True
                        layout=[ [sg.Text("Enter Patient Name: "),sg.InputText('',key='patname')],
                                 [sg.Text("Enter Date of Dose 1: "),sg.InputText('',key='DOV1')],
                                 [sg.Text("Enter Date of Dose 2: "),sg.InputText('',key='DOV2')],
                                 [sg.Text("Enter Vaccine Name: "),sg.InputText('',key='vname')],
                                 [sg.Text("Booster(Y/N): "),sg.InputText('',key='booster')],
                                 [sg.Button("Ok")]]   
                        window=sg.Window("COVID 19 Database", layout)
                        while True:
                            event, values = window.read()
                            if event == sg.WIN_CLOSED or event == 'Ok': 
                                window.close()
                                patname=values['patname']
                                DOV1=values['DOV1']
                                DOV2=values['DOV2']
                                vname=values['vname']
                                booster=values['booster']
                                break                            
                if updated:
                        clause="UPDATE patient set patname='{}', DOV1='{}', DOV2='{}', vname='{}', booster='{}' where eid = {}".format(patname,DOV1,DOV2,vname,booster,eid)
                        try:
                            cur.execute(clause)
                            conn.commit()
                        except:
                            conn.rollback()
                        break
 
                else: 
                    layout=[[sg.Text("Record not found")],
                            [sg.Button("Ok")]]
                    window=sg.Window("COVID 19 Database", layout)
                    event, values = window.read()
                    if event == sg.WIN_CLOSED or event == 'Ok': 
                        window.close()
    
def search_1():
    searched=False
    l=[]
    layout=[[sg.Text("Enter Emirates ID: "),sg.InputText('',key='eid')],
            [sg.Button("Ok")]]
    window=sg.Window("COVID 19 Database", layout)
    event, values = window.read()
    if event =='Ok':
        window.close()
        eid=int(values['eid'])
        clause="SELECT * from patient where eid = {}".format(eid)
        cur.execute(clause)
        data=cur.fetchall()
        for i in data:
            d=[i[0],i[1],i[2],i[3],i[4],i[5]]
            l.append(d)
            if d[0]==eid:
                searched=True
        if searched:   
            headings=["Emirates ID","Patient Name","Date of Dose 1","Date of Dose 2","Vaccine","Booster"]
            layout = [[sg.Table(values=l, headings=headings, max_col_width=25,
            auto_size_columns=True,
            justification='centre',
            num_rows=20,
            key='-TABLE-',
            tooltip='This is a table')],
            [sg.Button('Close')],
            [sg.Text('Read = read which rows are selected')]]
            window = sg.Window('The Table Element', layout)
            while True:
                    event, values = window.read()
                    if event == sg.WIN_CLOSED or event == 'Close': 
                        window.close()
                        break
        else: 
            layout=[[sg.Text("No Records to Display")],
                    [sg.Button("Ok")]]
            window=sg.Window("COVID 19 Database", layout)
            event, values = window.read()
            while True:
                if event == sg.WIN_CLOSED or event == 'Ok': 
                        window.close()
                        break

def delete_1():
    deleted=False
    layout=[[sg.Text("Enter Emirates ID of Pateint to Delete: "),sg.InputText('',key="eid")],
            [sg.Button("Submit")]]
    window=sg.Window("COVID 19 Database", layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Submit':
                window.close()
                eid=int(values['eid'])
                cur.execute("SELECT* FROM patient")
                data=cur.fetchall()
                for i in data:
                    if i[0]==eid:
                        deleted=True
    if deleted:
        clause="delete from patient where eid = {}".format(eid)
        try:
            cur.execute(clause)
            conn.commit()
        except:
            conn.rollback()

    else: 
        layout=[[sg.Text("Record not found")],
                [sg.Button("Close")]]
        window=sg.Window("COVID 19 Database", layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close': 
            window.close()
        
def display_2():
    l=[]
    cur=conn.cursor()
    cur.execute("SELECT* FROM variant")
    data=cur.fetchall()
    for i in data:
        d=[i[0],i[1],i[2]]
        l.append(d)
    if len(data)>0:       
        headings=["S.No.","Variant Name","Date of Origin"]
        layout = [[sg.Table(values=l, headings=headings, max_col_width=25,
        auto_size_columns=True,
        justification='centre',
        num_rows=20,
        key='-TABLE-',
        row_height=25)],
        [sg.Button('Close')]]
        window = sg.Window('The Table Element', layout)
        while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Close': 
                    window.close()
                    break
    else: 
        layout=[[sg.Text("No Records to Display")],
                [sg.Button("Ok")]]
        window=sg.Window("COVID 19 Database", layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok': 
                window.close()
def insert_2():
    layout=[ [sg.Text("Enter Variant Name: "),sg.InputText('',key='cname')],
             [sg.Text("Enter Date of Origin: "),sg.InputText('',key='DOO')],
             [sg.Button("Ok")]]   
    window=sg.Window("COVID 19 Database", layout)
    while True:
            event, values = window.read()
            if event =='Ok':
                window.close()
                cname=values['cname']
                DOO=values['DOO']
                cur=conn.cursor()
                clause="INSERT INTO variant (cname,DOO) VALUE ('{}','{}')".format(cname,DOO)
                try:
                    cur.execute(clause)
                    conn.commit()
                except:
                    conn.rollback()
                break
            elif event == sg.WIN_CLOSED :
                    window.close()
                    break
def update_2():
    updated=False
    cur=conn.cursor()
    cur.execute("set sql_safe_updates=0")
    layout=[[sg.Text("Enter S.No. of Variant to Update: "),sg.InputText('',key='cid')],
            [sg.Button("Ok")]]
    window=sg.Window("COVID 19 Database", layout)
    while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED :
                    window.close()
                    break
            elif event == 'Ok':
                window.close()
                cid=int(values['cid'])
                cur.execute("SELECT* FROM variant")
                data=cur.fetchall()
                for i in data:
                    if i[0]==cid:
                        updated=True
                        layout=[ [sg.Text("Enter Variant Name: "),sg.InputText('',key='cname')],
                                 [sg.Text("Enter Date of Origin: "),sg.InputText('',key='DOO')],
                                 [sg.Button("Ok")]]   
                        window=sg.Window("COVID 19 Database", layout)
                        while True:
                            event, values = window.read()
                            if event == sg.WIN_CLOSED or event == 'Ok': 
                                window.close()
                                cname=values['cname']
                                DOO=values['DOO']
                                break                            
                if updated:
                        clause="UPDATE variant set cname='{}', DOO='{}' where cid = {}".format(cname,DOO,cid)
                        try:
                            cur.execute(clause)
                            conn.commit()
                        except:
                            conn.rollback()
                        break 
                else: 
                    layout=[[sg.Text("Record not found")],
                            [sg.Button("Ok")]]
                    window=sg.Window("COVID 19 Database", layout)
                    event, values = window.read()
                    if event == sg.WIN_CLOSED or event == 'Ok': 
                        window.close()

def search_2():
    searched=False
    l=[]
    layout=[[sg.Text("Enter S.No. of Variant to Search: "),sg.InputText('',key='cid')],
            [sg.Button("Ok")]]
    window=sg.Window("COVID 19 Database", layout)
    event, values = window.read()
    if event =='Ok':
        window.close()
        cid=int(values['cid'])
        clause="SELECT * from variant where cid = '{}'".format(cid)
        cur.execute(clause)
        data=cur.fetchall()
        for i in data:
            d=[i[0],i[1],i[2]]
            l.append(d)
            if d[0]==cid:
                searched=True        
        if searched:   
            headings=["S.No.","Variant Name","Date of Origin"]
            layout = [[sg.Table(values=l, headings=headings, max_col_width=25,
            auto_size_columns=True,
            justification='centre',
            num_rows=20,
            key='-TABLE-',
            tooltip='This is a table')],
            [sg.Button('Close')],
            [sg.Text('Read = read which rows are selected')]]
            window = sg.Window('The Table Element', layout)
            while True:
                    event, values = window.read()
                    if event == sg.WIN_CLOSED or event == 'Close': 
                        window.close()
                        break
        else: 
            layout=[[sg.Text("No Records to Display")],
                    [sg.Button("Ok")]]
            window=sg.Window("COVID 19 Database", layout)
            event, values = window.read()
            while True:
                if event == sg.WIN_CLOSED or event == 'Ok': 
                        window.close()
                        break
def delete_2():
    deleted=False
    layout=[[sg.Text("Enter S.No. of Variant to Delete: "),sg.InputText('',key="cid")],
            [sg.Button("Submit")]]
    window=sg.Window("COVID 19 Database", layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Submit':
                window.close()
                cid=int(values['cid'])
                cur.execute("SELECT* FROM variant")
                data=cur.fetchall()
                for i in data:
                    if i[0]==cid:
                        deleted=True
    if deleted:
        clause="delete from variant where cid = {}".format(cid)
        try:
            cur.execute(clause)
            conn.commit()
        except:
            conn.rollback()

    else: 
        layout=[[sg.Text("Record not found")],
                [sg.Button("Close")]]
        window=sg.Window("COVID 19 Database", layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close': 
            window.close()

        
def display_3():
    l=[]
    cur=conn.cursor()
    cur.execute("SELECT* FROM infected")
    data=cur.fetchall()
    for i in data:
        d=[i[0],i[1],i[2],i[3]]
        l.append(d)
    if len(data)>0:       
        headings=["Identification No.","Patient Name","Date of PCR Test","Emirates ID"]
        layout = [[sg.Table(values=l, headings=headings, max_col_width=25,
        auto_size_columns=True,
        justification='centre',
        num_rows=20,
        key='-TABLE-',
        row_height=25)],
        [sg.Button('Show Vaccinated')],
        [sg.Button('Close')]]
        window = sg.Window('The Table Element', layout)
        while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Close': 
                    window.close()
                    break
                elif event =="Show Vaccinated":
                    window.close()
                    l1=[]
                    cur=conn.cursor()
                    cur.execute("Select iid,pname,DOP,Vname,DOV1,DOV2,booster  from infected,patient where infected.eid=patient.eid;")
                    data=cur.fetchall()
                    for i in data:
                        d=[i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
                        l1.append(d)
                    if len(data)>0:       
                        headings=["Identification ID","Patient Name","Date of PCR Test","Vaccine","Date of Dose1","Date of Dose 2","Booster"]
                        layout = [[sg.Table(values=l1, headings=headings, max_col_width=25,
                        auto_size_columns=True,
                        justification='right',
                        num_rows=20,
                        key='-TABLE-',
                        row_height=25)],
                        [sg.Button('Close')]]
                        window = sg.Window('The Table Element', layout)
                        while True:
                            event, values = window.read()
                            if event == sg.WIN_CLOSED or event == 'Close': 
                                window.close()
                                break
                    else: 
                        layout=[[sg.Text("No Records to Display")],
                                [sg.Button("Ok")]]
                        window=sg.Window("COVID 19 Database", layout)
                        event, values = window.read()
                        if event == sg.WIN_CLOSED or event == 'Ok': 
                                window.close()
                                    
    else: 
        layout=[[sg.Text("No Records to Display")],
                [sg.Button("Ok")]]
        window=sg.Window("COVID 19 Database", layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok': 
                window.close()
  
def insert_3():
    layout=[ [sg.Text("Enter Patient Name: "),sg.InputText('',key='pname')],
             [sg.Text("Enter Date of PCR: "),sg.InputText('',key='DOP')],
             [sg.Text("Enter Emirates ID "),sg.InputText('',key='eid')],
             [sg.Button("Ok")]]   
    window=sg.Window("COVID 19 Database", layout)
    while True:
            event, values = window.read()
            if event =='Ok':
                window.close()
                pname=values['pname']
                DOP=values['DOP']
                eid=int(values['eid'])
                cur=conn.cursor()
                clause="INSERT INTO infected (pname,DOP,eid) VALUE('{}','{}',{})".format(pname,DOP,eid)
                try:
                    cur.execute(clause)
                    conn.commit()
                except:
                    conn.rollback()
                break
            elif event == sg.WIN_CLOSED :
                    window.close()
                    break
def update_3():
    updated=False
    cur=conn.cursor()
    cur.execute("set sql_safe_updates=0")
    layout=[[sg.Text("Enter ID: "),sg.InputText('',key='iid')],
            [sg.Button("Ok")]]
    window=sg.Window("COVID 19 Database", layout)
    while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED :
                    window.close()
                    break
            elif event == 'Ok':
                window.close()
                iid=int(values['iid'])
                cur.execute("SELECT* FROM infected")
                data=cur.fetchall()
                for i in data:
                    if i[0]==iid:
                        updated=True
                        layout=[ [sg.Text("Enter Patient Name: "),sg.InputText('',key='pname')],
                                 [sg.Text("Enter Date of PCR: "),sg.InputText('',key='DOP')],
                                 [sg.Text("Enter Emirates ID: "),sg.InputText('',key='eid')],
                                 [sg.Button("Ok")]]   
                        window=sg.Window("COVID 19 Database", layout)
                        while True:
                            event, values = window.read()
                            if event == sg.WIN_CLOSED or event == 'Ok': 
                                window.close()
                                pname=values['pname']
                                DOP=values['DOP']
                                eid=int(values['eid'])
                                break                            
                if updated:
                        clause="UPDATE infected set pname='{}', DOP='{}',eid={} where iid = {}".format(pname,DOP,eid,iid)
                        try:
                            cur.execute(clause)
                            conn.commit()
                        except:
                            conn.rollback()
                        break
 
                else: 
                    layout=[[sg.Text("Record not found")],
                            [sg.Button("Ok")]]
                    window=sg.Window("COVID 19 Database", layout)
                    event, values = window.read()
                    if event == sg.WIN_CLOSED or event == 'Ok': 
                        window.close()

def search_3():
    searched=False
    l=[]
    layout=[[sg.Text("Enter ID to Search: "),sg.InputText('',key='iid')],
            [sg.Button("Ok")]]
    window=sg.Window("COVID 19 Database", layout)
    event, values = window.read()
    if event =='Ok':
        window.close()
        iid=int(values['iid'])
        clause="SELECT * from infected where iid = {}".format(iid)
        cur.execute(clause)
        data=cur.fetchall()
        for i in data:
            d=[i[0],i[1],i[2],i[3]]
            l.append(d)
            if d[0]==iid:
                searched=True
        if searched:   
            headings=["Identification No.","Patient Name","Date of PCR Test","Emirates ID"]
            layout = [[sg.Table(values=l, headings=headings, max_col_width=25,
            auto_size_columns=True,
            justification='centre',
            num_rows=20,
            key='-TABLE-',
            tooltip='This is a table')],
            [sg.Button('Close')],
            [sg.Text('Read = read which rows are selected')]]
            window = sg.Window('The Table Element', layout)
            while True:
                    event, values = window.read()
                    if event == sg.WIN_CLOSED or event == 'Close': 
                        window.close()
                        break
        else: 
            layout=[[sg.Text("No Records to Display")],
                    [sg.Button("Ok")]]
            window=sg.Window("COVID 19 Database", layout)
            event, values = window.read()
            while True:
                if event == sg.WIN_CLOSED or event == 'Ok': 
                        window.close()
                        break

def delete_3():
    deleted=False
    layout=[[sg.Text("Enter ID of Pateint to Delete: "),sg.InputText('',key="iid")],
            [sg.Button("Submit")]]
    window=sg.Window("COVID 19 Database", layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Submit':
                window.close()
                iid=int(values['iid'])
                cur.execute("SELECT* FROM infected")
                data=cur.fetchall()
                for i in data:
                    if i[0]==iid:
                        deleted=True
    if deleted:
        clause="delete from infected where iid = {}".format(iid)
        try:
            cur.execute(clause)
            conn.commit()
        except:
            conn.rollback()

    else: 
        layout=[[sg.Text("Record not found")],
                [sg.Button("Close")]]
        window=sg.Window("COVID 19 Database", layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close': 
            window.close()
        
layout=[    [sg.Text("***********************************************")],
            [sg.Text("Welcome to the UAE COVID 19 database")],
            [sg.Text("Please select an option")],
            [sg.Text("a)Vaccination Records\nb)COVID Records\nc)Exit")],
            [sg.Text("Enter Your Choice"),sg.InputText()],
            [sg.Button("OK")] ]
window=sg.Window("COVID 19 Database", layout)
while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or values[0]=='c': 
            window.close()
            break
        elif values[0]=='a':
            a()
        elif values[0]=='b':
            b()
                       
                        

                        

