#!/bin/bash

# Set variables
BACKUP_DIR="db_backups/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="sample_db_incremental_$TIMESTAMP"
BACKUP_PATH="$BACKUP_DIR/$BACKUP_NAME"

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_PATH

# Perform incremental backup using custom format (-Fc) which is compressed and binary
pg_dump -Fc sample_db > "$BACKUP_PATH/incremental_backup.dump"

# Create a metadata file
echo "Backup created at: $(date)" > "$BACKUP_PATH/metadata.txt"
echo "Database: sample_db" >> "$BACKUP_PATH/metadata.txt"
echo "Backup type: Incremental" >> "$BACKUP_PATH/metadata.txt"
echo "Backup format: Custom (compressed binary)" >> "$BACKUP_PATH/metadata.txt"
echo "Number of tables: $(psql -d sample_db -t -c "SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public';")" >> "$BACKUP_PATH/metadata.txt"
echo "Number of rows in users table: $(psql -d sample_db -t -c "SELECT count(*) FROM users;")" >> "$BACKUP_PATH/metadata.txt"
echo "Backup size: $(du -h "$BACKUP_PATH/incremental_backup.dump" | cut -f1)" >> "$BACKUP_PATH/metadata.txt"

echo "Incremental backup created in directory: $BACKUP_PATH" 