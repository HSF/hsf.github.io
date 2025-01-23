# HSF Logos

This directory contains the HSF logo redone in SVG (Inkscape), after the original
version done my Joschka Lingemann.

- `hsf-logo-text.svg` classic HSF logo, including the full "HEP Software
  Foundation" text at the bottom
- `hsf-logo-no-text.svg` no text at the bottom
- `hsf-logo-text-pale.svg` interaction lines in white, with the bottom text
  lighter grey
- `hsf-logo-shield-full.svg` chunkier version of the logo much more suited to
  making shields on <shields.io> (as these logos are dark, the interaction lines
  are white in this version)
- `hsf-logo-shield-s-only.svg` shield logo that only has the interaction lines
  and the "S"

## HSF Project Badges

For shield logos, the SVG is base64 encoded, then passed in as a URL parameter.
See [shields.io](https://shields.io/docs/logos) documentation.

To get the base64 encoding of one of the logos, try:

```shell
base64 -o - -i hsf-logo-shield-full.svg
```

Links for the current versions of the badges, including cached versions, are on the [badges page](https://hepsoftwarefoundation.org/projects/badges.html).

## Colour Notes

The HSF red is #aa0000. The lower text is grey 40%, aka #999999.

For the HSF project affiliations, gold is #FFD700, silver is #C0C0C0 and bronze is #CD7F32 (the first two are also the standard HTML/CSS colour names *gold* and *silver*).
