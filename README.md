# WebExtensionConvert
Automatically Convert WebExtension API between browsers.

## Usage

  ```bash
  python convert.py <path> convertType
  ```

  currently supported covertType are:<br>
  c-f    Convert chrome API to firefox API<br>
  f-c    Convert firefox API to chrome API<br>

## Compatibility check
This tool will check API used in the extension is deprecated or not available on the target browser and show the location where problems are.
But it will convert for the target browser in any way.