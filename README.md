# PDM Template for pyhat project

This is an opinionated template to generate PyHAT project with `pdm` and `fastapi`.

This templated is based on [PyHAT SimpleSite](https://github.com/rainmana/PyHAT-SimpleSite)

You can read more about PyHAT on [PyHAT Awesome](https://github.com/PyHAT-stack/awesome-python-htmx)

## Start a new project

To initialize a new project with this template, you can execute:

```bash
pdm init https://github.com/ppalazon/pdm-template-pyhat
pdm init git@github.com:ppalazon/pdm-template-pyhat.git
```

You can read more about `PDM` templates on [usage template](https://pdm-project.org/latest/usage/template/)

After you've initialized this project, you can install all dependencies with the following command:

```bash
pdm update
```

## PDM Scripts

There are some `pdm` scripts to run `uvicorn` and `tailwind`

- `npm run start` - Execute `uvicorn` on watch mode
- `npm run tailwind` - Compile `tailwindcss` on watch mode

## Icon generator

You can generate your own image on [Logo Maker](https://www.namecheap.com/logo-maker).
I generate one with transparent background and I crop its margin to avoid problems on html

Once, you've downloaded you can generate a favicon on [Favicon generator](https://favicon.io/favicon-converter/)
