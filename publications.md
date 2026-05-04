---
layout: page
title: Publications
eyebrow: Research Output
description: Collection-backed publication entries with abstracts, links, and table-of-contents graphics.
permalink: /publications/
redirect_from:
  - /publications.html
---
{% assign pubs = site.publications | sort: "date" | reverse %}

<section class="section-shell flush-top">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Publication Library</p>
      <h2>Recent papers and featured abstracts</h2>
    </div>
  </div>
  <div class="publication-list">
    {% for item in pubs %}
    <article class="publication-card">
      {% if item.toc_figure %}
      <a href="{{ item.url | absolute_url }}" class="publication-card__media">
        <img src="{{ item.toc_figure | absolute_url }}" alt="{{ item.title }}" />
      </a>
      {% endif %}
      <div class="publication-card__body">
        <p class="mini-meta">{{ item.journal }} • {{ item.date | date: "%B %Y" }}</p>
        <h2><a href="{{ item.url | absolute_url }}">{{ item.title }}</a></h2>
        <p class="pub-authors">{{ item.authors }}</p>
        <p>{{ item.abstract | truncate: 320 }}</p>
        <ul class="actions">
          <li><a href="{{ item.url | absolute_url }}" class="button small">Details</a></li>
          {% if item.external_url %}<li><a href="{{ item.external_url }}" class="button small">Journal Link</a></li>{% endif %}
        </ul>
      </div>
    </article>
    {% endfor %}
  </div>
</section>
