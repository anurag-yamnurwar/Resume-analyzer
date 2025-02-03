import PyPDF2
import os
import re

# Keywords for different job roles
job_keywords = {
    'AI & ML Engineer': [
        'artificial intelligence', 'machine learning', 'deep learning',
        'nlp', 'opencv', 'computer vision', 'tensorflow', 'mediapipe', 'matplotlib',
        'pytorch', 'keras', 'reinforcement learning', 'data mining',
        'neural networks', 'predictive modeling', 'feature engineering',
        'big data', 'algorithm', 'data preprocessing', 'model deployment'
    ],
    'Data Scientist': [
        'python', 'machine learning', 'pandas', 'numpy',
        'tensorflow', 'keras', 'scikit-learn', 'data analysis', 'matplotlib',
        'statistics', 'data visualization', 'R', 'big data',
        'data wrangling', 'data cleaning', 'data storytelling', 'hypothesis testing',
        'machine learning algorithms', 'feature selection'
    ],
    'Web Developer': [
        'html', 'css', 'javascript', 'angular', 'react',
        'node', 'bootstrap', 'jquery', 'responsive design',
        'restful APIs', 'frontend', 'backend', 'version control',
        'git', 'web performance', 'vue.js', 'web accessibility',
        'progressive web apps', 'cross-browser compatibility'
    ],
    'Full Stack Developer': [
        'html', 'css', 'javascript', 'node', 'express',
        'mongodb', 'react', 'angular', 'mysql', 'php', 'django',
        'restful APIs', 'version control', 'git', 'cloud services',
        'microservices', 'API design', 'authentication', 'containerization'
    ],
    'MERN Stack Developer': [
        'mern', 'mongodb', 'express', 'react', 'node.js',
        'javascript', 'restful APIs', 'redux', 'hooks', 'backend',
        'frontend', 'responsive design', 'authentication', 'state management',
        'single page applications', 'web sockets'
    ],
    'Java Developer': [
        'java', 'spring', 'hibernate', 'j2ee', 'servlet',
        'maven', 'restful APIs', 'microservices', 'git',
        'design patterns', 'unit testing', 'debugging', 'oracle',
        'jdbc', 'spring boot', 'security', 'api development'
    ],
    'Mobile Developer': [
        'android', 'kotlin', 'swift', 'flutter',
        'react native', 'ios development', 'ruby', 'mobile UI/UX',
        'cross-platform development', 'API integration', 'mobile performance',
        'app lifecycle', 'google play', 'app store', 'responsive UI'
    ],
    'Database Administrator': [
        'sql', 'mysql', 'oracle', 'sql server', 'mongodb',
        'database management', 'query optimization', 'nosql',
        'postgresql', 'data modeling', 'backup recovery',
        'performance tuning', 'security management', 'data integrity',
        'data warehousing', 'ETL processes'
    ],
    'Cyber Security': [
        'malware analysis', 'penetration testing',
        'vulnerability scanning', 'firewall', 'encryption',
        'ids', 'ips', 'siem', 'risk assessment',
        'security policies', 'incident response', 'network security',
        'threat modeling', 'security audits', 'incident management'
    ],

}

def text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    if not os.path.exists(pdf_path):
        return ""

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        return ''.join(page.extract_text() or '' for page in reader.pages).lower()

def analyze_resume(text):
    """Analyze resume and return matches for all job roles."""
    matches = {}
    for role, keywords in job_keywords.items():
        match_count = sum(
            1 for keyword in keywords if re.search(r'\b' + re.escape(keyword) + r'\b', text, re.IGNORECASE))
        if match_count > 0:
            matches[role] = match_count
    return matches

def suggest_best_role(matches):
    """Suggest the best job role based on keyword matches."""
    if not matches:
        return "Unknown Role", 0

    best_role = max(matches, key=matches.get)
    return best_role, matches[best_role]

def list_resumes(resumes):
    """Display a formatted list of resumes with indexing."""
    print("\n--- Available Resumes ---")
    for index, resume in enumerate(resumes):
        print(f"{index + 1}. {resume}")
    print()

def display_matched_keywords(matches):
    """Display matched keywords in a tabular format."""
    print("\n--- Matched Keywords ---")
    print(f"{'Job Role':<30} {'Matches':<10}")
    print("-" * 40)
    for role, count in matches.items():
        print(f"{role:<30} {count:<10}")
    print("-" * 40)

def main(folder_path):
    """Main execution."""
    if not os.path.exists(folder_path):
        print("Error: The specified folder does not exist.")
        return

    # List resumes in the folder
    resumes = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    print(f"Total resumes found: {len(resumes)}")

    if not resumes:
        print("No resumes to process.")
        return

    list_resumes(resumes)

    while True:
        try:
            user_input = input("Enter the name or index of the student (or type 'exit' to quit): ").strip()
            if user_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            if user_input.isdigit():
                index = int(user_input) - 1
                if 0 <= index < len(resumes):
                    selected_resume = resumes[index]
                else:
                    print("Error: Invalid index selected.")
                    continue
            else:
                matching_resumes = [r for r in resumes if user_input.lower() in r.lower()]
                if matching_resumes:
                    print(f"Found {len(matching_resumes)} matching resumes:")
                    list_resumes(matching_resumes)

                    # Automatically select the first matching resume
                    selected_resume = matching_resumes[0]
                else:
                    print("No matching resumes found. Please try again.")
                    continue

            # Analyze the selected resume
            pdf_path = os.path.join(folder_path, selected_resume)
            resume_text = text_from_pdf(pdf_path)

            matches = analyze_resume(resume_text)
            best_role, best_match_count = suggest_best_role(matches)

            print(f"\n--- Analysis for '{selected_resume}' ---")
            print(f"Best Suggested Job Role: {best_role} with {best_match_count} keyword matches")

            # Display matched keywords
            display_matched_keywords(matches)

            # print("\n" + ("-" * 30))  # Separator for clarity

        except KeyboardInterrupt:
            print("\nExiting the program. Goodbye!")
            break  # Break the loop on keyboard interrupt
        except Exception as e:
            print(f"An error occurred: {e}")

# Set the folder path and run the main function
folder_path = r'/data-science-work/anurag/Assignment_2\SampleResumes'
main(folder_path)
