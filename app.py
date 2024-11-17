from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    blood_pressure = float(request.form['blood_pressure'])
    blood_sugar = float(request.form['blood_sugar'])
    height = float(request.form['height']) / 100  # 轉換成公尺
    weight = float(request.form['weight'])
    
    # 計算 BMI
    bmi = weight / (height ** 2)
    
    # 根據 BMI 給出建議
    if bmi >= 27:
        bmi_advice = "啊～「肥胖」，需要立刻力行「健康體重管理」囉！建議減少高脂肪、高糖食物的攝取，如甜點、油炸食物、含糖飲料等。多選擇富含纖維的食物，例如蔬菜、水果和全穀類，有助於增加飽足感。增加有氧運動，如快走、慢跑或騎自行車，每週至少進行150分鐘，幫助燃燒熱量。每餐適量控制，避免暴飲暴食，並養成規律的飲食習慣，避免宵夜。"
    elif 24 <= bmi < 27:
        bmi_advice = "「體重過重」了，要小心囉，趕快力行「健康體重管理」！建議控制每天的總熱量攝取，減少高熱量食物如糕點、含糖飲料等。可以考慮多吃高蛋白低脂肪的食物，如魚、豆類、瘦肉等，有助於保持肌肉質量。每天堅持運動，如散步、快走、爬樓梯等，逐步養成運動習慣。"
    elif 18.5 <= bmi < 24:
        bmi_advice = "恭喜！「健康體重」，要繼續保持！可以繼續保持現在的飲食和運動習慣。建議選擇均衡飲食，包含蛋白質、碳水化合物、健康脂肪以及維生素和礦物質，確保營養充足。保持每週的運動頻率，如散步、瑜伽、慢跑等，讓身體保持健康活力。"
    else:
        bmi_advice = "「體重過輕」，需要多運動，均衡飲食，以增加體能，維持健康！建議多攝取高熱量、高蛋白的食物，如堅果、酪梨、牛奶、豆類等。可以增加優質碳水化合物的攝取，如全穀類、燕麥、紅薯等，為身體提供足夠的能量。每天進行適量的力量訓練，如舉重或阻力訓練，增強肌肉，幫助體重增長。"
    
    # 定義 fontLargestStrong, fontSecondStrong, fontNormalStrong, fontNormal 等變數
    fontLargestStrong = {'blood_pressure': [], 'blood_sugar': [], 'bmi': []}
    fontSecondStrong = {'blood_pressure': [], 'blood_sugar': [], 'bmi': []}
    fontNormalStrong = {'blood_pressure': [], 'blood_sugar': [], 'bmi': []}
    fontNormal = {'blood_pressure': [], 'blood_sugar': [], 'bmi': []}

    # 渲染模板並傳遞所有變數
    return render_template('result.html', 
                           bmi=bmi, 
                           bmi_advice=bmi_advice, 
                           blood_pressure=blood_pressure, 
                           blood_sugar=blood_sugar,
                           fontLargestStrong=fontLargestStrong,
                           fontSecondStrong=fontSecondStrong,
                           fontNormalStrong=fontNormalStrong,
                           fontNormal=fontNormal)

if __name__ == '__main__':
    app.run(debug=True)
