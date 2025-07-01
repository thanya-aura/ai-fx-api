import requests

url = "https://ai-fx-api.onrender.com/analyze"  # ✅ Replace with your real Render URL

data = {
    "agent": "fx_plus"  # Choose: fx_standard, fx_plus, fx_premium
}

with open("fx_test.xlsx", "rb") as f:
    files = {
        "file": ("fx_test.xlsx", f, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    }
    response = requests.post(url, files=files, data=data)

print("Status:", response.status_code)
print("Response:", response.json())
