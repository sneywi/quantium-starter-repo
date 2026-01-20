import csv

input_files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv",
]

output_file = "processed_sales_data.csv"

with open(output_file, mode="w", newline="") as out_csv:
    writer = csv.writer(out_csv)
    
    writer.writerow(["sales", "date", "region"])

    for file in input_files:
        with open(file, mode="r") as in_csv:
            reader = csv.reader(in_csv)
            line_count = 0
            for row in reader:
                if line_count == 0:
                    line_count += 1
                    continue

                product, price, quantity, date, region = row

                if product != "pink morsel":
                    continue
                price_value = float(price.replace("$", ""))
                sales = price_value * int(quantity)

                writer.writerow([sales, date, region])
                line_count += 1

print("processed_sales_data.csv created successfully")