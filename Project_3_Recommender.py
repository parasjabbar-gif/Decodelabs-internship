import math

# Dataset
jobs = {
    "Cloud Architect": ["Python", "Cloud Computing", "AWS", "Automation", "Terraform", "Linux"],
    "Data Scientist": ["Python", "SQL", "Machine Learning", "Statistics", "Pandas", "NumPy"],
    "DevOps Engineer": ["AWS", "Docker", "Kubernetes", "Automation", "Linux", "CI/CD"],
    "Backend Developer": ["Python", "Java", "APIs", "Databases", "Django", "Spring Boot"],
    "Frontend Developer": ["JavaScript", "React", "CSS", "HTML", "UI/UX", "Tailwind"],
    "ML Engineer": ["Python", "TensorFlow", "Machine Learning", "Cloud Computing", "APIs"],
    "Security Analyst": ["Linux", "Python", "Networking", "Security", "Firewalls", "Penetration Testing"]
}

# Build vocabulary from all skills
def build_vocabulary():
    all_skills = set()
    for skills in jobs.values():
        for skill in skills:
            all_skills.add(skill)
    return sorted(list(all_skills))

vocabulary = build_vocabulary()

# Calculate IDF (gives higher weight to rare terms)
def compute_idf():
    num_docs = len(jobs)
    idf_values = {}
    
    for skill in vocabulary:
        docs_with_skill = 0
        for job_skills in jobs.values():
            if skill in job_skills:
                docs_with_skill += 1
        
        if docs_with_skill > 0:
            idf_values[skill] = math.log(num_docs / docs_with_skill)
        else:
            idf_values[skill] = 0
    
    return idf_values

idf_scores = compute_idf()

# Convert skills list to TF-IDF weighted vector
def to_tfidf_vector(skills):
    vector = []
    for skill in vocabulary:
        # TF = 1 if skill present, else 0
        tf = 1 if skill in skills else 0
        tfidf = tf * idf_scores[skill]
        vector.append(tfidf)
    return vector

# Calculate cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = math.sqrt(sum(a * a for a in vec1))
    mag2 = math.sqrt(sum(b * b for b in vec2))
    
    if mag1 == 0 or mag2 == 0:
        return 0
    return dot_product / (mag1 * mag2)

# Handle cold start problem with onboarding survey
def cold_start_survey():
    print("\n You are a new user! Please select some topics:")
    popular_skills = ["Python", "JavaScript", "Cloud Computing", "Machine Learning", 
                      "AWS", "Docker", "React", "Databases", "Security", "APIs"]
    
    for i, skill in enumerate(popular_skills, 1):
        print(f"  {i}. {skill}")
    
    choices = input("Choose 3 numbers (e.g., 1,3,5): ").split(",")
    selected = []
    for c in choices:
        try:
            idx = int(c.strip()) - 1
            if 0 <= idx < len(popular_skills):
                selected.append(popular_skills[idx])
        except:
            pass
    
    return selected if len(selected) >= 3 else popular_skills[:3]

# Main Program
print("=" * 60)
print("     TECH STACK RECOMMENDER v2.0 (TF-IDF)")
print("=" * 60)

# Get user input
print("\n Enter your 3 skills (comma separated):")
user_input = input("Skills: ").strip()
user_skills = [s.strip().title() for s in user_input.split(",")]

# Cold Start Check - if user enters less than 2 skills, run survey
if len(user_skills) < 2 or all(s == "" for s in user_skills):
    user_skills = cold_start_survey()

print(f"\n  Your skills: {', '.join(user_skills)}")

# Generate user vector
user_vector = to_tfidf_vector(user_skills)

# Calculate recommendations for each job role
results = []
for job, skills in jobs.items():
    job_vector = to_tfidf_vector(skills)
    score = cosine_similarity(user_vector, job_vector)
    results.append((job, score))

# Sort by score (highest first) and display Top 3
results.sort(key=lambda x: x[1], reverse=True)

print("\n" + "=" * 60)
print("   TOP 3 RECOMMENDED CAREER PATHS")
print("=" * 60)

for i, (job, score) in enumerate(results[:3], 1):
    percentage = score * 100
    print(f"\n{i}.  {job}")
    print(f"   Match Score: {percentage:.1f}%")
    
    # Show matching skills
    job_skills = jobs[job]
    matched = [s for s in user_skills if s in job_skills]
    if matched:
        print(f"    Matching skills: {', '.join(matched)}")
    else:
        print(f"    No direct skill match - but close!")