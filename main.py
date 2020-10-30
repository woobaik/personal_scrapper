import poong
import air_today


for article in air_today.result:
    print(article.split('\n'))

poong_data = poong.export_bj_info()

for bj in poong_data:
    print("===========================")
    print(f"{bj['name']}", end="\n")
    print("===========================")
    print(f"{bj['name']} has earned {bj['daily']} today")
    print(f"{bj['name']} has been earned {bj['monthly']} this month")
    print(f"{bj['name']} got donation of {bj['pph']} per hour")
