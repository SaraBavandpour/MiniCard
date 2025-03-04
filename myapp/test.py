from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class USDToIRRView(APIView):
    usd_to_irr_rate = None  # متغیر ذخیره‌سازی نرخ دلار به ریال

    def get_usd_to_irr(self):
        # آدرس API
        api_url = "https://api.exchangerate-api.com/v4/latest/USD"

        # ارسال درخواست به API
        response = requests.get(api_url)

        # بررسی پاسخ
        if response.status_code == 200:
            data = response.json()
            # ذخیره نرخ دلار به ریال
            self.usd_to_irr_rate = data['rates'].get('IRR', None)
            return self.usd_to_irr_rate
        else:
            return None

    def get(self, request):
        # استفاده از تابع برای بازگرداندن نرخ
        rate = self.get_usd_to_irr()
        if rate:
            return Response({"usd_to_irr": rate})
        else:
            return Response({"error": "Failed to fetch rate"}, status=500)
