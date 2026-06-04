#!/usr/bin/env bash
# exit on error
set -o errexit

echo "--- Starting Build Process ---"

# 1. Install dependencies
echo "Installing requirements..."
pip install -r requirements.txt

# 2. Collect static files for Django admin and DRF browsable API
echo "Collecting static files..."
python manage.py collectstatic --noinput

# 3. Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

echo "--- Build Process Completed Successfully! ---"
