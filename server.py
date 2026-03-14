import http.server
import socketserver
import os

# Render provides a specific PORT, otherwise default to 8080 locally
PORT = int(os.environ.get("PORT", 8080))

class SecureHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # These headers unlock SharedArrayBuffer for the WASM terminal
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), SecureHTTPRequestHandler) as httpd:
    print(f"🚀 WebBuntu Server Running on Port: {PORT}")
    httpd.serve_forever()