# python_projects:

This is a repository of my python projects as I learn this lenguage.

To create the skeleton of this repository I used the following scripts in bash:

**Create the skeleton folders:**
```bash
for i in {01..52};
    do 
        mkdir Exercise$i;
    done
```

**Create the skeleton .py files:**
```bash
for i in {01..52};
    do 
        cd Exercise$i && touch ex$i.py && cd ..;
    done
```

**Create the skeleton README.md files:**
```bash
for i in {01..52};
    do 
        cd Exercise$i && touch README.md && echo "# Exercise $i" > README.md && cd ..;
    done
```