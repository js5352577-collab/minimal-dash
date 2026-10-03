import requests

def get_weather():
    try:
        # إحداثيات مدينة صافيتا، سوريا
        url = "https://open-meteo.com"
        response = requests.get(url, timeout=5).json()
        weather = response.get("current_weather", {})
        temp = weather.get("temperature")
        wind = weather.get("windspeed")
        print(f"🌤️  الطقس في صافيتا: {temp}°C | سرعة الرياح: {wind} كم/س")
    except Exception:
        print("🌤️  الطقس: تعذر جلب بيانات الطقس حالياً.")

def get_currency():
    try:
        url = "https://er-api.com"
        data = requests.get(url, timeout=5).json()
        eur = data["rates"].get("EUR")
        gbp = data["rates"].get("GBP")
        print(f"💵 أسعار العملات مقابل الدولار: اليورو = {eur:.2f} | الجنيه الإسترليني = {gbp:.2f}")
    except Exception:
        print("💵 أسعار العملات: تعذر الاتصال بخدمة الأسعار.")

def get_quote():
    try:
        url = "https://zenquotes.io"
        data = requests.get(url, timeout=5).json()
        quote = data[0]["q"]
        author = data[0]["a"]
        print(f"✨ اقتباس اليوم: \"{quote}\" - {author}")
    except Exception:
        print("✨ اقتباس اليوم: النجاح هو الانتقال من فشل إلى فشل دون فقدان الحماس.")

if __name__ == "__main__":
    print("========================================")
    print("      أهلاً بك في لوحة تحكمك اليومية      ")
    print("========================================")
    get_weather()
    get_currency()
    get_quote()
    print("========================================")
