# Sharing fixtures
# Ref: https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session

import os
import subprocess
import shlex
import shutil
import tempfile
import pytest

@pytest.fixture(scope="module")
def git_repo():
    git_extras_cwd = os.getcwd()
    tmp_dir = tempfile.mkdtemp()
    tmp_file_a = tempfile.mkstemp(dir=tmp_dir)
    tmp_file_b = tempfile.mkstemp(dir=tmp_dir)
    os.chdir(tmp_dir)
    result = subprocess.run(shlex.split("git init"), capture_output=True)
    print(result.stdout.decode())
    print(result.stderr.decode())
    result = subprocess.run(shlex.split("git add ."), capture_output=True)
    print(result.stdout.decode())
    print(result.stderr.decode())
    subprocess.run(shlex.split("git config --local user.name \"test\""))
    subprocess.run(shlex.split("git config --local user.email \"test@git-extras.com\""))
    result = subprocess.run(shlex.split("git commit -m 'chore: initial commit'"), capture_output=True)
    print(result.stdout.decode())
    print(result.stderr.decode())
    yield [git_extras_cwd, tmp_dir, tmp_file_a, tmp_file_b]
    shutil.rmtree(tmp_dir, ignore_errors=True)
