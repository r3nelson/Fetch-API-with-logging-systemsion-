def get_logs (file_path):
    debug_logs = []
    info_logs = []
    warning_logs = []
    error_logs =[]

    debug_levels = ['DEBUG','INFO','WARNING','ERROR']

    with open(file_path, 'r') as f:
        start_condition = False
        end_condition = False
        all_logs = f.readlines()
        # print(type(all_logs))
        # for i in range(len(all_logs)):

        # for index, line in enumerate(all_logs):
        #     if line == '\n':
        #         continue
        logs = []
        log = ''
        for line in all_logs:
            
            if line == '\n':
                # log_type.append(log)
                logs.append(log)
                log = ''
                # print('newline')
            log+= line
            # log.append(line.strip())

    
    print(logs)
    # for log in logs:
    #     if "DEBUG" in log:
    #         debug_logs.append(log)
    #     if "INFO" in log:
    #         info_logs.append(log)
    #     if "WARNING" in log:
    #         warning_logs.append(log)
    #     if "ERROR" in log:
    #         error_logs.append(log)

    # print(info_logs)
    
    # with open ('test.txt', 'w+') as f:
    #     f.write(str(info_logs))
            
        
# print(get_logs('../logs/manga/manga.log'))
    
def get_logs (file_path):
    # debug_levels = ['DEBUG','INFO','WARNING','ERROR']

    # logs= {'DEBUG': [], 'INFO': [], 'WARNING':[], 'ERROR': []}
    # level = None
    # with open(file_path, 'r') as f:
    #     for line in f.readlines():
            # if "DEBUG" in line:
            #     level = "DEBUG"
            # if "INFO" in line:
            #     level = "INFO"
            # if "WARNING" in line:
            #     level = "WARNING"
            # if "ERROR" in line:
            #     level = "ERROR"
    
    with open(file_path, 'r') as f:

        line = f.readline()
        while line:
            # Process the line (e.g., print it)
            print(line.strip())
            
            # Read the next line
            line = f.readline()
            
        
                    

print(get_logs('../logs/manga/manga.log'))