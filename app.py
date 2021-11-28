from flask import Flask, render_template, request
import burntcalories as bc

app=Flask(__name__)

@app.route("/")
def submit():
    return render_template("index.html")

@app.route("/",methods=['GET','POST'])
def home():
    if request.method=='POST':
        Gender=int(request.form['Gender'])
        Age=int(request.form['Age'])
        Height=int(request.form['Height'])
        Weight=int(request.form['Weight'])
        Duration=int(request.form['Duration'])
        Heart_Rate=int(request.form['Heart_Rate'])
        Body_Temp=int(request.form['Body_Temp'])
        calories=bc.predict_burnt_calories(Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp)
        cals = calories
        
    return render_template("index.html",predicted_calories=cals)




if __name__=="__main__":
    app.run(debug=True)