# Import libraries
from Flask import flask, render_template, 
    request, redirect

app = flask("Inna App")

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
    render_template("transactions.html", transactions=transactions)


# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "GET":
        return render_template('form.html')

    
    transation = {
            'id': len(transactions)+1
            'date': request.form['date']
            'amount': float(request.form['amount'])
            }
    transactions.append(transaction)
    return redirect.for_url('get_transactions')   

# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method=="GET":
        for transaction in transactions:
            if(transaction.id == transaction_id):
                return render_template("edit.html", transaction)
    if request.method=="POST":
        for transaction in transactions:
            if(transaction.id == transaction_id):
                transaction.data = request.form.data;
                transaction.date = request.form.date;
                return redirect(for_url('get_transactions'))

    return {"message": "Transaction not found", 404}



# Delete operation

# Run the Flask app
    