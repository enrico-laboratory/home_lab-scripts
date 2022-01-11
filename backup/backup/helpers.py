from datetime import datetime

from backup.backup.backup_dict import BackupDict


def give_me_now() -> str:
    # datetime object containing current date and time
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def logging(hostname: str, directory_name: str, output: str):
    directory_name = directory_name[1:]
    log_file_name = \
        BackupDict.logs_directory + give_me_now() + "-" + hostname + "-" + directory_name + ".log"
    with open(log_file_name, "w") as log_file:
        log_file.write(output)

