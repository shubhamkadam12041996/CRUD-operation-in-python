from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template("index.html");  
 
@app.route("/add")  
def add():  
    return render_template("add.html")  
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            productname = request.form["name"]  
            productdescription = request.form["des"]   		
            productprise = request.form["prise"]  
            productquantity = request.form["quantity"]				
            imagepath = request.form["path"]           
            with sqlite3.connect("product.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into product (pname, pdes,Prise,quantity , pimg) values (?,?,?,?,?)",(productname,productdescription,productprise,productquantity,imagepath))  
                con.commit()  
                msg = "product Added successfully"
                
        except:  
            con.rollback()  
            msg = "We can not add the product to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()  
 
@app.route("/view")  
def view():  
    con = sqlite3.connect("product.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from product")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  
 
@app.route("/Edit")  
def Edit():
	con = sqlite3.connect("product.db")
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("select * from product")
	rows = cur.fetchall()
	return render_template("Edit.html",rows = rows)


@app.route("/updateproduct",methods = ["POST","GET"])  
def updateproduct():
    id = request.form["custId"]
    con = sqlite3.connect("product.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from product where pid = ?",id)
    rows = cur.fetchall()
    return render_template("Edit_product.html",rows = rows)
	
@app.route("/delete")  
def delete():  
    return render_template("delete.html")  
 
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("product.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from product where pid = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html",msg = msg)  


@app.route("/updatedetails",methods = ["POST","GET"])  
def updatedetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:
            id = request.form["pid"]
            productname = request.form["name"]  
            productdescription = request.form["des"]   		
            productprise = request.form["prise"]  
            productquantity = request.form["quantity"]				
            imagepath = request.form["path"]           
            with sqlite3.connect("product.db") as con:  
                cur = con.cursor()
                sql_update_query ='''UPDATE product SET pname = ?, pdes = ?,Prise = ?,quantity = ? , pimg = ? WHERE pid = ?''', (productname,productdescription,productprise,productquantity,imagepath, id)
                cur.execute("UPDATE product SET pname = ?  , pdes = ? ,Prise = ?, quantity = ? , pimg = ? where pid = ? ",(productname,productdescription,productprise,productquantity,imagepath, id))
                con.commit()  
                msg = "product Update successfully"
                
        except:  
            con.rollback()  
            msg = "We can not Update product "  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()
            
if __name__ == "__main__":  
    app.run(debug = True)  
