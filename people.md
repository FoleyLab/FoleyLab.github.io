---
layout: page
title: People
eyebrow: Group Members
description: Current group members and selected alumni.
permalink: /people/
redirect_from:
  - /elements/
  - /elements.html
---
{% assign current_people = site.people | where: "status", "current" | sort: "sort_order" %}
{% assign alumni = site.people | where: "status", "alumni" | sort: "sort_order" %}

<section class="section-shell flush-top">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Current Team</p>
      <h2>Researchers in the Foley Lab</h2>
    </div>
  </div>
  <div class="people-grid">
    {% for person in current_people %}
    <article class="person-card">
      {% if person.image %}<img src="{{ person.image | absolute_url }}" alt="{{ person.name }}" />{% endif %}
      <h3><a href="{{ person.url | absolute_url }}">{{ person.name }}</a></h3>
      <p class="mini-meta">{{ person.role }}</p>
      <p>{{ person.research_focus }}</p>
      {% if person.email %}<p><a href="mailto:{{ person.email }}">{{ person.email }}</a></p>{% endif %}
    </article>
    {% endfor %}
  </div>
</section>

<section class="section-shell">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Alumni</p>
      <h2>Selected alumni and former trainees</h2>
    </div>
  </div>
  <div class="people-grid">
    {% for person in alumni %}
    <article class="person-card person-card--alumni">
      {% if person.image %}<img src="{{ person.image | absolute_url }}" alt="{{ person.name }}" />{% endif %}
      <h3><a href="{{ person.url | absolute_url }}">{{ person.name }}</a></h3>
      <p class="mini-meta">{{ person.role }}</p>
      <p>{{ person.research_focus }}</p>
      {% if person.current_position %}<p><strong>Current position:</strong> {{ person.current_position }}</p>{% endif %}
    </article>
    {% endfor %}
  </div>
</section>
