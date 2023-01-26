import requests

### 1. ottenere lista dei nomi degli oggetti
### 2. per ogni nome, ottenere l'oggetto
### 3. salvare oggetto chiamandolo con {obj_name}_new
### 4. eliminare oggetto precedente
### 5. stampare nuova lista dei nomi degli oggetti

all_objs = requests.get('http://0.0.0.0:8080/objects').json()

for obj_name in all_objs:
    obj = requests.get(f'http://0.0.0.0:8080/objects/{obj_name}').json()
    print(f'{obj_name}: {obj}')
    resp = requests.post(f'http://0.0.0.0:8080/objects/{obj_name}_new', json=obj).text
    print(resp)
    resp = requests.delete(f'http://0.0.0.0:8080/objects/{obj_name}').text
    print(resp)
    print()

print()

new_objs = requests.get('http://0.0.0.0:8080/objects').json()
print(f'New objects: {new_objs}')