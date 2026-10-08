# Getting Started with RStudio, A Gentle Tour

**Clinical Data Analysis in R - Phase I | Neudata**

Welcome! Before we meet for the course, we would like to introduce you to the tool you will be working in: **RStudio**. Please do not worry about learning it all now. This manual is simply a friendly walk around the "workspace" so that when you sit down on day one, nothing on the screen feels unfamiliar.

A quick reassurance before we begin: you do **not** need any programming experience, and you do **not** need to memorise anything here. Think of this the way you would think of walking into a new clinic or ward for the first time, you just want to know where the sink is, where the notes are kept, and where the sharps bin lives. Once you know where things are, the rest follows naturally.

---

## 1. The big picture: four panes in a 2x2 grid

When you open RStudio, the window is divided into **four rectangular areas called "panes"**, arranged in a simple 2x2 grid, two on the left, two on the right. Each pane has a job. That is the whole idea. Once you know which corner does what, you will always know where to look.

Here is a simple sketch of the layout:

```
+-----------------------------+-----------------------------+
|                             |                             |
|   TOP-LEFT                  |   TOP-RIGHT                 |
|   Source / Editor           |   Environment / History     |
|   (where you WRITE code      |   (what R currently         |
|    and open your scripts)   |    remembers)               |
|                             |                             |
+-----------------------------+-----------------------------+
|                             |                             |
|   BOTTOM-LEFT               |   BOTTOM-RIGHT              |
|   Console                   |   Files / Plots /           |
|   (where code RUNS)         |   Packages / Help           |
|                             |                             |
+-----------------------------+-----------------------------+
```

A couple of gentle notes:

- The panes on the **right** (top-right and bottom-right) each contain several **tabs** along their top edge, little clickable labels like *Environment*, *History*, *Files*, *Plots*, *Packages*, *Help*. Clicking a tab simply brings that view to the front, exactly like tabs in a paper folder.
- When you first open RStudio you may see only **three** panes, because the top-left Source pane stays hidden until you open a script. As soon as you open a file, it appears. Do not be alarmed if a corner looks empty at first.

That's the map. Now let's visit each area in turn.

---

## 2. What each pane and tab is for

### Source pane (top-left): where you write

This is your writing surface: a plain, tidy page where you **type, edit, and save** your code. Files you write here are saved as **`.R`** files (plain R scripts) or **`.Rmd`** files (R Markdown, code and written notes together, which we use for reports). Nothing here runs on its own; it just sits and waits, like notes on a page, until you choose to run it.

*A clinician will use it to:* keep a saved, re-runnable record of an analysis, for example a script that reads in your patient dataset, cleans it, and produces a summary table you can regenerate at any time.

### Console (bottom-left): where code runs

This is the engine room. Code that runs, runs **here**, and its results appear here as text. You will notice a **`>`** symbol at the left edge, this is the **prompt**, R's way of saying "I'm ready, go ahead." You can type a command directly after the `>` and press Enter to run it immediately.

*A clinician will use it to:* try a quick one-off calculation or check, for instance, asking R for the average age in a dataset without needing to save anything.

### Environment (top-right tab), what R remembers

The Environment tab lists the **objects currently held in R's memory**, your datasets, tables, and any values you have created and given a name. When you load the course data into an object called `clinical_data`, it will appear here, usually with a note of how many rows (patients) and columns (variables) it holds.

*A clinician will use it to:* confirm at a glance that a dataset loaded correctly and has the expected number of patients before analysing it.

### History (top-right tab): past commands

Sitting next to Environment is the **History** tab, a running list of **every command you have run** this session. You can select a past command and send it back to the Console or Source to reuse it.

*A clinician will use it to:* recover a command they typed earlier but forgot to save into their script.

### Files (bottom-right tab): your folder browser

The Files tab is a plain **file browser**, much like File Explorer on Windows or Finder on a Mac, but showing the contents of your project folder. You can see your scripts, your data files, and open any of them with a click.

*A clinician will use it to:* find and open the dataset file `Data/clinical_data_clean.csv` or reopen a script from a previous day.

### Plots (bottom-right tab): where graphs appear

Whenever your code produces a graph, it appears in the **Plots** tab. Along the top of this tab are small buttons: **Zoom** (opens the graph larger in its own window) and **Export** (saves it as an image or PDF, or copies it to the clipboard). There are also left/right arrows to step back through earlier plots.

*A clinician will use it to:* view a survival curve or a distribution of blood pressures, then export it to drop into a slide or manuscript.

### Packages (bottom-right tab), installed add-ons

R comes with a core set of tools, and thousands more live in **packages**, optional add-ons that extend what R can do. The Packages tab lists the ones **installed** on your computer, each with a **tick box**. Ticking a box loads that package for use. (You can also load them by typing a command, which we generally prefer, more on that below.)

*A clinician will use it to:* confirm that a needed package, such as `tidyverse` (a popular collection for handling data), is installed and available.

### Help (bottom-right tab): the documentation

The Help tab shows **documentation**, the official manual page for any R function, explaining what it does and how to use it. You can bring up the help page for a function by typing a question mark before its name in the Console:

```r
?mean
```

*A clinician will use it to:* look up exactly what a function expects, for example, checking how `mean()` handles missing values before trusting a result.

---

## 3. Exactly how to...

Below is a set of small, self-contained guides. Each assumes you have never done this before. Where a keyboard shortcut helps, we give both the **Windows** version (using the **Ctrl** key) and the **Mac** version (using the **Cmd** key, ⌘).

---

### How to open the course project

The course is delivered as a **project**, a self-contained folder with a special file inside it named **`Clinical_Data_Analysis_PreCourse.Rproj`**.

1. Open the course folder in File Explorer (Windows) or Finder (Mac).
2. **Double-click** the file **`Clinical_Data_Analysis_PreCourse.Rproj`**.
3. RStudio opens with the project loaded. You will see the project's name in the **top-right corner** of the RStudio window.

**What is an `.Rproj` file, and why does it matter?** It is a small marker that says "this folder is a project." Opening it does one very important, quietly helpful thing: it sets R's **working directory** to that folder. The working directory is simply the place R looks in first when you ask it to open a file. Because you opened via the `.Rproj`, you can refer to the data as `Data/clinical_data_clean.csv` and R will find it, no long, fragile file paths, no guessing where things live. Always start your day by opening the project this way.

---

### How to open an `.R` or `.Rmd` file

Two easy routes: use whichever feels natural:

- **From the Files pane (bottom-right):** click the **Files** tab, then **click the file's name**. It opens in the Source pane (top-left).
- **From the menu:** click **File > Open File...**, then browse to the file and click **Open**.

---

### How to run ONE line of code

1. In the Source pane, **click anywhere on the line** you want to run (you do not need to select the whole line, just place the cursor on it).
2. Press **Ctrl + Enter** (Windows) or **Cmd + Enter** (Mac). You can also click the **Run** button at the top-right of the Source pane.
3. The line runs in the Console below, and any result appears there. The cursor helpfully jumps to the next line, ready to go again.

---

### How to run SEVERAL lines of code

1. **Click and drag** to select all the lines you want to run (highlight them).
2. Press **Ctrl + Enter** (Windows) or **Cmd + Enter** (Mac), or click **Run**. Every selected line runs in order.

To run the **entire file** from top to bottom in one go, click the **Source** button (top-right of the Source pane), or press **Ctrl + Shift + Enter** (Windows) / **Cmd + Shift + Enter** (Mac).

---

### How to stop running code

Sometimes code takes longer than expected, or you started something by mistake. To stop it:

- Click the small **red Stop sign** () that appears at the top-right of the **Console** while code is running, **or**
- Click inside the Console and press the **Esc** key.

R will halt what it is doing and return you to the friendly `>` prompt. Nothing is broken, you have simply asked it to stand down.

---

### How to find an object

An "object" is anything you have created and named, most often a dataset.

- Look in the **Environment** tab (top-right). Every object you have made is listed there by name, such as `clinical_data`.
- Alternatively, **type its name** in the Console and press Enter, R will print it out so you can see it.

---

### How to view a dataset

To see your data laid out as a proper spreadsheet:

- In the **Environment** tab, **click the object's name** (e.g. `clinical_data`), **or**
- Type this in the Console and press Enter:

```r
View(clinical_data)
```

Note the **capital V** in `View`. A spreadsheet-style viewer opens in the Source area, where you can scroll through rows (patients) and columns (variables), and even sort or filter to inspect the data. This viewer is for **looking only**, it does not change your data.

---

### How to find a plot

- Any graph you create appears in the **Plots** tab (bottom-right).
- Click **Zoom** to open it larger in its own window for a proper look.
- Click **Export** to save it as an image or PDF, or to copy it.
- Use the **left/right arrows** at the top of the Plots tab to step back and forth through graphs you made earlier in the session.

---

### How to install and load a package (the fridge analogy)

This is the one idea that most often confuses beginners, so let's make it simple with an everyday picture.

Imagine a package is a **fridge full of useful ingredients**.

- **Installing** is *buying and delivering the fridge to your kitchen*. You do this **once**. After that, the fridge lives in your house.
- **Loading** is *opening the fridge door to reach the ingredients*. You do this **every time you cook**, that is, every new R session.

In R:

**Install once** (per computer):

```r
install.packages("tidyverse")
```

Note the **quotation marks** around the name. You only run this once; you do not need to install it again each time.

**Load every session** (each time you open RStudio and want to use it):

```r
library(tidyverse)
```

No quotation marks needed here. If you open R tomorrow and a command that worked yesterday suddenly complains it "could not find" a function, the usual cause is simply that you have not opened the fridge yet, run the `library()` line and carry on.

---

### How to save your work

- To save the script you are editing, press **Ctrl + S** (Windows) or **Cmd + S** (Mac), or click the small **disk icon** at the top of the Source pane.
- Please save **often**: after every meaningful change, just as you would save a document you cared about.

**One crucial thing to understand:** the objects listed in the **Environment** pane are **temporary**. They live in memory and vanish when you close RStudio. That is completely fine and normal, because your **script is the permanent record**. A saved script can rebuild every object from scratch, any time, by simply running it again. So we treasure the script, and we let the Environment come and go.

---

## 4. Good habits (worth adopting from day one)

> **A few gentle habits that will save you grief:**
>
> - **Work in scripts, not the Console.** Type your real work into a Source-pane script and run it from there, so you always have a saved record. Use the Console only for quick, throwaway checks.
> - **Comment your code** with the `#` symbol. Anything after a `#` on a line is a note for humans, ignored by R. Explain *why* you did something, your future self will thank you.
>   ```r
>   # Read in the cleaned patient dataset
>   clinical_data <- read.csv("Data/clinical_data_clean.csv")
>   ```
> - **Save often**: Ctrl/Cmd+S becomes a reflex quickly.
> - **When things get strange, restart R.** If R starts behaving oddly, go to **Session > Restart R**. This gives you a clean, empty slate. Then re-run your script from the top. This fixes a surprising number of mysterious problems, and it is nothing to worry about.

---

## 5. A closing word

That is the whole tour. If it feels like a lot, please remember that you truly do not need to hold it all in your head, you only need to know that the map exists and that every part of it will be here waiting for you. On day one we will open the project together, run our first lines, and load the `clinical_data` dataset side by side, at an unhurried pace. Nobody is expected to arrive fluent. You already read patient notes, weigh evidence, and reason carefully every day, those are exactly the skills that matter here, and R is simply a new instrument for the same clinical thinking. We look forward to getting started with you.
