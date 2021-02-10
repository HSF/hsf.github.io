## To add a new organization

Proposals are attached to an organization (e.g. CERN, Fermilab…). If you are a new organization, you need to create a MD file describing your organization in this directory. This is a very simple file, containing only a (short, one paragraph) front matter section that defines the attributes of your organization.

A proposal is attached to an organization by its attribute organization that must match (case insensitive) the organization attribute defined in organization MD file. This attribute can be a single value or a list. For a list, use the following syntax in the front matter section:

organization:
 - CERN
 - Fermilab

To create a new organization, copy `_gsocorgs/2020/cern.md`, create a file for your organization and edit its contents as appropriate. The file name should be in lower case matching the organization attribute. Each organization must have a logo in the folder hsf.github.io/images in png format, named `ORG-logo.png` upper case. For example for the organization CC-IN2P3, the organization file should be named `cc-in2p3.md` and the logo file should be `CC-IN2P3-logo.png`.

Note that most organizations already have MD files in the previous year folders - they can be copied in the 2021 folder (instead of modifying CERN.md) and changed to match the rules above. 
