import pandas as pd
from datetime import datetime

EXCEL_FILE = "yurigaoka_bus_timetable.xlsx"

today = datetime.now().weekday()

if today <= 4:
    day_type = "Weekday"
elif today == 5:
    day_type = "Saturday"
else:
    day_type = "SundayHoliday"

now = datetime.now()
now_minutes = now.hour * 60 + now.minute

all_buses = []

for stop in [1, 2]:
    sheet = f"Stop{stop}_{day_type}"
    df = pd.read_excel(EXCEL_FILE, sheet_name=sheet)

    for _, row in df.iterrows():
        h = int(row["Hour"])
        minutes_text = str(row["Minutes"])

        minute_list = minutes_text.split(",")

        for m in minute_list:
            m = int(m.strip())
            total = h * 60 + m

            if total >= now_minutes:
                all_buses.append({
                    "time": total,
                    "hour": h,
                    "minute": m,
                    "stop": stop
                })

if len(all_buses) == 0:
    print("本日の運行は終了しました")
else:
    next_bus = sorted(all_buses, key=lambda x: x["time"])[0]
    diff = next_bus["time"] - now_minutes

    if diff <= 1:
        hurry = "まだギリギリ間に合います"
    elif diff <= 3:
        hurry = "そろそろ出てもよさそうです"
    elif diff <= 10:
        hurry = "問題ありません、しかし、心構えはしておきましょう"
    else:
        hurry = "まだまだ余裕があります"

    print("-----結果-----")
    print(f"{diff}分後に到着")
    print(f"{next_bus['stop']}番乗り場")
    print(hurry)