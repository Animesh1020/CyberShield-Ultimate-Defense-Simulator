import os
import time
import random
import logging
import json
import sys
import hashlib
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict
from getpass import getpass
from colorama import init, Fore, Style
from datetime import datetime
import base64
import curses
import arcade

init(autoreset=True)

class UltimateCyberDefensePlatform:
    def __init__(self, data_file='cyber_defense_data.json', leaderboard_file='leaderboard.json'):
        self.data_file = data_file
        self.leaderboard_file = leaderboard_file
        self.users = self.load_users()
        self.leaderboard = self.load_leaderboard()
        self.current_user = None
        self.attack_vectors = [
            {"name": "Phishing Email", "complexity": 3, "points": 10},
            {"name": "Social Engineering", "complexity": 5, "points": 15},
            {"name": "Malware Injection", "complexity": 7, "points": 20},
            {"name": "Zero-Day Exploit", "complexity": 9, "points": 25}
        ]
        
        logging.basicConfig(
            filename='cyber_defense.log', 
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )

    def load_users(self):
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.users, f, indent=4)

    def hacker_terminal_animation(self, message):
        for _ in range(3):
            for color in [Fore.GREEN, Fore.RED, Fore.CYAN]:
                sys.stdout.write(f"\r{color}")
                for char in message:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.05)
                sys.stdout.write("\r" + " " * len(message))
        print(f"\n{Fore.GREEN}{message}{Style.RESET_ALL}")
    def load_leaderboard(self):
        try:
            with open(self.leaderboard_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def cyber_quiz(self):
        questions = [
            {"question": "What is the strongest password format?", "options": ["A: 123456", "B: Password123", "C: !@#GjhRT12$%"], "answer": "C"},
            {"question": "What is the safest way to browse the internet?", "options": ["A: Using VPN & HTTPS", "B: Clicking every link", "C: Downloading random files"], "answer": "A"}
        ]
        score = 0
        for q in questions:
            print(Fore.YELLOW + q["question"] + Style.RESET_ALL)
            for opt in q["options"]:
                print(opt)
            answer = input("Your answer (A, B, or C): ").upper()
            if answer == q["answer"]:
                print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
                score += 10
            else:
                print(Fore.RED + "Wrong answer!" + Style.RESET_ALL)
        print(f"Your final score: {score}")
        time.sleep(2)

    def network_packet_simulation(self):
        print(Fore.CYAN + "Simulating network packets..." + Style.RESET_ALL)
        for i in range(5):
            packet = f"Packet {i+1}: [Data Transfer Secure]"
            print(Fore.GREEN + packet + Style.RESET_ALL)
            time.sleep(1)
        print(Fore.YELLOW + "Network Security Verified!" + Style.RESET_ALL)
        time.sleep(2)

    def cyber_defense_game(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.GREEN}🎮 CYBER DEFENSE CHALLENGE{Style.RESET_ALL}")
            print("1. Detect Phishing Attempt")
            print("2. Block Social Engineering")
            print("3. Neutralize Malware")
            print("4. Cybersecurity Quiz")
            print("5. Network Packet Simulation")
            print("6. Exit Game")
            
            choice = input("Select your defense strategy: ")
            
            if choice == '6':
                break
            elif choice == '4':
                self.cyber_quiz()
            elif choice == '5':
                self.network_packet_simulation()
            else:
                attack = random.choice(self.attack_vectors)
                self.hacker_terminal_animation(f"INCOMING {attack['name']} THREAT!")
                user_response = input(f"{Fore.YELLOW}Defend against {attack['name']}? (yes/no): {Style.RESET_ALL}").lower()
                if user_response == 'yes':
                    print(f"{Fore.GREEN}✅ THREAT NEUTRALIZED!{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}❌ SYSTEM COMPROMISED!{Style.RESET_ALL}")
                time.sleep(2)

    def main_menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.GREEN}🛡️ CYBER DEFENSE CONTROL PANEL{Style.RESET_ALL}")
            print("1. Start Cyber Defense Game")
            print("2. Exit")
            choice = input("Select operation: ")
            if choice == '1':
                self.cyber_defense_game()
            elif choice == '2':
                break

    def run(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.GREEN}🖥️ CYBER DEFENSE TRAINING SYSTEM{Style.RESET_ALL}")
            print("1. Start Game")
            print("2. Exit")
            choice = input("Select operation: ")
            if choice == '1':
                self.main_menu()
            elif choice == '2':
                break

if __name__ == "__main__":
    simulator = UltimateCyberDefensePlatform()
    simulator.run()