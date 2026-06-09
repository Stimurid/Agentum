# RUN_ENVIRONMENT_AUDIT

Проведи environment audit перед target install.

Проверь:

- какой agent runtime используется;
- есть ли поддержка hooks/settings;
- есть ли Python для hook syntax check;
- как устроены sandbox и approvals;
- есть ли ограничения на shell/PowerShell;
- можно ли запускать proving-ground локально.

Правила:

- не делай install в этом же шаге;
- не делай deploy/secrets actions;
- не подменяй audit красивыми догадками.

Верни:

- capabilities;
- missing capabilities;
- safe install path: copy / vendor / submodule;
- risks and required human approvals.
