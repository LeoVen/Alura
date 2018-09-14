# HTML5 & CSS3 Notes

### Absolute lengths

|Unit|Description|
|:--:|:----------|
|cm|centimeters|
|mm|millimeters|
|in|inches (1in = 96px = 2.54cm)|
|px|pixels (1px = 1/96th of 1in) (relative to viewing device)|
|pt|points (1pt = 1/72 of 1in)|
|pc|picas (1pc = 12 pt)|

### Relative lengths

|Unit|Description|
|:--:|:----------|
|em|Relative to the font-size of the element (2em means 2 times the size of the current font)|
|ex|Relative to the x-height of the current font (rarely used)|
|ch|Relative to width of the "0" (zero)|
|rem|Relative to font-size of the root element|
|vw|Relative to 1% of the width of the viewport|
|vh|Relative to 1% of the height of the viewport|
|vmin|Relative to 1% of viewport's smaller dimension|
|vmax|Relative to 1% of viewport's larger dimension|
|%|Relative to the parent element|

### Vendor Prefixes

Chrome/Safari
```CSS
-webkit-border-radius: 10px;
```

Firefox
```CSS
-moz-border-radius: 10px;
```

Internet Explorer/Edge
```CSS
-ms-border-radius: 10px;
```

Opera
```CSS
-o-border-radius: 10px;
```

https://caniuse.com/