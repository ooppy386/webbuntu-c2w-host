import http.server
import socketserver
import os

# Render dynamically assigns a port, so we must read it from the environment.
# If we are running locally, it defaults back to 8000.
PORT = int(os.environ.get("PORT", 8000))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Required for SharedArrayBuffer (Terminal) to work
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        
        # Changed from "require-corp" to "credentialless". 
        # This allows the WebSurf iframes to function on Render without breaking the Terminal!
        self.send_header("Cross-Origin-Embedder-Policy", "credentialless")
        
        super().end_headers()

# Start the server
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()