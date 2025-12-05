### Canva → Bulk Cover Page Export → Rename PDFs → Upload → Students Download Individually.

Perfect for universities, colleges, and departments distributing hundreds of lab-report cover pages every semester.

---

# 📘 Lab Report Cover Page Distribution Panel

A lightweight, browser-based system for distributing **personalized lab report cover pages** to students—automatically, accurately, and without manual messaging.

Built with **HTML, CSS, & JavaScript (no backend needed)**.

---

## 🎯 Purpose

Teachers often need to distribute **unique lab report cover pages** containing:

* Student name
* Registration number
* Session
* Course code
* Section
* Department logo
* Submission info

When there are **100–500+ students**, manually sending each PDF becomes slow and error-prone.

This tool automates the entire process.

---

# 🛠️ Workflow Overview

### **1️⃣ Bulk generate personalized lab cover pages in Canva**

### **2️⃣ Export all PDFs**

### **3️⃣ Rename PDFs by registration number**

### **4️⃣ Upload PDFs + CSV to this panel**

### **5️⃣ Students search and download their own cover page**

This system becomes your **distribution portal**.

---

# 🧾 Step 1 — Create Lab Cover Pages in Canva

You create one master design in Canva with placeholders like:

* {{Name}}
* {{RegNo}}
* {{Session}}
* {{Course}}
* {{Department}}

### Then use Canva’s **Bulk Create**:

1. Go to **Apps → Bulk Create**
2. Upload your student data CSV
3. Link each placeholder → CSV fields
4. Generate the full batch of personalized cover pages
5. Download them all together as **PDF** (standard or print)

---

# 🏷️ Step 2 — Prepare File Names

Canva often exports PDFs like:

```
1_19502004263.pdf  
2_19502004264.pdf  
3_19502004265.pdf
```

Use this rename rule:

```
OLD: 1_19502004263.pdf  
NEW: 19502004263.pdf
```

You can use the Python renamer script:

```python
import os

folder_path = r"C:\Path\To\PDFs"

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        parts = filename.split("_", 1)
        if len(parts) == 2:
            new_name = parts[1]
            os.rename(os.path.join(folder_path, filename),
                      os.path.join(folder_path, new_name))
```

---

# 📂 Step 3 — Place PDFs into `/pdfs` Folder

Your project directory must look like:

```
project/
│
├── index.html
├── students.csv
├── popup.png
│
└── pdfs/
      ├── 19502004263.pdf
      ├── 19502004264.pdf
      ├── 19502004265.pdf
      └── ...
```

**Each PDF name must EXACTLY match the student's regNo**.

---

# 🗃️ Step 4 — Prepare `students.csv`

`students.csv` tells the system which student belongs to which PDF.

Example:

```csv
name,regNo,session
Imran Hossain,19502004263,2019-20
Md. Shahadat Hossain,19502004264,2019-20
Imran Newaz Emu,19502004265,2019-20
Razib,19502004266,2019-20
Shuli Akter,19502004267,2019-20
```

> You can export this list directly from your university database or Excel file.

---

# 🌐 Step 5 — Host & Use the Panel

### You must use a local or online server

Because browsers block CSV loading using `file://`

Use any of these:

* VS Code → Live Server
* `python -m http.server`
* Netlify / GitHub Pages / Cloudflare Pages

When students open the portal:

### They can:

* Type their **Name** or **Registration Number**
* See auto-suggestions (Google-style)
* Download their own **lab report cover page PDF**
* See a popup “message/notice” image on download
* Use it on mobile easily

---

# 📱 Mobile-First Design

The UI is optimized for mobile because most students will use phones.

Includes:

* Flexible search input
* Auto-suggestion list
* Scrollable table
* Touch-friendly download buttons
* Popup compatible on small screens

---

# 🎉 Advantages for Teachers & Lab Instructors

### 🚀 Saves Hours of Manual Work

No more sending PDFs individually through:

* Messenger
* WhatsApp
* Email
* Google Classroom
* Drive sharing

### 🔎 Prevents Mistakes

Students download **their exact file**, matched by reg number.

### 📥 Fast Distribution

Upload once → thousands of students download instantly.

### 🔐 Private & Offline-Friendly

Runs without backend or database.
No data leaves the department.

### 🧪 Perfect for:

* Lab report cover pages
* Assignment cover pages
* Viva cards
* Admit cards
* Practical exam cover sheets
* Internship or project folders

---

# 🔧 Future Add-Ons (Optional)

If you want, your system can be expanded to include:

* QR Code for quick verification
* Student activity logs (who downloaded their cover page)
* Multi-course filtering
* Department branding theme
* Auto-emailing PDFs
* Dark mode
* Admin interface for managing CSV uploads

---