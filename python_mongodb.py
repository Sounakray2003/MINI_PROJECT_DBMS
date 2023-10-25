import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MINI_PROJECT"]

mycol_1=mydb["item"]
mycol_2=mydb["customer_detail"]
mycol_3=mydb["Billing"]
mycol_4=mydb["Shipping"]

num_1=int(input("Enter number of items:"));

for i in range(num_1):
    name=input("ENter name of item")
    id=int(input("Enter item_id of "+name+" :"))
    iq=int(input("Enter initial_quantity"))
    loc=input("Enter location:")
    price=int(input("Enter price:"))

    mycol_1.insert_one({"item_name":name,"item_id":id,"Initial_Quantity":iq,
                        "Current_Quantity":iq,"Location":loc,"Price":price})
