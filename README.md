# Chat Assistant for SQLite Database
This project is an AI-powered chat assistant that translates natural language queries into SQLite SQL queries and retrieves results from a database. It leverages a pre-trained language model to generate SQL queries based on user input and executes them on an SQLite database.
### Features:
- Converts natural language queries into valid SQLite SQL queries.

- Retrieves relevant data from the SQLite database.

- Provides an interactive web interface for user input.

- Uses a fine-tuned Qwen model for SQL query generation.

### Project Structure:        

    
    ├── app     
    │   ├── main.py              
    │   ├── model.py            
    │   ├── query_handler.py   
    |   ├── save_model.py
    │   ├── templates/
    │   │   ├── index.html 
    |
    ├── database
    │   ├── company.db  
    |
    ├── model_data
    |
    ├── README.md          
## Installation & Setup:
1. Clone the repository:
  ```sh
  git clone https://github.com/vaibhavprajapati-22/Chat-Assistant-for-SQLite-Database
  cd Chat-Assistant-for-SQLite-Database
  ```
2. Go to app directory:
  ```sh
  cd app
  ```
3. Save the trained model:
```sh
python save_model.py
```
4. Run main script:
```sh
python main.py
```
![Screenshot 2025-02-09 002838](https://github.com/user-attachments/assets/423801ac-faa8-4d5b-8d64-88118476065d)

## Limitation:
- The model may sometimes generate incorrect or inefficient SQL queries.
- Currently supports only a predefined database schema.
- On Deploying the model on vercel, latency increases due to nonavailability of GPU.

## Suggestions for Improvement:
- Improve prompt engineering to ensure more accurate SQL generation.
- Try different open-source model that can generate more accurate sql queries.
- Better interface can be mode for model responses.

  

