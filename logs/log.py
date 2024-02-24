from datetime import datetime

def log(message):
    timestamp_format = '%H:%M:%S-%h-%d-%Y'
    # get current timestamp
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("logs/transaction_logs.txt","a") as file:
        file.write(timestamp + ': ' + message + '\n')