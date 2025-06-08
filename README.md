# Security Leak Scanner

A Python-based tool to scan Git repositories for secret leaks using **TruffleHog** and **Gitleaks**. Supports both local repositories and remote GitHub URLs, providing a clear summary of detected leaks.

---

## **Features**

- **Dual Scanner Support:** Runs both TruffleHog and Gitleaks for comprehensive scanning.
- **Flexible Input:** Accepts either a local repository path or a GitHub URL.
- **Clear Summaries:** Outputs leak type, file, commit, author, date, and reason.
- **Demo Repository:** Includes a sample repo with fake secrets for testing.
- **Sample Outputs & Screenshots:** See real scan results and summaries.
- **Documentation:** Step-by-step instructions for installation and usage.

---

## **Usage**

Run the script with a local path or GitHub URL:

```bash
python3 simleaks.py demo-repo/
# or
python3 simleaks.py https://github.com/username/repo.git
```

After scanning, the script prints a summary table with all findings.

---

## **Project Structure**

```
security-leak-scanner/
├── simleaks.py         # Main Python scanner script
├── demo-repo/          # Example repo with intentional fake secrets
├── screenshots/        # Images of scan outputs and summaries
└── README.md           # Project overview and instructions
```

---

## **Screenshots**

- **Tool Execution:** Demonstrates the script running on sample data.
- ![image](https://github.com/user-attachments/assets/7eb6dbc4-0cf6-415f-907b-57a896ff1769)

- **Scan Results:** Shows findings from both TruffleHog and Gitleaks.
- ![image](https://github.com/user-attachments/assets/1ac9df24-2c93-4f0b-8c0d-9ef972f81a71)
![image](https://github.com/user-attachments/assets/a59ab14b-2aa2-4d43-be14-fd16609db0b7)

- **Summary Output:** Final leak summary as printed by the script.
![image](https://github.com/user-attachments/assets/825c20ab-0a31-40b1-a606-0e1d8f915842)
![image](https://github.com/user-attachments/assets/581e9cd6-5b26-499c-8e06-d4bfdf97e213)

---

## **Future Scope**

- Interactive selection of URL or local path
- Option to choose scanning tool(s): TruffleHog, Gitleaks, or both
- Generate HTML/Markdown summary reports for sharing
- Dockerize for simplified deployment
- Email notifications or alert systems for detected leaks

---

## **Disclaimer**

> This tool is for educational purposes only.  
> **Do not scan any repositories without explicit permission from the owner.**

---

## **Blog**

A detailed blog post covering project details, setup, and key learnings will be published soon.
https://github.com/damnkrishna/CyberGaurd-j/blob/61bff2e1ad83dafba2b96f7655f858331a98b777/project-blog/Repo-Leak-scanner.md
