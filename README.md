# libretranslate_py
## Requirements:
#### Python 3+, `aiohttp`, `requests`
## Import
```py
import libretranslate
```
## Example usage
#### Synchronious
```py
j = libretranslate.translate_sync("http://localhost:5000", "Привет", "auto", "en")
```
#### Asynchronious
```py
j = await libretranslate.translate_async("http://localhost:5000", "Привет", "auto", "en")
```
#### Process return value
```
if "translatedText" in j:
    print(j["translatedText"])
else:
    print("Error:", j["error"])
```