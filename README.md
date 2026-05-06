## Настройка окружения

После клонирования репозитория выполни:
```bash
git config core.hooksPath .githooks
virtualenv .  && source bin/activate && pip3 install -r requirements.txt
chmod +x .git/hooks/pre-commit
```

Это подключит pre-commit хук с проверкой Semgrep.
