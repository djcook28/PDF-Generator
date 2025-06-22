# 📝 PDF Notebook Generator

This Python script dynamically generates a multi-page PDF notebook based on topic data stored in a CSV file. Each topic is rendered with a header, lined pages for writing, and custom footers indicating the topic name and page number — all formatted using the FPDF library.

---

## 🚀 Features

- Creates structured note pages from a CSV file
- Auto-generates lined pages like a ruled notebook
- Adds topic headers and footers to each page
- Fully customizable via the `topics.csv` file

---

## 🛠 Technologies Used

- `Python`
- `FPDF` (for PDF generation)
- `pandas` (for reading CSV data)

---

## 📄 Example CSV Format

Ensure you have a `topics.csv` file in the same directory with the following columns:

```csv
Topic,Pages
Mathematics,3
History,2
Biology,4
```

## 📚 Real-World Applications- Custom printable notebooks for students or educators
- Conference/workshop handouts
- Journaling or guided workbook design
- Automated generation of documentation or forms

