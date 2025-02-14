# Import libraries
from flask import Flask, render_template, request, redirect, url_for

app = Flask("Inna App")

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Instantiate Flask functionality

# Sample data

# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)


# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "GET":
        return render_template('form.html')

    
    transation = {
            'id': len(transactions)+1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
            }
    transactions.append(transation)
    return redirect(url_for('get_transactions'))   

# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method=="GET":
        for transaction in transactions:
            if(transaction["id"] == transaction_id):
                return render_template("edit.html", transaction=transaction)
    if request.method=="POST":
        for transaction in transactions:
            if(transaction["id"] == transaction_id):
                transaction["date"] = request.form["date"]
                transaction["amount"] = request.form["amount"]
                return redirect(url_for('get_transactions'))

    return {"message": "Transaction not found"}, 404


# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    print(f"Inna: {transaction_id}")
    for transaction in transactions:
        print(f'Inna Check: {transaction["id"]}')
        if transaction["id"] == transaction_id :
            transactions.remove(transaction)
            return redirect(url_for("get_transactions"))
    return {"message": "Transaction not found"}, 404


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
    