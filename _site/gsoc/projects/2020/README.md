## To add a new project

* Create a file `project_MYPROJECT.md` look at `_gsocprojects/2019/project_HSF.md` for an example. This is a very simple file, containing only a front matter section that defines the attributes of your organization. The 2 mandatory attributes are project (your project name) and layout (which must be default). In addition you can use 2 optional attributes:

   * title: the name of the project to use in the page title. By default, project attribute is used.
   * description: a description of your project that will be added before the list of proposals attached to the project.
It can be several lines: look at the `_gsocprojects/2018/project_SixTrack.md` example for detailed syntax. The content is a standard Markdown text indented by at least one space (the number is not important but must be the same for all lines).
   * logo: the logo file name in directory `images`

A proposal is attached to a project by its attribute `project` that must match (not case sensitive) the project attribute defined in project MD file. This attribute can be a single value or a list. For a list, use the following syntax in the front matter section:

project:
 - ROOT
 - GeantV
