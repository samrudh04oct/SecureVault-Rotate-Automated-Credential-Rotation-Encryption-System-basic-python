import customtkinter as ctk
import threading
import sys
import time
import io
import schedule
from vault import rotate_password

# Appearance Settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class RedirectText(io.StringIO):
    def __init__(self, textbox):
        super().__init__()
        self.textbox = textbox

    def write(self, string):
        self.textbox.configure(state="normal")
        self.textbox.insert("end", string)
        self.textbox.configure(state="disabled")
        self.textbox.see("end")
    
    def flush(self):
        pass

class VaultApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Secure Vault Manager")
        self.geometry("600x450")
        self.resizable(False, False)

        # Title Label
        self.label_title = ctk.CTkLabel(self, text="Vault Auto-Rotation Service", font=("Roboto", 24, "bold"))
        self.label_title.pack(pady=20)

        # Status Frame
        self.status_frame = ctk.CTkFrame(self)
        self.status_frame.pack(pady=10, padx=20, fill="x")
        
        self.label_status = ctk.CTkLabel(self.status_frame, text="Status: STOPPED", font=("Roboto", 16), text_color="red")
        self.label_status.pack(pady=10)

        # Buttons Frame
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.btn_start = ctk.CTkButton(self.button_frame, text="Start Service", command=self.start_service, fg_color="green", hover_color="darkgreen")
        self.btn_start.grid(row=0, column=0, padx=10)

        self.btn_stop = ctk.CTkButton(self.button_frame, text="Stop Service", command=self.stop_service, fg_color="red", hover_color="darkred", state="disabled")
        self.btn_stop.grid(row=0, column=1, padx=10)

        self.btn_rotate = ctk.CTkButton(self.button_frame, text="Rotate Now", command=self.rotate_now, fg_color="orange", hover_color="darkorange")
        self.btn_rotate.grid(row=0, column=2, padx=10)

        # Log Window
        self.log_label = ctk.CTkLabel(self, text="Activity Log:", anchor="w")
        self.log_label.pack(pady=(10, 0), padx=20, fill="x")

        self.log_textbox = ctk.CTkTextbox(self, height=150)
        self.log_textbox.pack(pady=5, padx=20, fill="x")
        self.log_textbox.configure(state="disabled")

        # Redirect stdout
        sys.stdout = RedirectText(self.log_textbox)

        # Service Variables
        self.running = False
        self.thread = None

    def start_service(self):
        if not self.running:
            self.running = True
            self.label_status.configure(text="Status: RUNNING", text_color="#00FF00")
            self.btn_start.configure(state="disabled")
            self.btn_stop.configure(state="normal")
            
            self.thread = threading.Thread(target=self.run_scheduler, daemon=True)
            self.thread.start()
            print("[INFO] Service started.")

    def stop_service(self):
        if self.running:
            self.running = False
            self.label_status.configure(text="Status: STOPPED", text_color="red")
            self.btn_start.configure(state="normal")
            self.btn_stop.configure(state="disabled")
            print("[INFO] Service stopped.")

    def run_scheduler(self):
        schedule.every(4).hours.do(self.safe_rotate)
        while self.running:
            schedule.run_pending()
            time.sleep(1)

    def safe_rotate(self):
        try:
            print("[INFO] Rotating password via Schedule...")
            rotate_password()
        except Exception as e:
            print(f"[ERROR] Logic failed: {e}")

    def rotate_now(self):
        print("[INFO] Manual rotation triggered...")
        threading.Thread(target=self.safe_rotate_manual, daemon=True).start()

    def safe_rotate_manual(self):
        try:
            rotate_password()
            print("[SUCCESS] Manual rotation complete.")
        except Exception as e:
            print(f"[ERROR] Manual rotation failed: {e}")

if __name__ == "__main__":
    app = VaultApp()
    app.mainloop()