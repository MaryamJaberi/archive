# Seal a Simorgh-only bundle with the share password (DS_SHARE_PASS) into the main repo.
set -e
SC=/home/claude/work
R=/home/claude/maryamjaberi.github.io/daneshsara
[ -n "$DS_SHARE_PASS" ] || { echo "no share pass; skipped"; exit 0; }
rm -rf $SC/share_src && mkdir -p $SC/share_src/daneshsara/data
cp -r $SC/vault_src/daneshsara/simorgh $SC/share_src/daneshsara/
cp -r $SC/vault_src/daneshsara/data/simorgh $SC/share_src/daneshsara/data/
mkdir -p $R/share
DS_VAULT_PASS="$DS_SHARE_PASS" python3 $R/build/vault.py $SC/share_src $R/share/simorgh.enc | tail -1
rm -rf $SC/share_check && DS_VAULT_PASS="$DS_SHARE_PASS" python3 $R/build/vault.py --extract $R/share/simorgh.enc $SC/share_check >/dev/null
cmp $SC/share_check/daneshsara/simorgh/index.html $SC/vault_src/daneshsara/simorgh/index.html && echo share-verified
