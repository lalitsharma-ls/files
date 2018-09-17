class Telecom:
    
    plan_details=[]
    
    def __init__(self):
        plan_details=[]
                        
        
    def add_plan(self):
        
        plan_name= input("Input the plan name")
        sms =int(input("Enter the monthly free sms"))
        rental = int(input("Enter the monthly rental"))
        internet = int(input("Enter the monthly free internet"))
        calls = int(input("Enter the monthly free calls"))
        call_charges = int(input("Enter the Call Charges"))
        data_charges = int(input("Enter the Data Charges"))
        roaming = int(input("Enter the User Details"))
       
        dict_of_plan= {'plan': plan_name, 'sms': sms, 'rental': rental, 'internet': internet, 'calls': calls, 'call charges': call_charges, 'data charges': data_charges, 'roaming charges': roaming} 
        
        Telecom.plan_details.append(dict_of_plan)
        
    def show_plan(self):
        for plans in Telecom.plan_details:
            print("plan name"+plans.get(plan_name))
        
    def get_plan(self,plan1):
        for plans in Telecom.plan_details:
            print("user details")
            if plans.get('rental')==plan1:
                print(plan_name)
    plan= Telecom();
    print("***** TELECOM OPERATOR APPLICATION *****")
    cont='y'
    while(cont=='y'):
   
        plan.add_plan()
        print("printing plan details")
        plan.show_plan()
        print("****filter data******")