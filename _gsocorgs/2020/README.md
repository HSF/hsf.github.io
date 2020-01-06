## To add a new organization

Proposals are attached to an organization (e.g. CERN, Fermilab…). If you are a new organization, you need to create a MD file describing your organization in this directory. This is a very simple file, containing only a front matter section that defines the attributes of your organization.

A proposal is attached to an organization by its attribute organization that must match (case insensitive) the organization attribute defined in organization MD file. This attribute can be a single value or a list. For a list, use the following syntax in the front matter section:

organization:
 - CERN
 - Fermilab
To create a new organization, copy `_gsocorgs/2020/cern.md`, create a file for your organization and edit its contents as appropriate.
