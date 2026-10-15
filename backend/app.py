import os
from flask import Flask,request,jsonify
from flask_cors import CORS
import pandas as pd,joblib
app=Flask(__name__); CORS(app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model=joblib.load(os.path.join(BASE_DIR, 'placement_model.pkl'))
scaler=joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))
FEATURES=['CGPA','SSC_Marks','HSC_Marks','Internships','Projects','Certifications','AptitudeScore','SoftSkillsRating','Backlogs','Extracurricular','PlacementTraining']
@app.get('/')
def home(): return jsonify({'status':'ok','message':'Placify AI Placement Prediction API'})
@app.post('/predict')
def predict():
    d=request.get_json(force=True)
    row={k:d[k] for k in FEATURES}; row['Extracurricular']=1 if row['Extracurricular']=='Yes' else 0; row['PlacementTraining']=1 if row['PlacementTraining']=='Yes' else 0
    X=pd.DataFrame([row],columns=FEATURES); xs=scaler.transform(X); prob=float(model.predict_proba(xs)[0][1]*100); pred=int(model.predict(xs)[0])
    category='High Chance' if prob>=75 else ('Medium Chance' if prob>=50 else 'Low Chance')
    factors=sorted([(f,abs(float(c))) for f,c in zip(FEATURES,model.coef_[0])],key=lambda x:x[1],reverse=True)[:3]
    suggestions=[]
    if d['Internships']<2: suggestions.append('Add an internship or practical industry experience.')
    if d['Projects']<2: suggestions.append('Build at least one more strong, role-relevant technical project.')
    if d['AptitudeScore']<75: suggestions.append('Practice aptitude and logical reasoning 3–4 times per week.')
    if d['SoftSkillsRating']<4: suggestions.append('Work on communication, mock interviews and presentation skills.')
    if d['Certifications']<2: suggestions.append('Complete a relevant certification aligned with your target role.')
    if not suggestions: suggestions=['Keep strengthening role-specific technical skills.','Practice mock interviews and aptitude regularly.','Quantify project and internship impact on your resume.']
    return jsonify({'prediction':'Placed' if pred else 'Not Placed','probability':round(prob,2),'category':category,'confidence':round(max(prob,100-prob),2),'top_factors':factors,'suggestions':suggestions})
if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
