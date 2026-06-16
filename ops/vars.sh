***REMOVED***
# Centralized variables for MyOwnClone deployment
# Source this file before running deploy scripts

# VPS Host - use DNS hostname when possible
export VPS_HOST="${VPS_HOST:-localhost}"
export PUBLIC_HOST="${PUBLIC_HOST:-https://your-domain.com}"

# For development/testing, use localhost
# export VPS_HOST="127.0.0.1"
# export PUBLIC_HOST="http://localhost:3000"