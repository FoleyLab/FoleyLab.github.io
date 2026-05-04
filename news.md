---
layout: page
title: News
eyebrow: Lab Updates
description: Announcements, highlights, events, and milestones from the Foley Lab.
permalink: /news/
redirect_from:
  - /blog/
  - /blog.html
---
{% assign items = site.news | sort: "date" | reverse %}

<section class="section-shell flush-top">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Collection-Based Updates</p>
      <h2>Recent news from the group</h2>
    </div>
  </div>
  <div class="feature-grid">
    {% for item in items %}
    <article class="story-card">
      {% if item.image %}<img src="{{ item.image | absolute_url }}" alt="{{ item.title }}" />{% endif %}
      <div class="story-card__body">
        <p class="mini-meta">{{ item.date | date: "%B %d, %Y" }}</p>
        <h3><a href="{{ item.url | absolute_url }}">{{ item.title }}</a></h3>
        <p>{{ item.content | strip_html | truncate: 190 }}</p>
        <a href="{{ item.url | absolute_url }}" class="text-link">Read more</a>
      </div>
    </article>
    {% endfor %}
  </div>
</section>

<section class="section-shell accent-shell">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Legacy Archive</p>
      <h2>Earlier blog-format posts</h2>
    </div>
  </div>
  <div class="feature-grid">
    {% assign legacy_posts = site.posts | where: "category", "post" | sort: "date" | reverse %}
    {% for item in legacy_posts limit:6 %}
    <article class="story-card compact">
      {% if item.image %}<img src="{{ item.image | absolute_url }}" alt="{{ item.title }}" />{% endif %}
      <div class="story-card__body">
        <p class="mini-meta">{{ item.date | date: "%B %d, %Y" }}</p>
        <h3><a href="{{ item.url | absolute_url }}">{{ item.title }}</a></h3>
        <p>{{ item.content | strip_html | truncate: 140 }}</p>
      </div>
    </article>
    {% endfor %}
  </div>
</section>
