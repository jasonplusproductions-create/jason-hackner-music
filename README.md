# Jason Hackner Music

Static site for **themlc.jasonplusproductions.com**.

This branch/repo is **split out** from [subscription-guard](https://github.com/jasonplusproductions-create/subscription-guard) — it contains only the music site, not the Subscription Guard app.

## Clone (export branch)

```bash
git clone -b jason-hackner-music --single-branch https://github.com/jasonplusproductions-create/subscription-guard.git jason-hackner-music
cd jason-hackner-music
```

## Own repo (recommended)

Create **`jason-hackner-music`** on GitHub, then:

```bash
git remote rename origin old-origin
git remote add origin https://github.com/jasonplusproductions-create/jason-hackner-music.git
git push -u origin main
```

## Artist identity photos

Add before deploy (from `Artist Identity - Jason H`):

| File | Source |
|------|--------|
| `artist-identity-06.jpg` | Pic 6 — footer |
| `artist-identity-09.jpg` | Pic 9 — gallery |

See `ASSETS.md`.

## Work with Cline (recommended)

1. Open this folder in **VS Code** with the **Cline** extension.
2. Cline reads `.clinerules` automatically — same idea as Cursor’s `.cursorrules`.
3. Example prompt:

   *"Read ASSETS.md and .clinerules. Confirm artist-identity-06 and 09 are wired in index.html. Help me deploy to Vercel."*

For **Subscription Guard** (the Next.js app), use the separate `subscription-guard` repo — its `.clinerules` points at `AGENTS.md` and `NEXT_STEPS.md`.

## Deploy (Vercel)

- Root: `.` (this folder)
- No build command
- `vercel.json` included
