from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")

print("Model loaded succesfully!")
save_directory = "../model_data"

tokenizer.save_pretrained(save_directory)
model.save_pretrained(save_directory)

print("Model and tokenizer saved successfully!")      