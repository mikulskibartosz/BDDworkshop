1. Get the virtualenv path:

```bash
poetry env use python
```



---

cd bddtter
poetry run python3 app.py

poetry run behave --tags=@rest
poetry run behave --tags=@lru
poetry run behave --tags=@mock

poetry run behave

