from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 設定健康建議的函數
def get_health_advice(blood_pressure, blood_sugar, bmi):
    advice = []
    
    # 血壓建議
    if blood_pressure and blood_pressure > 140:
        advice.append("警告：您的血壓偏高，請儘快就醫。")
    elif blood_pressure and blood_pressure < 90:
        advice.append("警告：您的血壓過低，請多休息並保持水分。")
    
    # 血糖建議
    if blood_sugar and blood_sugar > 126:
        advice.append("警告：您的血糖過高，請及時檢查。")
    elif blood_sugar and blood_sugar < 70:
        advice.append("警告：您的血糖過低，請立即補充糖分。")
    
    # BMI建議
    if bmi:
        if bmi < 18.5:
            advice.append("您的體重過輕，請保持均衡飲食。")
        elif 18.5 <= bmi < 24.9:
            advice.append("您的體重正常，繼續保持健康生活方式。")
        elif bmi >= 25:
            advice.append("您的體重過重，建議進行適當的運動及飲食控制。")
    
    if not advice:
        advice.append("您的健康指標正常，請繼續保持！")
    
    return advice

# 主頁路由
@app.route('/')
def home():
    return render_template('home.html')

# 輸入資訊頁路由
@app.route('/input', methods=['GET', 'POST'])
def input_info():
    health_advice = None

    if request.method == 'POST':
        blood_pressure = request.form.get('blood_pressure')
        blood_sugar = request.form.get('blood_sugar')
        height = request.form.get('height')
        weight = request.form.get('weight')

        # 檢查數值並轉換
        blood_pressure = float(blood_pressure) if blood_pressure else None
        blood_sugar = float(blood_sugar) if blood_sugar else None
        height = float(height) if height else None
        weight = float(weight) if weight else None

        # 計算BMI
        bmi = None
        if height and weight:
            height_m = height / 100
            bmi = weight / (height_m ** 2)

        # 健康建議邏輯
        health_advice = get_health_advice(blood_pressure, blood_sugar, bmi)

    return render_template('input.html', health_advice=health_advice)

if __name__ == '__main__':
    app.run(debug=True)

