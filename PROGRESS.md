# Forecast Detective — Learning Progress

Tracker kept by Claude (the learning coach). You write the code; this file records where we are.

## How we work
- One branch per week (`week-1-engine`, ...), one PR per week, commit after every task.
- Each task: concept → example (not the answer) → task → "done when" check.
- Hints start small and get bigger only if you're still stuck.
- Code review after each task; you fix the issues yourself.
- Interview "why" quiz at the end of each week.

## Plan (about 7 h/week, 4 weeks)
- **Week 1, Puzzle engine:** 1.1 repo setup · 1.2 explore Open-Meteo · 1.3 `build_clues()` · 1.4 pytest + fixtures · 1.5 distance/bearing (test-first) · 1.6 city list + loader · 1.7 PR + quiz
- **Week 2, API + DB:** 2.1 Postgres in Docker · 2.2 SQLAlchemy models · 2.3 Alembic + seed · 2.4 `GET /puzzle/today` · 2.5 `POST .../guess` · 2.6 API tests · 2.7 puzzle generation + mocking
- **Week 3, Players + frontend:** 3.1 hashing + signup · 3.2 login/JWT · 3.3 streaks/stats · 3.4 leaderboard · 3.5 clues UI + chart · 3.6 guess UI + share
- **Week 4, Ship it:** 4.1 GitHub Actions CI · 4.2 Dockerfile · 4.3 deploy (Render + Neon) · 4.4 safe daily puzzle creation · 4.5 polish + README · 4.6 mock interview

## Design decisions
- 2026-11-24: The answer is a **city** (feedback = distance in km + compass direction).
- 2026-11-24: Sky/nature photo is a **stretch goal**, not part of the core game.

## Log

### 2026-11-24: Task 1.1 ✅ DONE
- `main` and `week-1-engine` pushed to GitHub (freddyxue08-bit/forecast_detective), both at `063c6f3`.
- Learned along the way: VS Code "New File" uses the selected folder; `.gitignore` patterns and `#` comments; `pip freeze >`; `>` vs `>>`; `git branch -m old new` vs renaming the current branch; remotes and `push -u`.
- Claude wrote: README polish, final `.gitignore` (explained line by line), the push commands (explained).

Task 1.1 details:
- Done: folder `~/forecast_detective` and venv created and activated.
- Found in review: `README.md` was created *inside* `.venv/` instead of the project root. The `.gitignore` you pasted is the one Python creates automatically inside `.venv/`. There is no root `.gitignore` yet.
- Learned: what `.gitignore` is for (rebuildable files, generated files, secrets, editor clutter). First attempt contained the explanation text instead of patterns; `#` comments are the fix.
- README: finished (Claude did the wording/formatting polish at your request; it's docs, not code).
- `.gitignore`: v3 had inline comments (`.venv #...`), which Git reads as part of the pattern, so nothing matched. Claude wrote the final version at your request and explained each line. Key lessons: `#` is a comment only at the start of a line; a trailing `/` means folder; `.env` holds secrets.
- Done: `httpx` installed, `requirements.txt` via `pip freeze` (learned: dependencies), git init, first commit `063c6f3` (only the 4 right files tracked, so `.gitignore` works ✓), branch `week-1-engine` ✓.
- Still to do: rename `master` → `main`, create GitHub repo, add remote, push both branches.
- Update: README moved to the root ✓. Root `.gitignore` created but **empty (0 bytes)**, probably not saved yet.
- Still to do: write your own root `.gitignore`, install `httpx` + `requirements.txt`, `git init`, commit, push to GitHub, create branch `week-1-engine`.

### Task 1.2: Explore Open-Meteo (started 2026-11-24)
- Goal: `scripts/explore_weather.py` geocodes a city, fetches a year of daily weather, prints a summary, and saves raw JSON to `tests/fixtures/`.
- 2026-11-26, step 1 ✅: geocoding works and prints `Toronto, Canada: 43.70643, -79.39864`.
  - Learned: reading API docs (endpoint / params / response shape / errors), nested access (dict key → list index → dict key), storing results in variables, dict keys vs list positions, f-strings.
  - Watch-outs: run the code before asking for a check; key typos (`lattitude`); quotes around strings.
- 2026-11-26, step 2 ✅: chained request fetches 2025 daily weather and prints 5 daily keys + `365`.
  - Learned: parallel lists, reading tracebacks (last line + your file's line), the crash line isn't always the cause line, 400 errors show the built URL, `%2C` = comma, multi-line params dicts.
  - Claude laid out both params dicts with blanks at your request; you filled them.
- 2026-11-27, step 3 (almost): hottest day + total rain printed (Toronto: 2025-06-24, 36.0 °C; 817.2 mm); `CITY` constant; `tests/fixtures/toronto_2025.json` saved (lowercase). Left: second city fixture, commit + push.
  - Learned: `max` / `.index` / `sum` / `round`, `with open(..., "w")` + `json.dump`, constants in CAPS, lowercase filenames (Linux is case-sensitive), `+` = space in URLs.

**Next up (next session):** if not done, commit step 2. Then task 1.2 step 3: print the hottest day (`max` → `.index` → same position) and total rain (`sum`, `round`), save `weather` to `tests/fixtures/toronto_2025.json` (`mkdir -p tests/fixtures`, `json.dump`), repeat for a hot desert/tropical city. Bonus: what unit is `daylight_duration`? Then task 1.3 (`build_clues()`).
