# libretranslate_py
## Requirements:
Python 3+, `aiohttp`, `requests`
Import
```py
import libretranslate
```
## Example usage
Synchronious
```py
j = libretranslate.translate_sync("http://localhost:5000", "Привет", "auto", "en")
```
Asynchronious
```py
j = await libretranslate.translate_async("http://localhost:5000", "Привет", "auto", "en")
```
Process return value
```py
if "translatedText" in j:
    print(j["translatedText"])
else:
    print("Error:", j["error"])
```

## TODOS
- Add more methods

## Have ideas or need help? 
Create issue or concat me via nosare@yandex.ru or Interlocked#6505