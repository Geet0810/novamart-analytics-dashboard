"""
GitHub Push Script - Initialize repo and push to GitHub
"""

from git import Repo
import os
import sys

def push_to_github(repo_path, github_url, branch="main"):
    """Initialize git repo and push to GitHub"""
    
    try:
        print(f"📁 Working directory: {repo_path}")
        os.chdir(repo_path)
        
        # Initialize repository
        print("🔧 Initializing git repository...")
        repo = Repo.init(repo_path)
        
        # Configure git
        with repo.config_writer() as git_config:
            git_config.set_value("user", "name", "Your Name").release()
            git_config.set_value("user", "email", "your-email@example.com").release()
        
        print("✅ Git configured")
        
        # Add all files
        print("📄 Adding all files...")
        repo.index.add([item.path for item in repo.untracked_files])
        repo.index.add(A=True)
        
        print("✅ Files added")
        
        # Create initial commit
        print("💾 Creating initial commit...")
        repo.index.commit("Initial commit: NovaMart Analytics Dashboard - Complete Streamlit application with 7 pages and 20+ visualizations")
        
        print("✅ Commit created")
        
        # Rename branch to main
        if repo.active_branch.name != branch:
            repo.active_branch.rename(branch)
            print(f"✅ Branch renamed to {branch}")
        
        # Add remote
        print(f"🔗 Adding remote: {github_url}")
        if 'origin' in [remote.name for remote in repo.remotes]:
            repo.delete_remote('origin')
        
        origin = repo.create_remote('origin', github_url)
        
        print("✅ Remote configured")
        
        # Push to GitHub
        print(f"🚀 Pushing to GitHub ({branch})...")
        origin.push(branch)
        
        print(f"""
✅ SUCCESS! Your repository has been pushed to GitHub!

📊 Next Steps:
1. Go to: {github_url}
2. Verify all files are there
3. Deploy to Streamlit Cloud:
   - Visit: https://streamlit.io/cloud
   - Connect your GitHub account
   - Click "New app"
   - Select this repository
   - Set main file path to: app.py
   - Click "Deploy"

🎉 Your dashboard will be live in minutes!
        """)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Get GitHub URL from user
    github_url = input("🔑 Enter your GitHub repository URL (e.g., https://github.com/username/repo-name.git): ").strip()
    
    if not github_url:
        print("❌ Repository URL is required!")
        sys.exit(1)
    
    repo_path = os.getcwd()
    push_to_github(repo_path, github_url)
