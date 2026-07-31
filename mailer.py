#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HDN-Mailer - Advanced Email Phishing Simulator
Educational Purpose Only - Ethical Hacking Training
"""

import os
import sys
import json
import time
import smtplib
import ssl
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import colorama
from colorama import Fore, Back, Style

# ============ FIX UNICODE ENCODING ============
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# ============ CONFIGURATION ============
colorama.init(autoreset=True)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SMTP_CONFIG = os.path.join(BASE_DIR, "smtp_config.json")
SENT_LOG = os.path.join(BASE_DIR, "sent_log.txt")
DRAFTS_DIR = os.path.join(BASE_DIR, "drafts")

# Create directories
os.makedirs(DRAFTS_DIR, exist_ok=True)

# ============ EMAIL TEMPLATES ============

EMAIL_TEMPLATES = {
    'password_reset': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Reset</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
        .container { max-width: 600px; margin: 30px auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { background: #0095f6; padding: 30px; text-align: center; }
        .header h1 { color: white; margin: 0; font-size: 24px; }
        .content { padding: 30px; }
        .content h2 { color: #333; }
        .content p { color: #666; line-height: 1.6; }
        .button { display: inline-block; padding: 14px 40px; background: #0095f6; color: white; text-decoration: none; border-radius: 4px; font-weight: bold; margin: 20px 0; }
        .button:hover { background: #0077c8; }
        .footer { padding: 20px; text-align: center; color: #999; font-size: 12px; border-top: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{{COMPANY}} Security</h1>
        </div>
        <div class="content">
            <h2>Hi {{TARGET_NAME}},</h2>
            <p>We received a request to reset your {{COMPANY}} password.</p>
            <p>Click the button below to reset your password:</p>
            <div style="text-align: center;">
                <a href="{{PHISH_LINK}}" class="button">Reset Password</a>
            </div>
            <p>If you didn't request this, please ignore this email.</p>
            <p style="font-size: 14px; color: #888;"><strong>Link:</strong> {{PHISH_LINK}}</p>
        </div>
        <div class="footer">
            <p>{{COMPANY}} Security Team</p>
            <p>This is a simulated training email.</p>
        </div>
    </div>
</body>
</html>''',

    'security_alert': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security Alert</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
        .container { max-width: 600px; margin: 30px auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { background: #dc3545; padding: 30px; text-align: center; }
        .header h1 { color: white; margin: 0; font-size: 24px; }
        .content { padding: 30px; }
        .alert-box { background: #fff3cd; border: 1px solid #ffc107; padding: 15px; border-radius: 4px; margin: 15px 0; }
        .button { display: inline-block; padding: 14px 40px; background: #dc3545; color: white; text-decoration: none; border-radius: 4px; font-weight: bold; margin: 20px 0; }
        .button:hover { background: #c82333; }
        .footer { padding: 20px; text-align: center; color: #999; font-size: 12px; border-top: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Security Alert</h1>
        </div>
        <div class="content">
            <h2>Hi {{TARGET_NAME}},</h2>
            <p>We detected unusual login activity on your {{COMPANY}} account.</p>
            <div class="alert-box">
                <strong>Location:</strong> {{SPOOF_LOCATION}}<br>
                <strong>Device:</strong> {{SPOOF_DEVICE}}<br>
                <strong>Time:</strong> {{TIMESTAMP}}
            </div>
            <p>If this wasn't you, please secure your account immediately:</p>
            <div style="text-align: center;">
                <a href="{{PHISH_LINK}}" class="button">Secure Your Account</a>
            </div>
        </div>
        <div class="footer">
            <p>{{COMPANY}} Security Team</p>
        </div>
    </div>
</body>
</html>''',

    'invoice': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Invoice</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
        .container { max-width: 600px; margin: 30px auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { background: #28a745; padding: 30px; text-align: center; }
        .header h1 { color: white; margin: 0; font-size: 24px; }
        .content { padding: 30px; }
        .invoice-box { background: #f8f9fa; padding: 15px; border-radius: 4px; }
        .button { display: inline-block; padding: 14px 40px; background: #28a745; color: white; text-decoration: none; border-radius: 4px; font-weight: bold; margin: 20px 0; }
        .button:hover { background: #218838; }
        .footer { padding: 20px; text-align: center; color: #999; font-size: 12px; border-top: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Invoice #{{INVOICE_NUM}}</h1>
        </div>
        <div class="content">
            <h2>Hi {{TARGET_NAME}},</h2>
            <p>Please find your invoice from {{COMPANY}}.</p>
            <div class="invoice-box">
                <p><strong>Invoice #:</strong> {{INVOICE_NUM}}</p>
                <p><strong>Amount:</strong> {{AMOUNT}}</p>
                <p><strong>Due Date:</strong> {{TIMESTAMP}}</p>
            </div>
            <div style="text-align: center;">
                <a href="{{PHISH_LINK}}" class="button">View Invoice</a>
            </div>
        </div>
        <div class="footer">
            <p>{{COMPANY}} Billing Department</p>
        </div>
    </div>
</body>
</html>''',

    'shared_document': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shared Document</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
        .container { max-width: 600px; margin: 30px auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { background: #6f42c1; padding: 30px; text-align: center; }
        .header h1 { color: white; margin: 0; font-size: 24px; }
        .content { padding: 30px; }
        .doc-box { background: #f8f9fa; padding: 15px; border-radius: 4px; }
        .button { display: inline-block; padding: 14px 40px; background: #6f42c1; color: white; text-decoration: none; border-radius: 4px; font-weight: bold; margin: 20px 0; }
        .button:hover { background: #5a32a3; }
        .footer { padding: 20px; text-align: center; color: #999; font-size: 12px; border-top: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Document Shared</h1>
        </div>
        <div class="content">
            <h2>Hi {{TARGET_NAME}},</h2>
            <p>{{SENDER_NAME}} shared a document with you.</p>
            <div class="doc-box">
                <p><strong>Document:</strong> {{DOC_NAME}}</p>
                <p><strong>Size:</strong> {{FILE_SIZE}}</p>
                <p><strong>Shared:</strong> {{SHARE_TIME}}</p>
            </div>
            <div style="text-align: center;">
                <a href="{{PHISH_LINK}}" class="button">View Document</a>
            </div>
        </div>
        <div class="footer">
            <p>{{COMPANY}} Document Sharing</p>
        </div>
    </div>
</body>
</html>''',

    'custom': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{SUBJECT}}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
        .container { max-width: 600px; margin: 30px auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .content { padding: 30px; }
        .button { display: inline-block; padding: 14px 40px; background: #007bff; color: white; text-decoration: none; border-radius: 4px; font-weight: bold; margin: 20px 0; }
        .footer { padding: 20px; text-align: center; color: #999; font-size: 12px; border-top: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="container">
        <div class="content">
            <h2>Hi {{TARGET_NAME}},</h2>
            {{CUSTOM_BODY}}
            <div style="text-align: center;">
                <a href="{{PHISH_LINK}}" class="button">{{BUTTON_TEXT}}</a>
            </div>
        </div>
        <div class="footer">
            <p>{{COMPANY}} Team</p>
        </div>
    </div>
</body>
</html>'''
}

# ============ EMAIL CRAFTER CLASS ============

class EmailCrafter:
    def __init__(self):
        self.config = self.load_config()
    
    def load_config(self):
        if os.path.exists(SMTP_CONFIG):
            try:
                with open(SMTP_CONFIG, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_config(self, config):
        with open(SMTP_CONFIG, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
    
    def test_smtp(self, config):
        """Test SMTP connection"""
        try:
            if config.get('use_ssl'):
                server = smtplib.SMTP_SSL(config['server'], config['port'], timeout=10)
            else:
                server = smtplib.SMTP(config['server'], config['port'], timeout=10)
                server.starttls()
            
            server.login(self.config['email'], self.config['password'])
            server.quit()
            return True
        except Exception as e:
            print(f"  {Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
            return False
    
    def generate_email_body(self, template_key, custom_data, target_name, company, phish_link):
        """Generate email body with variables replaced"""
        if template_key and template_key in EMAIL_TEMPLATES:
            body = EMAIL_TEMPLATES[template_key]
            replacements = {
                '{{TARGET_NAME}}': target_name,
                '{{COMPANY}}': company,
                '{{PHISH_LINK}}': phish_link,
                '{{SENDER_NAME}}': self.config.get('sender_name', 'Security Team'),
                '{{SENDER_EMAIL}}': self.config.get('email', ''),
                '{{TIMESTAMP}}': datetime.now().strftime('%b %d, %Y  %I:%M %p UTC'),
                '{{SPOOF_LOCATION}}': 'Unknown Location',
                '{{SPOOF_DEVICE}}': 'Windows 11 / Chrome',
                '{{AMOUNT}}': '$299.00',
                '{{INVOICE_NUM}}': f"INV-{int(time.time()) % 100000}",
                '{{DOC_NAME}}': 'Important_Document.pdf',
                '{{FILE_SIZE}}': '2.4 MB',
                '{{SHARE_TIME}}': datetime.now().strftime('%I:%M %p'),
                '{{SUBJECT}}': custom_data.get('subject', 'Important Notice'),
                '{{CUSTOM_BODY}}': custom_data.get('body', ''),
                '{{BUTTON_TEXT}}': custom_data.get('button_text', 'Click Here')
            }
            for key, value in replacements.items():
                body = body.replace(key, value)
            return body
        else:
            return custom_data.get('body', '')
    
    def send_email(self, to_email, to_name, subject, body, config):
        """Send email via SMTP"""
        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = f"{self.config.get('sender_name', 'Security Team')} <{self.config['email']}>"
            msg['To'] = to_email
            msg['Subject'] = subject if subject else 'Important: Security Notice'
            
            html_part = MIMEText(body, 'html', 'utf-8')
            msg.attach(html_part)
            
            if config.get('use_ssl'):
                server = smtplib.SMTP_SSL(config['server'], config['port'], timeout=30)
            else:
                server = smtplib.SMTP(config['server'], config['port'], timeout=30)
                server.starttls()
            
            server.login(self.config['email'], self.config['password'])
            server.send_message(msg)
            server.quit()
            
            print(f"  {Fore.GREEN}[✓] DELIVERED -> {to_email}{Style.RESET_ALL}")
            
            with open(SENT_LOG, 'a', encoding='utf-8') as f:
                f.write(f"{datetime.now().isoformat()} | {to_email} | {to_name} | {subject} | OK\n")
            
            return True
        except Exception as e:
            print(f"  {Fore.RED}[✗] FAILED -> {to_email}: {str(e)}{Style.RESET_ALL}")
            return False
    
    def craft_email(self):
        print(f"""
{Fore.RED}╔══════════════════════════════════════════╗
{Fore.RED}║{Fore.WHITE}          HDN-MAILER v1.0                {Fore.RED}║
{Fore.RED}║{Fore.YELLOW}    Email Phishing Simulator               {Fore.RED}║
{Fore.RED}║{Fore.MAGENTA}    [ Code: Hasnain Darknet ]            {Fore.RED}║
{Fore.RED}║{Fore.CYAN}    Educational Purpose Only                {Fore.RED}║
{Fore.RED}╚══════════════════════════════════════════╝{Style.RESET_ALL}
        """)
        
        # ========== STEP 1: SMTP Setup ==========
        print(f"{Fore.CYAN}[*] STEP 1: Email Account Setup{Style.RESET_ALL}")
        print(f"{Fore.WHITE}─────────────────────────────────────{Style.RESET_ALL}")
        print(f"  {Fore.GREEN}[1]{Style.RESET_ALL} Gmail (App Password)")
        print(f"  {Fore.GREEN}[2]{Style.RESET_ALL} Outlook/Hotmail")
        print(f"  {Fore.GREEN}[3]{Style.RESET_ALL} Yahoo")
        print(f"  {Fore.GREEN}[4]{Style.RESET_ALL} Custom SMTP")
        print(f"  {Fore.GREEN}[5]{Style.RESET_ALL} Use saved config")
        
        smtp_choice = input(f"  {Fore.CYAN}[?] Select provider: {Style.RESET_ALL}")
        
        smtp_config = {
            'server': 'smtp.gmail.com',
            'port': 587,
            'use_ssl': False
        }
        
        if smtp_choice == '1':
            smtp_config['server'] = 'smtp.gmail.com'
            smtp_config['port'] = 587
            print(f"  {Fore.YELLOW}[!] Gmail requires App Password. Generate at: myaccount.google.com/apppasswords{Style.RESET_ALL}")
        elif smtp_choice == '2':
            smtp_config['server'] = 'smtp-mail.outlook.com'
            smtp_config['port'] = 587
        elif smtp_choice == '3':
            smtp_config['server'] = 'smtp.mail.yahoo.com'
            smtp_config['port'] = 587
        elif smtp_choice == '4':
            custom = input(f"  {Fore.CYAN}[?] SMTP server:port: {Style.RESET_ALL}")
            if ':' in custom:
                server, port = custom.split(':')
                smtp_config['server'] = server
                smtp_config['port'] = int(port)
                if str(port) == '465':
                    smtp_config['use_ssl'] = True
            else:
                smtp_config['server'] = custom
                smtp_config['port'] = 587
        elif smtp_choice == '5':
            if 'email' in self.config:
                print(f"  {Fore.GREEN}[✓] Loaded: {self.config['email']}{Style.RESET_ALL}")
                smtp_config = self.config.get('smtp_config', smtp_config)
            else:
                print(f"  {Fore.RED}[!] No saved config{Style.RESET_ALL}")
                return
        
        # Get credentials if not saved
        if 'email' not in self.config or smtp_choice != '5':
            self.config['email'] = input(f"  {Fore.CYAN}[?] Your email: {Style.RESET_ALL}")
            self.config['password'] = input(f"  {Fore.CYAN}[?] Password/App Password: {Style.RESET_ALL}")
            self.config['sender_name'] = input(f"  {Fore.CYAN}[?] Display name: {Style.RESET_ALL}")
            self.config['smtp_config'] = smtp_config
            
            save = input(f"  {Fore.YELLOW}[?] Save credentials? (y/n): {Style.RESET_ALL}")
            if save.lower() == 'y':
                self.save_config(self.config)
                print(f"  {Fore.GREEN}[✓] Credentials saved{Style.RESET_ALL}")
        
        # Test SMTP
        print(f"\n  {Fore.CYAN}[*] Testing SMTP connection...{Style.RESET_ALL}")
        if self.test_smtp(smtp_config):
            print(f"  {Fore.GREEN}[✓] SMTP authenticated{Style.RESET_ALL}")
        else:
            print(f"  {Fore.RED}[✗] SMTP FAILED{Style.RESET_ALL}")
            print(f"  {Fore.YELLOW}[!] Tips:{Style.RESET_ALL}")
            print(f"    - Gmail: Enable 2FA and generate App Password")
            print(f"    - Check SMTP server details")
            print(f"    - Try port 465 with SSL for Gmail")
            input("  Press Enter to continue...")
            return
        
        # ========== STEP 2: Template Selection ==========
        print(f"\n{Fore.CYAN}[*] STEP 2: Choose Template{Style.RESET_ALL}")
        print(f"{Fore.WHITE}─────────────────────────────────────{Style.RESET_ALL}")
        template_list = list(EMAIL_TEMPLATES.keys())
        for i, tmpl in enumerate(template_list, 1):
            print(f"  {Fore.GREEN}[{i}]{Style.RESET_ALL} {tmpl.replace('_', ' ').title()}")
        
        tmpl_choice = input(f"  {Fore.CYAN}[?] Template: {Style.RESET_ALL}")
        
        selected_template = None
        custom_data = {}
        
        if tmpl_choice.lower() == 'c' or tmpl_choice == str(len(template_list)):
            selected_template = 'custom'
            custom_data['subject'] = input(f"  {Fore.CYAN}[?] Subject: {Style.RESET_ALL}")
            print(f"  {Fore.CYAN}[?] Body (type END on new line to finish):{Style.RESET_ALL}")
            lines = []
            while True:
                line = input()
                if line == "END":
                    break
                lines.append(line)
            custom_data['body'] = '\n'.join(lines)
            custom_data['button_text'] = input(f"  {Fore.CYAN}[?] Button text: {Style.RESET_ALL}")
        else:
            try:
                idx = int(tmpl_choice) - 1
                selected_template = template_list[idx]
            except:
                selected_template = template_list[0]
        
        # ========== STEP 3: Target Details ==========
        print(f"\n{Fore.CYAN}[*] STEP 3: Target Details{Style.RESET_ALL}")
        print(f"{Fore.WHITE}─────────────────────────────────────{Style.RESET_ALL}")
        
        # Get target(s)
        print(f"  {Fore.GREEN}[1]{Style.RESET_ALL} Single target")
        print(f"  {Fore.GREEN}[2]{Style.RESET_ALL} Multiple targets (CSV)")
        target_mode = input(f"  {Fore.CYAN}[?] Mode: {Style.RESET_ALL}")
        
        targets = []
        
        if target_mode == '1':
            email = input(f"  {Fore.CYAN}[?] Target email: {Style.RESET_ALL}")
            name = input(f"  {Fore.CYAN}[?] Target name: {Style.RESET_ALL}")
            targets.append({'email': email, 'name': name}
