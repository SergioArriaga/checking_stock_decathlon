# checking_stock_decathlon
With python and selenium we can check if there are stock in decathlon page for one item given in the URL

The test results will be negative if there is still no stock. As soon as there is product stock (item passed through URL) the tests result will be OK

Examples URL:

- https://www.decathlon.es/es/p/kit-de-pesas-y-barras-de-musculacion-cross-training-domyos-de-50-kg/_/R-p-301315?mc=8501164
- https://www.decathlon.es/es/p/rueda-abdominal-crosstraining-musculacion-ab-wheel/_/R-p-167411?mc=8381582

# **Execution**

run cmd command:

python -m unittest discover --pattern=*.py
