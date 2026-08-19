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

## Deploy (Vercel)

- Root: `.` (this folder)
- No build command
- `vercel.json` included
