# HSF Website Github Actions

## Link Checker

The link checker action runs though the `link_check.yaml`
action file.

The underlying checker is from Tom Cort, 
[markdown-link-check](https://github.com/tcort/markdown-link-check). This
is wrapped by Gaurav Nelson's [github-action-markdown-link-check](https://github.com/gaurav-nelson/github-action-markdown-link-check).

Note this checker checks markdown files directly, thus it will not check any links
in `html` files on the site. To deal with the fact that Jekyll builds the site
and creates pages from the markdown, thus internal links from `page.md` become
`page.html`, Jekyll is run first to build the site and then internal links
are mapped into `_site`.

As this action is principally to make partial checks on pull requests the
`check-modified-files-only` option is set, which will avoid most false positives
from ephemeral website glitches. See the configuration file `mdcheck.json`.
Should some links need to be masked, this can be done by setting an
`ignorePatterns` in the configuration file or adding some 
[disabling comments](https://github.com/tcort/markdown-link-check#disable-comments)
to the markdown page to be checked.
