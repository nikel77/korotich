import cgi
import http.server
import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8090
Handler = http.server.SimpleHTTPRequestHandler


class ReqHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            filename = 'task.html'
        else:
            filename = self.path[1:]

        self.send_response(200)
        if filename[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
        elif filename[-3:] == '.js':
            self.send_header('Content-type', 'application/javascript')
        else:
            self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fh:
            html = fh.read()
            self.wfile.write(html)

    def do_POST(self):
        timestamp = datetime.utcnow()
        content_type, pdict = cgi.parse_header(self.headers['content-type'])
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        content_length = int(self.headers.get('Content-length'), 0)
        pdict['CONTENT-LENGTH'] = content_length
        if content_type == 'multipart/form-data':
            payload = cgi.parse_multipart(self.rfile, pdict)
            text_input = payload['textInput'][0]
            single_file_content = payload['singleFileInput'][0].decode('ascii')
            multiple_file_content = [text.decode('utf-8') for text in payload['multipleFileInput']]
            data_dict = {'text_input': text_input,
                         'single_file_content': single_file_content,
                         'multiple_file_content': multiple_file_content,
                         }
            with open('{}.json'.format(timestamp), 'x') as new_data_file:
                json.dump(data_dict, new_data_file)
        self.send_response(200)


server = HTTPServer(('', PORT), ReqHandler)
print("Web Server running on port: {}".format(PORT))
server.serve_forever()
