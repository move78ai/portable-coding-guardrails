# Platform installation notes

## ChatGPT web

Best default: create a Project, paste `exports/chatgpt/PROJECT_INSTRUCTIONS.md` into Project instructions, then append the fields from `templates/PROJECT_APPENDIX.md`.

Use `exports/chatgpt/GLOBAL_FALLBACK_SHORT.txt` only when no project scope is available.

## ChatGPT Codex

Copy `exports/codex/AGENTS.md` to the repository as `AGENTS.md` and fill in the project appendix.

## Claude.ai web

Best default: create a Claude Project, paste `exports/claude/PROJECT_INSTRUCTIONS.md`, then append the fields from `templates/PROJECT_APPENDIX.md`.

## Claude Code locally

Copy `exports/claude/CLAUDE.md` to the repo root as `CLAUDE.md` and fill in the appendix.

## Gemini web

Create a Gem and paste `exports/gemini/GEM_INSTRUCTIONS.md`. Pair it with repo docs when possible.

## Any platform without persistent instructions

Use `exports/any-llm/BOOTSTRAP_PROMPT.md` as the first message in a new coding chat.
