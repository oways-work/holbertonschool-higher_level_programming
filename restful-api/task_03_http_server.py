#!/usr/bin/python3
"""
Task 3: Develop a simple API using Python with the http.server module
"""
import http.server
import socketserver
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    A simple HTTP request handler that serves JSON and text data.
    """

    def do_GET(self):
        """
        Handle GET requests to the server.
        """
        # Endpoint: /
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Endpoint: /data
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # Endpoint: /status (as per Instructions)
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            
        # Endpoint: /info (covering the discrepancy in Expected Output)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-
