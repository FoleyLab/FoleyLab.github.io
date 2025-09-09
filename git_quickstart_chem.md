# Git & GitHub Quickstart (Computational Chemistry)

## Setup
- Install Git and create a GitHub account.
- Configure identity:
  - `git config --global user.name "Your Name"`
  - `git config --global user.email "you@institution.edu"`
- SSH (recommended):
  - `ssh-keygen -t ed25519 -C "you@institution.edu"`
  - Add the public key to GitHub → Settings → SSH and GPG keys.

## Everyday loop (CLI)
```bash
git status
git pull                       # update main
git checkout -b feature/task   # new branch
# edit files
git add file1.py inputs/*.in
git commit -m "Message in imperative mood"
git push -u origin feature/task
# open PR on GitHub
```
## GitHub Desktop loop
1. Clone → New Branch → Edit.
2. Stage changes visually → Commit with a clear summary.
3. Push → Create Pull Request → Request review → Merge.

## .gitignore (chemistry‑flavored)
- Ignore obvious scratch and huge transient files: `scratch/`, `tmp/`, `*.log` (if massive), etc.
- Gaussian: `*.chk`, `*.fchk`
- ORCA: `*.gbw`
- VASP: `WAVECAR`, `CHGCAR`, `AECCAR*`, `EIGENVAL`, `PROCAR`, `XDATCAR`, `OUTCAR`, `OSZICAR`, `vasprun.xml`
- Python: `__pycache__/`, `*.pyc`, `.ipynb_checkpoints/`
- OS/Editor cruft: `.DS_Store`, `Thumbs.db`

If a large file is **important to keep**, track it with Git LFS rather than ignoring it.

## Large files (Git LFS)
```bash
git lfs install
git lfs track "*.gbw"
git lfs track "WAVECAR"
git add .gitattributes
git add <large files>
git commit -m "Track large files via Git LFS"
git push
```

## Notebooks & Reproducibility
- Keep outputs light; consider `nbstripout`.
- Use `nbdime` for readable diffs.
- Capture environments in `environment.yml` or `requirements.txt`.

## HPC Tips
- Use SSH on clusters; configure `git config --global` on each machine.
- No GitHub Desktop on HPC—use CLI.
- Don’t commit secrets; keep tokens out of repos.

## Troubleshooting
- Public key errors → re-add SSH key to GitHub; test: `ssh -T git@github.com`.
- Merge conflicts → edit the marked sections, then `git add` and `git commit`.
- Large file rejections → use LFS or remove from history.
