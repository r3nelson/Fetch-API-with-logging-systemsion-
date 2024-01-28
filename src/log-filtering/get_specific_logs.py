# return logs of specific level ("DEBUG", "INFO", "WARNING", and/or "ERROR")
def get_specific_logs(log_lines, all_logs, level):
    logs = all_logs[level]
    
    for key in logs:
        start, end = key
        for i in range(start,end):
            print(log_lines[i].strip())