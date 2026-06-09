# CREATE_KIT_REPO

Ты создаёшь standalone repository `protected-agent-kit`.

Задача: собрать инфраструктурный repo для protected coding-agent work. Это не target repo и не runtime prompt dump.

Правила:

- не смешивай archive, runtime kit, profiles, evals и handoff prompts в один файл;
- не тащи весь corpus в runtime layer;
- сначала создай skeleton слоёв;
- затем заполни manifest, registries и design doctrine;
- затем создай `v0_minimal`;
- затем profiles, evals и install docs;
- не делай target install из этого prompt.

Верни:

- созданную структуру;
- краткий diff summary;
- список незаполненных intentional templates, если они действительно нужны.
