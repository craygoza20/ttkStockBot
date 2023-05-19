import tkinter as tk
import ttkbootstrap as ttk

class GUI(tk.Tk):
    # Create default label font
    

    def __init__(self):
        super().__init__()
        self.title("Trading App")
        self.geometry("800x600")  # Set minimum window size
        self.maxsize(800, 600)  # Set maximum window size
        self.style = ttk.Style("superhero")
        self.label_font = ("Helvetica", 18)
        self.output_shown = tk.StringVar(self,"Welcome!")
        self.login_screen()
        
    def login_screen(self):
        self.clear_screen()
        
        # Create login frame
        login_frame = ttk.Frame(self)
        login_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create login widgets
        title_label = ttk.Label(login_frame, text="ALPACA BOT", font=("Helvetica", 48))
        title_label.pack(pady=(80,10))
        username_label = ttk.Label(login_frame, text="Username:", font=self.label_font)
        username_label.pack(pady=(30,10))
        username_entry = ttk.Entry(login_frame, width=30)
        username_entry.pack(pady=10)
        
        password_label = ttk.Label(login_frame, text="Password:", font=self.label_font)
        password_label.pack(pady=10)
        password_entry = ttk.Entry(login_frame, show="*", width=30)
        password_entry.pack(pady=10)
        
        login_button = ttk.Button(login_frame, text="Login", command=self.show_landing_menu, width=15)
        login_button.pack(pady=10)
        
    def show_landing_menu(self):
        self.clear_screen()
        
        # Create landing menu frames
        landing_button_frame = ttk.Frame(self, borderwidth=5, relief='raised')
        landing_output_frame = ttk.Frame(self, borderwidth=5, relief='sunken')

        landing_button_frame.grid(column=0, row=0, padx=10, pady=100)
        landing_output_frame.grid(column=1, row=0)

        # Create landing menu button widgets
        paper_trading_button = ttk.Button(landing_button_frame, text="Paper Trading", command=self.show_paper_trading, width=25, padding=20)
        paper_trading_button.pack(pady=10,fill=tk.Y)
        
        live_trading_button = ttk.Button(landing_button_frame, text="Live Trading", command=self.show_live_trading, width=25, padding=20)
        live_trading_button.pack(pady=10, fill=tk.Y)
        
        view_portfolio_button = ttk.Button(landing_button_frame, text="View Portfolio", command=self.show_view_portfolio, width=25, padding=20)
        view_portfolio_button.pack(pady=10, fill=tk.Y)
        
        search_stock_quote_button = ttk.Button(landing_button_frame, text="Search Stock Quote", command=self.show_search_stock_quote, width=25, padding=20)
        search_stock_quote_button.pack(pady=10, fill=tk.Y)
        
        view_bot_performance_button = ttk.Button(landing_button_frame, text="View Bot Performance", command=self.show_view_bot_performance, width=25, padding=20)
        view_bot_performance_button.pack(pady=10, fill=tk.Y)
        

        # Create landing menu output variable
        landing_output_label = ttk.Label(landing_output_frame, textvariable=self.output_shown, font=self.label_font)
        landing_output_label.pack()


    def show_paper_trading(self):
        self.output_shown.set("Paper trading")
        # Add functionality for the Paper Trading screen
    
    def show_live_trading(self):
        self.output_shown.set("Live trading")
        # Add functionality for the Live Trading screen
    
    def show_view_portfolio(self):
        self.output_shown.set("View portfolio")
        # Add functionality for the View Portfolio screen
    
    def show_search_stock_quote(self):
        self.output_shown.set("Search stock quote")
        # Add functionality for the Search Stock Quote screen
    
    def show_view_bot_performance(self):
        self.output_shown.set("Bot performance")
        # Add functionality for the View Bot Performance screen
    
    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
