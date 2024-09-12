import os
import shutil
import paramiko
import logging
from datetime import datetime

# Configuration
SOURCE_DIR = '/path/to/source/directory'
BACKUP_DIR = '/path/to/backup/directory'
REMOTE_SERVER = 'remote.server.com'
REMOTE_PORT = 22
REMOTE_USERNAME = 'username'
REMOTE_PASSWORD = 'password'
REMOTE_PATH = '/path/to/remote/directory'

# Configure logging
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def create_backup(source_dir, backup_dir):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_filename = os.path.join(backup_dir, f'backup_{timestamp}.tar.gz')
    try:
        shutil.make_archive(base_name=backup_filename[:-7], format='gztar', root_dir=source_dir)
        logging.info(f"Backup created successfully: {backup_filename}")
        return backup_filename
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        return None

def transfer_backup(backup_filename, remote_server, remote_port, remote_username, remote_password, remote_path):
    try:
        transport = paramiko.Transport((remote_server, remote_port))
        transport.connect(username=remote_username, password=remote_password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(backup_filename, os.path.join(remote_path, os.path.basename(backup_filename)))
        sftp.close()
        transport.close()
        logging.info(f"Backup transferred successfully to {remote_server}:{remote_path}")
        return True
    except Exception as e:
        logging.error(f"Failed to transfer backup: {e}")
        return False

def main():
    # Step 1: Create a backup of the specified directory
    backup_filename = create_backup(SOURCE_DIR, BACKUP_DIR)
    if not backup_filename:
        logging.error("Backup creation failed.")
        return
    
    # Step 2: Transfer the backup to the remote server
    if not transfer_backup(backup_filename, REMOTE_SERVER, REMOTE_PORT, REMOTE_USERNAME, REMOTE_PASSWORD, REMOTE_PATH):
        logging.error("Backup transfer failed.")
        return

    logging.info("Backup operation completed successfully.")

if __name__ == "__main__":
    main()
