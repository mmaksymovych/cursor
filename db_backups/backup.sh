#!/bin/bash

# Set variables
BACKUP_DIR="db_backups/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="sample_db_$TIMESTAMP"
BACKUP_PATH="$BACKUP_DIR/$BACKUP_NAME"

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_PATH

# Perform backup using custom format (-Fc) which is compressed and binary
pg_dump -Fc sample_db > "$BACKUP_PATH/full_backup.dump"

# Create a metadata file
echo "Backup created at: $(date)" > "$BACKUP_PATH/metadata.txt"
echo "Database: sample_db" >> "$BACKUP_PATH/metadata.txt"
echo "Backup type: Full" >> "$BACKUP_PATH/metadata.txt"
echo "Backup format: Custom (compressed binary)" >> "$BACKUP_PATH/metadata.txt"
echo "Number of tables: $(psql -d sample_db -t -c "SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public';")" >> "$BACKUP_PATH/metadata.txt"
echo "Backup size: $(du -h "$BACKUP_PATH/full_backup.dump" | cut -f1)" >> "$BACKUP_PATH/metadata.txt"

echo "Full backup created in directory: $BACKUP_PATH" 