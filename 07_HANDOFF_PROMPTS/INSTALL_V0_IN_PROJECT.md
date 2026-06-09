# INSTALL_V0_IN_PROJECT

Ты не устанавливаешь kit автоматически. Сначала идентифицируешь target project и работаешь по profile.

Порядок:

1. Назови active project, root path, protected paths, neighboring repos, rollback path.
2. Выбери конкретный профиль из `05_PROFILES`.
3. Определи, какие compact runtime files реально нужны target repo.
4. Не копируй `01_RESEARCH_ARCHIVE` и `02_REGISTRIES` в runtime.
5. Не вставляй persona humor в dry guard/runtime prompts.
6. Покажи dry run: какие файлы будут copied/adapted, какие не будут.
7. Попроси human review перед реальной установкой.

Верни:

- chosen profile;
- files to copy/adapt;
- files not to copy;
- validation plan;
- rollback plan;
- diff summary после выполнения, если install был разрешён.
