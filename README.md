<div align="center">

<img src="https://raw.githubusercontent.com/vaxicy/butter-custard-theme/main/store-assets/icon.png?v=1" alt="Butter Custard Theme icon" width="96">

# Butter Custard Theme

Buttery light and caramel dark colour themes for VS Code.

[![VS Code Theme](https://img.shields.io/badge/VS%20Code-Theme-C2AD29?logo=visual-studio-code)](https://marketplace.visualstudio.com/items?itemName=lilinhuang.butter-custard-theme)
![Version](https://img.shields.io/badge/version-1.0.0-C2AD29)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

</div>

## Features

- Two themes in one extension: **Butter Custard Theme Light** and **Butter Custard Theme Dark**.
- Warm custard canvas in light mode (`#FEFED7`), deep cocoa canvas in dark mode (`#3C320B`).
- One golden accent drives the cursor, badges, buttons, active tab, links and active list rows.
- Muted dessert palette for syntax: mustard keywords, olive strings, caramel types, sage functions.
- Workbench-wide theming: activity bar, side bar, tabs, panel, terminal, command palette,
  lists, inputs, badges, notifications, diffs and Git decorations.
- Semantic highlighting enabled, so TypeScript, JavaScript and Python pick up accurate
  class, interface, enum, function, method, parameter, property and variable colours.

## Screenshots

Light

![Butter Custard Theme Light](https://raw.githubusercontent.com/vaxicy/butter-custard-theme/main/store-assets/screenshots/en/butter-custard-theme-light.png)

Dark

![Butter Custard Theme Dark](https://raw.githubusercontent.com/vaxicy/butter-custard-theme/main/store-assets/screenshots/en/butter-custard-theme-dark.png)

Both previews are real Visual Studio Code windows captured with the extension
installed, using the same file and the same layout — what you see is what the
theme renders.

## Palette

| Role | Light | Dark |
| --- | --- | --- |
| Editor background | `#FEFED7` | `#3C320B` |
| Foreground | `#353521` | `#FEFEBE` |
| Accent (cursor, badges) | `#C2AD29` | `#DBC00F` |
| Selection | `#FDE863` | `#5A5418` |
| Side bar | `#FFFFE5` | `#4B3E11` |
| Status bar | `#FFFFE5` | `#9C7B02` |

## Syntax

Keywords and tags carry the mustard accent, strings sit in olive, numbers and
constants in deep gold, types and classes in caramel, functions and methods in
sage green, while comments stay quiet and italic. The light variant keeps a
cocoa foreground (`#353521`) on custard paper, and the dark variant lifts it to
warm cream (`#FEFEBE`) on cocoa.

## Install

1. Open the Extensions view (`Ctrl+Shift+X` / `Cmd+Shift+X`).
2. Search for **Butter Custard Theme**.
3. Click **Install**.

Or install from the command line:

```
code --install-extension lilinhuang.butter-custard-theme
```

## Usage

1. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
2. Run **Preferences: Color Theme** (or `Ctrl+K Ctrl+T`).
3. Pick **Butter Custard Theme Light** or **Butter Custard Theme Dark**.

## Notes

- The colour themes were generated with [ThemeBake](https://themebake.pages.dev) and
  then tuned by hand.
- Preview screenshots are produced by `scripts/capture-screenshots.ps1`, which launches a
  throwaway VS Code profile with the extension installed and grabs the real window.

## Feedback

Suggestions and issues are welcome — please open an issue or pull request on
the project repository.

## License

MIT — see [LICENSE](LICENSE).
