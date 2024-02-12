import tkinter as tk
 
  ### using try and except function




 
    
def calculate():   
 
     
            
            
            
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
 

 






def append_char(char):
    entry.insert(tk.END, char)
 






def clear_entry():
    clear_entry==0
    entry.delete(0, tk.END)
    
    
def  backspace_entry():
    backspace_entry==0
    entry.backspace(0,tk.END)
    

 



root = tk.Tk()
root.title("Calculator")

 
    
    
    
    
    
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

 
    
    
    
    
    
    
button_labels = [
    ('C', '%', 'D', '()'),
    ('1', '2', '3', '+' ),
    ('4', '5', '6', '-'),
    ('7', '8', '9', '*'),
    ('.', '0', '=', '/')
   # ('%','clear_entry','!')
]

 
   
    
    
    
for i in range(len(button_labels)):
    for j in range(len(button_labels[i])):
        label = button_labels[i][j]
        
        
        if label == '=':
            btn = tk.Button(root, text=label, padx=40, pady=20, command=calculate)
            
            
            
            
            
        elif label == 'D':
            btn = tk.Button(root, text=label, padx=40, pady=20, command= backspace_entry)
            
            
            
            
        elif label == 'C':
            btn = tk.Button(root, text=label, padx=40, pady=20, command=clear_entry)
            
            
        ## using lambda function
        
        
        else:
            btn = tk.Button(root, text=label, padx=40, pady=20, command=lambda char=label: append_char(char))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

        
        
root.mainloop()