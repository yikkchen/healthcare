from flask import Flask, render_template, request

app = Flask(__name__)

# 設定健康建議的函數
def get_health_advice(blood_pressure, blood_sugar, bmi):
    advice = []
    if blood_pressure > 130:
        advice.append("Your blood pressure is high. Consider reducing salt intake and managing stress.")
    if blood_sugar > 140:
        advice.append("Your blood sugar is high. Monitor your sugar intake and consider a low-sugar diet.")
    if bmi > 25:
        advice.append("Your BMI is above the normal range. Regular exercise and a balanced diet can help.")

    if not advice:
        advice.append("Your health metrics are within the normal range. Keep up the good work!")

    return advice

# 主頁面路由
@app.route('/', methods=['GET', 'POST'])
def index():
    health_advice = None
    if request.method == 'POST':
        blood_pressure = float(request.form.get('blood_pressure'))
        blood_sugar = float(request.form.get('blood_sugar'))
        bmi = float(request.form.get('bmi'))
        
        # 取得健康建議
        health_advice = get_health_advice(blood_pressure, blood_sugar, bmi)
        
    return render_template('index.html', health_advice=health_advice)

if __name__ == '__main__':
    app.run(debug=True)
