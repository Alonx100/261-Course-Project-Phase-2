#   Alon Rehin
#   CIS261
#   Project Phase 2
def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname
def GetDatesWorked():
   
    fromdate = input("What is the start date? enter the date in mm/dd/yyyy " )
    todate = input("What is the end date? enter the date in mm/dd/yyyy ")

    return fromdate,todate
    




def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

#def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
#    print(empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    # the following code creates a for loop to read through EmpDetailList and assign values in list to variables
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1] 
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        #write code to assign values to todate, empname, hours, hourlyrate, and taxrate from EmpLst




        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print("Employee name:", empname) 
        print("Starting date:", fromdate)
        print("Ending date:", todate) 
        print("Hours worked:", f"{hours:,.2f}") 
        print("Hour rate:", f"{hourlyrate:,.2f}")
        print("Gross pay:", f"{grosspay:,.2f}") 
        print("Tax rate:", f"{taxrate:,.1%}") 
        print("Income tax", f"{incometax:,.2f}")  
        print("Net pay", f"{netpay:,.2f}")
        print()
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        # the following line of code assigns TotEmployees totals to dictionary 
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHou"] = TotHours
        EmpTotals["TotGross"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNet"] = TotNetPay





#def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
 #   print()
  #  print(f"Total Number Of Employees: {TotEmployees}")
   # print(f"Total Hours Worked: {TotHours:,.2f}")
    #print(f"Total Gross Pay: {TotGrossPay:,.2f}")
    #print(f"Total Income Tax:  {TotTax:,.2f}")
    #print(f"Total Net Pay: {TotNetPay:,.2f}")

def PrintTotals(EmpTotals):    
    print()
    # use dictionary to print totals
    # the following line of code prints Total Employees from the dictionary
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    # write code to print TotalHrs, TotGrossPay, TotTax and TotNetPay from dictionary
    print(f'Total Number Of Hours: {EmpTotals["TotHou"]}')
    print(f'Total Number Of Groos Pay: {EmpTotals["TotGross"]}')
    print(f'Total Tax: {EmpTotals["TotTax"]}')
    print(f'Total Net Pay: {EmpTotals["TotNet"]}')





if __name__ == "__main__":
   # TotEmployees = 0
    #TotHours = 0.00
    #TotGrossPay = 0.00
    #TotTax = 0.00
    #TotNetPay = 0.00

    EmpDetailList = []
    EmpTotals = {
       "TotEmp" : "" ,
       "TotHou" : "" , 
       "TotGross" : "" ,
       "TotTax" :  "" ,
       "TotNet" : "" ,
                }

    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()

       # grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        #printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)

        #write code to insert fromdate, todate, empname, hours, hourlyrate, and taxrate into list EmpDetail
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]

        #the following code appends the list EmpDetail to the list EmpDetailList
        EmpDetailList.append(EmpDetail)


        #TotEmployees += 1
        #TotHours += hours
        #TotGrossPay += grosspay
        #TotTax += incometax
        #TotNetPay += netpay
    printinfo(EmpDetailList)
    PrintTotals (EmpTotals)



