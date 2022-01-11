from backup.backup_dict import BackupDict
from backup.helpers import logging
from backup.rdiff_backup import RdiffBackup

rdiff_backup = RdiffBackup()
backup_destination_basedir = BackupDict.backup_destination_basedir

for directory_to_backup in BackupDict.backup_directory_list:
    hostname = directory_to_backup.get("hostname")
    source = hostname + "::" + directory_to_backup.get("source")
    destination = backup_destination_basedir + hostname + directory_to_backup.get("destination")
    include_list = directory_to_backup.get("include_list")
    exclude_list = directory_to_backup.get("exclude_list")

    output = rdiff_backup.backup(source, destination, "-v5", include_list, exclude_list)

    logging(hostname, destination, output)
