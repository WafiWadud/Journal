# Styling in (pandoc) Markdown

If you want to add styles to markdown and your in pandoc you have to use the `<style>` or the `<link rel="stylesheet" href="{x}.css">` where x is the file\'s name.

Example:

```markdown
<style>
.red {
  color: red;
}
</style>

This text is red {.red}
```

This will output:

<style>
.red {
  color: red;
}
</style>

[This text is red]{.red}

[Previous Page](Entry1.md) [Next Page](Entry3.md)
