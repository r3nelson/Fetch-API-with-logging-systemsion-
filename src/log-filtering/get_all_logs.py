
def get_all_logs(log_lines):
    
    # create list of where every log starts and stops
    log_block_indexes = []
    for i in range(len(log_lines)):
        if i == 0:
            log_block_indexes.append(i)
            continue
        if log_lines[i] == '\n':
            log_block_indexes.append(i)
    
    # find start and end indexes for each log block
    log_blocks ={}
    for i in range(len(log_block_indexes) - 1):
        if i == 0:
            log_blocks[i] = [log_block_indexes[i], log_block_indexes[i+1]]
        else:
            log_blocks[i] = [log_block_indexes[i] + 1 , log_block_indexes[i+1]]
            
    
    # assign log to level of DEBUG, INFO, WARNING, or ERROR
    def assign_log_level(line):
        if "DEBUG" in line:
            return "DEBUG"
        if "INFO" in line:
            return "INFO"
        if "WARNING" in line:
            return "WARNING"
        if "ERROR" in line:
            return "ERROR"
        
    # add level to log blocks (e.g., logblock[key] = [start, end, level])
    for key in log_blocks:
        line = log_lines[log_blocks[key][0]]
        level = assign_log_level(line)
        log_blocks[key].append(level)
    
    all_logs = {'DEBUG': {}, 'INFO': {}, 'WARNING': {}, 'ERROR': {}}
    
    # function to seperate logs based on level
    def categorize_logs (start, end, level):
        key = tuple([start,end])
        all_logs[level].setdefault(key,[])

        for i in range(start,end):
            value = log_lines[i]  
            try:
                all_logs[level][key].append(value)
            except Exception as e:
                print(f"An error occurred: {e}")

    # seperate logs based on level
    for i in log_blocks:
        start, end, level = log_blocks[i]
        categorize_logs(start,end,level)

    return all_logs
            