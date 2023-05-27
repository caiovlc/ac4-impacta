import requests

def get_data():
    response = requests.get('http://localhost:5000/teste')
    return response.json()

def post_data(data):
    response = requests.post('http://localhost:5000/teste', json=data)
    return response.json()

def delete_data():
    response = requests.delete('http://localhost:5000/teste')
    return response.json()

if __name__ == '__main__':
    # Exemplo de uso
    print(get_data())
    print(post_data({'name': 'Caio'}))
    print(delete_data())