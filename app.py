from flask import Flask, render_template, request, send_from_directory
import jsonify
import requests
import pickle
import numpy as np
import sklearn
#from tensorflow import keras

app = Flask(__name__)
model = pickle.load(open('randomforest.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')


def Home():
    return render_template('home.html')
#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        
        Gender = request.form['Gender']
        if(Gender=='Male'):
            Gender=0
        else:
            Gender=1
        
        ms = request.form['Marital status']
        if(ms=='Unmarried'):
            ms=0
        else:
            ms=1
        
        profession= request.form['Profession']
        if(profession=='Student'):
            profession=0
        elif(profession=='Employed'):
            profession=1
        else:
            profession=2

        lwf=request.form['Living With Family']
        if(lwf=='Yes'):
            lwf=0
        else:
            lwf=1

        sd=request.form['Sleeping Duration']
        if(sd=='8-10 hours'):
            sd=0
        elif(sd=='6-8 hours'):
            sd=1
        elif(sd=='4-6 hours'):
            sd=2
        else:
            sd=3

        pc = request.form['Tested Positive For COVID']
        if(pc=='Yes'):
            pc=1
        else:
            pc=0
        
        depressed=request.form['Depression Problems From Past']
        if(depressed=='Yes'):
            depressed=1
        else:
            depressed=0

        stilldepressed=request.form['Still Having Depression']
        if(stilldepressed=='Yes'):
            stilldepressed=0
        else:
            stilldepressed=1

        dt=request.form['Depression tenure']
        if(dt=='1- 3 month'):
            dt=0
        elif(dt=='more than 3 months'):
            dt=1
        elif(dt=='less then a week'):
            dt=2
        else:
            dt=3
        
        pa=request.form['Physical Activities']
        if(pa=='30min - 1hr'):
            pa=0
        elif(pa=='1-2 hr'):
            pa=1
        elif(pa=='2-3 hr'):
            pa=2
        elif(pa=='3-4 hr'):
            pa=3
        elif(pa=='4 + hr'):
            pa=4
        else:
            pa=5
        
        rd=request.form['Regular Diet']
        if(rd=='5'):
            rd=0
        elif(rd=='4 meals/day'):
            rd=1
        elif(rd=='3 meals/day'):
            rd=2
        elif(rd=='2 meals/day'):
            rd=3
        else:
            rd=4

        ft=request.form['Family Time']
        if(ft=='Frequently'):
            ft=0
        elif(ft=='Sometimes'):
            ft=1
        elif(ft=='Once or Twice a week'):
            ft=2
        else:
            ft=3

        lostcovid=request.form['Lost someone due to COVID']
        if(lostcovid=='Yes'):
            lostcovid=1
        else:
            lostcovid=0
        
        owntime=request.form['Hours spent on your own per day']
        if(owntime=='More than 2'):
            owntime=0
        elif(owntime=='Not at all'):
            owntime=1
        elif(owntime=='1 - 2'):
            owntime=2
        else:
            owntime=3

        club=request.form['Member of any club']
        if(club=='Yes'):
            club=1
        else:
            club=0
        
        fdt=request.form['Time With Friends']
        if(fdt=='Frequently'):
            fdt=0
        elif(fdt=='Sometimes'):
            fdt=1
        elif(fdt=='Once or Twice in a week'):
            fdt=2
        else:
            fdt=3

        socialmed=request.form['Do you have Social Media Addiction']
        if(socialmed=='Yes'):
            socialmed=0
        elif(socialmed=='Maybe'):
            socialmed=1
        else:
            socialmed=2

        worried=request.form['Worried all the time']
        if(worried=='Yes'):
            worried=0
        else:
            worried=1

        irritated=request.form['Got easily annoyed or irritable']
        if(irritated=='Yes'):
            irritated=0
        else:
            irritated=1
        
        explorer=request.form['Explorer']
        if(explorer=='love to explore'):
            explorer=2
        elif(explorer=='Little'):
            explorer=1
        else:
            explorer=0

        overreact=request.form['Tended to overreact on Situations']
        if(overreact=='Sometimes'):
            overreact=0
        elif(overreact=='Frequently'):
            overreact=1
        elif(overreact=='Rarely'):
            overreact=2
        else:
            overreact=3
        
        quote=request.form['Select a Quote']
        if(quote=='q1'):
            quote=0
        elif(quote=='q2'):
            quote=1
        elif(quote=='q3'):
            quote=2
        elif(quote=='q4'):
            quote=3
        elif(quote=='q5'):
            quote=4
        elif(quote=='q6'):
            quote=5
        elif(quote=='q7'):
            quote=6
        else:
            quote=7




        prediction=model.predict([[Age,Gender,ms,profession,lwf,sd,pc,depressed,stilldepressed,dt,pa,rd,ft,lostcovid,owntime,club,fdt,socialmed,
        worried,irritated,explorer,overreact,quote]])
        output=prediction[0]
        if output==0:
            return render_template('sad.html')
        else:
            return render_template('happy.html')
    
if __name__=="__main__":
    app.run(debug=True)