---
layout: page
title: Research Software
eyebrow: Open-Source Ecosystem
description: Software developed and supported by the Foley Lab for computational chemistry, cavity QED, nanophotonics, and scientific education.
permalink: /software/
---
{% assign software_items = site.software | sort: "order" %}
{% assign core_software = software_items | where: "section", "core" %}
{% assign community_software = software_items | where: "section", "community" %}

<section class="section-shell flush-top software-overview">
  <div class="feature-split">
    <div class="rich-copy">
      <p>The Foley Lab develops and contributes to open research software for light-matter theory, quantum chemistry, nanophotonics, and computational science education.</p>
      <p>This page highlights maintained lab projects alongside community software ecosystems where the group contributes methods, examples, and training materials.</p>
    </div>
    <div class="software-overview__panel">
      <p class="eyebrow">Software Focus</p>
      <h2>Reusable tools for computational science</h2>
      <p>Project cards are collection-backed so the lab can add repositories, documentation links, package metadata, and logos as the software portfolio grows.</p>
    </div>
  </div>
</section>

<section class="section-shell">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Lab-Maintained Packages</p>
      <h2>Core Lab Software</h2>
    </div>
  </div>
  <div class="software-grid">
    {% for item in core_software %}
    {% include software-card.html item=item %}
    {% endfor %}
  </div>
</section>

<section class="section-shell accent-shell">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Broader Ecosystem</p>
      <h2>Community Contributions</h2>
    </div>
  </div>
  <div class="software-grid">
    {% for item in community_software %}
    {% include software-card.html item=item %}
    {% endfor %}
  </div>
</section>
