# load_image_from_table

## дирректория_проекта

дирректория_проекта
    feed # дирректория выгрузки картинок
    config.py # от сюда подгружается конфигурация proxy, если нужно, по умолчанию None
    load_images.py # основной скрипт
    load_xl.py # здесь определена функция которая загружает данные из xlsx файла
    sours.xlsx # здесь опредены Артикулы и соответсвующие Списки url картинок

## Установка

```bash
# win
python -m venv .venv
# lin
python3 -m venv .venv

# win
.\.venv\Scripts\activate
# lin
source .venv/bin/activate

pip install -U pip
pip install -r requirements.txt
```

## Запуск

- все файлы и дирректроии указанные в "дирректория_проекта" должны быть.
- настройки proxy должны быть установлены в `config.py`. Если прокси не нужен - значение должно быть `None`
- данные для загрузки должны быть в `sours.xlsx` в том виде как они представлены в репозитории

```bash
# win
python load_images.py
# lin
python3 load_images.py

```

