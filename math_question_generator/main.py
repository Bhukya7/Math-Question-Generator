from question_templates import MultipleChoiceQuestion, init_document_styles
from docx import Document
from image_generator import create_package_image
import os

def generate_questions():
    """Generate all questions and compile into a Word document"""
    # Create outputs directory if it doesn't exist
    os.makedirs("outputs/images", exist_ok=True)
    
    doc = Document()
    init_document_styles(doc)
    
    # Question 1 - Combinatorics
    q1 = MultipleChoiceQuestion(
        title="School Uniform Combinations",
        description="Calculate possible uniform combinations based on color choices",
        question="""Each student at East High School wears a uniform consisting of 1 shirt, 1 pair of pants, and 1 tie. The table shows the colors available for each item of clothing. How many different complete uniforms are possible?

## Uniform Choices

| Shirt Color | Pants Color | Tie Color |
|-------------|-------------|-----------|
| White       | Black       | Red       |
| Blue        | Navy        | Blue      |
| Gray        | Khaki       | Green     |
| Yellow      |             | Yellow    |""",
        instruction="Calculate all possible combinations considering available colors",
        difficulty="moderate",
        order=1,
        options=["6", "9", "12", "15", "18"],
        correct_index=2,
        explanation="There are 3 shirt options (White, Blue, Gray), 2 pants options (Black, Navy), and 2 tie options (Red, Blue). Total combinations are 3 × 2 × 2 = 12. Yellow shirt has no matching pants, so it cannot form a complete uniform.",
        subject="Quantitative Math",
        unit="Problem Solving",
        topic="Counting Principles"
    )
    
    # Question 2 - Geometry with Image
    image_path = os.path.abspath("outputs/images/package.png")
    create_package_image(image_path)
    
    q2 = MultipleChoiceQuestion(
        title="Packed Spheres Dimensions",
        description="Calculate dimensions of a rectangular package containing spheres",
        question=f"""The top view of a rectangular package of 8 tightly packed balls is shown. If each ball has a radius of 3 centimeters, which of the following are closest to the dimensions, in centimeters, of the rectangular package?
[IMAGE: {image_path}]""",
        instruction="Calculate based on sphere diameter and packing arrangement",
        difficulty="hard",
        order=2,
        options=["6 × 12 × 6", "6 × 24 × 6", "6 × 24 × 12", "12 × 24 × 12", "12 × 24 × 24"],
        correct_index=2,
        explanation="Each ball has diameter 6 cm (2 × radius). The package width would be 4 × 6 cm = 24 cm, height 2 × 6 cm = 12 cm, and depth equal to diameter = 6 cm.",
        subject="Quantitative Math",
        unit="Geometry and Measurement",
        topic="Volume"
    )
    
    # Add questions to document
    for question in [q1, q2]:
        question.add_to_document(doc)
    
    # Save the document with error handling
    output_path = os.path.abspath("outputs/questions.docx")
    try:
        if os.path.exists(output_path):
            os.remove(output_path)
        doc.save(output_path)
        print(f"Successfully generated document at: {output_path}")
    except PermissionError:
        print("Error: Could not save document. Please close the file if it's open and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    generate_questions()