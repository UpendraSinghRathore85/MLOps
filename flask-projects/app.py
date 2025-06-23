from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return 'Hello, Upendra, this is my first flask app!'

@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}! This is a Flask route with a parameter."


@app.route("/aboutus", methods=["GET"])
def aboutus():
    return "Hello we are mlOps learners."


model_pickle = open("classifier.pkl", "rb")
clf = pickle.load(model_pickle)

@app.route('/predict', methods=['POST'])
def predict():
    loan_req = request.get_json()
    print(loan_req)
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']

    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status": pred}




if __name__ == '__main__':
    app.run(debug=True)
