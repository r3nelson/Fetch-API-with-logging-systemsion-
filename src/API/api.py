from fastapi import FastAPI
from ..log_filtering.read_logfile import read_logfile
from ..log_filtering.get_all_logs import get_all_logs
from ..log_filtering.get_specific_logs import get_specific_logs

app = FastAPI()

# currently returns all logs as object
# need to change to string for easier viewing
@app.get("/logs/all")
def display_all_logs():
    log_lines = read_logfile('manga.log')
    # log_lines = read_logfile('../../logs/manga/manga.log')
    all_logs = get_all_logs(log_lines)

    # reformat all_logs because tuples can't be converted to json
    for key in list(all_logs.keys()):
          for sub_key in list(all_logs[key].keys()):
               new_key = str(sub_key)
               all_logs[key][new_key] = all_logs[key].pop(sub_key)
    return all_logs


# returns debug logs as string for easier viewing 
@app.get("/logs/debug")
def display_debug_logs():
    log_lines = read_logfile('manga.log')
    # log_lines = read_logfile('../../logs/manga/manga.log')
    all_logs = get_all_logs(log_lines)
    debug_logs = get_specific_logs(log_lines, all_logs, "DEBUG")
    return debug_logs

# returns info logs as string for easier viewing 
@app.get("/logs/info")
def display_info_logs():
    log_lines = read_logfile('manga.log')
    # log_lines = read_logfile('../../logs/manga/manga.log')
    all_logs = get_all_logs(log_lines)
    info_logs = get_specific_logs(log_lines, all_logs, "INFO")
    return info_logs

# returns warning logs as string for easier viewing 
@app.get("/logs/warning")
def display_warning_logs():
    log_lines = read_logfile('manga.log')
    # log_lines = read_logfile('../../logs/manga/manga.log')
    all_logs = get_all_logs(log_lines)
    warning_logs = get_specific_logs(log_lines, all_logs, "WARNING")
    return warning_logs

# returns error logs as string for easier viewing 
@app.get("/logs/error")
def display_error_logs():
    log_lines = read_logfile('manga.log')
    # log_lines = read_logfile('../../logs/manga/manga.log')
    all_logs = get_all_logs(log_lines)
    error_logs = get_specific_logs(log_lines, all_logs, "ERROR")
    return error_logs