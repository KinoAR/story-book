# Story Book
> Created by Kino Rose - NierPixel.com

A microservice designed to allow you to access the json file for your ink stories directly from your console.


## How to Start the Server

```bash
# gunicorn -b :portnumber file_name:app
gunicorn -b :8083 story:app
```


## Technologies

* Falcon
* Inkle
* Ink
* Mypy for static type checking
* gunicorn