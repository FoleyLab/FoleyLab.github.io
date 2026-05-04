# Foley Lab Website Content Guide

Most updates now happen by adding or editing small Markdown files.

## Add a person

1. Create a new file in `_people/`.
2. Copy one of the existing files and update:
   - `name`
   - `role`
   - `status` as `current` or `alumni`
   - `image`
   - `email`
   - `research_focus`
   - `education`
3. Add a short paragraph below the front matter.

## Add a publication

1. Create a new file in `_publications/`.
2. Include:
   - `title`
   - `date`
   - `journal`
   - `authors`
   - `external_url`
   - `toc_figure`
   - `abstract`
3. Optionally add extra notes or highlights below the front matter.

## Add a news item

1. Create a new file in `_news/`.
2. Include:
   - `title`
   - `date`
   - `image`
3. Write the news item body below the front matter.

## Add images

- Put images in `images/`.
- Reference them as `/images/filename.png` in front matter.

## Research tools

- The tools page lives at `tools.md`.
- Front-end behavior for widgets lives in `assets/js/research-tools.js`.
- Styling for the redesign lives in `assets/css/foleylab.css`.
- Future calculation logic can be dropped into the existing widget handlers without changing the page structure.
