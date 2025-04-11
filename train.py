

from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

def load_dataset(file_path, tokenizer):
    return TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=128,
    )

def main():
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    train_dataset = load_dataset("reddit_stories.txt", tokenizer)
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir="./model",
        overwrite_output_dir=True,
        num_train_epochs=5,
        per_device_train_batch_size=2,
        save_steps=500,
        save_total_limit=1,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        data_collator=data_collator,
    )

    trainer.train()
    trainer.save_model("./model")
    tokenizer.save_pretrained("./model")

if __name__ == "__main__":
    main()
