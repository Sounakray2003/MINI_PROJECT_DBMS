import pymongo

from flask import Flask, render_template, request

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MINI_PROJECT"]

mycol_1 = mydb["item"]
mycol_2 = mydb["customer_detail"]
mycol_3 = mydb["Billing"]
mycol_4 = mydb["Shipping"]


@app.route("/index1")
def index1():
    return render_template("index1.html")


@app.route("/process1", methods=["GET", "POST"])
def process1():
    user_input1 = request.form["user_input1"]
    user_input2 = request.form["user_input2"]
    user_input3 = request.form["user_input3"]
    user_input4 = request.form["user_input4"]
    user_input5 = request.form["user_input5"]

    mycol_1.insert_one(
        {
            "item_name": user_input1,
            "item_id": user_input2,
            "Initial_Quantity": user_input3,
            "Current_Quantity": user_input3,
            "Location": user_input4,
            "Price": user_input5,
        }
    )
    return "Data inserted successfully"


@app.route("/index2")
def index2():
    return render_template("index2.html")


@app.route("/process2", methods=["GET", "POST"])
def process2():
    user_input1 = request.form["user_input9"]
    user_input2 = request.form["user_input6"]
    user_input3 = request.form["user_input7"]
    user_input4 = request.form["user_input8"]

    mycol_4.insert_one(
        {
            "item_name": user_input1,
            "item_id": user_input2,
            "Shipped_Location": user_input3,
            "DATE": user_input4,
        }
    )
    return "Data inserted successfully"


if __name__ == "__main__":
    app.run(debug=True)


# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["MINI_PROJECT"]

# mycol_1=mydb["item"]
# mycol_2=mydb["customer_detail"]
# mycol_3=mydb["Billing"]
# mycol_4=mydb["Shipping"]

# num_1=int(input("Enter number of items:"))

# for i in range(num_1):
#     name=input("ENter name of item")
#     id=int(input("Enter item_id of "+name+" :"))
#     iq=int(input("Enter initial_quantity"))
#     loc=input("Enter location:")
#     price=int(input("Enter price:"))

#     mycol_1.insert_one({"item_name":name,"item_id":id,"Initial_Quantity":iq,
#                         "Current_Quantity":iq,"Location":loc,"Price":price})


# num_2=int(input("Enter number of shipped items:"))

# for i in range(num_2):
#     name=input("ENter name of item")
#     id=int(input("Enter item_id of "+name+" :"))
#     s_l=int(input("Enter shipped location"))
#     date=input("Enter shipping date as dd/mm/yyyy format:")

#     mycol_4.insert_one({"item_name":name,"item_id":id,"Shipped location":s_l,
#                         "Date":date})
