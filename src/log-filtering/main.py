from read_logfile import read_logfile
from get_all_logs import get_all_logs
from get_specific_logs import get_specific_logs

def main():
     # return list of all log lines (will be used to index line numbers)
     log_lines = read_logfile('../../logs/manga/manga.log')
     
     # create dictionary of all logs (all_logs = {"DEBUG": debug_logs, "INFO": info_logs, "WARNING": warning_logs, "ERROR": error_logs })
     all_logs = get_all_logs(log_lines)

     # return logs of specific level ("DEBUG", "INFO", "WARNING", and/or "ERROR")
     level = input("Enter a log level: ").upper()
     error_logs = get_specific_logs(log_lines, all_logs, level)

main()