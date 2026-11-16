#!/bin/bash
# build simorgh wiki privately, seal into vault, revert public tree. Usage: rebuild.sh "commit message"
set -e
SC=/home/claude/work
R=/home/claude/maryamjaberi.github.io/daneshsara
cd $SC/mk && python3 -I build_all.py | head -1
cd $R
sed -i "s/\['psy', 'soc', 'tabar', 'phil', 'tarikh'\]/['psy', 'soc', 'tabar', 'phil', 'tarikh', 'simorgh']/" build/validate.py
sed -i 's/psy|soc|tabar|phil|tarikh|simorgh/psy|soc|tabar|phil|tarikh/g; s/psy|soc|tabar|phil|tarikh/psy|soc|tabar|phil|tarikh|simorgh/g' core/schema/concept.schema.json
mkdir -p iran && cp $SC/vault_src/daneshsara/iran/*.json iran/
python3 build/validate.py 2>&1 | grep -v "^registry" | grep -v -i kant | tail -4
python3 build/reader.py simorgh | tail -1
V=$SC/vault_src/daneshsara
rm -rf $V/data/simorgh/concepts && cp -r data/simorgh/concepts $V/data/simorgh/concepts && cp data/simorgh/order.json $V/data/simorgh/ && cp simorgh/entries.html $V/simorgh/entries.html
N=$(ls data/simorgh/concepts | wc -l)
[ -n "$DS_VAULT_PASS" ] || { echo "no pass"; exit 1; }
rm -rf $SC/pre_x && python3 build/vault.py --extract vault/bundle.enc $SC/pre_x >/dev/null && echo pass-ok
python3 build/vault.py $SC/vault_src vault/bundle.enc | tail -1
rm -rf $SC/vault_check && mkdir $SC/vault_check && python3 build/vault.py --extract vault/bundle.enc $SC/vault_check >/dev/null
cmp $SC/vault_check/daneshsara/simorgh/entries.html simorgh/entries.html && echo verified-$N
git checkout -- build/validate.py core/schema/concept.schema.json core/sources.json core/registry.json
rm -rf data/simorgh; git checkout -- simorgh iran; git clean -fdq simorgh iran
bash $SC/mk/share.sh
cd .. && git add daneshsara/vault/bundle.enc && { [ -f daneshsara/share/simorgh.enc ] && git add daneshsara/share/simorgh.enc; } ; git status --short
