# [playwright python](https://playwright.dev/python/)

## 1. Set up

- Clone source code
- Create virtual environment name: `playwrightenv`

```BASH
python -m venv playwrightenv
```

- Activate virtual environment

```BASH
source playwrightenv/Scripts/activate
```

- Install python packages (_including playwright_)

```BASH
pip install -r requirements.txt
```

- Install the required browsers:

```BASH
playwright install
```

## 2. Run test command

Reference [docs](https://playwright.dev/python/docs/test-runners)

```BASH
pytest <filename>.py --html=report/report.html
```

## 3. View report

Open file `report/report.html` with your browser
