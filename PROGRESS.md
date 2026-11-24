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

### 2026-11-24: Task 1.1 (in progress)
- Done: folder `~/forecast_detective` and venv created and activated.
- Found in review: `README.md` was created *inside* `.venv/` instead of the project root. The `.gitignore` you pasted is the one Python creates automatically inside `.venv/`. There is no root `.gitignore` yet.
- Learned: what `.gitignore` is for (rebuildable files, generated files, secrets, editor clutter). First attempt contained the explanation text instead of patterns; `#` comments are the fix.
- README: finished (Claude did the wording/formatting polish at your request; it's docs, not code).
- `.gitignore`: v3 had inline comments (`.venv #...`), which Git reads as part of the pattern, so nothing matched. Claude wrote the final version at your request and explained each line. Key lessons: `#` is a comment only at the start of a line; a trailing `/` means folder; `.env` holds secrets.
- Still to do: `httpx` + `requirements.txt`, `git init`, check `git status`, commit, push, branch `week-1-engine`.
- Update: README moved to the root ✓. Root `.gitignore` created but **empty (0 bytes)**, probably not saved yet.
- Still to do: write your own root `.gitignore`, install `httpx` + `requirements.txt`, `git init`, commit, push to GitHub, create branch `week-1-engine`.

**Next up:** finish 1.1, then 1.2 (explore the Open-Meteo API).
