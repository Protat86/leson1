def find_laptop_sales(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            if 'laptop' in line:
                print(f"Рядок {line_number}: {line.strip()}")


find_laptop_sales('sales.txt')
