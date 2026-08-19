# Jason Hackner Music

Static site for **themlc.jasonplusproductions.com** — classic soul and pop, live from Charlotte.

Split out of [subscription-guard](https://github.com/jasonplusproductions-create/subscription-guard) into its own repo.

## Setup (first time)

```bash
git clone https://github.com/jasonplusproductions-create/jason-hackner-music.git
cd jason-hackner-music
```

## Artist identity photos (required before deploy)

From `C:\Users\jaydh\suno generate\Artist Identity - Jason H`, copy into this folder (site root):

| Your file | Save as | Where on site |
|-----------|---------|---------------|
| Pic **6** (leather jacket) | `artist-identity-06.jpg` | Footer row, 3rd thumbnail |
| Pic **9** (suit, red tie) | `artist-identity-09.jpg` | Gallery, slide 2 |

See `ASSETS.md` for the full asset list.

## Deploy (Vercel)

1. Create/import this repo in Vercel.
2. **Root directory:** `.` (repo root — `index.html` is at the top level).
3. No build command; static HTML deploy.
4. Custom domain: `themlc.jasonplusproductions.com` (or your existing MLC domain).

## Local preview

```bash
npx --yes serve .
# open http://localhost:3000
```

## What changed vs old live site

- Footer + gallery no longer use `20251215_153747.jpg` (Mark Larson).
- Uses `artist-identity-06.jpg` and `artist-identity-09.jpg` instead (you supply these).

## Create this repo on GitHub (one-time)

If the remote repo does not exist yet, create an empty public repo named **`jason-hackner-music`** under `jasonplusproductions-create`, then:

```bash
git remote add origin https://github.com/jasonplusproductions-create/jason-hackner-music.git
git push -u origin main
```

If you already have the standalone folder from an export:

```bash
cd jason-hackner-music
git init -b main
git add -A
git commit -m "Initial commit: Jason Hackner Music site"
git remote add origin https://github.com/jasonplusproductions-create/jason-hackner-music.git
git push -u origin main
```
