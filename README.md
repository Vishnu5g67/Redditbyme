# Redditbyme
Python tool to scrape a Reddit user's posts and comments, then generate a user persona using ChatGPT. Built for the AI/LLM Intern assignment at BeyondChats. Outputs a structured text file ready for manual analysis. No OpenAI API needed.
# Reddit User Persona Generator

This project was created as part of the assignment for the AI/LLM Intern role at BeyondChats. The goal is to analyze a Reddit user's posts and comments, and generate a user persona based on their behavior, tone, and interests.

The solution involves scraping a Reddit user's content using the Reddit API, saving it to a text file, and optionally analyzing it to generate a detailed persona.

---

## Project Overview

- Accepts a Reddit profile URL as input
- Fetches recent posts and comments from that user
- Saves the content to a `.txt` file
- The user persona can be generated manually 

This version of the project avoids calling the OpenAI API directly, as the account quota was exceeded. Instead, persona generation is done manually.

---

## Files Included

- `main.py` – Python script to fetch Reddit data and save it
- `kojied_rawdata.txt` – Example scraped data from the user "kojied"
- `kojied_persona.txt` – Manually generated persona from that data
- `README.md` – Project documentation

---

## Technologies Used

- Python 3.10+
- PRAW (Python Reddit API Wrapper)

---

## How to Use

1. **Clone the repository**  
   Use Git or download the project as a ZIP.

2. **Install dependencies**

pip install praw

markdown
Copy
Edit

3. **Run the script**

python main.py

less
Copy
Edit

When prompted, paste a Reddit profile URL such as:

https://www.reddit.com/user/kojied/

yaml
Copy
Edit

4. **Output**

The script will save a file named `{username}_rawdata.txt` (e.g., `kojied_rawdata.txt`) containing the user's recent posts and comments.

---

## How to Generate a Persona (Manual Approach)

If you're not using the OpenAI API (due to quota limits), you can generate the persona manually like this:

1. Go to [https://chat.openai.com](https://chat.openai.com)
2. Paste the following instruction:

Generate a detailed user persona based on the following Reddit posts and comments.
Include personality traits, interests, subreddit activity, writing style, and tone.
Cite specific posts or comments to support each point.

yaml
Copy
Edit

3. Then paste the contents of the `.txt` file you generated from the script.

4. Copy the ChatGPT response and save it as `{username}_persona.txt`.

---

## Notes

- The script uses only public Reddit data and respects privacy boundaries.
- It is designed to work with active Reddit users who have visible post and comment history.

---

## Author

Vishnu Vardhan  
GitHub: [https://github.com/Vishnu5g67]  
LinkedIn: [https://www.linkedin.com/in/vishnu-vardhan-raipally-88125125a/]

---

## Purpose

This repository is part of the 48-hour take-home assignment for the AI/LLM Intern position at BeyondChats. All work is original and created specifically for this assessment.
Final Steps
