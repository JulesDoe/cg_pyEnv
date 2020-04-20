# CodinGame Python Multi-file Script

Simple script to collate python class definitions across multiple files with `python build.py <file>`.

Can incoporate `build.py` into your own workflow but below I describe a convenient workflow I used for OceanOfCode with **Sublime Text 3**

## Sample Workflow

Sublime-Text, `pyEnv.sublime-project` includes a build configuration to automatically run `build.py` on currently active file in the editor.

**Note:** `build.py` must exist in the same directory as the file to be built

1. Open the sublime-text project (Project->Open Project...)

2. Set build system to "Compile to CG" if not already set (Tools->Build System)

3. Build project, will output to `cg.out` (Tools->Build or use shortcut!)

4. Follow instructions to install [CG Sync](https://www.codingame.com/forum/t/codingame-sync-beta/614)

5. Watch the `cg.out` file (output from `build.py`)

6. (Optional) Toggle 'Auto Play' ON to automatically play the latest build

7. Enjoy the reduced clutter from working in a single file...

Furthermore, I found [CG Enhancer](https://www.codingame.com/forum/t/cg-enhancer/59441) also quite useful if only to increase the entire right-side panel to stderr output for debugging.

- Had to replace line:10 with `// @require https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js` to get it running on Violentmonkey since jquery-latest is depreciated

## Issues

In its present form, it is minimally working for the purposes of collating split files for cg (nowhere robust for other applications)

1. Generate dependency tree and resolve order of imports automatically

2. ??? because haven't used this for other purposes yet >.<