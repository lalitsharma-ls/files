class blood_bank:
    user_details=[]
    def  __init__(self):
        
        user_detail=[]
        
    
    def add_user(self):
        name=input("enter your name ")
        age=input("enter your age ")
        address=input("enter your address ")
        email_id=input("enter your email id ")
        mobile=int(input("enter your mobile "))
        blood_group=input("enter your blood group ")
        gender=input("enter your gender ")
        
        dict_of_user={'name': name,'age':age,'address':address,'email':email_id,'mobile':mobile,'blood_group':blood_group,'gender':gender}
        blood_bank.user_details.append(dict_of_user);
    
    def show_donor(self):
        for donor in blood_bank.user_details:
            print("name "+donor.get('name'))
    
    def get_data(self,group):
        for donor in blood_bank.user_details:
            print("======user detials=========")
            if donor.get('blood_group') == group:
                print("name "+ donor.get('name'))
                print("name "+ donor.get('age'))
                print("name "+ donor.get('address'))
                print("name "+ str(donor.get('mobile')))
        
        

bank= blood_bank();
print("***** blood_bank *****")
cont='y'
while(cont=='y'):
    
    bank.add_user()
    print("printing user detials")
    bank.show_donor()
    cont=input("enter y to continue else n ")

print("***** filter data ******")
group_blood=input("enter blood group to filter users ")
bank.get_data(group_blood)
    
    