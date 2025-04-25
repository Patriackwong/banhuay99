import datetime

# จำลองผลหวย
today = datetime.datetime.today().strftime('%d/%m/%Y')
html_template = f"""
<!DOCTYPE html>
<html lang="th">
<head><meta charset="UTF-8"><title>ผลหวย</title></head>
<body>
<h2>ผลหวยประจำวันที่ {today}</h2>
<p>รางวัลที่ 1: <strong>123456</strong></p>
<p>เลขท้าย 2 ตัว: <strong>78</strong></p>
<p>เลขหน้า 3 ตัว: <strong>012, 345</strong></p>
<p>เลขท้าย 3 ตัว: <strong>678, 901</strong></p>
</body>
</html>
"""

# บันทึกผลไปที่ index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)
