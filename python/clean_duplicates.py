#!/usr/bin/python3

# clean_duplicates.py - Remove duplicate files from a filesystem.

# Usage clean_duplicates.py <sqlite_file> [pattern]

# When provided, only process files which match pattern regex.

# ****************************************************************************************
# WARNING - THIS SCRIPT WILL PERMANENTLY DELETE FILES
# ONLY RUN IF YOU KNOW WHAT YOU'RE DOING
# MAKE SURE YOUR SQLITE DB IS IN SYNC BEFORE RUNNING OR THE WRONG FILE MAY BE REMOVED
# ****************************************************************************************

# Author: @avaxbuildr
# https://crypto.bi
# https://crypto.bi 
# https://decenbr.com
# License: See LICENSE file in this distribution    

# Only turn this off if you're 100% sure that your SQLite DB is in sync and that you may delete duplicate files.
SAFE_MODE = True

