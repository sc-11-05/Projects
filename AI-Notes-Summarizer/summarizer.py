from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# ------------------
# Summarize the text
# ------------------
def summarize_text(text, style="short"):

    # short or long text
    if style == "short":
        max_len = 50
        min_len = 15
    elif style == "detailed":
        max_len = 180
        min_len = 60
    else:
        max_len = 100
        min_len  = 30

    chunks = chunk_text(text)
    summaries = []
    
    for chunk in chunks:
        if style == "short":
            prompt = "Summarie briefly: " + chunk
        
        elif style == "detailed":
            prompt = "Summarize in detail with explanation: " + chunk
        
        else:
            prompt = "Summarize: " + chunk

        inputs = tokenizer(prompt, return_tensors="pt", max_length = 1024, truncation=True)

        summary_ids = model.generate(
            inputs["input_ids"],
            max_length = max_len,
            min_length = min_len,
            length_penalty = 1.0 if style == "detailed" else 2.0,
            num_beams = 8,
            no_repeat_ngram_size = 3,
            early_stopping = True
        )

        summary = tokenizer.decode(summary_ids[0], skip_special_token=True)

        summary = summary.replace("<s>","").replace("</s>","").strip()
        summaries.append(summary)

        full_summary = " ".join(summaries)

        # convert to bullet points
        sentences = full_summary.split(". ")
        bullets = "\n".join([f"- {s.strip()}" for s in sentences if s.strip()])
    return bullets

# ------------------------------
# Breaking long text into chunks
# ------------------------------
def chunk_text(text, max_chunk=500):
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_chunk):
        chunk = " ".join(words[i: i+max_chunk])
        chunks.append(chunk)

    return chunks

# ----------------
# User Interaction
# ----------------
# text = input("Enter your notes: \n")
# style = input("Choose your style (short/detailed): ").lower()

# result = summarize_text(text)

# print("Summary")
# print(result)
