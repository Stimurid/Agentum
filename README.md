# protected-agent-kit

`protected-agent-kit` — локальный standalone repository для защищённой работы с coding agents и persona agents.

Это не target application repo и не runtime prompt dump. Репозиторий хранит корпус, guard kit, persona fragments, install profiles, evals и handoff prompts так, чтобы ими можно было пользоваться осознанно, а не тащить весь архив в живой runtime.

## Зачем нужен этот repo

Он нужен, чтобы защитная архитектура агента не жила только:

- в чате;
- в памяти модели;
- в одном конкретном проекте;
- в случайной подборке красивых prompt fragments.

`protected-agent-kit` отделяет:

- corpus и registries;
- теоретические модели;
- минимальный runtime kit;
- persona style fragments;
- target profiles;
- install docs;
- eval/proving-ground;
- handoff prompts.

## Текущие контрольные точки

- `deae7f6` — bootstrap protected-agent-kit corpus
- `8a25c96` — add v0 minimal protected-agent kit
- `4472301` — add persona anti-idolatry humor fragments

## Слои репозитория

### `00_MANIFEST`

Project charter, design principles, glossary, saturation и final acceptance report.

### `01_RESEARCH_ARCHIVE`

Волны внутреннего synthesis archive. Это не новые web-sources и не runtime instructions. Это компактная фиксация исследовательских фаз, из которых собирался kit.

### `02_REGISTRIES`

Source registry, pattern registry, failure-mode registry, golden formulations, anti-patterns, decision log.

### `03_THEORY`

Короткие operational theory docs: context-only vs runtime guard, runtime supply chain, memory surface, executable influence, glyphcrack, safety as distinction, Assuna/MG translation.

### `04_KITS/v0_minimal`

Минимальный runtime-readable guard kit:

- compact `AGENTS.md`
- compact `CLAUDE.md`
- template `settings.json`
- hook skeletons
- command markdowns
- compact runtime docs

Это минимальный runtime kit, а не вся теория.

### `04_KITS/persona_fragments`

Отдельный style layer для persona agents. Сейчас здесь есть anti-idolatry humor fragments. Этот слой не должен попадать в dry guard/runtime enforcement prompts.

### `05_PROFILES`

Project-specific profiles и install guides:

- `generic_repo`
- `litops`
- `moderbober`
- `whitecrow`
- `quinta`

### `06_EVALS`

Manual proving-ground:

- eval scenarios
- dynamic eval seeds
- test prompts
- runbook
- results template

### `07_HANDOFF_PROMPTS`

Русскоязычные paste-ready prompts для создания repo, backfill, environment audit, target install и persona humor patching.

### `08_INSTALL`

Copy/vendor/submodule tradeoffs, Claude Code profile, Codex profile и copy checklist.

## Safe usage

Рабочий порядок:

1. Прочитать `00_MANIFEST` и `02_REGISTRIES`.
2. Выбрать target profile.
3. Понять, нужен ли `v0_minimal` или persona/style layer.
4. Копировать только компактный профильный slice.
5. Прогнать local eval/proving-ground.
6. Делать target install только после human review.

## Как не использовать kit

Не надо:

- копировать весь research archive в runtime files target repo;
- ставить persona humor в dry guard prompts;
- трактовать `AGENTS.md`/`CLAUDE.md` как hard enforcement;
- автоматически устанавливать kit в Litops, ModerBober, WhiteCrow, Quinta или любой другой repo прямо из этого repository;
- переписывать registries ради красоты;
- считать "создан файл" эквивалентом "продукт готов".

## Как начать с generic profile

Если target repo обычный, начни с:

- `05_PROFILES/generic_repo/PROFILE.md`
- `05_PROFILES/generic_repo/INSTALL.md`
- `08_INSTALL/copy_v0_checklist.md`
- `08_INSTALL/claude_code_profile.md` или `08_INSTALL/codex_profile.md`

## Как адаптировать под Litops / ModerBober / WhiteCrow / Quinta

Используй только соответствующий профиль:

- Litops: защищай source/occurrence/drop/workset/registry/trace/prompt-body distinctions.
- ModerBober: защищай production/runtime/provider/reporting/UI surfaces.
- WhiteCrow: защищай source PDFs, annotations, cite-back, metadata, vault projection.
- Quinta: защищай invention/workbench/persona layers и не смешивай persona humor с dry runtime guard.

## Что дальше

Следующий безопасный шаг после этого repo — first real target-profile installation with human review, starting from one chosen profile and the proving-ground.
