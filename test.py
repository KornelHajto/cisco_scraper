import json
import re

from bs4 import BeautifulSoup


def scrape_exam_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []

    soup = BeautifulSoup(html_content, "html.parser")

    questions_data = []

    # In the provided HTML, questions seem to be enclosed in <p> tags
    # usually starting with a <strong> tag containing a number (e.g., "1. ", "25. ")
    all_paragraphs = soup.find_all("p")

    for p in all_paragraphs:
        # Get clean text
        text = p.get_text(" ", strip=True)

        # Regex to check if paragraph starts with a number followed by a dot (e.g., "1.")
        # This identifies the start of a question block
        if re.match(r"^\d+\.", text):
            q_obj = {
                "question_number": text.split(".")[0],
                "question_text": text,
                "options": [],
                "correct_answers": [],
                "type": "multiple_choice",  # default
                "explanation": "N/A",
            }

            # Iterate through siblings to find answers and explanations
            # until we hit the next question or run out of siblings
            curr_element = p.next_sibling

            while curr_element:
                # Skip NavigableStrings (whitespace/newlines)
                if hasattr(curr_element, "name") and curr_element.name is not None:
                    # STOP condition: If we hit another <p> that looks like a question
                    if curr_element.name == "p":
                        next_text = curr_element.get_text(strip=True)
                        if re.match(r"^\d+\.", next_text):
                            break

                    # CASE 1: Standard Multiple Choice (<ul>)
                    if curr_element.name == "ul":
                        list_items = curr_element.find_all("li")
                        for li in list_items:
                            option_text = li.get_text(strip=True)
                            q_obj["options"].append(option_text)

                            # Check for the specific class used in your HTML
                            if "correct_answer" in li.get("class", []):
                                q_obj["correct_answers"].append(option_text)

                    # CASE 2: Matching Questions (<table>)
                    elif curr_element.name == "table":
                        q_obj["type"] = "matching"
                        rows = curr_element.find_all("tr")
                        for row in rows:
                            cols = row.find_all("td")
                            # Join columns with a separator
                            row_text = " : ".join(
                                [c.get_text(strip=True) for c in cols]
                            )
                            if row_text:
                                q_obj["options"].append(row_text)
                                # In these dumps, the table usually represents the correct matched state
                                q_obj["correct_answers"].append(row_text)

                    # CASE 3: Explanations (div class="message_box success")
                    elif curr_element.name == "div":
                        classes = curr_element.get("class", [])
                        if "message_box" in classes and "success" in classes:
                            # Remove the "Explanation:" prefix if strictly necessary, usually raw text is fine
                            q_obj["explanation"] = curr_element.get_text(
                                " ", strip=True
                            )

                curr_element = curr_element.next_sibling

            # Only add if we actually found a question structure
            questions_data.append(q_obj)

    return questions_data


# --- Execution ---
if __name__ == "__main__":
    # Ensure you have your html file named 'exam.html' in the same directory
    # Or change the path below
    input_file = "exam.html"

    results = scrape_exam_data(input_file)

    if results:
        print(f"Successfully extracted {len(results)} questions.\n")

        # Print preview of first 3 extracted questions
        for i, q in enumerate(results[:3]):
            print(f"--- Question {q['question_number']} ---")
            print(f"Text: {q['question_text']}")
            print(f"Type: {q['type']}")
            print(f"Correct Answer(s): {q['correct_answers']}")
            print(f"Explanation: {q['explanation'][:100]}...")  # Truncated for display
            print("")

        # Optional: Save to JSON file
        with open("extracted_questions.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
            print("Full data saved to 'extracted_questions.json'")
    else:
        print("No questions found. Check the filename or HTML structure.")
