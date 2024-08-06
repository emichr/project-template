# Welcome to MkDocs

!!! NOTE: Some features in this file are RENDERED FULLY ONLY by `mkdocs`

For full documentation visit [mkdocs.org](https://www.mkdocs.org){:target="_blank"}.

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

```
    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
```
## Logo
Change the logo under `docs/assets/logo.svg` or remove the `logo` line in `mkdocs.yml` to remove the logo.

## Useful markdown syntax examples:

### Custom icons
```
my icon is :myicons-icon1:
```
My icon is :myicons-icon1:

!!! important
    If "serving" the documentation using `mkdocs serve`, remember to shutdown and reserve it after adding new icons!

### Links

```
Example of a [link](#){:target="_blank"}
```
Example of a [link](#){:target="_blank"}

```
Example of a link to a page [my page](./Topic/index.md)
```
Example of a link to a page [my page](./Topic/index.md)
_____

### Tab groups

```
=== "Group 1"
    ```bash
    Text group 1here
    ```
=== "Group 2"
    ```bash
    Text group 2 here
    ```
```
=== "Group 1"
    Text
    ```bash
    Text group 1 here
    ```
=== "Group 2"
    Text
    ```bash
    Text group 2 here
    ```
_____

### Tables

* Use a [table generator](https://tableconvert.com/){:target="_blank"}

or 

```
| A | B | C |
|:--|:-:|--:|
| 1 | 2 | 3 |
| a | b | c |
```

| A | B | C |
|:--|:-:|--:|
| 1 | 2 | 3 |
| a | b | c |