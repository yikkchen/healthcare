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
            fontLargestStrong['blood_sugar'].append("！注意！你的血糖高於正常範圍")
            fontLargestStrong['blood_sugar'].append("正常情況下，你的血糖應該為：")
            fontLargestStrong['blood_sugar'].append("空腹血糖：70~100mg/dL")
            fontLargestStrong['blood_sugar'].append("飯後兩小時血糖：70~140mg/dL")
            fontLargestStrong['blood_sugar'].append("！改善！")
            fontLargestStrong['blood_sugar'].append("避免吃高升糖指數的食物，選擇 GI 值低於 55 的低升糖指數食物，例如：糙米、燕麥、山藥、大部分蔬菜、豆魚蛋肉類、小番茄、芭樂、木瓜等。")
            fontLargestStrong['blood_sugar'].append("避免吃含精緻糖的食物，像是冰糖、砂糖、高果糖漿等精製糖，避免食用麵包、冰淇淋、甜甜圈等含精緻糖的食物。")
            fontLargestStrong['blood_sugar'].append("避免吃高油脂食物，選擇植物油來替代動物性脂肪（如：豬油、牛油、奶油、培根等）。")
            fontLargestStrong['blood_sugar'].append("避免吃高鈉食物，並避免過度飲酒。")
        elif blood_sugar < 70:
            fontLargestStrong['blood_sugar'].append("！注意！你的血糖低於正常範圍")
            fontLargestStrong['blood_sugar'].append("正常情況下，你的血糖應該為：")
            fontLargestStrong['blood_sugar'].append("空腹血糖：70~100mg/dL")
            fontLargestStrong['blood_sugar'].append("飯後兩小時血糖：70~140mg/dL")
            fontLargestStrong['blood_sugar'].append("請注意您身理上是否有虛弱、嗜睡、飢餓、臉色蒼白、冒冷汗、心跳加快、發冷、抽筋、頭暈等症狀；心理上可能會有情緒改變及行為改變。")
            fontLargestStrong['blood_sugar'].append("！改善！造成低血糖的原因有：")
            fontLargestStrong['blood_sugar'].append("藥物：自行調整藥物劑量不正確、用藥時間不規律等。")
            fontLargestStrong['blood_sugar'].append("飲食：三餐不定時、用藥後未進食等。")
            fontLargestStrong['blood_sugar'].append("運動：空腹運動、過度運動等。")
            fontLargestStrong['blood_sugar'].append("如果長時間處於低血糖狀態，建議就醫。")
        else:
            fontLargestStrong['blood_sugar'].append("Your blood sugar is normal. Keep it up!")
    else:
        fontLargestStrong['blood_sugar'].append("No blood sugar data")

    # BMI 建議
    if isinstance(weight, float) and isinstance(height, float):
        bmi = round(weight / (height / 100) ** 2, 2)
        if bmi >= 27:
            fontLargestStrong['bmi'].append(f"你的{bmi} -> 啊～「肥胖」，需要立刻力行「健康體重管理」囉！建議減少高脂肪、高糖食物的攝取，如甜點、油炸食物、含糖飲料等。多選擇富含纖維的食物，例如蔬菜、水果和全穀類，有助於增加飽足感。增加有氧運動，如快走、慢跑或騎自行車，每週至少進行150分鐘，幫助燃燒熱量。每餐適量控制，避免暴飲暴食，並養成規律的飲食習慣，避免宵夜。")
        elif 24 <= bmi < 27:
            fontLargestStrong['bmi'].append(f"你的{bmi} -> 「體重過重」了，要小心囉，趕快力行「健康體重管理」！建議控制每天的總熱量攝取，減少高熱量食物如糕點、含糖飲料等。可以考慮多吃高蛋白低脂肪的食物，如魚、豆類、瘦肉等，有助於保持肌肉質量。每天堅持運動，如散步、快走、爬樓梯等，逐步養成運動習慣。")
        elif 18.5 <= bmi < 24:
            fontLargestStrong['bmi'].append(f"你的{bmi} -> 恭喜！「健康體重」，要繼續保持！可以繼續保持現在的飲食和運動習慣。建議選擇均衡飲食，包含蛋白質、碳水化合物、健康脂肪以及維生素和礦物質，確保營養充足。保持每週的運動頻率，如散步、瑜伽、慢跑等，讓身體保持健康活力。")
        else:
            fontLargestStrong['bmi'].append(f"你的{bmi} -> 「體重過輕」，需要多運動，均衡飲食，以增加體能，維持健康！建議多攝取高熱量、高蛋白的食物，如堅果、酪梨、牛奶、豆類等。可以增加優質碳水化合物的攝取，如全穀類、燕麥、紅薯等，為身體提供足夠的能量。每天進行適量的力量訓練，如舉重或阻力訓練，增強肌肉，幫助體重增長。")
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

# 新增 GI 值介紹頁面的路由
@app.route('/GI')
def GI():
    return render_template('GI.html')


if __name__ == '__main__':
    app.run(debug=True)