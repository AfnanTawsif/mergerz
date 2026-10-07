[![PyPI](https://img.shields.io/pypi/v/mergerz?style=flat-square&label=PyPI)](https://pypi.org/project/mergerz/) [![Python](https://img.shields.io/pypi/pyversions/mergerz?style=flat-square&label=Python)](https://pypi.org/project/mergerz/)

<p align="center">
  <img src="./media/screenshot1.webp" alt="Mergerz main menu" width="600">
</p>

**[View all screenshots →](./media/screenshots.md)**

# Introduction

**Mergerz is a free, PDF-focused desktop utility for editing, organizing, transforming, optimizing, securing, converting, and presenting documents with a PDF-native workflow that preserves text, vectors, page content and quality.**

The goal is simple:

> **Do more to your documents without unnecessarily destroying what is already inside them.**

Mergerz is built around a **PDF-native editing philosophy**. Operations such as invert, crop, rotate, flip, stretch, and other page transformations are performed directly on PDF pages and their underlying content whenever possible, rather than unnecessarily rasterizing the entire page.

This means less unnecessary bloat, faster processing, better scalability, and better preservation of vectors, text, and overall document quality.

# Installation

## Requirements

- Python 3.10 or newer
- PySide6-supported desktop platform

Optional functionality such as OCR, PDF-to-DOCX and LibreOffice conversion can be installed separately through Mergerz's plugin system.


## Install & Launch

Install or upgrade Mergerz with:

`python -m pip install --upgrade mergerz`

Then launch using:

`mergerz`

That is it.

---

# Why Choose Mergerz?

### Free to use

Mergerz is designed as a free desktop utility rather than a subscription-based document editor.

### PDF-native by design

The editor is built to avoid full-page rasterization for ordinary PDF editing operations. Text, vector artwork and page geometry can remain native instead of being flattened into a giant image.

### Full desktop application

No caller script. No terminal-driven menu. No manual script editing.

Install it and launch:

`mergerz`

### Huge feature set

Mergerz is no longer just a PDF merger. It now combines document editing, printing, optimization, conversion, OCR, security, page design, image processing and workflow automation in one application.

### Performance-focused

CPU-heavy tasks use background workers and multiprocessing where beneficial. Operations can use configurable worker counts, thresholds, temporary storage and memory policies.

### Strong cancellation and recovery

Long-running operations expose live progress and logs, with cancellation support where safe. Temporary work is staged separately and many save operations are verified before replacing or updating a destination.

### Smart memory handling

Processes like thumbnail rendering includes memory-safety logic and configurable memory policies to reduce the chance of exhausting RAM on large documents.

### Automatic application updates

Mergerz can quietly check PyPI after startup, notify you when a newer version exists, install the exact release and restart itself automatically.

### Modular plugin system

Heavy optional features are separated from the core installation. OCR, PDF-to-DOCX and LibreOffice functionality can be installed, updated or removed independently.


### Sleek dark UI

The application uses a custom dark desktop interface with custom window chrome, responsive layouts, modern dialogs, live previews and carefully designed workflow screens.


**[Explore all features →](./docs/features.md)**

---

# Design Philosophy

Mergerz is built around a few principles:

### 1. Don't rasterize what does not need to be rasterized.

A PDF already contains structured content.

Crop, rotation, flipping, stretch, page numbering, borders, watermarks and core filtering workflows are designed to operate on the document rather than turning the whole page into a screenshot first.

### 2. Heavy dependencies should be optional.

OCR, PDF2DOCX and LibreOffice are useful, but not every user needs them.

### 3. Large operations should be observable.

Show the user what is happening through progress, logs, status messages and result summaries.

### 4. Cancellation should be safe.

Do not abandon workers, child processes or temporary files just because the user pressed Cancel.

### 5. Never modify the source unnecessarily.

Use temporary output, verification and atomic replacement whenever practical.

### 6. Never ruin previous edits.

New edit operations are done on top of previous editing results, so that we can expected outputs.

### 6. Performance should scale with the workload.

Small tasks should stay lightweight.

Large workloads should be able to use multiprocessing, worker pools, caching and memory-aware strategies.

---

# Changelog

See the full release history:

https://github.com/AfnanTawsif/mergerz/releases

---

# Issues & Feature Requests

Bug reports, feature requests and technical feedback are welcome through GitHub Issues:

https://github.com/AfnanTawsif/mergerz/issues

---

# Contact

For questions, feedback or development-related contact:

- Facebook: https://www.facebook.com/not.tawsif
- Instagram: https://www.instagram.com/_hey_tawsif_/
- Telegram: https://t.me/KindaDeadNgl
- Email: acer.only2001@gmail.com

---

# License

**All Rights Reserved.**

Mergerz is free to use, but the source code, application, branding and associated assets are not released under the MIT License or another permissive open-source license.

Do not redistribute, relicense, modify for redistribution, or commercially repackage the project without permission from the author.

---

<p align="center">
  <b>Mergerz</b><br>
  A document workspace built to do more - while preserving more.
</p>

<p align="center">
  © Afnan Tawsif - All Rights Reserved
</p>
