#!/bin/bash

# Check if backup file is provided
if [ -z "$1" ]; then
    echo "Please provide a backup file to restore"
    echo "Usage: ./restore.sh <backup_file>"
    exit 1
fi

# Set variables
BACKUP_FILE="$1"
RESTORE_DB="db_restored"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
RESTORE_DIR="db_backups/restores"
RESTORE_PATH="$RESTORE_DIR/${RESTORE_DB}_${TIMESTAMP}"

# Create restore directory if it doesn't exist
mkdir -p $RESTORE_DIR

# Drop the database if it exists and create new one
psql postgres -c "DROP DATABASE IF EXISTS $RESTORE_DB;"
psql postgres -c "CREATE DATABASE $RESTORE_DB;"

# Restore the database from backup
pg_restore -d $RESTORE_DB "$BACKUP_FILE"

# Create a restore metadata file
echo "Restore completed at: $(date)" > "$RESTORE_PATH/metadata.txt"
echo "Source backup: $BACKUP_FILE" >> "$RESTORE_PATH/metadata.txt"
echo "Restored database: $RESTORE_DB" >> "$RESTORE_PATH/metadata.txt"
echo "Number of tables: $(psql -d $RESTORE_DB -t -c "SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public';")" >> "$RESTORE_PATH/metadata.txt"
echo "Number of rows in users table: $(psql -d $RESTORE_DB -t -c "SELECT count(*) FROM users;")" >> "$RESTORE_PATH/metadata.txt"

echo "Database restored successfully to: $RESTORE_DB"
echo "Restore metadata saved in: $RESTORE_PATH" 