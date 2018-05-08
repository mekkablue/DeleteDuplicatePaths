# DeleteDuplicatePaths

This is a plugin for the [Glyphs font editor](http://glyphsapp.com/) by Georg Seifert.

It deletes path duplicates. It does not care if the points are set to smooth (green) or not (blue), only if the coordinates are the same, and the closed/open status is the same.

After installation, it will add the menu item *Filter > Delete Duplicate Paths* (de: *Doppelte Pfade löschen*).

### Installation

1. Go to *Window > Plugin Manager.*
2. Click on the *Install* button next to *Delete Duplicate Glyphs.*
3. Restart the app.

### Usage Instructions

1. Select a glyph in Edit view, or select any number of glyphs in Font or Edit View.
2. Choose *Filter > Delete Duplicate Paths*.

Alternatively, you can also use it as a custom parameter. In *File > Font Info > Instances > Custom Parameters,* add a parameter by pressing the Plus button, choosing *Filter* from the *Property* pop-up menu, and type `DeleteDuplicatePaths` in its *Value.*

At the end of the parameter value, you can hang `;exclude:` or `;include:`, followed by a comma-separated list of glyph names. This will apply the filter only to the included glyphs, or the glyphs not excluded, respectively. Example:

```
DeleteDuplicatePaths; include: a, b, c, s, Aogonek, three
```

### Requirements

The plugin has only been tested for Glyphs 2.5.x on macOS High Sierra. It may not work on older configurations.

### License

Copyright 2018 Rainer Erich Scheichelbauer (@mekkablue).
Based on sample code by Georg Seifert (@schriftgestalt) and Jan Gerner (@yanone).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
