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

@app.route("/index3")
def index3():
    return render_template("index3.html")


@app.route("/process3", methods=["GET", "POST"])
def process3():
    user_input1 = request.form["user_input10"]
    user_input2 = request.form["user_input11"]
    user_input3 = request.form["user_input12"]
    user_input4 = request.form["user_input13"]

    mycol_2.insert_one(
        {
            "Customer_name": user_input1,
            "Order_id": user_input2,
            "item_ordered": user_input3,
            "customer_location": user_input4,
        }
    )
    return "Data inserted successfully"

@app.route("/index4")
def index4():
    return render_template("index4.html")


@app.route("/process4", methods=["GET", "POST"])
def process4():
    user_input1 = request.form["user_input14"]
    user_input2 = request.form["user_input15"]
    user_input3 = request.form["user_input16"]
    user_input4 = request.form["user_input17"]
    user_input5 = request.form["user_input18"]
    user_input6 = request.form["user_input19"]
    mycol_3.insert_one(
        {
            "Order_date": user_input1,
            "item_id": user_input2,
            "Order_key": user_input3,
            "Quatity": user_input4,
            "item_key": user_input5,
            "Amount": user_input6,
        }
    )
    return "Data inserted successfully"

if __name__ == "__main__":
    app.run(debug=True)

