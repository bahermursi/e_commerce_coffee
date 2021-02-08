# e_commerce_coffee
Django E-commerce Coffee


# How to run:

install requirements.txt
```bash
pip3 install -r requirements.txt
```
Start Django app
```bash
python3 manage.py runserver
```

Availble in the app the following GET Apis:
1) Coffee Machines API: "http://127.0.0.1:8000/coffee/machines"
    - Query using any of the following fields {'product_type,'water_line_compatible'} remove or leave it empty if not needed.
2) Coffee Pods API: "http://127.0.0.1:8000/coffee/pods"
    - Query using any of the following fields {'product_type,'coffee_pods','pack_size'} remove or leave it empty if not needed.
