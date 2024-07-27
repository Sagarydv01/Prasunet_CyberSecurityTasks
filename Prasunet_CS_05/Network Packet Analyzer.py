"""
TASK-05: NETWORK PACKET ANALYZER

Develop a packet sniffer tool that and analyzes network captures packets. 
Display relevant information such as source and destination IP addresses, 
protocols, and payload data. 
Ensure the ethical use of the tool for educational purposes.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
from scapy.all import sniff, IP, TCP, UDP
import threading

def packet_callback(packet):
    try:
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst

            if TCP in packet:
                protocol = "TCP"
            elif UDP in packet:
                protocol = "UDP"
            else:
                protocol = "Other"

            payload = packet[IP].payload

            packet_info = f"Source IP: {src_ip}\nDestination IP: {dst_ip}\nProtocol: {protocol}\nPayload: {payload}\n\n"
            text_area.insert(tk.END, packet_info)
            text_area.yview(tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while processing the packet: {e}")

def start_sniffing(interface):
    try:
        sniff(iface=interface, prn=packet_callback, store=False)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during packet sniffing: {e}")

def start_button_click():
    interface = interface_entry.get()
    if not interface:
        messagebox.showwarning("Warning", "Please enter a network interface.")
        return
    try:
        threading.Thread(target=start_sniffing, args=(interface,), daemon=True).start()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while starting the sniffing process: {e}")

def clear_button_click():
    try:
        text_area.delete(1.0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while clearing the text area: {e}")

root = tk.Tk()
root.title("Network Packet Analyzer")

interface_label = tk.Label(root, text="Network Interface:")
interface_label.pack(pady=5)
interface_entry = tk.Entry(root)
interface_entry.pack(pady=5)

start_button = tk.Button(root, text="Start Sniffing", command=start_button_click)
start_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_button_click)
clear_button.pack(pady=5)

text_area = scrolledtext.ScrolledText(root, width=60, height=20)
text_area.pack(pady=10)

root.mainloop()

# Task Completed!
# Sagar Yadav