def total_salary(path):
    total_sum = 0
    devs_count = 0
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                name, salary_str = cleaned_line.split(',')
                total_sum = total_sum + int(salary_str)
                devs_count += 1
    except FileNotFoundError:
        return (0, 0)
    
    # ZeroDivisionError protection
    if devs_count == 0:
        average_salary = 0
    else:
        average_salary = total_sum / devs_count
        
    return (total_sum, average_salary)