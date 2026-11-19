#!/bin/bash
# میز فرمان: دادهٔ داشبورد را از وضعیتِ امروزِ دو مخزن می‌سازد.
# اجرا: tools/dashboard.sh <مسیر کلون MaryamJaberi.github.io> <فایل خروجی>
set -e
HERE=$(cd "$(dirname "$0")/.." && pwd)
python3 "$HERE/vault_src/daneshsara/build/status.py" "$1/daneshsara" "$HERE/vault_src/daneshsara" "$2"
