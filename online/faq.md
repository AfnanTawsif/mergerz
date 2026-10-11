# FAQ

## FAQ-001

**Question:** Why does plugin installation fail?

**Answer:**
The selected Python version may be incompatible with one or more libraries required by the plugin. Before installing, choose a Python version supported by that plugin from the interpreter dropdown, then try again. If the installation still fails, review the installation log for details.

---

## FAQ-002

**Question:** Does Mergerz require an internet connection?

**Answer:**
No. Core PDF processing runs locally. An internet connection is needed to check for Mergerz updates, install or update plugins and their dependencies, download the LibreOffice converter when required, and fetch the online changelog and FAQ.

---

## FAQ-003

**Question:** Will increasing the multiprocessing worker count improve performance?

**Answer:**
It can help with tasks that can be processed in parallel, but more workers are not always faster. The default is chosen according to your CPU's logical core count, with a maximum of four workers. In most cases, keep the default. Too many workers can increase CPU and memory usage, generate more heat, add overhead, or even make a task slower.

---

## FAQ-004

**Question:** How can I contact support?

**Answer:**
Open Settings → About → Developer and use one of the contact buttons there to reach the developer.

---
