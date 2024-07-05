<link rel="stylesheet" href="index.css">

# Styling in (pandoc) Markdown {#gradient}

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

This text is red {color: red;}

[Previous Page](Entry1.md) [NEXT Page](Entry3.md)
