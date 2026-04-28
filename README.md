# Amazon Automation Test

## Description
This project automates Amazon product search, extracts price, and adds items to cart.

## Test Cases
- Search iPhone → print price → add to cart
- Search Samsung Galaxy → print price → add to cart

## Run Steps
pip install -r requirements.txt
playwright install
pytest -n 2

## Tech Stack
- Python
- Playwright
- Pytest
