import requests

def scan_file(api_key, file_path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': api_key}

    
    with open(file_path, 'rb') as file:
        files = {'file': (file_path, file)}
        response = requests.post(url, files=files, params=params)
    return response.json()

if __name__ == '__main__': 
    api_key = '17e92edca1284595725cbef759bf14a1a97084beca535ac5fc889f30bfcedb97'
    file_path = input("what is the path to your file?") 
    scan_result = scan_file(api_key, file_path)
    print("Scan result:", scan_result)
