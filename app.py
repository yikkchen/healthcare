from flask import Flask, render_template, request

app = Flask(__name__)

# 設定健康建議的函數
def get_health_advice(blood_pressure, blood_sugar, height, weight):
    # 將建議按健康指標分成字典形式
    fontLargestStrong = {'blood_pressure': [], 'blood_sugar': [], 'bmi': []}
    fontSecondStrong = {'blood_pressure': [], 'blood_sugar': [], 'bmi': []}
    fontNormalStrong = {'blood_pressure': [], 'blood_sugar': [], 'bmi': []}
    fontNormal = {'blood_pressure': [], 'blood_sugar': [], 'bmi': []}
    
    # 血壓建議
    if isinstance(blood_pressure, float):
        if blood_pressure > 130:
            fontSecondStrong['blood_pressure'].append("高血壓症狀：")
            fontSecondStrong['blood_pressure'].append("高血壓發病原因：")
            fontLargestStrong['blood_pressure'].append("Your blood pressure is high. Consider reducing salt intake and managing stress.")
            fontNormalStrong['blood_pressure'].append("1. 遺傳(多基因型)")
            fontNormalStrong['blood_pressure'].append("2. 環境因素")
        elif blood_pressure < 90:
            fontSecondStrong['blood_pressure'].append("低血壓症狀：")
            fontSecondStrong['blood_pressure'].append("低血壓發病原因：")
            fontLargestStrong['blood_pressure'].append("Your blood pressure is low. Consider increasing salt intake and managing stress.")
        else:
            fontSecondStrong['blood_pressure'].append("正常：")
            fontLargestStrong['blood_pressure'].append("Your blood pressure is normal. Keep it up!")
    else:
        fontLargestStrong['blood_pressure'].append("No blood pressure data")

    # 血糖建議
    if isinstance(blood_sugar, float):
        if blood_sugar > 140:
            fontLargestStrong['blood_sugar'].append("Your blood sugar is high. Monitor your sugar intake and consider a low-sugar diet.")
        elif blood_sugar < 70:
            fontLargestStrong['blood_sugar'].append("Your blood sugar is low. Consider a high-sugar diet.")
        else:
            fontLargestStrong['blood_sugar'].append("Your blood sugar is normal. Keep it up!")
    else:
        fontLargestStrong['blood_sugar'].append("No blood sugar data")

    # BMI 建議
    if isinstance(weight, float) and isinstance(height, float):
        bmi = round(weight / (height / 100) ** 2, 2)
        if bmi > 25:
            fontLargestStrong['bmi'].append(f"Your BMI is {bmi}. It's above the normal range. Regular exercise and a balanced diet can help.")
        elif bmi < 18.5:
            fontLargestStrong['bmi'].append(f"Your BMI is {bmi}. It's below the normal range. You should eat more.")
        else:
            fontLargestStrong['bmi'].append(f"Your BMI is {bmi}. It's within the normal range. Keep it up!")
    else:
        fontLargestStrong['bmi'].append("Not enough data to calculate your BMI")

    return fontLargestStrong, fontSecondStrong, fontNormalStrong, fontNormal

# 主頁面路由
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# 結果頁面路由
@app.route('/result', methods=['POST'])
def result():
    # 取得表單數據
    blood_pressure = float(request.form.get('blood_pressure')) if request.form.get('blood_pressure') else None
    blood_sugar = float(request.form.get('blood_sugar')) if request.form.get('blood_sugar') else None
    height = float(request.form.get('height')) if request.form.get('height') else None
    weight = float(request.form.get('weight')) if request.form.get('weight') else None

    # 取得健康建議
    fontLargestStrong, fontSecondStrong, fontNormalStrong, fontNormal = get_health_advice(blood_pressure, blood_sugar, height, weight)

    return render_template(
        'result.html',
        fontLargestStrong=fontLargestStrong,
        fontSecondStrong=fontSecondStrong,
        fontNormalStrong=fontNormalStrong,
        fontNormal=fontNormal
    )

if __name__ == '__main__':
    app.run(debug=True)
