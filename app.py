from flask import Flask, render_template, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# المحرك الذكي لمحاكاة العمليات
class SmartEngine:
    def log(self, message):
        print(f"[{time.strftime('%H:%M:%S')}] {message}")

    def process_link(self, link, service):
        self.log(f"بدء فحص الرابط: {link} لخدمة {service}")
        time.sleep(2)
        self.log("جاري تجاوز جدران الحماية الرقمية...")
        time.sleep(2)
        self.log(f"تم تنفيذ عملية {service} بنجاح ✅")

engine = SmartEngine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_task():
    data = request.json
    # تشغيل المحرك في الخلفية حتى لا يتوقف الموقع
    threading.Thread(target=engine.process_link, args=(data['link'], data['service'])).start()
    return jsonify({"status": "success", "message": "المحرك بدأ العمل"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
