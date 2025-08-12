# 📘 Math Question Generator

🧮 A Python project that generates **math assessment questions** in Microsoft Word (`.docx`) format.  
🛠️ Supports **tables, images, LaTeX-style math**, and structured metadata.  
🎯 Ideal for creating exam papers, practice tests, or e-learning content.

---

## ✨ Features
- 📄 **Automatic Word Document Creation** (`.docx`)
- 🗂️ **Supports clean, grid-style tables**
- 📐 **Adds diagrams/images** for geometry questions
- 🔘 **Multiple Choice Questions (MCQ) formatting**
- 🏷️ **Includes subject, unit, topic, difficulty, and marks**
- 🚀 Easy to extend with new questions
- 🛡️ Robust **error + permission handling**
- ✨ Professional formatting with headings, captions, and alignment

---

## 🏗️ Architecture Diagram

```mermaid
flowchart TD
    A["📦 Math Question Generator"] --> B["🛠️ Core Components"]
    A --> C["📂 Outputs"]
    
    B --> B1["🐍 main.py"]
    B --> B2["📋 question_templates.py"]
    B --> B3["🎨 image_generator.py"]
    B --> B4["📦 requirements.txt"]
    
    C --> C1["📝 questions.docx"]
    C --> C2["🖼️ images/"]
    C2 --> C2a["📐 geometry_diagram.png"]
    C2 --> C2b["📈 plot_graph.png"]
    
    B1 -->|🔗 uses| B2
    B1 -->|🔗 uses| B3
    B2 -->|🔄 generates| C1
    B3 -->|🔄 generates| C2
    
    style A fill:#FF9E64,stroke:#333,color:#000,stroke-width:2px
    style B fill:#6ECCAF,stroke:#333,color:#000,stroke-width:2px
    style C fill:#5D9CEC,stroke:#333,color:#FFF,stroke-width:2px
    
    style B1 fill:#FF5F7E,stroke:#333,color:#FFF
    style B2 fill:#FF5F7E,stroke:#333,color:#FFF
    style B3 fill:#FF5F7E,stroke:#333,color:#FFF
    style B4 fill:#3A4F7A,stroke:#333,color:#FFF
    
    style C1 fill:#3A4F7A,stroke:#333,color:#FFF
    style C2 fill:#5D9CEC,stroke:#333,color:#FFF
    
    linkStyle default stroke:#7F7F7F,stroke-width:2px

```
## 📤 Output

- **`outputs/questions.docx`** → Final questions document
- **`outputs/images/diagram.png`** → Diagram for geometry question

---

## 🧩 Example Generated Content

### ❓ Question 1 — Combinatorics
**👕 Shirt/👖 Pants/👔 Tie color combination table (MCQ format)**

| 👕 Shirt Color | 👖 Pants Color | 👔 Tie Color |
|---------------|---------------|-------------|
| White         | Black         | Red         |
| Blue          | Navy          | Blue        |
| Gray          | Khaki         | Green       |
| Yellow        | -             | Yellow      |

### ❓ Question 2 — Algebra
**Solve for x:**  
`x² + 5x + 6 = 0`  
**🔍 Solution:** `x = -2` or `x = -3`

### ❓ Question 3 — Geometry
**📐 Calculate the area of the triangle:**  
- 🔼 Base = 5 units  
- 📏 Height = 7 units  
- 🧮 **Area** = ½ × base × height = `17.5 units²`
