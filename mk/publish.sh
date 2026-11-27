#!/bin/bash
# بسته‌ها را commit و push می‌کند و بعد نسخهٔ اشتراکی را فوری به‌روز می‌کند.
# اجرا بعد از rebuild.sh:  bash mk/publish.sh
set -e
R=/home/claude/maryamjaberi.github.io
cd "$R"
git add -A daneshsara/vault daneshsara/share
if git diff --cached --quiet; then
  echo "چیزی برای انتشار نیست"
else
  git commit -qm "به‌روزرسانی

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016f1Khrh8UNdKuGKoGoPMWW"
  git pull -q --rebase
  git push -q
  echo "فرستاده شد: $(git log --oneline -1 | cut -c1-9)"
fi
# نسخهٔ اشتراکی را از همگام‌سازیِ ساعتی جلو بینداز
if command -v gh >/dev/null && [ -s daneshsara/share/simorgh.enc ]; then
  sleep 20   # تا raw.githubusercontent نسخهٔ تازه را ببیند
  if gh api -X POST repos/MaryamJaberi/simorgh/actions/workflows/sync.yml/dispatches -f ref=main >/dev/null 2>&1; then
    echo "نسخهٔ اشتراکی: درخواست به‌روزرسانی فرستاده شد"
  else
    echo "نسخهٔ اشتراکی: درخواست نرفت؛ همگام‌سازیِ ساعتی خودش انجام می‌دهد"
  fi
fi
