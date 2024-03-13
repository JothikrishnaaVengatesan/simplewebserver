from http.server import HTTPServer, BaseHTTPRequestHandler
content="""
<!DOCTYPE html>
<html>
<head>
<title>top software Industries</title>
</head>
<body>
<table border="2" cellspacing="10"cellpadding="6">
<caption>Top 5 Revenue Generating Software companies</caption>
<tr>
<th>s.no</th>
<th>company</th>
<th>Revenue</th>
<th>FY</th>
</tr>
<tr>
<th>1</th>
<th>Microsoft</th>
<th>65 billion</th>
<th>2014</th>
</tr>
<tr>
<th>2</th>
<th>Oracle</th>
<th>29.6 billion</th>
<th>2013</th>
</tr>
<tr>
<th>3</th>
<th>SAP</th>
<th>$20.9</th>
<th>2013</th>
</tr>
<tr>
<th>4</th>
<th>Symantec</th>
<th>$6.8</th>
<th>2013</th>
</tr>
<tr>
<th>5</th>
<th>Symentec</th>
<th>$5.2</th>
<th>2013</th>
</tr>
<th>6</th>
<th>CA Technologies</th>
<th>4.7</th>
<th>2013</th>
</tr>
<th>7</th>
<th>Adobe Systems</th>
<th>$4.4</th>
<th>2013</th>
</tr>
<th>8</th>
<th>Fiserv</th>
<th>$4.5</th>
<th>2013</th>
</tr>
<th>9</th>
<th>Intuit</th>
<th>$4.2</th>
<th>2013</th>
</tr>
<th>10</th>
<th>Amadeus IT Group</th>
<th>$3.6 </th>
<th>2013</th>
</tr>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html;charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address=('',8000)
httpd=HTTPServer(server_address,myhandler)
print("My webserver is running...")
httpd.serve_forever()