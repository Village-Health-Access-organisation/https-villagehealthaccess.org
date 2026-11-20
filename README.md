# Village Health Access website

Static website for [villagehealthaccess.org](https://villagehealthaccess.org).
No framework and no build step on the host: the finished site is in `site/`.

## Edit the site

- Page text: `pages.py` (one section per page)
- Header and footer: `build.py`
- Colours, fonts and layout: `src/styles.css`
- Menu, copy buttons and forms: `src/site.js`
- Icons, share image, fonts, redirects and headers: `src/static/`

Then rebuild:

```bash
python3 build.py
```

This writes `site/` (the website) and `preview/index.html` (a single-file preview).
Commit both `pages.py` changes and the rebuilt `site/` folder.

Text wrapped in `<span class="ph">…</span>` shows as a yellow "To confirm" marker.
Search for `class="ph"` to find every fact that still needs a real value.

## Hosting (Cloudflare Pages)

- Framework preset: None
- Build command: (leave empty)
- Build output directory: `site`

`site/_redirects` sends old addresses (`/donors`, `/blog`) to the new pages.
`site/_headers` sets security and caching headers.

## Forms

Until a form service is connected, the contact, partner, donation pledge and
newsletter forms open a pre-filled email to the right inbox.
