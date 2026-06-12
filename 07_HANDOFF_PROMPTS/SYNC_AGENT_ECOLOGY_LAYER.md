# SYNC_AGENT_ECOLOGY_LAYER

Используй `Agentum` как центральную библиотеку агентного контура и выполни только bounded sync agent layer в целевой проект.

Твоя задача:

1. определить активный проект и его install profile;
2. определить, какие agent layers уже стоят локально;
3. выбрать только нужные слои из:
   - runtime guard;
   - subject ecology;
   - persona fragments;
   - profile-specific patches;
4. не трогать domain content и product logic;
5. вернуть diff summary и список точек установки.

Правила:

- не делай wholesale rewrite;
- не трактуй весь corpus как одну инструкцию;
- не обновляй target repo до проверки project identity;
- не смешивай dry runtime guard с persona humor;
- не обновляй слой по памяти — сверяйся с registry и install docs;
- если найден конфликт между local divergence и central layer, сначала опиши конфликт, потом предложи smallest patch batch.

Финальный результат должен содержать:

1. использованные файлы из `Agentum`;
2. какие слои были синхронизированы;
3. какие файлы target repo изменены;
4. какие локальные divergence points сохранены;
5. какие риски требуют ручного review.
