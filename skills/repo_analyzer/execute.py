import os
from pathlib import Path
import subprocess

def analyze_repo(repo_url: str):
    print(f"🔍 ClawMentor Bharat - Analyzing Repository: {repo_url}")
    print("="*60)
    
    # Clone temporarily to a hidden openclaw folder
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    temp_path = Path.home() / ".openclaw" / "temp" / repo_name
    temp_path.mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"📡 Cloning into: {temp_path}")
        subprocess.run(["git", "clone", "--depth", "1", repo_url, str(temp_path)], timeout=30, capture_output=True)
        
        files = list(temp_path.glob("**/*"))
        has_requirements = any(f.name == "requirements.txt" for f in files)
        has_packagejson = any(f.name == "package.json" for f in files)
        has_dockerfile = any(f.name.lower() == "dockerfile" for f in files)
        has_pom = any(f.name == "pom.xml" for f in files)
        
        print("\n✅ Repository Analysis Complete")
        print("-" * 30)
        tech_stack = []
        if has_requirements: tech_stack.append("Python (pip)")
        if has_packagejson: tech_stack.append("Node.js (npm)")
        if has_pom: tech_stack.append("Java (Maven)")
        
        print(f"🛠 **Tech Stack Detected**: {', '.join(tech_stack) if tech_stack else 'Unknown'}")
        print(f"🐳 **Docker Ready**: {'Yes' if has_dockerfile else 'No'}")
        print(f"🚀 **Build Feasibility**: {'High' if tech_stack else 'Medium'}")
        
    except Exception as e:
        print(f"❌ Could not clone or analyze repo: {e}")

if __name__ == "__main__":
    # Example usage for demo
    analyze_repo("https://github.com/sahanavs-2006/ClawMentor-Bharat")
