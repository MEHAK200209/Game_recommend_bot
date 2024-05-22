from transformers import GPTNeoForCausalLM, GPT2Tokenizer

# Download and save the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")

# Save the tokenizer and model to the local directory
model.save_pretrained("./gpt-neo-125M")
tokenizer.save_pretrained("./gpt-neo-125M")
