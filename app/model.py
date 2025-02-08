import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
save_directory = "../model_data"

tokenizer = AutoTokenizer.from_pretrained(save_directory)
model = AutoModelForCausalLM.from_pretrained(save_directory)

print("Model and tokenizer loaded successfully!")

def generate_sql_query(user_query):

    prompt = f"""You are an AI that converts natural language into **only** valid SQLite SQL queries. 

    Database Schema:
    1. Employees (ID, Name, Department, Salary, Hire_Date)
    2. Departments (ID, Name, Manager)

    **User Query:** {user_query}

    **SQL Query:**"""

    
    #print(prompt)
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs)
    sql_query = tokenizer.decode(output[0], skip_special_tokens=True).strip()
    if "SQL Query:" in sql_query:
        sql_query = sql_query.split("**SQL Query:**")[-1].strip()
    #print(sql_query)
    
    return sql_query
