
import network
import socket
import ujson

# Buat objek AP (Access Point) dengan nama "MicroPython-AP"
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='MicroPython', password='12345678')  # Ganti dengan SSID dan password Anda
login = False

# Fungsi untuk mengirimkan halaman HTML sebagai respons
def login_page():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Page</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
            .container { width: 300px; margin: 0 auto; margin-top: 100px; background-color: #fff; padding: 20px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); }
            h2 { text-align: center; }
            input[type="text"], input[type="password"], input[type="submit"] { width: 100%; padding: 10px; margin-top: 10px; margin-bottom: 10px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 3px; }
            button[type="button"] { border: none;background-color: #4caf50; color: #fff; cursor: pointer; border-radius: 5px; padding: 7px;}
            button[type="button"]:hover { background-color: #45a049; }
        </style>
    </head>
    <body>
        <div class="container">
          <h2>Login</h2>
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>

            <button type="button" onclick="auth()" style="width: 100%;">Login</button>
        </div>
        <script>
          function auth(){
            var username = document.getElementById('username').value
            var pass = document.getElementById('password').value
            var xhr = new XMLHttpRequest();
            
            if (username == 'admin' && pass=='123'){
              xhr.open('GET', '/loginTrue', true);
              xhr.send();
              alert('success');
              window.location.href = '/dashboard';
            }
            else{
              alert('invalid username or password');
            }
          }
        </script>
    </body>
    </html>
    """
    return html.encode('utf-8')  # Encode HTML content to utf-8 to ensure proper transmission

def auth():
    html =  """
      <!DOCTYPE html>
      <html lang="en">
      <body>
        <script>
          window.location.href = '/login';
        </script>
      </body>
      </html>
    """
    return html.encode('utf-8')  # Encode HTML content to utf-8 to ensure proper transmission
    
def web_page():
    html =  """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Main Page</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 20px; background-image: url('/background.jpg'); background-size: cover; }
            .container { max-width: 800px; margin: 0 auto; background-color: #fff; padding: 20px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); }

            .row { display: flex; flex-wrap: wrap; justify-content: space-between; }
            .column { flex-basis: calc(50% - 10px); margin-bottom: 20px; }
            input[type="text"] { width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 3px; margin-top: 5px; margin-bottom: 10px; outline: none; }
            button { padding: 10px 20px; border: none; border-radius: 5px; margin-bottom: 10px; cursor: pointer; color: #fff; transition: background-color 0.3s ease; }
            button[type="submit"] { background-color: #7d90ee; }
            button[type="submit"]:hover { background-color: #667acc; }
            @media only screen and (max-width: 600px) { .column { flex-basis: 100%; margin-bottom: 10px; } }
        </style>
    </head>
    <body>
        <div class="container">
            <div style="text-align: center; margin-bottom: -20px;">
                <button type="button" onclick="getDateTime()" style="background-color: #28a745;">Set Date Time</button>
            </div>
            <div style="text-align: center; margin-bottom: 20px;">
                <p id="datetime">00:00:00/00-00-0000</p>
            </div>
            <div class="row">
                <div class="column"><input type="text" id="string_1" name="string_1" required placeholder="input string 1" ></div>
                <div class="column"><input type="text" id="string_2" name="string_2" required placeholder="input string 2"></div>
                <div class="column"><input type="text" id="string_3" name="string_3" required placeholder="input string 3"></div>
                <div class="column"><input type="text" id="string_4" name="string_4" required placeholder="input string 4"></div>
                <div class="column"><input type="text" id="string_5" name="string_5" required placeholder="input string 5"></div>
                <div class="column"><input type="text" id="string_6" name="string_6" required placeholder="input string 6"></div>
                <div class="column"><input type="text" id="string_7" name="string_7" required placeholder="input string 7"></div>
                <div class="column"><input type="text" id="string_8" name="string_8" required placeholder="input string 8"></div>
                <div class="column"><input type="text" id="string_9" name="string_9" required placeholder="input string 9"></div>
                <div class="column"><input type="text" id="string_10" name="string_10" required placeholder="input string 10"></div>
            </div>

            <div style="text-align: center;">
                <button type="button" onclick="save()" style="background-color: #007bff;width: 100%;">Save</button>
            </div>
        </div>
        <script>
            var list_Date = [];
            var json_date = {};
            function getDateTime(){
                var browserTime = new Date();
                var formattedTime = browserTime.getHours() + ':' + browserTime.getMinutes() + ':' + browserTime.getSeconds() + '/' + ('0' + browserTime.getDate()).slice(-2) + '-' + ('0' + browserTime.getMonth()).slice(-2) + '-' + browserTime.getFullYear();
                list_Date.push(browserTime.getHours(),browserTime.getMinutes(),browserTime.getSeconds(),browserTime.getDate(),browserTime.getMonth(),browserTime.getFullYear());
                json_date = {
                  'hours':browserTime.getHours(),
                  'minute':browserTime.getMinutes(),
                  'seconds':browserTime.getSeconds(),
                  'date':browserTime.getDate(),
                  'month':browserTime.getMonth(),
                  'year':browserTime.getFullYear()
                };
                document.getElementById('datetime').innerText = formattedTime;
            }
            function save(){
                var data = {
                    "a": document.getElementById('string_1').value.trim(),
                    "b": document.getElementById('string_2').value.trim(),
                    "c": document.getElementById('string_3').value.trim(),
                    "d": document.getElementById('string_4').value.trim(),
                    "e": document.getElementById('string_5').value.trim(),
                    "f": document.getElementById('string_6').value.trim(),
                    "g": document.getElementById('string_7').value.trim(),
                    "h": document.getElementById('string_8').value.trim(),
                    "i": document.getElementById('string_9').value.trim(),
                    "j": document.getElementById('string_10').value.trim()
                };
                if (Object.values(data).some(str => str.trim() === '')) {
                    alert("String input tidak boleh kosong!");
                    return;
                }
                if (list_Date.length == 0) {
                    alert("Please set date time!");
                }
                else{
                  for(var key in data){
                      var json = {
                          "data": { [key]: data[key] },
                      };
                      var jsonData = JSON.stringify(json);
                      fetch('/save', {
                          method: 'POST',
                          body: jsonData
                      })
                  }
                  var json = {
                    "data": { "dateTime": list_Date },
                  };
                  var jsonData = JSON.stringify(json);
                  fetch('/save', {
                    method: 'POST',
                    body: jsonData
                  })
                  alert('success update data');
                  var inputs = document.querySelectorAll('.row input');

                  // Mengatur nilai semua input menjadi string kosong
                  inputs.forEach(function(input) {
                      input.value = '';
                  });
                  document.getElementById('datetime').innerText = "00:00:00/00-00-0000";
                }
            }
        </script>
    </body>
    </html>
    """
    return html  # Encode HTML content to utf-8 to ensure proper transmission

def save_data(data):
    datax = data.get('data', {})
    with open('config.txt', 'w') as file:
        file.write(
            datax.get('a', '') + ';' + 
            datax.get('b', '') + ';' + 
            datax.get('c', '') + ';' +
            datax.get('d', '') + ';' +
            datax.get('e', '') + ';' +
            datax.get('f', '') + ';' +
            datax.get('g', '') + ';' +
            datax.get('h', '') + ';' +
            datax.get('i', '') + ';' +
            datax.get('j', '') 
        )
        
def parse_json_body(request):
    lines = request.split(b"\r\n")
    idx = lines.index(b"") + 1  # Temukan indeks baris kosong yang menandakan akhir header
    body = b"\r\n".join(lines[idx:])  # Ambil semua baris setelah baris kosong
    if body:
        try:
            return ujson.loads(body)
        except ValueError as e:
            print("Gagal mengurai data JSON:", e)
            return None
    else:
        return None
        
# Buat socket untuk web server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8000)) 
s.listen(5)

# Tampilkan alamat IP saat ini
print('Alamat IP Web Server:', ap.ifconfig()[0])
newJson = {
  'data':{}
}
# Terima dan tanggapi permintaan dari klien
while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    
    if b"GET /loginTrue" in request:
      login = True
    if b"GET /login" in request:
      response = login_page()
    elif b"GET /dashboard" in request:
      if not login:
        response = auth()
      else:
        response = web_page()
    
    elif b"GET /" in request:
      if not login:
        response = auth()
      else:
        response = web_page()
        
    elif b"POST /save" in request:
        try: 
            json_data = parse_json_body(request)
            
            newJson['data'].update(json_data.get('data'))
            dateTime = json_data.get('data').get('dateTime')
            save_data(newJson)

        except Exception as e:
            print("Error saat memproses data JSON:", e)
        
        # Berikan respons ke klien
        response = "HTTP/1.1 200 OK\nContent-Type: text/plain\n\nData saved successfully"
        
    # Kirimkan halaman HTML sebagai respons
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close() 
