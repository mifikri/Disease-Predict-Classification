import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
import matplotlib.pyplot as plt

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease = [
'(vertigo) Paroymsal  Positional Vertigo',
'AIDS',
'Acne',
'Alcoholic hepatitis',
'Allergy',
'Arthritis',
'Bronchial Asthma',
'Cervical spondylosis',
'Chicken pox',
'Chronic cholestasis',
'Common Cold',
'Dengue',
'Diabetes ',
'Dimorphic hemmorhoids(piles)',
'Drug Reaction',
'Fungal infection',
'GERD',
'Gastroenteritis',
'Heart attack',
'Hepatitis B',
'Hepatitis C',
'Hepatitis D',
'Hepatitis E',
'Hypertension',
'Hyperthyroidism',
'Hypoglycemia',
'Hypothyroidism',
'Impetigo',
'Jaundice',
'Malaria',
'Migraine',
'Osteoarthristis',
'Paralysis (brain hemorrhage)',
'Peptic ulcer diseae',
'Pneumonia',
'Psoriasis',
'Tuberculosis',
'Typhoid',
'Urinary tract infection',
'Varicose veins',
'hepatitis A']

def save_model(model):
    json_model = model.to_json()
    open('model.json','w').write(json_model)
    model.save_weights('model_weights.h5', overwrite=True)

df = pd.read_csv('Training.csv')
dfTest = pd.read_csv('Testing.csv')

X = df[l1]
Y = df[['prognosis']]

XT = dfTest[l1]
YT = dfTest[['prognosis']]

encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
dummyY = np_utils.to_categorical(encoded_Y)

encoder.fit(YT)
encodedTest_Y = encoder.transform(YT)
dummyTestY = np_utils.to_categorical(encodedTest_Y)

xTrain, _, yTrain,_ = train_test_split(X, dummyY, test_size=0, random_state=0)
_, xTest, _,yTest = train_test_split(XT, dummyTestY, train_size=0, random_state=0)


model = Sequential()
model.add(Dense(400, input_dim=xTrain.shape[1], activation='relu'))
model.add(Dense(41, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

history = model.fit(xTrain,yTrain,validation_data=(xTest,yTest), batch_size=10,epochs=10, verbose=1)
ypred = np.argmax(model.predict(xTest), axis=1)
yreal = np.argmax(yTest, axis=1)
final_train_accuracy = np.mean((ypred == yreal).astype(np.float32))
print 'Accuracy on the training set:', final_train_accuracy
print ypred
print encoder.inverse_transform(ypred)

save_model(model)

plt.plot(history.history['acc'], label='acc')
plt.plot(history.history['val_acc'], label='val_acc')
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model acc')
plt.ylabel('acc')
plt.xlabel('Epoch')
plt.legend(['Train'], loc='upper left')
plt.show()