from flask import Flask, render_template, request

app = Flask(__name__)

# 設定健康建議的函數
def get_health_advice(blood_pressure, blood_sugar, bmi):
    advice = []
    if type(blood_pressure) is float:
        if blood_pressure > 130:
            advice.append("Your blood pressure is high. Consider reducing salt intake and managing stress.")
        elif blood_pressure < 90:
            advice.append("Your blood pressure is Low. Consider incresing salt intake and managing stress.")
        else:
            advice.append("Your blood pressure is normal. Keep it up!!!")
    else:
        advice.append("No bloood_pressure data")
    if type(blood_sugar) is float:
        if blood_sugar > 140:
            advice.append("Your blood sugar is high. Monitor your sugar intake and consider a low-sugar diet.")
        elif blood_sugar < 70:
            advice.append("Your blood sugar is low. Monitor your sugar intake and consider a high-sugar diet.")
        else:
            advice.append("Your blood sugar is normal. Keep it up!!!")
    else:
        advice.append("No blood_sugar data")
    if type(bmi) is float:
        if bmi > 25:
            advice.append("Your BMI is above the normal range. Regular exercise and a balanced diet can help.")
        elif bmi < 18.5:
            advice.append("Your BMI is below the normal range. you should eat more food")
        else:
            advice.append("Your BMI is normal range. Keep it up!!!")
    else:
        advice.append("No bmi data")

    if not advice:
        advice.append("Your health metrics are within the normal range. Keep up the good work!")

    return advice

# 主頁面路由
@app.route('/', methods=['GET', 'POST'])
def index():
    health_advice = None
    #type(request.form.get('blood_pressure')) is str
    if request.method == 'POST':
        if request.form.get('blood_pressure') != '':
            blood_pressure = float(request.form.get('blood_pressure'))
        else:
            blood_pressure = "NaN"
        if request.form.get('blood_sugar') != '':
            blood_sugar = float(request.form.get('blood_sugar'))
        else:
            blood_sugar = "NaN"
        if request.form.get('bmi') != '':
            bmi = float(request.form.get('bmi'))
        else:
            bmi = "NaN"
        
        # 取得健康建議
        health_advice = get_health_advice(blood_pressure, blood_sugar, bmi)
        
    return render_template('index.html', health_advice=health_advice)

if __name__ == '__main__':
    app.run(debug=True)
