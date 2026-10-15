import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

DATA='placement_data.csv'
FEATURES=['CGPA','SSC_Marks','HSC_Marks','Internships','Projects','Certifications','AptitudeScore','SoftSkillsRating','Backlogs','Extracurricular','PlacementTraining']

data=pd.read_csv(DATA)
for c in ['Extracurricular','PlacementTraining']:
    data[c]=data[c].map({'Yes':1,'No':0})
data['PlacementStatus']=data['PlacementStatus'].map({'Placed':1,'Not Placed':0})
X=data[FEATURES]; y=data['PlacementStatus']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
scaler=StandardScaler(); X_train=scaler.fit_transform(X_train); X_test=scaler.transform(X_test)
model=LogisticRegression(max_iter=1000,random_state=42); model.fit(X_train,y_train)
pred=model.predict(X_test); print('Accuracy:',round(accuracy_score(y_test,pred)*100,2),'%'); print(classification_report(y_test,pred))
joblib.dump(model,'placement_model.pkl'); joblib.dump(scaler,'scaler.pkl'); print('Saved placement_model.pkl and scaler.pkl')
