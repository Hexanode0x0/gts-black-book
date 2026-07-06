---
icon: lucide/book-user
---
# Contributing
Anyone can contribute to the GTS Black Book, and the type of content that's accepted is broad, so long as it's about GTS.

You can contribute whole modding guides, or just personal notes you think others would find useful.

If anything is unclear, do not hesitate to ask. You can leave a message on the [GTS Black Book Thread](https://discord.com/channels/902984082181484615/1520726956419710978), on the GTS Discord.

## Getting Started

To edit a page:

1. Go to the top of the page you want to edit. There you'll find both a view source and an edit button
2. Click edit, and you'll be taken to GitHub
3. GitHub will inform you that you need to fork the repo to make edits. Do that
4. Make the edits you wish, then go to your fork, which will be present as your repository, and click the compare and pull request button to send your changes for review

The minimal contribution setup only requires you to make a clone of the repo on GitHub, but your editing capabilities will be rather limited.

For that reason, the rest of this page will walk you through how to set up the project properly.

## Real Editing

To properly edit the book, you need to create a local copy of the project and install Zensical, which is the framework this book uses.

Doing so will allow you to view edits right as you make them and confirm that everything looks just as you want it to.

### Getting The Tools

=== "Windows"
    1. Create an account on GitHub
    2. [Install Git](https://git-scm.com/install/)
    2. [Install Python](https://www.python.org/downloads/)
    3. [Install GitHub desktop](https://desktop.github.com/download/) and log in
    3. Fork the [gts-black-book repo](https://github.com/hexanode0x0/gts-black-book) on GitHub using the fork button in the top-right
    4. On your fork, click the green code button, and copy the link there
    5. Go to your personal projects folder (or anywhere really) on your computer, Shift + Right-Click the empty space, and open the folder with Powershell or Terminal
    6. Run `git clone {link from step 4}`, eg. `git clone https://github.com/{your username}/gts-black-book.git`
    7. Go inside the repo with `cd gts-black-book`
    8. Run `python -m venv .venv` to set up the Python virtual environment
    9. Run `.venv\Scripts\Activate.ps1` to activate the virtual environment
    10. Run `pip install zensical`
    11. Run `zensical serve`
    12. Go back to your browser and type into the address bar "http://localhost:8000". You should see a local copy of the book, ripe for editing.
=== "Linux"
    1. Create an account on GitHub
    2. Install Git, Python, and GitHub Desktop with your package manager
    3. Log into GitHub Desktop
    4. Fork the [gts-black-book repo](https://github.com/hexanode0x0/gts-black-book) on GitHub using the fork button in the top-right
    4. On your fork, click the green code button, and copy the link there
    5. Go to your personal projects folder (or anywhere really) on your computer, Shift + Right-Click the empty space, and open a terminal
    6. Run `git clone {link from step 4}`, eg. `git clone https://github.com/{your username}/gts-black-book.git`
    7. Go inside the repo with `cd gts-black-book`
    8. Run `python -m venv .venv` to set up the Python virtual environment
    9. Run `source .venv/bin/activate` to activate the virtual environment
    10. Run `pip install zensical`
    11. Run `zensical serve`
    12. Go back to your browser and type into the address bar "http://localhost:8000". You should see a local copy of the book, ripe for editing.


!!! note
    `zensical serve` is what makes the webpage appear and rebuild automatically whenever you make changes.

    Sometimes you'll need to manually refresh the page to see changes, depending on which browser you use.

    If you close the terminal where you ran it, you'll need to activate the virtual environment again, and then run `zensical serve`.

### Actually Editing

To edit, you should use a code editor with Git interagtion, to make things easier on yourself. I recommend [Zed](https://zed.dev/), and it's what will be used for this guide, along with the following extensions:

* Git Firefly
* TOML
* Typos Spell Checker

The actual webpage is contained inside the 'docs' directory, The project structure is further divided into directories. Each directory has an 'index.md' file, which serves as the default page for it. You can add markdown files with other names too, but they will be shown as subsections.

To read about what formatting options are available, check [Zensical's documentation](https://zensical.org/docs/authoring/markdown). You can also copy formatting from other parts of the book and play around with them.

### Submitting
Once you are done with editing, click the Git :lucide-git-branch: icon at the bottom panel in Zed. This will open the Git view, where you can see each file you have edited and what those edits are.

You'll generally want to submit all your changes, by clicking the `Stage All` button at the top. You can click on each file to see what you've changed.

At the bottom, write a short commit message. Commits are changes you're generally happy with and want to keep, though you can always revert them later. Think of it as your 'done for the day' button. The message should be short and simple. Something like "Expanded Contributing Page" is fine.

Once you're ready to commit, click the `Commit` button near the bottom. Afterwards a `Push` button will appear. This will push your changes to the remote repository, aka, to GitHub. When you click it and go to your fork of the book on GitHub, you'll see a "Compare and Pull Request" button, which will allow you to send your changes to the main book.
