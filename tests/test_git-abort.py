import os
import subprocess
import shlex

class TestGitAbort:
    def test_init(self, git_repo):
        _, tmp_dir, tmp_a, tmp_b = git_repo
        subprocess.run(shlex.split("git branch A"))
        subprocess.run(shlex.split("git branch B"))
        subprocess.run(shlex.split("git checkout A"))
        file_a = open(tmp_a[1], "w", encoding="utf-8")
        file_a.write('a')
        file_a.close()
        subprocess.run(shlex.split("git add ."))
        subprocess.run(shlex.split("git commit -m \"A\""))
        subprocess.run(shlex.split("git checkout B"))
        file_b = open(tmp_a[1], "w", encoding="utf-8")
        file_b.write('b')
        file_b.close()
        subprocess.run(shlex.split("git add ."))
        subprocess.run(shlex.split("git commit -m \"B\""))
        subprocess.run(shlex.split("git status"))

    def test_cherry_pick(self, git_repo):
        git_extras_cwd = git_repo[0]
        result = subprocess.run(shlex.split("git cherry-pick A"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        result = subprocess.run(shlex.split("git status"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        assert "Unmerged path" in result.stdout.decode()
        subprocess.run(shlex.split(os.path.join(git_extras_cwd, 'bin', 'git-abort')))
        result = subprocess.run(shlex.split("git status"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        assert "nothing to commit, working tree clean" in result.stdout.decode()

    def test_merge(self, git_repo):
        git_extras_cwd = git_repo[0]
        git_extras_cwd = git_repo[0]
        result = subprocess.run(shlex.split("git merge --allow-unrelated-histories A"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        result = subprocess.run(shlex.split("git status"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        assert "Unmerged path" in result.stdout.decode()
        subprocess.run(shlex.split(os.path.join(git_extras_cwd, 'bin', 'git-abort')))
        result = subprocess.run(shlex.split("git status"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        assert "nothing to commit, working tree clean" in result.stdout.decode()

    def test_rebase(self, git_repo):
        git_extras_cwd = git_repo[0]
        git_extras_cwd = git_repo[0]
        result = subprocess.run(shlex.split("git rebase A"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        result = subprocess.run(shlex.split("git status"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        assert "Unmerged path" in result.stdout.decode()
        subprocess.run(shlex.split(os.path.join(git_extras_cwd, 'bin', 'git-abort')))
        result = subprocess.run(shlex.split("git status"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        assert "nothing to commit, working tree clean" in result.stdout.decode()

    def test_revert(self, git_repo):
        git_extras_cwd = git_repo[0]
        result = subprocess.run(shlex.split("git revert A"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        result = subprocess.run(shlex.split("git status"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        assert "Unmerged path" in result.stdout.decode()
        subprocess.run(shlex.split(os.path.join(git_extras_cwd, 'bin', 'git-abort')))
        result = subprocess.run(shlex.split("git status"), capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        assert "nothing to commit, working tree clean" in result.stdout.decode()
