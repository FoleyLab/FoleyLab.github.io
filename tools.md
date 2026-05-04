---
layout: page
title: Interactive Tools
eyebrow: Research Widgets
description: A home for browser-based tools related to light-matter interactions and lab workflows.
permalink: /tools/
---
<section class="section-shell flush-top">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Tooling Roadmap</p>
      <h2>Framework ready for future scientific calculators</h2>
    </div>
  </div>
  <div class="feature-grid">
    <article class="feature-card">
      <h3>Mie Theory</h3>
      <p>Planned support for nanoparticle scattering, absorption, and extinction calculations from user-defined radii, dielectric data, and wavelengths.</p>
    </article>
    <article class="feature-card">
      <h3>Transfer Matrix Optics</h3>
      <p>Planned thin-film stack builders for reflectivity, transmissivity, and absorptivity of layered materials.</p>
    </article>
    <article class="feature-card">
      <h3>Cavity QED Models</h3>
      <p>Planned widgets for constructing model Hamiltonians, diagonalizing cavity-matter systems, and visualizing polaritonic state character.</p>
    </article>
  </div>
</section>

<section class="section-shell accent-shell">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Prototype Widgets</p>
      <h2>Usable shell for future logic</h2>
    </div>
  </div>
  <div class="tool-grid">
    <article class="tool-card">
      <h3>Unit Conversion</h3>
      <p>Simple live conversion utility for common spectroscopy and cavity-QED units.</p>
      <form class="tool-form" data-tool="converter">
        <label for="converter-value">Value</label>
        <input id="converter-value" name="value" type="number" step="any" value="532" />
        <label for="converter-mode">Conversion</label>
        <select id="converter-mode" name="mode">
          <option value="nm-to-ev">Wavelength (nm) to Energy (eV)</option>
          <option value="ev-to-nm">Energy (eV) to Wavelength (nm)</option>
          <option value="cm-to-ev">Wavenumber (cm^-1) to Energy (eV)</option>
          <option value="ev-to-cm">Energy (eV) to Wavenumber (cm^-1)</option>
        </select>
        <button type="submit" class="button special small">Convert</button>
      </form>
      <div class="tool-output" data-tool-output="converter">Enter a value and choose a conversion.</div>
    </article>

    <article class="tool-card">
      <h3>Mie Theory Widget</h3>
      <p>Interface scaffold for future scattering and absorption calculations.</p>
      <form class="tool-form" data-tool="placeholder" data-placeholder="Mie theory backend coming soon.">
        <label for="mie-radius">Particle radius (nm)</label>
        <input id="mie-radius" name="radius" type="number" step="any" value="50" />
        <label for="mie-wavelength">Wavelength (nm)</label>
        <input id="mie-wavelength" name="wavelength" type="number" step="any" value="650" />
        <button type="submit" class="button small">Preview Widget Shell</button>
      </form>
      <div class="tool-output" data-tool-output="placeholder">Calculation logic can be attached later without redesigning the UI.</div>
    </article>

    <article class="tool-card">
      <h3>Transfer Matrix Widget</h3>
      <p>Ready for a future thin-film stack parser and spectrum solver.</p>
      <form class="tool-form" data-tool="placeholder" data-placeholder="Transfer-matrix backend coming soon.">
        <label for="tm-layers">Layer count</label>
        <input id="tm-layers" name="layers" type="number" step="1" value="3" />
        <label for="tm-range">Wavelength range (nm)</label>
        <input id="tm-range" name="range" type="text" value="400-800" />
        <button type="submit" class="button small">Preview Widget Shell</button>
      </form>
      <div class="tool-output" data-tool-output="placeholder">Use this shell for reflectivity, transmissivity, and absorptivity tools.</div>
    </article>
  </div>
</section>
