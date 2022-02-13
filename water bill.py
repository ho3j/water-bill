"""
Hossein Jalili
feb-13-2022
version 1.0.0
Issuance of water bill in Isfahan province

"""
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
import jdatetime
import subprocess
import platform
import getpass
import socket

#----------------------------------------------
clear=lambda : os.system("cls")
# jdatetime.set_locale('fa_IR')
now = jdatetime.datetime.now()
#----------------------------------------------

# print("*** start ***")
def ghabz():
    i=1
    lines=[]
    while True:
        print("---------------- try",str(i)," -----------------")
        shenase_id=input('\nBilling ID  for example: 1234567890123\n')
        print('\nBilling ID is: '+shenase_id,"\n")
        if shenase_id.isdigit()==False:
            clear()
            print('\nplease enter a valid number(0-9)\n')
            i += 1
            
        else:
            if len(shenase_id)==13:
                # q=input("Enter 'y' to download png : \n")
                break
            else:
                i += 1
                clear()
                print('\nplease enter a valid 13_number (1234567890123)\n')
                
    #----------------------------------------------

    path = os.path.dirname(os.path.abspath(__file__))
    address=os.path.join(path, 'chromedriver.exe')
    driver = webdriver.Chrome(executable_path=address)
    driver.get('https://crm.abfaesfahan.ir/'+shenase_id+"/Portal/bill")
    #----------------------------------------------
    time.sleep(10)

    try:
        Payment_code=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[3]/p[2]/span[2]').text)
    except:
        Payment_code="can't connect to server"
    try:
        The_row_number=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/p[1]/span[2]').text)
    except:
        The_row_number="can't connect to server"
    try:
        subscription_number_sharing_number=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/p[2]/span[2]').text)
    except:
        subscription_number_sharing_number="can't connect to server"
    try:
        Sheet_number=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/p[3]/span[2]').text)
    except:
        Sheet_number="can't connect to server"
    try:
        user=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/p/span[2]').text)
    except:
        user="can't connect to server"
    try:
        Residential=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div/div[2]/p[1]/span[2]').text)
    except:
        Residential="can't connect to server"
    try:
        Non_residential=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div/div[2]/p[2]/span[2]').text)
    except:
        Non_residential="can't connect to server"
    try:
        Empty_of_residence=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div/div[2]/p[3]/span[2]').text)
    except:
        Empty_of_residence="can't connect to server"
    try:
        Previous_reading_date=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[2]/p[1]/span[2]').text)
    except:
        Previous_reading_date="can't connect to server"
    try:
        Current_reading_date=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[2]/p[2]/span[2]').text)
    except:
        Current_reading_date="can't connect to server"
    try:
        number_of_days=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[3]/div/span[2]').text)
    except:
        number_of_days="can't connect to server"
    try:
        Previous_meter_number=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[4]/div/div[2]/p[1]/span[2]').text)
    except:
        Previous_meter_number="can't connect to server"
    try:
        Current_meter_number=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[4]/div/div[2]/p[2]/span[2]').text)
    except:
        Current_meter_number="can't connect to server"
    try:
        Consumption_in_cubic_meters=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[5]/p[1]/span[2]').text)
    except:
        Consumption_in_cubic_meters="can't connect to server"
    try:
        Consumption_per_liter=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[5]/p[2]/span[2]').text)
    except:
        Consumption_per_liter="can't connect to server"
    try:
        Average_monthly_consumption=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[5]/p[3]/span[2]').text)
    except:
        Average_monthly_consumption="can't connect to server"
    try:
        price_of_water=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/p[1]/span[2]').text)
    except:
        price_of_water="can't connect to server"
    try:
        Sewage_disposal_fee=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/p[2]/span[2]').text)
    except:
        Sewage_disposal_fee="can't connect to server"
    try:
        Taxes_and_duties=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/p[3]/span[2]').text)
    except:
        Taxes_and_duties="can't connect to server"
    try:
        Budget_Law=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/p[4]/span[2]').text)
    except:
        Budget_Law="can't connect to server"
    try:
        Total=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]/p[1]/span[2]').text)
    except:
        Total="can't connect to server"
    try:
        Discount=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]/p[2]/span[2]/span').text)
    except:
        Discount="can't connect to server"
    try:
        Debtor_or_creditor=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]/p[3]/span[2]/span').text)
    except:
        Debtor_or_creditor="can't connect to server"
    try:
        payment_dead_line=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[2]/p[2]/span[2]').text)
    except:
        payment_dead_line="can't connect to server"
    try:
        Payable=(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[2]/p[1]/span[2]/span').text)
    except:
        Payable="can't connect to server"

    time.sleep(2)
    clear()

    print("---------------- try",str(i)," -----------------")
    print("Today is: ",now)
    print("----------------")
    print('your Billing ID is: ',shenase_id)
    print('Payment code is: \t',Payment_code)
    print("----------------")
    print('The row number is: \t',The_row_number)
    print('subscription number sharing number is: \n',subscription_number_sharing_number)
    print('Sheet number is: \t',Sheet_number)
    print("----------------")
    print('user is: ',user,"\n")
    print("Number of units;")
    print('Residential: \t\t',Residential)
    print('Non-residential: \t',Non_residential)
    print('Empty of residence: \t',Empty_of_residence)
    print("----------------")
    print('Previous reading date is: \t',Previous_reading_date)
    print('Current reading date is: \t',Current_reading_date)
    print('Number of days: \t\t',number_of_days)
    print("----------------")
    print('Previous meter number is: \t',Previous_meter_number)
    print('Current meter number is: \t',Current_meter_number)
    print("----------------")
    print('Consumption in cubic meters: \t',Consumption_in_cubic_meters)
    print('Consumption per liter: \t\t',Consumption_per_liter)
    print('Average monthly consumption: \t',Average_monthly_consumption)
    print("----------------")
    print('price of water: \t',price_of_water)
    print('Sewage disposal fee: \t',Sewage_disposal_fee)
    print('Taxes and duties: \t',Taxes_and_duties)
    print('Budget Law: \t\t',Budget_Law)
    print("total: \t\t\t",Total)
    print("discount: \t\t",Discount)
    print("debtor or creditor: \t",Debtor_or_creditor)
    print("----------------")
    print('payment deadline: \t',payment_dead_line)
    print('payable: \t\t',Payable,"Rials")
    print("==========")


    if t.startswith('Y') or t.startswith('y'):
        try:
            lines=lines+[
            " Issuance of water bill in Isfahan province ",
            "\nToday is:             ",str(now),
            "\n----------------",
            "\nyour Billing ID is:     ",shenase_id,
            "\nPayment code is:        ",Payment_code,
            "\n----------------",
            "\nThe row number is:      ",The_row_number,
            "\nSubscription number sharing number is:  ",subscription_number_sharing_number,
            "\nSheet number is:        ",Sheet_number,
            "\n----------------",
            "\nuser is:                ","user",
            "\n\nNumber of units;",
            "\nResidential:            ",Residential,
            "\nNon-residential:        ",Non_residential,
            "\nEmpty of residence:     ",Empty_of_residence,
            "\n----------------",
            "\nPrevious reading date is:  ",Previous_reading_date,
            "\nCurrent reading date is:   ",Current_reading_date,
            "\nNumber of days:  ",number_of_days,
            "\n----------------",
            "\nPrevious meter number is:  ",Previous_meter_number,
            "\nCurrent meter number is:   ",Current_meter_number,
            "\n----------------",
            "\nConsumption in cubic meters:   ",Consumption_in_cubic_meters,
            "\nConsumption per liter:         ",Consumption_per_liter,
            "\nAverage monthly consumption:   ",Average_monthly_consumption,
            "\n----------------",
            "\nprice of water:          ",price_of_water,
            "\nSewage disposal fee:     ",Sewage_disposal_fee,
            "\nTaxes and duties:        ",Taxes_and_duties,
            "\nBudget Law:              ",Budget_Law,
            "\ntotal:                   ",Total,
            "\ndiscount:                ",Discount,
            "\ndebtor or creditor:      ",Debtor_or_creditor,
            "\n----------------",
            "\npayment deadline:        ",payment_dead_line,
            "\npayable:                 ",Payable,"Rials"]

            # print(lines)
            t_time="-"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(now.hour)+"-"+str(now.second)              
            
            with open(str(shenase_id)+t_time+'.txt', 'w') as f:
                for line in lines:
                    f.write(line)
                    f.write('\n')
        except:
            print("\ncan't save file")

    print("\n10 sec utill quit ")
    time.sleep(10)
    driver.quit()
    # print("\nquit is done\n")
    print("----------------------------------------------")

clear()
while True:
    clear()
    print("\nDeveloped by #ho3j ")
    print("____________________________________")
    try:
        
        host_name = socket.gethostname()
        ip_addr = socket.gethostbyname(host_name)
        print("os : \t\t\t",platform.system())
        print("Windows version : \t",platform.release())
        # print("Windows 32/64bit : \t",platform.machine())
        # print("Windows User : \t\t",getpass.getuser())
        print ("Host Name: \t\t {0}".format(host_name))
        print ("IP Address: \t\t {0}".format(ip_addr))
    except:
        print("can not print Information of windows ")

    try:
        print("____________________________________\n")
        print("                Hi, Good Luck ",getpass.getuser())
        # print("----------")
        print("""
                    Issuance of 
             water bill in Isfahan province
        |*************************************|
        |   1 :  Show only in the app         |
        |   2 :  View and with save txt file  |
        |   3 :  quit app                     |
        ***************************************
        """)
        i=int(input("Enter number of function :\t"))
        if i ==1:
            
            t="n"
            ghabz()
        elif i==2:
            
            t="y"
            ghabz()
        elif i==3:

            break
        else :
            clear()
            print("wrong  number !!! " ,end="\n \n")
            print( end=" ")
            qq = input("Enter 'Q' to quit app \n or 'Enter' to continue : \t ").lower()
            if qq =="q" :
                break
            else :
                clear()
                continue
    except:
        clear()
        print("Enter number !")

#----------------------------------------------