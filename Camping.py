import pymysql
import random
import os
from tkinter import *
import calendar
import datetime
from datetime import date

# Connect to the database
global connection
connection= pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='final',
                            charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
connection.autocommit(True)
        
#Destroy

def destroy(root):
        root.destroy()

#Show ERD
        
def ER():
        os.system('Diagram32_τελικό.png')

        
#Show DB
        
def DB():
        os.system('camping32-dbdesigner.pdf')
##SPOTS
def spots():
    canvas1.delete(ALL)
    canvas1.configure(bg='AntiqueWhite2')

    def execute():
        arrivaldate=a_date.get()
        departuredate=d_date.get()
        
        date1 = arrivaldate.split('-')
        date1=datetime.date(int(date1[0]),int(date1[1]),int(date1[2]))
        date2 = departuredate.split('-')
        date2=datetime.date(int(date2[0]),int(date2[1]),int(date2[2]))
        if date1>date2:
                canvas.create_text(200,0,font=("Arial", "10"),text='Wrong set of dates')
                canvas.configure(scrollregion=canvas.bbox("all"))
        else:
                sql='select * from spot where spot_code not in(select distinct spot_code from reservation rs join includes on includes.b_code=rs.booking_code join spot on spot_code=s_code where(rs.arrival_date between '+arrivaldate+' and '+departuredate+') OR (rs.departure_date BETWEEN '+arrivaldate+' AND '+departuredate+')  OR (rs.arrival_date<'+arrivaldate+' AND rs.departure_date>'+departuredate+'));'
                print(sql)
                with connection.cursor() as cursor:
                        try:
                                cursor.execute(sql)
                                connection.commit()
                                #print table
                                canvas.create_text(200,0,font=("Arial", "10"),text="Available Spots")
                                canvas.configure(scrollregion=canvas.bbox("all"))
                                i=20
                                for row in cursor:
                                        canvas.create_text(200,20+i,font=("Arial", "10"),text=row)
                                        canvas.configure(scrollregion=canvas.bbox("all"))
                                        i=i+20
                        except:
                                #error message
                            canvas.create_text(200,0,font=("Arial", "10"),text='Error in sql command')
                            canvas.configure(scrollregion=canvas.bbox("all"))
                        spots()
        
               
               
    #select table
    label = Label(canvas1, text="Arrival date ", font=("Arial", 10))
    label.grid(column=0, row=40)
    label.configure(background="AntiqueWhite2")
    a_date = Entry(canvas1,width=20)
    a_date.grid(column=0, row=60)
    
    #select columns
    
    label = Label(canvas1, text="Departure date", font=("Arial", 10))
    label.grid(column=0, row=80)
    label.configure(background="AntiqueWhite2")
    d_date = Entry(canvas1,width=20)
    d_date.grid(column=0, row=100)
    
    btn = Button(canvas1, text="Search", font=("Arial", 10), bg='grey',command=execute)
    btn.grid(column=0, row=200)


##INSERT

def insert():
    canvas1.delete(ALL)
    canvas1.configure(bg='AntiqueWhite2')
    def all_columns():
        global allcol
        allcol='1'
        canvas.delete(ALL)
        canvas.create_text(200,150,font=("Arial", "10"),text='PLEASE ADD VALUES FOR ALL OF THE COLUMNS')
        canvas.configure(scrollregion=canvas.bbox("all"))
        return allcol
        
    def specified_columns():
        global allcol
        canvas.delete(ALL)
        canvas.create_text(200,150,font=("Arial", "10"),text='PLEASE ADD VALUES FOR ALL OF THE SELECTED COLUMNS')
        canvas.configure(scrollregion=canvas.bbox("all"))
        allcol='0'
        return allcol
        
    def execute():
        sqlcolumns=columns.get()
        if (allcol=='1'):
            clm=''
        else: clm= '('+sqlcolumns+')'
        
        sql_table=table.get()
        sql_values=values.get()
       
        sql='INSERT INTO '+sql_table+' '+clm+'\n'+'VALUES '+'('+sql_values+');'
        print(sql)
        
        if sql == '':  return 0
        else:
            with connection.cursor() as cursor:
                try:
                    # Execute query.
                    cursor.execute(sql)
                    connection.commit()
                    #clear the canvas
                    canvas.delete(ALL)
                    canvas.create_text("cursor.description: ", cursor.description)
                    canvas.configure(scrollregion=canvas.bbox("all"))
                    i=20
                    #results 
                    for row in cursor:
                        canvas.create_text(200,150+i,font=("Arial", "10"),text=row)
                        canvas.configure(scrollregion=canvas.bbox("all"))
                        i=i+20
                except:
                        #error
                    canvas.delete(ALL)
                    canvas.create_text(200,150,font=("Arial", "10"),text='Error in sql command, try again. \nYou can allways check again the DB Schema \nby clicking the button above')
                    canvas.configure(scrollregion=canvas.bbox("all"))
                    insert()
               
               
    #select table
    label = Label(canvas1, text="Specify a table: ", font=("Arial", 10))
    label.grid(column=0, row=40)
    label.configure(background="AntiqueWhite2")
    table = Entry(canvas1,width=20)
    table.grid(column=0, row=60)
    
    #select columns
    
    label = Label(canvas1, text="Specify columns with ',' between them: ", font=("Arial", 10))
    label.grid(column=0, row=80)
    label.configure(background="AntiqueWhite2")
    columns = Entry(canvas1,width=20)
    columns.grid(column=0, row=100)
    
    #buttons
    
    btn = Button(canvas1, text="Select all columns", font=("Arial", 10),bg='grey', command=all_columns)
    btn.grid(column=0, row=120)             
    btn = Button(canvas1, text="Specified columns", font=("Arial", 10),bg='grey', command=specified_columns)
    btn.grid(column=0, row=140)
    btn = Button(canvas1, text="Execute", font=("Arial", 10), bg='grey',command=execute)
    btn.grid(column=0, row=200)
    
    label = Label(canvas1, text="Specify values with ',' between them: ", font=("Arial", 10))
    label.grid(column=0, row=160)
    label.configure(background="AntiqueWhite2")
    values = Entry(canvas1,width=20)
    values.grid(column=0, row=180)

        
##DELETE
def delete_data():
    canvas1.delete(ALL)
    def whole_table():
        global all_tabl
        canvas.delete(ALL)
        canvas.create_text(200,150,font=("Arial", "10"),text='PLEASE SELECT THE TABLE YOU WISH TO DELETE')
        canvas.configure(scrollregion=canvas.bbox("all"))
        all_tabl='1'
        return all_tabl
    
    def specified_data():
        global all_tabl
        canvas.delete(ALL)
        canvas.create_text(200,150,font=("Arial", "10"),text='PLEASE SELECT THE DATA YOU WISH TO DELETE')
        canvas.configure(scrollregion=canvas.bbox("all"))
        all_tabl='0'
        return all_tabl

    def execute():
        sql_table=table.get()
        if sql_table == '':
            canvas.delete(ALL)
            canvas.create_text(200,150,font=("Arial", "10"),text='PLEASE FILL IN THE BOXES THE DATA YOU WISH TO DELETE')
            canvas.configure(scrollregion=canvas.bbox("all"))
            return 0
        else:
            if(all_tabl=='1'):
                sql='DROP TABLE '+sql_table+';'
                
            elif(all_tabl=='0'):
                sql_value=value.get()
                sql_attribute=field.get()
                sql="DELETE FROM "+sql_table+" WHERE "+sql_attribute+"='"+sql_value+"';"
                print(sql)    
            try:
                with connection.cursor() as cursor:
                    
                    #print(sql)
                    cursor.execute(sql)
                    connection.commit()
                    canvas.delete(ALL)
                    canvas.create_text("cursor.description: ", cursor.description)
                    canvas.configure(scrollregion=canvas.bbox("all"))
                    i=20
                    for row in cursor:
                        canvas.create_text(200,150+i,font=("Arial", "10"),text=row)
                        canvas.configure(scrollregion=canvas.bbox("all"))
                        i=i+20
            except:
                canvas.delete(ALL)
                canvas.create_text(200,150,font=("Arial", "10"),text='Error in sql command, try again')
                canvas.configure(scrollregion=canvas.bbox("all"))
                delete_data()
                
            
    lbl = Label(canvas1, text="Specify a table: ", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=40)
    table = Entry(canvas1,width=20)
    table.grid(column=0, row=60)

    lbl = Label(canvas1, text="Specify values ", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=80)
    value = Entry(canvas1,width=20)
    value.grid(column=0, row=100)

    lbl = Label(canvas1, text="Specify attribute", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=120)
    field = Entry(canvas1,width=20)
    field.grid(column=0, row=140)
    
 
    btn = Button(canvas1, text="Delete whole tables", font=("Arial", 10), bg='grey',command=whole_table)
    btn.grid(column=0, row=160)

    btn = Button(canvas1, text="Delete specified values from table", font=("Arial", 10), bg='grey',command=specified_data)
    btn.grid(column=0, row=180)
  
    btn = Button(canvas1, text="Execute", font=("Arial", 10), bg='grey',command=execute)
    btn.grid(column=0, row=200)
    
##UPDATE TABLES

def update():
    canvas1.delete(ALL)
    def execute():
            
        sql_table=table.get()
        sql_columns=columns.get().split(',')
        
        sql_values=values.get().split(',')
        
        set_values=sql_columns+sql_values
        
        sql_condition=condition.get()
        
        if (sql_condition==''):
            where=''
        else: where= 'WHERE '+sql_condition
        col_val=[]
 
        for count in range(0,len(sql_columns)):
            col_val.append(set_values[count]+'='+set_values[count+len(sql_columns)])

        for x in col_val:
            sql='UPDATE '+sql_table+'\n'+'SET '+x+'\n'+where+';'
     
            if sql == '':  return 0
            else:
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(sql)
                        connection.commit()
                        canvas.delete(ALL)
                        canvas.create_text("cursor.description: ", cursor.description)
                        canvas.configure(scrollregion=canvas.bbox("all"))
                        i=20
                        for row in cursor:
                            canvas.create_text(200,150+i,font=("Arial", "10"),text=row)
                            canvas.configure(scrollregion=canvas.bbox("all"))
                            i=i+20
                except:
                    canvas.delete(ALL)
                    canvas.create_text(200,150,font=("Arial", "10"),text='Error in sql command, try again')
                    canvas.configure(scrollregion=canvas.bbox("all"))
                    update()
 
    lbl = Label(canvas1, text="Specify a table: ", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=40)
    table = Entry(canvas1,width=20)
    table.grid(column=0, row=60)


    lbl = Label(canvas1, text="Specify columns to update with ',' between them: ", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=80)
    columns = Entry(canvas1,width=20)
    columns.grid(column=0, row=100)


    lbl = Label(canvas1, text="Specify values with ',' between them: ", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=120)
    values = Entry(canvas1,width=20)
    values.grid(column=0, row=140)


    lbl = Label(canvas1, text="Specify condition (optional)", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=160)
    condition = Entry(canvas1,width=20)
    condition.grid(column=0, row=180)

    btn = Button(canvas1, text="Execute", font=("Arial", 10), bg='grey',command=execute)
    btn.grid(column=0, row=200)

#Run sql command
        
def sql_command():
        canvas1.delete(ALL)
        def execute():
            canvas.delete(ALL)
            query=entry.get()
            if query == '':  return 0
            else:
                with connection.cursor() as cursor:
                    try:
                        cursor.execute(query)
                        i=20
                        connection.commit()
                        for row in cursor:
                            canvas.create_text(200,20+i,font=("Arial", "10"),text=row)
                            canvas.configure(scrollregion=canvas.bbox("all"))
                            i=i+20
                    except:
                        #error message
                        canvas.create_text(200,0,font=("Arial", "10"),text='Error in sql command, try again')
                        canvas.configure(scrollregion=canvas.bbox("all"))
                        sql_command()
        
        #entry
                        
        entry = Entry(canvas1,width=30)
        entry.grid(column=0, row=60)
        
        #button
        
        btn = Button(canvas1, text="Execute", font=("Arial", 10), bg='grey',command=execute)
        btn.grid(column=0, row=80)
        

##Show guest info
        
def guests():
    #delete
    canvas.delete(ALL)
    with connection.cursor() as cursor:
        #sql command
        query_g="SELECT cl.id,cl._name,cl._surname,cl.phone_no,ic.s_code,rt.e_code FROM CLIENT cl JOIN does ds on cl.id=ds.cl_id JOIN reservation rs on ds.bk_code=rs.booking_code Join includes ic on ic.b_code=rs.booking_code Join rents rt on rt.bk_code=rs.booking_code ;"
        try:
            cursor.execute(query_g)
            connection.commit()
            #print table
            canvas.create_text(200,0,font=("Arial", "10"),text='The Campers are:')
            canvas.configure(scrollregion=canvas.bbox("all"))
            i=20
            for row in cursor:
                canvas.create_text(200,20+i,font=("Arial", "10"),text=row)
                canvas.configure(scrollregion=canvas.bbox("all"))
                i=i+20
        except:
            #error message
            canvas.create_text(200,0,font=("Arial", "10"),text='Error in sql command')
            canvas.configure(scrollregion=canvas.bbox("all"))
            guests()

#Show reservations
            
def todays_res():
    #delete
    canvas.delete(ALL)
    today = date.today()
    print(today)
    with connection.cursor() as cursor:
        #sql command
        query="SELECT rs.booking_code,rs.arrival_date,rs.departure_date,rs.check_in,rs.check_out,ic.s_code,rt.e_code FROM reservation rs Join includes ic on rs.booking_code=ic.b_code join rents rt on rt.bk_code=rs.booking_code WHERE (rs.arrival_date='+today+') OR (CHECK_IN='+today+');"
        try:
            cursor.execute(query)
            connection.commit()
            #print table
            canvas.create_text(200,0,font=("Arial", "10"),text="Today's Check in and Check out")
            canvas.configure(scrollregion=canvas.bbox("all"))
            i=20
            for row in cursor:
                canvas.create_text(200,20+i,font=("Arial", "10"),text=row)
                canvas.configure(scrollregion=canvas.bbox("all"))
                i=i+20
        except:
            #error message
            canvas.create_text(200,0,font=("Arial", "10"),text='Error in sql command')
            canvas.configure(scrollregion=canvas.bbox("all"))
            todays_res()

def payments():
    #delete
    canvas.delete(ALL)
    today = str(date.today())
    with connection.cursor() as cursor:
        #sql command
        query="select ps.payment_date,cl._surname,ps.client_id,pm.p_code,pm.payment_method FROM payment pm JOIN pays ps on pm.p_code=ps.payment_code Join client cl on cl.id=ps.client_id order by ps.payment_date desc;"
        try:
            cursor.execute(query)
            connection.commit()
            #print table
            canvas.create_text(200,0,font=("Arial", "10"),text="Payments")
            canvas.configure(scrollregion=canvas.bbox("all"))
            i=20
            for row in cursor:
                canvas.create_text(200,20+i,font=("Arial", "10"),text=row)
                canvas.configure(scrollregion=canvas.bbox("all"))
                i=i+20
        except:
            #error message
            canvas.create_text(200,0,font=("Arial", "10"),text='Error in sql command')
            canvas.configure(scrollregion=canvas.bbox("all"))
            payments()

def prices():
    canvas.delete(ALL)
    def execute():
            with connection.cursor() as cursor:
                    booking_code=b_code.get()
                    print(booking_code)
                    sql_pr="select sum(cost_per_day) as 'spot_cost'from spot join includes on includes.s_code=spot.spot_code join reservation on reservation.booking_code=includes.b_code where booking_code ='"+booking_code+"' union select sum(cost_per_day) as 'equipment_cost'from equipment join rents on rents.e_code=equipment.equipment_code join reservation on reservation.booking_code=rents.bk_code where booking_code ='"+booking_code+"';"

                    try:
                            cursor.execute(sql_pr)
                            connection.commit()
                            #print table
                            canvas.delete(ALL)
                            canvas.create_text(200,0,font=("Arial", "10"),text="Price for selected booking code ")
                            canvas.configure(scrollregion=canvas.bbox("all"))
                            i=20
                            for row in cursor:
                               canvas.delete(ALL)
                               canvas.create_text(200,20+i,font=("Arial", "10"),text=row)
                               canvas.configure(scrollregion=canvas.bbox("all"))
                               i=i+20
                    except:
                    #error message
                          canvas.delete(ALL)
                          canvas.create_text(200,0,font=("Arial", "10"),text='Error in sql command')
                          canvas.configure(scrollregion=canvas.bbox("all"))
                          prices()
                    

    lbl = Label(canvas1, text="Search price for booking code", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=40)
    b_code = Entry(canvas1,width=20)
    b_code.grid(column=0, row=60)

    btn = Button(canvas1, text="Execute", font=("Arial", 10), bg='grey',command=execute)
    btn.grid(column=0, row=80)

##INSRT client-res
def insert_res():
    today=str(date.today())
    canvas1.delete(ALL)
    canvas.delete(ALL)
    canvas.create_text(200,0,font=("Arial", "10"),text='Please write the values separated with , " ",')
    canvas.configure(scrollregion=canvas.bbox("all"))
    def new_client():
            with connection.cursor() as cursor:
                    client_info=client.get()
                    global cl
                    cl=client_info.split(",")
                    sql_client="INSERT INTO client(id,_name,_surname,phone_no) VALUES ("+client_info+");"
                    try:
                            cursor.execute(sql_client)
                            #print table
                            canvas.delete(ALL)
                            canvas.create_text(200,0,font=("Arial", "10"),text="new client")
                            canvas.configure(scrollregion=canvas.bbox("all"))
                            i=20
                            for row in cursor:
                                    canvas.create_text(200,20+i,font=("Arial", "10"),text=row)
                                    canvas.configure(scrollregion=canvas.bbox("all"))
                                    i=i+20
                    except pymysql.Error as error:
                            print("Failed to insert record into Client table {}".format(error))
            
           
            
    def new_res():
            with connection.cursor() as cursor:
                    reservation=reserv.get()
                    sql_res="insert into RESERVATION(booking_code,no_of_campers,category,arrival_date,departure_date,check_in,check_out,discount) values ("+reservation+");"
                    res=reservation.split(",")
                    try:
                            cursor.execute(sql_res)
                            canvas.delete(ALL)
                            canvas.create_text(200,0,font=("Arial", "10"),text="new reservation")
                            canvas.configure(scrollregion=canvas.bbox("all"))
                            print(cl[0],res[0],today)
                            sql_does="INSERT INTO DOES(cl_id,bk_code,booking_date)VALUES ("+cl[0]+","+res[0]+",'"+today+"');"
                            cursor.execute(sql_does)
                            spot=spt.get()
                            sql_icld="INSERT INTO INCLUDES(b_code,s_code) VALUES("+res[0]+",'"+spot+"');"
                            cursor.execute(sql_icld)
                            equip=eqp.get()
                            sql_eqp="insert into RENTS(bk_code,e_code) values ("+res[0]+",'"+equip+"');"
                            cursor.execute(sql_eqp)
                            connection.commit()  
                            i=20
                            for row in cursor:
                                    canvas.delete(ALL)
                                    canvas.create_text(200,20+i,font=("Arial", "10"),text=row)
                                    canvas.configure(scrollregion=canvas.bbox("all"))
                                    i=i+20
                    except pymysql.Error as error:
                            print("Failed to insert record into table {}".format(error))   
                            insert_res()
                    

    lbl = Label(canvas1, text="Client: id,name,surname,phone number", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=40)
    client = Entry(canvas1,width=60)
    client.grid(column=0, row=60)
    lbl = Label(canvas1, text="Reservation:booking code,no of campers,category,\narrival date,departure date,check in,check out,discount", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=80)
    reserv = Entry(canvas1,width=60)
    reserv.grid(column=0, row=100)
    
    lbl = Label(canvas1, text="select spot", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=120)
    spt = Entry(canvas1,width=60)
    spt.grid(column=0, row=140)
    
    lbl = Label(canvas1, text="select equipment", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=160)
    eqp = Entry(canvas1,width=60)
    eqp.grid(column=0, row=180)
    
    btn = Button(canvas1, text="New Client", font=("Arial", 10), bg='grey',command=new_client)
    btn.grid(column=0, row=200)
    btn = Button(canvas1, text="New Reservation", font=("Arial", 10), bg='grey',command=new_res)
    btn.grid(column=0, row=220)
#insert payment
def ins_paym():
    today=str(date.today())
    canvas1.delete(ALL)
    canvas.delete(ALL)
    canvas.create_text(200,0,font=("Arial", "10"),text='Please write the values separated with , " ",')
    canvas.configure(scrollregion=canvas.bbox("all"))
    def execute():
            with connection.cursor() as cursor:
                    client_id=clientid.get()
                    p_code=paymentcode.get()
                    p_method=p_meth.get()
                    bk_code=bcode.get()
                    sql_pays="INSERT INTO PAYS (client_id,payment_code,payment_date) VALUES ('"+client_id+"','"+p_code+"','"+today+"');"
                    sql_payment="INSERT INTO PAYMENT(p_code,payment_method) VALUES ('"+p_code+"','"+p_method+"');"
                    sql_con="insert into CONNECTS (pm_code,bkng_code) values ('"+p_code+"','"+bk_code+"');"    
                    try:
                            cursor.execute(sql_payment)
                            cursor.execute(sql_pays)
                            cursor.execute(sql_con)
                            #print table
                            canvas.delete(ALL)
                            canvas.create_text(200,0,font=("Arial", "10"),text="new client")
                            canvas.configure(scrollregion=canvas.bbox("all"))
                            i=20
                            for row in cursor:
                                    canvas.create_text(200,20+i,font=("Arial", "10"),text=row)
                                    canvas.configure(scrollregion=canvas.bbox("all"))
                                    i=i+20
                    except pymysql.Error as error:
                            print("Failed to insert record into Client table {}".format(error))
                    

    lbl = Label(canvas1, text="Client id:", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=40)
    clientid = Entry(canvas1,width=60)
    clientid.grid(column=0, row=60)
    
    lbl = Label(canvas1, text="Insert a new unique payment code(int)", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=80)
    paymentcode = Entry(canvas1,width=60)
    paymentcode.grid(column=0, row=100)
    
    lbl = Label(canvas1, text="select payment method 'CASH','CREDIT CARD','DEBIT CARD' OR 'PAYPAL'", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=120)
    p_meth = Entry(canvas1,width=60)
    p_meth.grid(column=0, row=140)
    
    lbl = Label(canvas1, text="Booking code:", font=("Arial", 10),bg='AntiqueWhite2')
    lbl.grid(column=0, row=160)
    bcode = Entry(canvas1,width=60)
    bcode.grid(column=0, row=180)
    
    btn = Button(canvas1, text="Execute", font=("Arial", 10), bg='grey',command=execute)
    btn.grid(column=0, row=200)

    
#Starting Screen
            
def start_screen():
    #Create window
    start= Tk()
    start.title('Welcome to Camp32 Database System')
    start.geometry("900x800+150+0")
    start.configure(background="AntiqueWhite2")
    #Create canvas
    canvas = Canvas(start, width = 600, height = 600)      
    canvas.pack(side = TOP, pady = 5)
    #Logo
    img = PhotoImage(file="logo_32.png")      
    canvas.create_image(0,0,anchor=NW, image=img)
    #Start Button
    button = Button(start, text = 'START',font=("Microsoft JhengHei", 10,'bold')) 
    button['command'] = start.destroy
    button.configure(background="AntiqueWhite3")
    button.configure(activebackground="floral white")
    button.pack()
    start.mainloop()

    

#MAIN

def main_menu():
    
# Create window
    global window
    window = Tk()
    window.title('Welcome to Camp32 Database System')
    window.geometry('1200x600')
    window.configure(background="AntiqueWhite2")
       
#label definition
    
    label1 = Label(window, text="Welcome to Camp32 Database System", font=("Arial", 10))
    label1.grid(column=0, row=0)
    label1.configure(background="AntiqueWhite2")
    
#creation of frame under the label
    
    global frame1
    frame1 = Frame(window)
    frame1.grid(column=0, row=40, sticky=NW)
    frame1.configure(background="floral white")
    
#label
    
    label2 = Label(window, text="SQL command output:", font=("Arial", 10))
    label2.grid(column=0,row=100,padx=0,pady=10,sticky=NW)
    label2.configure(background="floral white")
    
##SHOW ERD
    
    btn = Button(frame1, text="ERD", font=("Arial", 10), bg='AntiqueWhite2',command=ER)
    btn.grid(column=10, row=60)
    
##GUEST INFO
    
    btn = Button(frame1, text="Guest info", font=("Arial", 10),bg='AntiqueWhite2',command=guests)
    btn.grid(column=50, row=40)

##RESERVATIONS
    
    btn = Button(frame1, text="Today's Check in / Check out", font=("Arial", 10),bg='AntiqueWhite2')
    btn.grid(column=60, row=40)
    btn['command'] = todays_res

##SHOW DBDESIGNER

    btn = Button(frame1, text="DBSchema", font=("Arial", 10), bg='AntiqueWhite2',command=DB)
    btn.grid(column=20, row=60)
#AVAILABLE SPOTS
    btn = Button(frame1, text="Available spots", font=("Arial", 10),bg='AntiqueWhite2')
    btn.grid(column=30, row=60)
    btn['command'] = spots
#PAYMENTS
    btn = Button(frame1, text="Payments", font=("Arial", 10),bg='AntiqueWhite2')
    btn.grid(column=0, row=60)
    btn['command'] = payments
##Search for price
    btn = Button(frame1, text="Prices", font=("Arial", 10),bg='AntiqueWhite2')
    btn.grid(column=0, row=40)
    btn['command'] = prices
#frame 
    
    global frame
    frame = Frame(window)
    frame.grid(column=0, row=200,padx=0, pady=10 ,sticky=NW)
    frame.configure(background="floral white")
    
#canvas
    
    global canvas
    canvas = Canvas(frame, bg='#ffffff', width=600,height=450)
    canvas.grid(column=0, row=200)
    
#vertical scrollbar
    
    vbar = Scrollbar(frame, orient='vertical',command=canvas.yview)
    vbar.grid(row=200, column=200, sticky=NS)
    canvas.configure(yscrollcommand=vbar.set, background='#ffffff',scrollregion=canvas.bbox("all"))

#horizontal scrollbar
    
    hbar = Scrollbar(frame, orient='horizontal', command=canvas.xview)
    hbar.grid(row=0, column=0, sticky=EW)
    canvas.configure(xscrollcommand=hbar.set, background='#ffffff',scrollregion=canvas.bbox("all"))
    
#frame2
    global frame2
    frame2 = Frame(window)
    frame2.grid(column=1, row=200,padx=20, sticky=NW)
    
#canvas1
    global canvas1
    canvas1 = Canvas(frame2, bg="AntiqueWhite2", width=400,height=400)
    canvas1.grid(column=0, row=200)

#LOGO
      
    photo = PhotoImage(file = "logo_32_in.png")
    canvas1.create_image(200, 200, image=photo)
    
#buttons
    

    btn = Button(frame1, text="Insert data", font=("Arial", 10),bg='AntiqueWhite2',command=insert)
    btn.grid(column=10, row=40)

    btn = Button(frame1, text="Update data", font=("Arial", 10),bg='AntiqueWhite2',command=update)
    btn.grid(column=20, row=40)

    btn = Button(frame1, text="Delete data", font=("Arial", 10),bg='AntiqueWhite2',command=delete_data)
    btn.grid(column=30, row=40)

    btn = Button(frame1, text="SQL Command Submission", font=("Arial", 10),bg='AntiqueWhite2',command=sql_command)
    btn.grid(column=40, row=40)
    btn = Button(frame1, text="New client and reservation", font=("Arial", 10),bg='AntiqueWhite2',command=insert_res)
    btn.grid(column=40, row=60)
    btn = Button(frame1, text="New payment", font=("Arial", 10),bg='AntiqueWhite2',command=ins_paym)
    btn.grid(column=50, row=60)
    window.mainloop()
    



start_screen()
try:
  while True:
        main_menu()
finally:
    connection.close()
