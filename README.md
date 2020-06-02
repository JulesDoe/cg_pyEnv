# CodinGame Python Multi-file Script VS-Code

Minimaly forked from https://github.com/devYaoYH/cg_pyEnv and portet to Visual Studio Code on Windows.
**No guarantees at all** as i have no idea what im dooing here.

Simple script to collate python class definitions across multiple files with `python build.py <file>`.

Can incoporate `build.py` into your own workflow but below I describe a convenient workflow with **VS Code**

## Sample Workflow

`.vscode/tasks.json` includes a build configuration to automatically run `build.py` on currently active file in the editor.

**Note:** `build.py` must exist in the same directory as the file to be built

1. Hit `ctrl + shift + B`

2. Set build system to "Compile to CG" if not already set

3. Build project, will output to `cg.out` 

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
