
lowerl1=['back pain','constipation','abdominal pain','diarrhoea','mild fever','yellow urine',
'yellowing of eyes','acute liver failure','fluid overload','swelling of stomach',
'swelled lymph nodes','malaise','blurred and distorted vision','phlegm','throat irritation',
'redness of eyes','sinus pressure','runny nose','congestion','chest pain','weakness in limbs',
'fast heart rate','pain during bowel movements','pain in anal region','bloody stool',
'irritation in anus','neck pain','dizziness','cramps','bruising','obesity','swollen legs',
'swollen blood vessels','puffy face and eyes','enlarged thyroid','brittle nails',
'swollen extremeties','excessive hunger','extra marital contacts','drying and tingling lips',
'slurred speech','knee pain','hip joint pain','muscle weakness','stiff neck','swelling joints',
'movement stiffness','spinning movements','loss of balance','unsteadiness',
'weakness of one body side','loss of smell','bladder discomfort','foul smell of urine',
'continuous feel of urine','passage of gases','internal itching','toxic look (typhos)',
'depression','irritability','muscle pain','altered sensorium','red spots over body','belly pain',
'abnormal menstruation','dischromic  patches','watering from eyes','increased appetite','polyuria','family history','mucoid sputum',
'rusty sputum','lack of concentration','visual disturbances','receiving blood transfusion',
'receiving unsterile injections','coma','stomach bleeding','distention of abdomen',
'history of alcohol consumption','fluid overload','blood in sputum','prominent veins on calf',
'palpitations','painful walking','pus filled pimples','blackheads','scurring','skin peeling',
'silver like dusting','small dents in nails','inflammatory nails','blister','red sore around nose',
'yellow crust ooze']

l1=['Back Pain','Constipation','Abdominal Pain','Diarrhoea','Mild Fever','Yellow Urine',
'Yellowing of Eyes','Acute Liver Failure','Fluid Overload','Swelling of Stomach',
'Swelled Lymph Nodes','Malaise','Blurred and Distorted Vision','Phlegm','Throat Irritation',
'Redness of Eyes','Sinus Pressure','Runny Nose','Congestion','Chest Pain','Weakness in Limbs',
'Fast Heart Rate','Pain During Bowel Movements','Pain in Anal Region','Bloody Stool',
'Irritation in Anus','Neck Pain','Dizziness','Cramps','Bruising','Obesity','Swollen Legs',
'Swollen Blood Vessels','Puffy Face and Eyes','Enlarged Thyroid','Brittle Nails',
'Swollen Extremeties','Excessive Hunger','Extra Marital Contacts','Drying and Tingling Lips',
'Slurred Speech','Knee Pain','Hip Joint Pain','Muscle Weakness','Stiff Neck','Swelling Joints',
'Movement Stiffness','Spinning Movements','Loss of Balance','Unsteadiness',
'Weakness of One Body Side','Loss of Smell','Bladder Discomfort','Foul Smell of Urine',
'Continuous Feel of Urine','Passage of Gases','Internal Itching','Toxic Look (Typhos)',
'Depression','Irritability','Muscle Pain','Altered Sensorium','Red Spots Over Body','Belly Pain',
'Abnormal Menstruation','Dischromic  Patches','Watering From Eyes','increased Appetite','Polyuria','Family History','Mucoid Sputum',
'Rusty Sputum','Lack of Concentration','Visual Disturbances','Receiving Blood Transfusion',
'Receiving Unsterile Injections','Coma','Stomach Bleeding','Distention of Abdomen',
'History of Alcohol Consumption','Fluid Overload','Blood in Sputum','Prominent Veins on Calf',
'Palpitations','Painful Walking','Pus Filled Pimples','Blackheads','Scurring','Skin Peeling',
'Silver Like Dusting','Small Dents in Nails','Inflammatory Nails','Blister','Red Sore Around Nose',
'Yellow Crust Ooze']

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

def symtompsInput():
    l2=[]
    for x in range(0,len(lowerl1)):
        l2.append(0)
    return l2
