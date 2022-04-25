# checking_stock_decathlon
With python and selenium we can check if there are stock in decathlon page for one item given in the URL

The test results will be negative if there is still no stock. As soon as there is product stock (item passed through URL) the tests result will be OK.
A screenshot is saved in /screenshots to be checked later if you want

Examples URL:

- https://www.decathlon.es/es/p/bolsa-vela-tribord-5s/_/R-p-327336?mc=8601203&_adin=11551547647
- https://www.decathlon.es/es/p/rueda-abdominal-crosstraining-musculacion-ab-wheel/_/R-p-167411?mc=8660093&c=AZUL

# **Execution**

run cmd command:

python -m unittest discover --pattern=*.py
