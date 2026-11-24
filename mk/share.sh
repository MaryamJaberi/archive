# Seal a share bundle with the share password (DS_SHARE_PASS) into the main repo.
# از ۲۴ نوامبر ۲۰۲۶: محتوا را سطح محرمانگی تعیین می‌کند، نه نام پوشه.
# هر فایلی که سطحش از بالاترین سطحِ رول «مهمان» (در data/access/model.json) بیشتر باشد بیرون می‌ماند.
set -e
SC=/home/claude/work
R=/home/claude/maryamjaberi.github.io/daneshsara
[ -n "$DS_SHARE_PASS" ] || { echo "no share pass; skipped"; exit 0; }
rm -rf $SC/share_src
python3 $SC/mk/share_select.py $SC/vault_src/daneshsara $SC/share_src/daneshsara
mkdir -p $R/share
DS_VAULT_PASS="$DS_SHARE_PASS" python3 $R/build/vault.py $SC/share_src $R/share/simorgh.enc | tail -1
rm -rf $SC/share_check && DS_VAULT_PASS="$DS_SHARE_PASS" python3 $R/build/vault.py --extract $R/share/simorgh.enc $SC/share_check >/dev/null
cmp $SC/share_check/daneshsara/simorgh/par/index.html $SC/vault_src/daneshsara/simorgh/par/index.html && echo share-verified
python3 - "$SC/share_check/daneshsara" <<'PY'
import sys, os
bad = [p for p in ('simorgh/plan.html','simorgh/circle.html','simorgh/poll.html','simorgh/archive.html',
                   'simorgh/entries.html','data/simorgh/cheat-ledger.json','core/panel.html')
       if os.path.exists(os.path.join(sys.argv[1], p))]
print('نشتی در بستهٔ اشتراکی:', '، '.join(bad) if bad else 'ندارد')
sys.exit(1 if bad else 0)
PY
